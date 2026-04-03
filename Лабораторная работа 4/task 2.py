# TODO импортировать необходимые молули
import csv #импортируем модуль CSV
import json #импортируем модуль JSON

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, "r") as filecsv: #открываем файл input.csv в режиме чтения
        readcsv = csv.DictReader(filecsv, delimiter=",") #читаем CSV файл и заносим в переменную readcsv, превращая каждую строку в словарь
        a = [] #создаём пустой список в переменной a
        for b in readcsv: #перебираем все строки в readcsv
            a.append(b) #добавляем словарь b в конец списка a
    # TODO считать содержимое csv файла

    with open(OUTPUT_FILENAME, "w") as filejson: #открываем файл output.json в режиме записи
        json.dump(a, filejson, ensure_ascii=False, indent=4) #записываем объект питон a в JSON файл
    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
