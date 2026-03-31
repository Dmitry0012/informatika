# TODO Напишите функцию find_common_participants
def find_common_participants(g1, g2, arg=","): #создаём функцию, которая получает две строки с участниками
    l1 = g1.split(arg) #разбиваем первую строку на список участников и заносим в переменную l1
    l2 = g2.split(arg) #разбиваем вторую строку на список участников и заносим в переменную l2
    c = list(set(l1).intersection(set(l2))) #находим общих участников в двух списках (пересечение списков) и заносим в переменную c
    return sorted(c) #сортируем участников в алфавитном порядке и возвращаем в переменную c


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"


print(find_common_participants(participants_first_group, participants_second_group, "|")) #выводим список
# TODO Провеьте работу функции с разделителем отличным от запятой
