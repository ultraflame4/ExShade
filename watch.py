import os.path
import time
from pathlib import Path
from dirsync import sync
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# CONFIG START--------------------

# Path to the resoucepack folder
target_path = "ExShade"
# Name of the resourcepack
name="ExShade"
# Path to the minecraft resourcepacks folder where the resourcepack will be copied to
out_dir = "%appdata%/.minecraft/resourcepacks/"


# CONFIG END--------------------


def resolve_path(path: str) -> Path:
    return Path(os.path.expandvars(path)).absolute()


resolved_target = str(resolve_path(target_path))
resolved_out = resolve_path(out_dir)/name


class EventHandler(LoggingEventHandler):

    def on_modified(self, event):
        super().on_modified(event)
        print("Change detected, copying...")
        sync(
            resolved_target,
            resolved_out,
            "sync",
            verbose=True,
            create=True,
            purge=True
        )

observer = Observer()
observer.schedule(EventHandler(), resolved_target, recursive=True)
print(f"Watching {resolved_target} for changes...")
print("Will copy changes to:", resolved_out,"\n")
observer.start()
try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()