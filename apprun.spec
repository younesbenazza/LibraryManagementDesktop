# -*- mode: python ; coding: utf-8 -*-
import os
from pathlib import Path
from PyInstaller.utils.hooks import collect_data_files

# Dynamically set BASE_DIR based on current working directory
BASE_DIR = Path(os.getcwd()).resolve()

a = Analysis(
    ['apprun.py'],
    pathex=[str(BASE_DIR)],
    binaries=[],
    datas=[(os.path.join(BASE_DIR, 'static'), 'static'),  # Include static directory
                    (os.path.join(BASE_DIR, 'staticfiles'), 'staticfiles'),(os.path.join(BASE_DIR, 'db.sqlite3'), '.')],
    hiddenimports=['whitenoise', 'whitenoise.middleware'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='apprun',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
