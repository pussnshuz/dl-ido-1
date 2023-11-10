import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as f:
        lines = [line for line in csv.DictReader(f)]

    ...  # TODO Сериализовать в файл с отступами равными 4
    file = open(OUTPUT_FILENAME, 'w', encoding='utf8')
    json_lines = json.dumps(lines, indent=4)
    file.write(json_lines)
    file.close()


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
