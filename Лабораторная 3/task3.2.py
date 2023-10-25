# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, delimiter = ','):
    group1 = group1.split(delimiter)
    group2 = group2.split(delimiter)
    general = []
    for student in group2:
        if student in group1:
            general.append(student)
    return sorted(general)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, delimiter = '|'))
# TODO Провеьте работу функции с разделителем отличным от запятой
