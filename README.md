# ExShade
Experimental resourcepack for experimenting with shaders in vanilla minecraft.

## Features
- Rainbow lines (hitbox, block outline, etc). 
  - The xyz axis crosshair in the f3 menu still remains the same (filtered out).

## Development

### Shader documentation
Vanilla shaders are not officially supported and has no official documentation.

However there are unofficial documentation and resources available.
1. Unofficial Documentation by McTsts: https://github.com/McTsts/Minecraft-Shaders-Wiki/tree/main
2. Copy of the Default Shaders: https://github.com/misode/mcmeta/tree/assets/assets/minecraft/shaders

### Requirements.
All requirements are in [requirements.txt](requirements.txt)

`pip install -r requirements.txt` to install them.


### watch.py
This is the main file to run for development.

watch.py is a script that watches for changes in the resourcepack 
and copies them to the minecraft resourcepack folder.

Edit the values in the file to match your setup.




