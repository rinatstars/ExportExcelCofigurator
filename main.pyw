import json
import os
# import sys
from tkinter import *
from tkinter import ttk, messagebox, filedialog
from tkinter.scrolledtext import ScrolledText
# from typing import Dict, Any, List
# import darkdetect

# Периодическая таблица элементов (символ: название)
PERIODIC_TABLE = {
    'H': 'Водород', 'He': 'Гелий', 'Li': 'Литий', 'Be': 'Бериллий', 'B': 'Бор',
    'C': 'Углерод', 'N': 'Азот', 'O': 'Кислород', 'F': 'Фтор', 'Ne': 'Неон',
    'Na': 'Натрий', 'Mg': 'Магний', 'Al': 'Алюминий', 'Si': 'Кремний', 'P': 'Фосфор',
    'S': 'Сера', 'Cl': 'Хлор', 'Ar': 'Аргон', 'K': 'Калий', 'Ca': 'Кальций',
    'Sc': 'Скандий', 'Ti': 'Титан', 'V': 'Ванадий', 'Cr': 'Хром', 'Mn': 'Марганец',
    'Fe': 'Железо', 'Co': 'Кобальт', 'Ni': 'Никель', 'Cu': 'Медь', 'Zn': 'Цинк',
    'Ga': 'Галлий', 'Ge': 'Германий', 'As': 'Мышьяк', 'Se': 'Селен', 'Br': 'Бром',
    'Kr': 'Криптон', 'Rb': 'Рубидий', 'Sr': 'Стронций', 'Y': 'Иттрий', 'Zr': 'Цирконий',
    'Nb': 'Ниобий', 'Mo': 'Молибден', 'Tc': 'Технеций', 'Ru': 'Рутений', 'Rh': 'Родий',
    'Pd': 'Палладий', 'Ag': 'Серебро', 'Cd': 'Кадмий', 'In': 'Индий', 'Sn': 'Олово',
    'Sb': 'Сурьма', 'Te': 'Теллур', 'I': 'Йод', 'Xe': 'Ксенон', 'Cs': 'Цезий',
    'Ba': 'Барий', 'La': 'Лантан', 'Ce': 'Церий', 'Pr': 'Празеодим', 'Nd': 'Неодим',
    'Pm': 'Прометий', 'Sm': 'Самарий', 'Eu': 'Европий', 'Gd': 'Гадолиний', 'Tb': 'Тербий',
    'Dy': 'Диспрозий', 'Ho': 'Гольмий', 'Er': 'Эрбий', 'Tm': 'Тулий', 'Yb': 'Иттербий',
    'Lu': 'Лютеций', 'Hf': 'Гафний', 'Ta': 'Тантал', 'W': 'Вольфрам', 'Re': 'Рений',
    'Os': 'Осмий', 'Ir': 'Иридий', 'Pt': 'Платина', 'Au': 'Золото', 'Hg': 'Ртуть',
    'Tl': 'Таллий', 'Pb': 'Свинец', 'Bi': 'Висмут', 'Po': 'Полоний', 'At': 'Астат',
    'Rn': 'Радон', 'Fr': 'Франций', 'Ra': 'Радий', 'Ac': 'Актиний', 'Th': 'Торий',
    'Pa': 'Протактиний', 'U': 'Уран', 'Np': 'Нептуний', 'Pu': 'Плутоний', 'Am': 'Америций',
    'Cm': 'Кюрий', 'Bk': 'Берклий', 'Cf': 'Калифорний', 'Es': 'Эйнштейний', 'Fm': 'Фермий',
    'Md': 'Менделевий', 'No': 'Нобелий', 'Lr': 'Лоуренсий', 'Rf': 'Резерфордий', 'Db': 'Дубний',
    'Sg': 'Сиборгий', 'Bh': 'Борий', 'Hs': 'Хассий', 'Mt': 'Мейтнерий', 'Ds': 'Дармштадтий',
    'Rg': 'Рентгений', 'Cn': 'Коперниций', 'Nh': 'Нихоний', 'Fl': 'Флеровий', 'Mc': 'Московий',
    'Lv': 'Ливерморий', 'Ts': 'Теннессин', 'Og': 'Оганесон'
}

# Позиции элементов в таблице Менделеева (период, группа)
ELEMENT_POSITIONS = {
    'H': (1, 1), 'He': (1, 18),
    'Li': (2, 1), 'Be': (2, 2), 'B': (2, 13), 'C': (2, 14),
    'N': (2, 15), 'O': (2, 16), 'F': (2, 17), 'Ne': (2, 18),
    'Na': (3, 1), 'Mg': (3, 2), 'Al': (3, 13), 'Si': (3, 14),
    'P': (3, 15), 'S': (3, 16), 'Cl': (3, 17), 'Ar': (3, 18),
    'K': (4, 1), 'Ca': (4, 2), 'Sc': (4, 3), 'Ti': (4, 4),
    'V': (4, 5), 'Cr': (4, 6), 'Mn': (4, 7), 'Fe': (4, 8),
    'Co': (4, 9), 'Ni': (4, 10), 'Cu': (4, 11), 'Zn': (4, 12),
    'Ga': (4, 13), 'Ge': (4, 14), 'As': (4, 15), 'Se': (4, 16),
    'Br': (4, 17), 'Kr': (4, 18),
    'Rb': (5, 1), 'Sr': (5, 2), 'Y': (5, 3), 'Zr': (5, 4),
    'Nb': (5, 5), 'Mo': (5, 6), 'Tc': (5, 7), 'Ru': (5, 8),
    'Rh': (5, 9), 'Pd': (5, 10), 'Ag': (5, 11), 'Cd': (5, 12),
    'In': (5, 13), 'Sn': (5, 14), 'Sb': (5, 15), 'Te': (5, 16),
    'I': (5, 17), 'Xe': (5, 18),
    'Cs': (6, 1), 'Ba': (6, 2), 'La': (6, 3), 'Hf': (6, 4),
    'Ta': (6, 5), 'W': (6, 6), 'Re': (6, 7), 'Os': (6, 8),
    'Ir': (6, 9), 'Pt': (6, 10), 'Au': (6, 11), 'Hg': (6, 12),
    'Tl': (6, 13), 'Pb': (6, 14), 'Bi': (6, 15), 'Po': (6, 16),
    'At': (6, 17), 'Rn': (6, 18),
    'Fr': (7, 1), 'Ra': (7, 2), 'Ac': (7, 3), 'Rf': (7, 4),
    'Db': (7, 5), 'Sg': (7, 6), 'Bh': (7, 7), 'Hs': (7, 8),
    'Mt': (7, 9), 'Ds': (7, 10), 'Rg': (7, 11), 'Cn': (7, 12),
    'Nh': (7, 13), 'Fl': (7, 14), 'Mc': (7, 15), 'Lv': (7, 16),
    'Ts': (7, 17), 'Og': (7, 18),
    # Лантаноиды
    'Ce': (8, 4), 'Pr': (8, 5), 'Nd': (8, 6), 'Pm': (8, 7),
    'Sm': (8, 8), 'Eu': (8, 9), 'Gd': (8, 10), 'Tb': (8, 11),
    'Dy': (8, 12), 'Ho': (8, 13), 'Er': (8, 14), 'Tm': (8, 15),
    'Yb': (8, 16), 'Lu': (8, 17),
    # Актиноиды
    'Th': (9, 4), 'Pa': (9, 5), 'U': (9, 6), 'Np': (9, 7),
    'Pu': (9, 8), 'Am': (9, 9), 'Cm': (9, 10), 'Bk': (9, 11),
    'Cf': (9, 12), 'Es': (9, 13), 'Fm': (9, 14), 'Md': (9, 15),
    'No': (9, 16), 'Lr': (9, 17),
}


class PeriodicTableWindow(Toplevel):
    def __init__(self, parent, config_data, update_callback):
        super().__init__(parent)
        self.title("Периодическая таблица элементов")
        self.geometry("900x600")
        self.config_data = config_data
        self.update_callback = update_callback
        self.buttons = {}  # Словарь для хранения кнопок элементов

        # Главный контейнер
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Фрейм для таблицы
        self.table_frame = ttk.Frame(self.main_frame)
        self.table_frame.pack(fill=BOTH, expand=True)

        # Фрейм для кнопки закрытия
        self.button_frame = ttk.Frame(self.main_frame)
        self.button_frame.pack(fill=X, pady=(10, 0))

        # Создаем таблицу элементов
        self.create_table()

        # Кнопка закрытия
        ttk.Button(self.button_frame, text="Закрыть", command=self.destroy).pack(pady=10)

    def create_table(self):
        """Создает визуальное представление таблицы Менделеева"""
        frame = ttk.Frame(self.table_frame)
        frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Создаем сетку
        for row in range(1, 10):
            frame.rowconfigure(row, weight=1, minsize=30)
        for col in range(1, 19):
            frame.columnconfigure(col, weight=1, minsize=30)

        # Создаем и сохраняем кнопки для каждого элемента
        for symbol, (period, group) in ELEMENT_POSITIONS.items():
            btn = ttk.Button(
                frame,
                text=symbol,
                width=3,
                command=lambda s=symbol: self.toggle_element(s)
            )
            btn.grid(row=period, column=group, padx=2, pady=2, sticky="nsew")
            self.buttons[symbol] = btn  # Сохраняем кнопку в словаре

            # Устанавливаем начальный стиль
            self.update_button_style(symbol)

        # Подсказка для ф-элементов
        ttk.Label(frame, text="* Лантаноиды и актиноиды (ряды 8 и 9)").grid(
            row=10, column=1, columnspan=18, sticky=W, pady=(5, 0))

    def update_button_style(self, symbol):
        """Обновляет стиль кнопки для конкретного элемента"""
        btn = self.buttons[symbol]
        if symbol in self.config_data["coefficients"]:
            btn.configure(style="Active.TButton")  # Зеленый для выбранных
        else:
            btn.configure(style="Disabled.TButton")  # Красный для остальных

    def toggle_element(self, element):
        """Добавление или удаление элемента"""
        if element in self.config_data["coefficients"]:
            # Удаляем элемент
            del self.config_data["coefficients"][element]
            self.config_data["oxide_conversion"].pop(element, None)
            self.config_data["thresholds"].pop(element, None)
        else:
            # Добавляем элемент
            self.config_data["coefficients"][element] = 1.0
            self.config_data["oxide_conversion"][element] = False
            self.config_data["thresholds"][element] = {
                "lower": 0.000000001,
                "upper": 1000000.0
            }

        # Обновляем главное окно
        self.update_callback()

        # Обновляем только стиль этой кнопки
        self.update_button_style(element)


class SettingsEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Конфигуратор настроек химического анализа")
        self.root.geometry("1100x700")
        self.root.minsize(900, 600)
        self.output_format_var = StringVar()

        # Создаем все необходимые переменные перед созданием виджетов
        self.output_format_var = StringVar()
        self.sample_output_format_var = StringVar()
        self.xml_folder_var = StringVar()
        self.sig_fig_var = IntVar()
        self.delete_xml_var = BooleanVar()
        self.header_vars = {}
        self.raw_text = None

        # Загрузка иконки
        try:
            self.root.iconbitmap(default=self.resource_path("icon.ico"))
        except:
            pass

        # Настройка стилей
        self.setup_styles()

        # Данные конфигурации
        self.config_data = {
            "xml_folder": "",
            "output_filename_format": "{date}_{method}_{executor}",
            "include_header": True,
            "header_fields": {
                "customer": True,
                "executor": True,
                "date": True,
                "method": True,
                "device": False,
                "organization": False
            },
            "coefficients": {},
            "oxide_conversion": {},
            "thresholds": {},
            "significant_figures": 3,
            "delete_xml_after_processing": True
        }

        # Путь к файлу конфигурации
        self.config_file = ""

        # Создаем флаг инициализации
        self.initializing = True

        # Создание интерфейса
        self.create_widgets()

        # Сохраняем оригинальные данные для сравнения
        self.original_config = None
        self.modified = False
        # Привязываем обработчик закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        # Загрузка последнего открытого файла
        self.load_last_config()

        # Включаем обработчики после инициализации
        self.initializing = False

    def resource_path(self, relative_path):
        """Получить абсолютный путь к ресурсу для работы с PyInstaller"""
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)

    def setup_styles(self):
        """ Настройка стилей виджетов """
        style = ttk.Style()

        # if darkdetect.isDark():
        #     #self.root.tk.call("source", self.resource_path("azure.tcl"))
        #     #self.root.tk.call("set_theme", "dark")
        #     #style.theme_use("azure-dark")
        #     bg_color = "#333333"
        #     fg_color = "#ffffff"
        #     active_fg = "#4CAF50"  # Зеленый (активные)
        #     disabled_fg = "#F44336"  # Красный (выбранные)
        # else:
        #     #self.root.tk.call("source", self.resource_path("azure.tcl"))
        #     #elf.root.tk.call("set_theme", "light")
        #     #style.theme_use("azure-light")
        #     bg_color = "#f5f5f5"
        #     fg_color = "#000000"
        #     active_fg = "#2E7D32"  # Темно-зеленый (активные)
        #     disabled_fg = "#C62828"  # Темно-красный (выбранные)

        bg_color = "#f5f5f5"
        active_fg = "#2E7D32"  # Темно-зеленый (активные)
        disabled_fg = "#C62828"  # Темно-красный (выбранные)

        style.configure("TNotebook.Tab", padding=[10, 5])
        style.configure("Treeview", rowheight=25)
        style.configure("TButton", padding=6)
        style.configure("Large.TButton", font=("Segoe UI", 10, "bold"))

        # Стиль для ВЫБРАННЫХ элементов (красный текст)
        style.configure("Disabled.TButton", foreground=disabled_fg)

        # Стиль для АКТИВНЫХ элементов (зеленый текст)
        style.configure("Active.TButton", foreground=active_fg)

        self.root.configure(bg=bg_color)

    def create_widgets(self):
        """Создание элементов интерфейса"""
        # Главный контейнер
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)

        # Панель вкладок
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=BOTH, expand=True)

        # Вкладка общих настроек
        self.create_general_tab()

        # Вкладка элементов
        self.create_elements_tab()

        # Вкладка сырых данных
        self.create_raw_data_tab()

        # Панель статуса
        self.status_var = StringVar()
        self.status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=SUNKEN)
        self.status_bar.pack(fill=X, padx=1, pady=(0, 1))

        # Панель инструментов
        self.create_toolbar(main_frame)

        # Инициализация данных
        self.update_ui_from_config()

    def create_toolbar(self, parent):
        """Создание панели инструментов"""
        toolbar = ttk.Frame(parent)
        toolbar.pack(fill=X, pady=(5, 0))

        ttk.Button(toolbar, text="Открыть", command=self.open_config, style="Large.TButton").pack(side=LEFT, padx=2)
        ttk.Button(toolbar, text="Сохранить", command=self.save_config, style="Large.TButton").pack(side=LEFT, padx=2)
        ttk.Button(toolbar, text="Сохранить как...", command=self.save_config_as, style="Large.TButton").pack(side=LEFT,
                                                                                                              padx=2)
        ttk.Button(toolbar, text="Справка", command=self.show_help, style="Large.TButton").pack(side=RIGHT, padx=2)

    def create_general_tab(self):
        """Создание вкладки общих настроек"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Общие настройки")

        # Поля ввода
        frame = ttk.LabelFrame(tab, text="Основные параметры", padding=10)
        frame.pack(fill=X, padx=5, pady=5)

        ttk.Label(frame, text="Папка с XML:").grid(row=0, column=0, sticky=W, pady=2)
        ttk.Entry(frame, textvariable=self.xml_folder_var, width=60).grid(row=0, column=1, padx=5, sticky=EW)
        ttk.Button(frame, text="Обзор...", command=self.browse_xml_folder).grid(row=0, column=2, padx=5)

        ttk.Label(frame, text="Формат имени файла:").grid(row=1, column=0, sticky=W, pady=2)
        ttk.Entry(frame, textvariable=self.output_format_var, width=60).grid(row=1, column=1, columnspan=2, padx=5,
                                                                             sticky=EW)

        ttk.Label(frame, text="Пример:").grid(row=2, column=0, sticky=W, pady=2)
        ttk.Entry(frame, textvariable=self.sample_output_format_var, width=60,
                  state='disabled').grid(row=2, column=1, columnspan=2, padx=5, sticky=EW)

        ttk.Label(frame, text="Значимые цифры:").grid(row=3, column=0, sticky=W, pady=2)
        ttk.Spinbox(frame, textvariable=self.sig_fig_var, from_=1, to=10, width=5).grid(row=3, column=1, sticky=W,
                                                                                        padx=5)

        ttk.Checkbutton(frame, text="Удалять XML после обработки", variable=self.delete_xml_var).grid(row=4, column=0,
                                                                                                      columnspan=3,
                                                                                                      sticky=W, pady=5)

        # Поля заголовка
        header_frame = ttk.LabelFrame(tab, text="Поля заголовка", padding=10)
        header_frame.pack(fill=X, padx=5, pady=5)

        self.header_vars = {}
        for i, (field, label) in enumerate([
            ("customer", "Заказчик\n{customer}"),
            ("executor", "Исполнитель\n{executor}"),
            ("date", "Дата\n{date}"),
            ("method", "Метод\n{method}"),
            ("device", "Прибор\n{device}"),
            ("organization", "Организация\n{organization}")
        ]):
            var = BooleanVar()
            self.header_vars[field] = var
            ttk.Checkbutton(header_frame, text=label, variable=var).grid(
                row=i // 3, column=i % 3, sticky=W, padx=5, pady=2)

        # Первоначальная загрузка данных без обработчиков иначе загружаются пустые ячейки
        self.update_ui_from_config()

        # Обработчики изменений
        self.xml_folder_var.trace_add('write', lambda *_: self.update_config_and_json())
        self.output_format_var.trace_add('write', lambda *_: self.update_filename_example())
        self.sig_fig_var.trace_add('write', lambda *_: self.update_config_and_json())
        self.delete_xml_var.trace_add('write', lambda *_: self.update_config_and_json())

        # Обработчики изменений для чекбоксов заголовка
        for var in self.header_vars.values():
            var.trace_add('write', lambda *_: self.update_config_and_json())

    def update_filename_example(self, *args):
        if not hasattr(self, 'sample_output_format_var'):
            return
        """Обновляет пример имени файла"""
        try:
            from datetime import datetime
            format_str = self.output_format_var.get()

            # Параметры для примера
            params = {
                'date': datetime.now().strftime("%Y%m%d"),
                'method': "ПКСА",
                'executor': "Иванов И.О.",
                'customer': "ООО Фирма",
                'device': "Гранд-Поток",
                'organization': "Лаборатория"
            }

            # Безопасное форматирование
            try:
                example = format_str.format(**params)
            except KeyError:
                # Если есть неизвестные параметры, оставляем их как есть
                example = format_str.format(
                    **{k: params.get(k, f'{{{k}}}') for k in re.findall(r'{(\w+)}', format_str)})

            self.sample_output_format_var.set(example)
        except Exception:
            self.sample_output_format_var.set("Ошибка в формате")

        # Обновляем конфигурацию
        self.update_config_and_json()

    def create_elements_tab(self):
        """Создание вкладки работы с элементами"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="Химические элементы")

        # Кнопка для открытия таблицы элементов
        btn_frame = ttk.Frame(tab)
        btn_frame.pack(fill=X, padx=5, pady=5)

        ttk.Button(
            btn_frame,
            text="Изменить список элементов",
            command=self.show_periodic_table,
            style="Large.TButton"
        ).pack(pady=10)

        # Таблица добавленных элементов со свойствами
        tree_frame = ttk.Frame(tab)
        tree_frame.pack(fill=BOTH, expand=True, padx=5, pady=5)

        # Вертикальный скроллбар
        y_scroll = ttk.Scrollbar(tree_frame, orient=VERTICAL)
        y_scroll.pack(side=RIGHT, fill=Y)

        self.element_tree = ttk.Treeview(
            tree_frame,
            columns=("element", "coefficient", "oxide", "lower", "upper"),
            show="headings",
            yscrollcommand=y_scroll.set
        )
        self.element_tree.pack(fill=BOTH, expand=True)

        # Настройка скроллбаров
        y_scroll.config(command=self.element_tree.yview)

        self.element_tree.heading("element", text="Элемент")
        self.element_tree.heading("coefficient", text="Коэффициент")
        self.element_tree.heading("oxide", text="Оксид")
        self.element_tree.heading("lower", text="Нижний порог")
        self.element_tree.heading("upper", text="Верхний порог")

        self.element_tree.column("element", width=80, anchor=CENTER)
        self.element_tree.column("coefficient", width=80, anchor=CENTER)
        self.element_tree.column("oxide", width=60, anchor=CENTER)
        self.element_tree.column("lower", width=100, anchor=CENTER)
        self.element_tree.column("upper", width=100, anchor=CENTER)

        self.element_tree.bind("<<TreeviewSelect>>", self.on_element_select)

        # Панель редактирования параметров выбранного элемента
        edit_frame = ttk.LabelFrame(tab, text="Параметры элемента", padding=10)
        edit_frame.pack(fill=X, padx=5, pady=5)

        ttk.Label(edit_frame, text="Коэффициент:").grid(row=0, column=0, sticky=W, pady=2)
        self.coeff_var = DoubleVar()
        ttk.Spinbox(
            edit_frame,
            textvariable=self.coeff_var,
            from_=0.000000001,
            to=1000000,
            increment=1,
            width=10
        ).grid(row=0, column=1, sticky=W, padx=5)

        self.oxide_var = BooleanVar()
        ttk.Checkbutton(
            edit_frame,
            text="Конвертировать в оксид",
            variable=self.oxide_var
        ).grid(row=0, column=2, padx=10)

        ttk.Label(edit_frame, text="Нижний порог:").grid(row=1, column=0, sticky=W, pady=2)
        self.lower_var = DoubleVar()
        ttk.Spinbox(
            edit_frame,
            textvariable=self.lower_var,
            from_=0,
            to=1e6,
            increment=0.1,
            format="%.7f",
            width=12
        ).grid(row=1, column=1, sticky=W, padx=5)

        ttk.Label(edit_frame, text="Верхний порог:").grid(row=1, column=2, sticky=W, pady=2)
        self.upper_var = DoubleVar()
        ttk.Spinbox(
            edit_frame,
            textvariable=self.upper_var,
            from_=0,
            to=1e6,
            increment=0.1,
            format="%.7f",
            width=12
        ).grid(row=1, column=3, sticky=W, padx=5)

        ttk.Button(
            edit_frame,
            text="Применить",
            command=self.apply_element_settings
        ).grid(row=1, column=4, padx=10)

    def update_callback_periodic_table(self):
        self.update_elements_tree()
        self.update_raw_data_tab()

    def show_periodic_table(self):
        """Открывает окно с периодической таблицей"""
        PeriodicTableWindow(self.root, self.config_data, self.update_callback_periodic_table)

    def create_raw_data_tab(self):
        """Создание вкладки сырых данных"""
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text="JSON данные")

        self.raw_text = ScrolledText(tab, wrap=NONE, font=("Consolas", 10))
        self.raw_text.pack(fill=BOTH, expand=True, padx=5, pady=5)

        ttk.Button(tab, text="Обновить из текста", command=self.update_from_raw).pack(side=BOTTOM, pady=5)

        # Первоначальное заполнение данных
        self.update_raw_data_tab()

    def browse_xml_folder(self):
        """Выбор папки с XML файлами"""
        folder = filedialog.askdirectory()
        if folder:
            self.xml_folder_var.set(folder)
            self.update_config_and_json()

    def on_element_select(self, event):
        """Обработка выбора элемента в таблице Treeview"""
        selected = self.element_tree.selection()
        if not selected:
            return

        element = self.element_tree.item(selected[0], "values")[0]

        # Заполняем поля параметров элемента
        self.coeff_var.set(self.config_data["coefficients"].get(element, 1.0))
        self.oxide_var.set(self.config_data["oxide_conversion"].get(element, False))

        thresholds = self.config_data["thresholds"].get(element, {})
        self.lower_var.set(thresholds.get("lower", 0.0000001))
        self.upper_var.set(thresholds.get("upper", 1000000.0))

    def apply_element_settings(self):
        """Применение изменённых параметров выбранного элемента"""
        selected = self.element_tree.selection()
        if not selected:
            messagebox.showwarning("Ошибка", "Выберите элемент для изменения")
            return

        element = self.element_tree.item(selected[0], "values")[0]

        try:
            # Валидация коэффициента
            coeff = self.coeff_var.get()
            if coeff <= 0:
                raise ValueError("Коэффициент должен быть положительным числом")

            # Валидация порогов
            lower = self.lower_var.get()
            upper = self.upper_var.get()
            if lower >= upper:
                raise ValueError("Нижний порог должен быть меньше верхнего")

            # Обновляем параметры элемента
            self.config_data["coefficients"][element] = coeff
            self.config_data["oxide_conversion"][element] = self.oxide_var.get()
            self.config_data["thresholds"][element] = {
                "lower": lower,
                "upper": upper
            }

            self.update_elements_tree()
            self.status_var.set(f"Обновлены параметры элемента: {element}")

            self.update_config_and_json()

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def update_elements_tree(self):
        """Обновление таблицы Treeview с текущими добавленными элементами"""
        if not hasattr(self, 'element_tree') or self.element_tree is None:
            return  # Выходим, если элемент еще не создан

        for item in self.element_tree.get_children():
            self.element_tree.delete(item)

        for element in sorted(self.config_data["coefficients"].keys()):
            coeff = self.config_data["coefficients"][element]
            oxide = "Да" if self.config_data["oxide_conversion"].get(element, False) else "Нет"
            lower = self.config_data["thresholds"].get(element, {}).get("lower", 0.000000001)
            upper = self.config_data["thresholds"].get(element, {}).get("upper", 1000000.0)

            # Функция для форматирования чисел
            def format_number(x):
                if x == 0:
                    return "0"
                abs_x = abs(x)
                if abs_x >= 10000 or abs_x <= 0.0001:
                    return "{:.1e}".format(x).replace("e-0", "e-").replace("e+0", "e+")
                return "{:.7f}".format(x).rstrip('0').rstrip('.') if '.' in "{:.7f}".format(x) else "{:.7f}".format(x)

            self.element_tree.insert("", END, values=(
                element,
                f"{coeff:g}",
                oxide,
                format_number(lower),
                format_number(upper)
            ))

        # Обновляем JSON данные на вкладке
        self.update_raw_data_tab()

    def update_raw_data_tab(self):
        """Обновление вкладки с сырыми JSON данными"""
        if hasattr(self, 'raw_text') and self.raw_text is not None:
            self.raw_text.delete("1.0", END)
            self.raw_text.insert("1.0", json.dumps(self.config_data, indent=4, ensure_ascii=False))
        else:
            return

    def update_config_and_json(self):
        """Обновляет конфигурацию и JSON данные"""

        if self.initializing:
            return  # Пропускаем обновление во время инициализации

        self.update_config_from_ui()
        self.update_raw_data_tab()

        # Помечаем как измененное
        self.modified = True

    def update_from_raw(self):
        """Обновление конфигурации из сырых JSON данных"""
        try:
            new_data = json.loads(self.raw_text.get("1.0", END))

            # Проверка структуры данных
            required_keys = {
                "xml_folder", "output_filename_format", "include_header",
                "header_fields", "coefficients", "oxide_conversion",
                "thresholds", "significant_figures", "delete_xml_after_processing"
            }

            if not all(key in new_data for key in required_keys):
                raise ValueError("Неверная структура конфигурационного файла")

            self.config_data = new_data
            self.update_ui_from_config()
            self.status_var.set("Конфигурация обновлена из JSON данных")

        except json.JSONDecodeError as e:
            messagebox.showerror("Ошибка", f"Неверный JSON формат:\n{str(e)}")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

    def update_ui_from_config(self):
        """Обновление интерфейса из текущей конфигурации"""

        # Временно отключаем обработчики
        self.initializing = True

        # Общие настройки
        self.xml_folder_var.set(self.config_data.get("xml_folder", ""))
        self.output_format_var.set(self.config_data.get("output_filename_format", ""))
        self.sig_fig_var.set(self.config_data.get("significant_figures", 3))
        self.delete_xml_var.set(self.config_data.get("delete_xml_after_processing", True))

        # Поля заголовка
        header_fields = self.config_data.get("header_fields", {})
        for field, var in self.header_vars.items():
            var.set(header_fields.get(field, False))

        # Включаем обработчики обратно
        self.initializing = False

        # Обновляем Treeview
        self.update_elements_tree()

        # Обновляем пример
        self.update_filename_example()

        # Сырые данные
        self.update_raw_data_tab()

    def update_config_from_ui(self):
        """Обновление конфигурации из значений интерфейса"""
        # Общие настройки
        self.config_data["xml_folder"] = self.xml_folder_var.get()
        self.config_data["output_filename_format"] = self.output_format_var.get()
        self.config_data["significant_figures"] = self.sig_fig_var.get()
        self.config_data["delete_xml_after_processing"] = self.delete_xml_var.get()

        # Поля заголовка
        self.config_data["header_fields"] = {
            field: var.get() for field, var in self.header_vars.items()
        }

    def open_config(self):
        """Открытие файла конфигурации"""
        file_path = filedialog.askopenfilename(
            filetypes=[("JSON файлы", "*.json"), ("Все файлы", "*.*")],
            title="Открыть файл конфигурации"
        )

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    new_data = json.load(f)

                # Проверка структуры файла
                required_keys = {
                    "xml_folder", "output_filename_format", "include_header",
                    "header_fields", "coefficients", "oxide_conversion",
                    "thresholds", "significant_figures", "delete_xml_after_processing"
                }

                if not all(key in new_data for key in required_keys):
                    raise ValueError("Неверная структура конфигурационного файла")

                self.config_data = new_data
                self.config_file = file_path
                self.update_ui_from_config()
                self.save_last_config()
                self.status_var.set(f"Открыт файл: {file_path}")

            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось открыть файл:\n{str(e)}")

    def save_config(self):
        """Сохранение конфигурации"""
        if not self.config_file:
            self.save_config_as()
            return

        try:
            self.update_config_from_ui()

            # Проверка обязательных полей
            if not self.xml_folder_var.get():
                raise ValueError("Не указана папка с XML файлами")

            if not self.config_data["coefficients"]:
                raise ValueError("Не выбрано ни одного элемента")

            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(self.config_data, f, indent=4, ensure_ascii=False)

            # Обновляем оригинальную конфигурацию
            self.original_config = json.dumps(self.config_data, sort_keys=True)
            self.modified = False

            self.save_last_config()
            self.status_var.set(f"Файл сохранён: {self.config_file}")

        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл:\n{str(e)}")

    def save_config_as(self):
        """Сохранение конфигурации с выбором имени файла"""
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON файлы", "*.json"), ("Все файлы", "*.*")],
            title="Сохранить файл конфигурации"
        )

        if file_path:
            self.config_file = file_path
            self.save_config()

    def load_last_config(self):
        """Загрузка последнего открытого файла конфигурации"""
        try:
            with open("last_config.txt", "r") as f:
                last_file = f.read().strip()
                if os.path.exists(last_file):
                    self.config_file = last_file
                    with open(last_file, "r", encoding="utf-8") as f2:
                        self.config_data = json.load(f2)
                        # Сохраняем оригинальную конфигурацию
                        self.original_config = json.dumps(self.config_data, sort_keys=True)
                    self.update_ui_from_config()
                    return True
        except:
            pass
        return False

    def check_for_changes(self):
        """Проверяет, были ли изменения в конфигурации"""
        if not self.original_config:
            return False

        current_config = json.dumps(self.config_data, sort_keys=True)
        return current_config != self.original_config

    def save_last_config(self):
        """Сохранение пути к последнему открытому файлу"""
        if self.config_file:
            try:
                with open("last_config.txt", "w") as f:
                    f.write(self.config_file)
            except:
                pass

    def show_help(self):
        """Отображение справки"""
        help_text = """Конфигуратор настроек химического анализа

1. Общие настройки:
   - Укажите папку с XML файлами
   - Настройте формат имени выходного файла
   - Выберите поля заголовка

2. Химические элементы:
   - Нажмите кнопку "Изменить список элементов" для выбора элементов
   - Настраивайте коэффициенты, конвертацию в оксиды и пороги значений

3. JSON данные:
   - Просмотр и редактирование сырых данных конфигурации

Файлы конфигурации сохраняются в формате JSON.
"""
        messagebox.showinfo("Справка", help_text)

    def run(self):
        """Запуск главного цикла"""
        self.root.mainloop()

    def on_close(self):
        """Обработчик закрытия окна"""
        if self.check_for_changes():
            response = messagebox.askyesnocancel(
                "Сохранение изменений",
                "Настройки были изменены. Сохранить изменения перед выходом?",
                icon=messagebox.WARNING
            )

            if response is None:  # Нажата Cancel
                return  # Отмена закрытия
            elif response:  # Нажата Yes
                self.save_config()

        # Закрываем окно
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = SettingsEditor(root)
    app.run()