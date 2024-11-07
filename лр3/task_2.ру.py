# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, k=","):
    first = set(participants_first_group.split(k))
    second = set(participants_second_group.split(k))
    common_set = first.intersection(second)
    common_set = list(common_set)
    return (common_set)
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, k="|"))

# TODO Провеьте работу функции с разделителем отличным от запятой
