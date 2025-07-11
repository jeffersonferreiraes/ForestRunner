# -*- mode: python -*-
from PyInstaller.utils.hooks import collect_data_files

a = Analysis(
    ['main.py'],
    pathex=['.', './code'],  # Adiciona ambos os caminhos
    binaries=[],
    datas=[
        ('assets/images/*', 'assets/images'),
        ('assets/audio/*', 'assets/audio'),
        ('code/*.py', 'code')
    ],
    hiddenimports=['pygame._sdl2'],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='ForestRunner',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='assets/images/icon.ico')