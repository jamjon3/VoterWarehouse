import PyInstaller.__main__

PyInstaller.__main__.run([
    'voterwarehouse.py',
    '--onefile',
    '--nowindowed',
    '--hidden-import=Import.Florida',
    '--hidden-import=Warehouse.Florida',
    '--hidden-import=Import.Georgia',
    '--hidden-import=Warehouse.Georgia',
    '--hidden-import=Import.NorthCarolina',
    '--hidden-import=Warehouse.NorthCarolina',
    '--hidden-import=Import.State',
    '--hidden-import=Warehouse.State'
])
