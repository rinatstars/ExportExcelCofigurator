# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

# Добавляем иконку и другие ресурсы
added_files = [
    ('icon.ico', '.'),  # Добавляем иконку
    # ('other_data/*', 'data')  # Пример добавления других файлов
]

a = Analysis(
    ['main.pyw'],
    pathex=[],  # Можно добавить пути к дополнительным модулям
    binaries=[],
    datas=added_files,  # Добавляем наши файлы
    hiddenimports=[
        # Другие скрытые импорты при необходимости
    ],
    hookspath=[],  # Можно указать путь к кастомным хукам
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],  # Можно исключить ненужные модули
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
    optimize=0,  # Можно изменить уровень оптимизации (0, 1, 2)
)

pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=block_cipher,
    optimize=0
)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='ExportExcelConfigurator',  # Лучше задать понятное имя
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Сжатие исполняемого файла
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Для GUI приложения
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.ico'  # Явно указываем иконку
)