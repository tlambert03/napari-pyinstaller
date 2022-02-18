# napari-pyinstaller
minimal example of bundling napari with pyinstaller

1. clone repo
2. run `pip install -r requirements.txt` (preferably in a new environment containing Python **3.8**)
3. you may need to delete `.../site-packages/_pyinstaller_hooks_contrib/hooks/stdhooks/hook-OpenGL.py`, (see https://stackoverflow.com/a/63052808)
4. run `build.sh` on *nix platorms or `build.bat` on windows
