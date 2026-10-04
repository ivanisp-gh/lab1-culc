# Py Lab 1 Calc

Небольшой проект на Python с двумя основными функциями:

- Калькулятор математических выражений
- Конвертер длины, температуры и веса

## Возможности

### Калькулятор

Поддерживаемые операции:

- Сложение: `+`
- Вычитание: `-`
- Умножение: `*`
- Деление: `/`
- Целочисленное деление: `//`
- Остаток от деления: `%`
- Скобки: `()`
- Отрицательные и дробные числа

Примеры:

```python
from toolkit.calculator import calculation

print(calculation("2+2*2"))
# 6.0

print(calculation("(2+2)*2"))
# 8.0

print(calculation("7//2"))
# 3.0

print(calculation("10%3"))
# 1.0
```

При попытке деления на ноль вызывается ошибка `DivisionByZeroError`.

```python
from toolkit.errors import DivisionByZeroError

try:
    calculation("5/0")
except DivisionByZeroError:
    print("На ноль делить нельзя")
```

## Конвертер величин

Конвертер поддерживает:

- Длину: `mm`, `cm`, `m`, `km`
- Температуру: `C`, `F`, `K`
- Вес: `g`, `kg`

Можно использовать точку или запятую в дробных числах.

### Примеры длины

```python
from toolkit.converter import convert

print(convert("1m"))
# 1000.0mm - 100.0cm - 1.0m - 0.001km

print(convert("2,5m"))
# 2500.0mm - 250.0cm - 2.5m - 0.0025km
```

Отрицательная длина вызывает ошибку `NegativeDistanceError`.

```python
from toolkit.errors import NegativeDistanceError

try:
    convert("-5m")
except NegativeDistanceError:
    print("Расстояние не может быть отрицательным")
```

### Примеры температуры

```python
print(convert("0C"))
# 0.0C - 32.0F - 273.15K

print(convert("32F"))
# 0.0C - 32.0F - 273.15K

print(convert("273.15K"))
# 0.0C - 32.0F - 273.15K
```

Также допускается запись со знаком градуса:

```python
print(convert("0 °C"))
# 0.0C - 32.0F - 273.15K
```

Температура ниже абсолютного нуля вызывает ошибку `BelowAbsoluteZeroError`.

```python
from toolkit.errors import BelowAbsoluteZeroError

try:
    convert("-274C")
except BelowAbsoluteZeroError:
    print("Температура ниже абсолютного нуля")
```

### Примеры веса

```python
print(convert("1kg"))
# 1000.0g - 1.0kg

print(convert("500g"))
# 500.0g - 0.5kg

print(convert("2,5 kg"))
# 2500.0g - 2.5kg
```

## Установка

Клонируйте репозиторий:

```bash
git clone [https://github.com/ivanisp-gh/lab1-culc.git](https://github.com/ivanisp-gh/lab1-culc.git)
```

Перейдите в папку проекта:

```bash
cd lab1-culc
```

## Запуск тестов

Для запуска тестов используется `pytest`.

Установите `pytest`:

```bash
pip install pytest
```

Запустите тесты из корневой папки проекта:

```bash
pytest
```

Или с более подробным выводом:

```bash
pytest -v
```

## Структура проекта

```text
lab1-culc/
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
├── pytest.ini.txt
└── README.md
```

## Ошибки

В проекте используются собственные ошибки:

- `DivisionByZeroError` — деление на ноль в калькуляторе
- `NegativeDistanceError` — отрицательная длина
- `BelowAbsoluteZeroError` — температура ниже абсолютного нуля
- `ValueError` — неверно введённое выражение или величина
