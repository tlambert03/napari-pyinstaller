echo "removing old files..."
rmdir /s /q build
rmdir /s /q dist


echo "building app..."

SET scriptpath=%~dp0
pyinstaller --noconfirm --clean --log-level=INFO "%scriptpath%\napari.spec"
