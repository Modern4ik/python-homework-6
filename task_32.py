# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def get_value_from_user(message: str) -> int:
    flag = True

    while flag:
        try:
            user_value = int(input(message))

            flag = False
        except ValueError:
            print("Вы должны ввести целое число!")
    
    return user_value

def get_list() -> list:
    return [randint(-10, 10) for _ in range(15)]

def get_indexes_by_range(lst: list, first_border: int, second_border: int) -> dict:         # Тут сделал проверку для того, чтобы если у нас первая граница
    if first_border > second_border:                                                        # окажется больше, чем вторая, то мы должны идти от большего к 
        return {f"index {index}": lst[index] for index in range(len(lst))                   # меньшему. Так как по дефолту у функции range шаг равен 1, то
                 if lst[index] in range(first_border, second_border - 1, - 1)}              # нужно было сделать отрицательный шаг равный - 1 и отнять у второй
    else:                                                                                   # границы единицу, чтобы её включало.
        return {f"index {index}": lst[index] for index in range(len(lst))
                 if lst[index] in range(first_border, second_border + 1)}

def print_report(res) -> None:
    if len(res) > 0:
        print(f"Индексы элементов с значениями, попавшими в заданный диапозон -> {res}")
    else:
        print("Ни один элемент данного массива не попал в заданный диапозон!")

########################################################################################

numb_list = get_list()
print(f"Исходный список чисел -> {numb_list}")

border_1 = get_value_from_user("Введите первую границу диапозона: ")
border_2 = get_value_from_user("Введите вторую границу диапозона: ")

result = get_indexes_by_range(numb_list, border_1, border_2)

print()
print_report(result)