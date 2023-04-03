import os.path
import shutil
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from watchdog.observers.polling import PollingObserver

# CONFIG START--------------------

# Path to the resoucepack folder
target_path = "ExShade"
# Name of the resourcepack
name = "ExShade"
# Path to the minecraft resourcepacks folder where the resourcepack will be copied to
out_dir = "%appdata%/.minecraft/resourcepacks/"


# CONFIG END--------------------


def resolve_path(path: str) -> Path:
    return Path(os.path.expandvars(path)).absolute()


resolved_target = resolve_path(target_path)
resolved_out = resolve_path(out_dir) / name


def processPathChange(s_path: str, change_name:str, silence=False)->Path:
    rel = Path(s_path).relative_to(resolved_target)
    out_path = resolved_out / rel
    if not silence:
        print(f"({change_name}) Change detected, in...", s_path)
    return out_path


class EventHandler(LoggingEventHandler):

    def on_modified(self, event):
        super().on_modified(event)
        p = processPathChange(event.src_path, "Modified")
        if not p.exists():
            os.makedirs(p.parent, exist_ok=True)
        shutil.copy(event.src_path, p)

    def on_deleted(self, event):
        super().on_deleted(event)
        p = processPathChange(event.src_path, "Deleted")
        if p.exists():
            os.remove(p)

    def on_moved(self, event):
        super().on_moved(event)
        final = processPathChange(event.dest_path, "Moved")
        prev = processPathChange(event.src_path, "Moved", silence=True)

        if not prev.exists():
            os.makedirs(prev.parent, exist_ok=True)
            shutil.copy(event.dest_path, final)
        else:
            shutil.move(prev, final)

    def on_created(self, event):
        super().on_created(event)
        p = processPathChange(event.src_path, "Created")
        if not p.exists():
            os.makedirs(p.parent, exist_ok=True)
        shutil.copy(event.src_path, p)




observer = PollingObserver()
observer.schedule(EventHandler(), resolved_target, recursive=True)
print(f"Watching {resolved_target} for changes...")
print("Will copy changes to:", resolved_out, "\n")
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
