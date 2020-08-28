# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT, BUNDLE

import napari

sys.modules["FixTk"] = None


def get_icon():
    logo_file = "logo.ico" if sys.platform.startswith("win") else "logo.icns"
    return logo_file


NAME = "napari-app"
WINDOWED = True
DEBUG = False
UPX = False
BLOCK_CIPHER = None

a = Analysis(
    ["main.py"],
    hookspath=["hooks"],
    excludes=[
        "FixTk",
        "tcl",
        "tk",
        "_tkinter",
        "tkinter",
        "Tkinter",
        "matplotlib",
    ],
    cipher=BLOCK_CIPHER,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=BLOCK_CIPHER)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=NAME,
    debug=DEBUG,
    upx=UPX,
    console=(not WINDOWED),
    icon=get_icon(),
    version=napari.__version__,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    upx=UPX,
    name=NAME,
)

if sys.platform == "darwin":
    app = BUNDLE(
        coll,
        name=NAME + ".app",
        icon=get_icon(),
        bundle_identifier=f"com.{NAME}.{NAME}",
        info_plist={
            "CFBundleIdentifier": f"com.{NAME}.{NAME}",
            "CFBundleShortVersionString": napari.__version__,
            "NSHighResolutionCapable": "True",
        },
    )
