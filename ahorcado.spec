# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['ahorcado.py'],
    pathex=[],
    binaries=[],
    datas=[('musica_fondo.mp3', '.'), ('correcto.mp3', '.'), ('huh.mp3', '.'), ('corazon.mp3', '.'), ('musica_partida.mp3', '.'), ('musica_victoria.mp3', '.'), ('musica_derrota.mp3', '.'), ('verdugo_nuevo.png', '.'), ('verdugo_6.png', '.'), ('verdugo_5.png', '.'), ('verdugo_4.png', '.'), ('verdugo_3.png', '.'), ('verdugo_2.png', '.'), ('verdugo_1.png', '.'), ('verdugo_D.png', '.'), ('verdugo_V.png', '.')],
    hiddenimports=[],
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
    name='ahorcado',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
