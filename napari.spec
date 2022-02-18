# -*- mode: python ; coding: utf-8 -*-
import sys
from PyInstaller.building.build_main import Analysis, PYZ, EXE, COLLECT, BUNDLE
from PyInstaller.utils.hooks import copy_metadata
import napari

sys.modules["FixTk"] = None


NAME = "napari-app"
WINDOWED = True
DEBUG = False
UPX = False
BLOCK_CIPHER = None


def get_icon():
    logo_file = "logo.ico" if sys.platform.startswith("win") else "logo.icns"
    return logo_file


def get_version():
    if sys.platform != "win32":
        return None

    from PyInstaller.utils.win32 import versioninfo as vi

    ver_str = napari.__version__
    version = ver_str.replace("+", ".").split(".")
    version = [int(x) for x in version if x.isnumeric()]
    version += [0] * (4 - len(version))
    version = tuple(version)[:4]
    return vi.VSVersionInfo(
        ffi=vi.FixedFileInfo(filevers=version, prodvers=version),
        kids=[
            vi.StringFileInfo(
                [
                    vi.StringTable(
                        "000004b0",
                        [
                            vi.StringStruct("CompanyName", NAME),
                            vi.StringStruct("FileDescription", NAME),
                            vi.StringStruct("FileVersion", ver_str),
                            vi.StringStruct("LegalCopyright", ""),
                            vi.StringStruct("OriginalFileName", NAME + ".exe"),
                            vi.StringStruct("ProductName", NAME),
                            vi.StringStruct("ProductVersion", ver_str),
                        ],
                    )
                ]
            ),
            vi.VarFileInfo([vi.VarStruct("Translation", [0, 1200])]),
        ],
    )


a = Analysis(
    ["main.py"],
    hiddenimports=['imageio.plugins.tifffile',
                   'imageio.plugins.pillow_legacy',
                   'imageio.plugins.ffmpeg',
                   'imageio.plugins.bsdf',
                   'imageio.plugins.dicom',
                   'imageio.plugins.feisem',
                   'imageio.plugins.fits',
                   'imageio.plugins.gdal',
                   'imageio.plugins.dicom',
                   'imageio.plugins.example',
                   'imageio.plugins.freeimage',
                   'imageio.plugins.freeimagemulti',
                   'imageio.plugins.grab',
                   'imageio.plugins.lytro',
                   'imageio.plugins.npz',
                   'imageio.plugins.pillow',
                   'imageio.plugins.pillow_info',
                   'imageio.plugins.pillow_legacy',
                   'imageio.plugins.pillowmulti',
                   'imageio.plugins.simpleitk',
                   'imageio.plugins.spe',
                   'imageio.plugins.swf',
                   'napari._event_loop',
                   'napari.view_layers'
                   ],
    datas = copy_metadata("napari"),
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
    version=get_version(),
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
