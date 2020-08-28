#!/bin/sh

# apt-get install libzmq3-dev

echo "removing old files..."
rm -rf build
rm -rf dist


echo "building app..."
pyinstaller --noconfirm --clean --log-level=INFO napari.spec


# if [[ "$OSTYPE" == "darwin"* ]]; then
#     echo "creating mac .dmg ..."
#     mkdir dist/dmg
#     ln -s /Applications dist/dmg
#     cp -r dist/napari.app dist/dmg
#     hdiutil create dist/napari.dmg -srcfolder dist/dmg
#     rm -rf dist/dmg
#     rm -rf dist/napari

#     # broken pkg building command
#     # productbuild --component ./dist/napari.app /Applications napari.pkg \
#     #   --sign "3rd Party Mac Developer Installer: napari team"
# fi
