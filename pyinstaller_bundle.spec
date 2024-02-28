# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(['src/main.py'],
             pathex=['UPDATE TO PROJECT ROOT'],
             binaries=[],
             datas=[('src/dictionaries/*.json', 'dictionaries'), ('src/gui/*.ico', 'gui')],
             hiddenimports=['os', 'shutil', 'xml.etree.ElementTree', 'json', 'sys', 'tkinter', 'PIL.ImageTk', 'PIL.Image', 'tkinter.filedialog'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['**/__pycache__/'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += Tree('src/core', prefix='core')
a.datas += Tree('src/gui', prefix='gui')

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='Word文档繁简转换器',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True)
