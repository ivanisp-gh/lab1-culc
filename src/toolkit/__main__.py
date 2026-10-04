import sys

from toolkit.calculator import calculation
from toolkit.converter import convert
from toolkit.errors import ToolkitError


def main() -> None:
    argv = sys.argv[1:]

    if not argv or argv[0] == "--help":
        print("Использование: python -m toolkit <команда> [аргументы]")
        print("Команды: calc EXPRESSION | convert VALUE | --help")
        print("Пример: python -m toolkit convert 80mm")
        sys.exit(0)

    command = argv[0]
    args = argv[1:]

    try:
        if command == "calc":
            if not args:
                raise ToolkitError("Укажите выражение для calc")
            expression = " ".join(args)
            result = calculation(expression)
            print(result)

        elif command == "convert":
            if not args:
                raise ToolkitError("Укажите значение для convert")
            value_with_unit = args[0]
            result = convert(value_with_unit)
            print(result)

        else:
            raise ToolkitError(f"Неизвестная команда: {command}")

    except ToolkitError as error:
        print(f"Ошибка: {error}", file=sys.stderr)
        sys.exit(2)


if __name__ == "__main__":
    main()