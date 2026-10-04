# py-lab1-calc

## Описание

Программа представляет собой калькулятор и конвертер величин.

Калькулятор вычисляет математические выражения, а конвертер переводит единицы длины, массы и температуры.

## Структура программы

```text
src/toolkit/
```

В этой папке находится весь код программы.

```text
tests/
```

В этой папке находятся тесты программы.

## Установка

Для работы программы необходимы Python и библиотека `pytest`.

Установить `pytest` можно командой:

```powershell
python -m pip install pytest
```

## Запуск программы

Сначала откройте терминал в папке программы:

```powershell
cd "...\py-lab1-calc"
```

Затем выполните команду:

```powershell
$env:PYTHONPATH = "$PWD\src"
```

После этого программу можно запускать.

## Калькулятор

Пример вычисления:

```powershell
python -m toolkit calc "2+2*2"
```

Другие примеры:

```powershell
python -m toolkit calc "(2+2)*2"
python -m toolkit calc "10/2"
python -m toolkit calc "7%2"
```

Калькулятор поддерживает следующие операции:

```text
+
-
*
/
//
%
()
```

## Конвертер величин

### Перевод длины

```powershell
python -m toolkit convert 10cm
python -m toolkit convert 2m
python -m toolkit convert 3km
```

### Перевод массы

```powershell
python -m toolkit convert 500g
python -m toolkit convert 2kg
```

### Перевод температуры

```powershell
python -m toolkit convert 25C
python -m toolkit convert 32F
python -m toolkit convert 273.15K
```

Если между числом и единицей измерения есть пробел, значение нужно заключить в кавычки:

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

## Справка

Для просмотра справки программы выполните команду:

```powershell
python -m toolkit --help
```
