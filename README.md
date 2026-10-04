# py-lab1-calc

Мой проект — это калькулятор и конвертер величин.

Калькулятор умеет считать примеры, а конвертер переводит длину, вес и температуру.

## Что есть в проекте

```text
src/toolkit/
```

В этой папке находится весь код программы.

```text
tests/
```

В этой папке находятся тесты.

## Установка

Для работы нужен Python и библиотека pytest.

Установить pytest:

```powershell
python -m pip install pytest
```

## Запуск программы

Сначала нужно открыть терминал в папке проекта:

```powershell
cd "...\py-lab1-calc"
```

Потом нужно написать эту команду:

```powershell
$env:PYTHONPATH = "$PWD\src"
```

После этого можно запускать программу.

## Калькулятор

Пример:

```powershell
python -m toolkit calc "2+2*2"
```

Ещё примеры:

```powershell
python -m toolkit calc "(2+2)*2"
python -m toolkit calc "10/2"
python -m toolkit calc "7%2"
```

Калькулятор умеет работать с:

```text
+
-
*
/
//
%
()
```

## Конвертер

Примеры перевода длины:

```powershell
python -m toolkit convert 10cm
python -m toolkit convert 2m
python -m toolkit convert 3km
```

Примеры перевода веса:

```powershell
python -m toolkit convert 500g
python -m toolkit convert 2kg
```

Примеры перевода температуры:

```powershell
python -m toolkit convert 25C
python -m toolkit convert 32F
python -m toolkit convert 273.15K
```

Если есть пробел, нужно писать значение в кавычках:

```powershell
python -m toolkit convert "2,5 kg"
```

## Тесты

Запустить все тесты:

```powershell
python -m pytest -v
```

Запустить только тесты калькулятора:

```powershell
python -m pytest tests/test_calculator.py -v
```

Запустить только тесты конвертера:

```powershell
python -m pytest tests/test_converter.py -v
```

## Помощь

```powershell
python -m toolkit --help
```
