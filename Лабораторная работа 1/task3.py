list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# индекс середины
middle_index = len(list_players) // 2 #количество людей в команде

first_team = list_players[:middle_index] #список людей в первой команде
second_team = list_players[middle_index:] #список людей во второй команде

print(first_team)
print(second_team)
