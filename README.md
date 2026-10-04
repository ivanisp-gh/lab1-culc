# py-lab1-calc

Консольное приложение с двумя командами:

- `calc` — вычисляет математические выражения;
- `convert` — переводит длину, температуру и массу.

## Структура проекта

```text
py-lab1-calc/
├── src/
│   └── toolkit/
│       ├── __init__.py
│       ├── __main__.py
│       ├── calculator.py
│       ├── converter.py
│       └── errors.py
├── tests/
│   ├── test_calculator.py
│   └── test_converter.py
├── pyproject.toml
└── README.md
```

## Требования

- Python 3.10 или новее
- `pytest` для запуска тестов

Проверить версию Python:

```powershell
python --version
```

Установить pytest:

```powershell
python -m pip install pytest
```

## Запуск проекта

Код проекта находится в папке `src`, поэтому перед запуском нужно добавить её в путь поиска Python.

Откройте PowerShell в корне проекта:

```powershell
cd "C:\Users\yariv\OneDrive\Desktop\labs\py-lab1-calc"
```

В этом же окне терминала выполните:

```powershell
$env:PYTHONPATH = "$PWD\src"
```

Эту команду нужно выполнить один раз после открытия нового окна PowerShell. Она действует до закрытия терминала.

## Команда calc

Общий вид:

```powershell
python -m toolkit calc "выражение"
```

Примеры:

```powershell
python -m toolkit calc "2+2*2"
python -m toolkit calc "(2+2)*2"
python -m toolkit calc "10 / 2 + 3"
python -m toolkit calc "7//2"
python -m toolkit calc "7%2"
```

Поддерживаемые операции:

```text
+   сложение
-   вычитание
*   умножение
/   деление
//  целочисленное деление
%   остаток от деления
()  скобки
```

## Команда convert

Общий вид:

```powershell
python -m toolkit convert "значение и единица"
```

### Длина

Поддерживаются: `mm`, `cm`, `m`, `km`.

```powershell
python -m toolkit convert 80mm
python -m toolkit convert 15cm
python -m toolkit convert 2.5m
python -m toolkit convert 3km
```

### Масса

Поддерживаются: `g`, `kg`.

```powershell
python -m toolkit convert 500g
python -m toolkit convert 2.5kg
python -m toolkit convert "2,5 kg"
```

### Температура

Поддерживаются: `C`, `F`, `K`.

```powershell
python -m toolkit convert 25C
python -m toolkit convert 32F
python -m toolkit convert 273.15K
python -m toolkit convert "0 C"
```

Для значений с пробелом обязательно используйте кавычки:

```powershell
python -m toolkit convert "2,5 kg"
python -m toolkit convert "32 F"
```

## Справка

```powershell
python -m toolkit --help
```

или:

```powershell
python -m toolkit
```

## Запуск тестов

Сначала в терминале установите путь к папке `src`:

```powershell
$env:PYTHONPATH = "$PWD\src"
```

Затем запустите все тесты:

```powershell
python -m pytest -v
```

Запуск только тестов калькулятора:

```powershell
python -m pytest tests/test_calculator.py -v
```

Запуск только тестов конвертера:

```powershell
python -m pytest tests/test_converter.py -v
```
