# ExShade
Experimental resourcepack for experimenting with shaders in vanilla minecraft.

![image](https://user-images.githubusercontent.com/34125174/229444723-f22856bb-4c6e-4037-9caa-32a5b56caffe.png)
![image](https://user-images.githubusercontent.com/34125174/229444880-164b96b2-de1c-4daf-99e9-881d8d905aa3.png)
![image](https://user-images.githubusercontent.com/34125174/229444950-948edd68-9fef-488e-bf24-73405a74f4f6.png)


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




