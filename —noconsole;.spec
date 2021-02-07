# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['—noconsole;', '—add-data', 'data;', '—add-data', 'MONEY.txt;', '—add-data', 'volume.txt;', '—add-data', 'KILL_COUNT.txt;', '—add-data', 'shop_pers_loc.json;', 'new_phis.py'],
             pathex=['C:\\Users\\Roman\\PycharmProjects\\Git_project1'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='—noconsole;',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='—noconsole;')
