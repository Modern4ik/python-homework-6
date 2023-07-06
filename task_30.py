# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

def get_value_from_user(message: str) -> int:
    flag = True

    while flag:
        try:
            if message == "Введите кол-во элементов арифм. прогрессии: ":
                user_value = int(input(message))

                if user_value > 0:
                    flag = False
                else:
                    print("Кол-во элементов не может быть равно или меньше 0!")
            else:
                user_value = int(input(message))

                flag = False
        except ValueError:
                print("Ошибка ввода!Введите целое число!")
    
    return user_value

def get_progression(first_el: int, step: int, el_count: int) -> list:
    return [first_el + (i - 1) * step for i in range(1, el_count + 1)]

def print_report(res: list) -> None:
    print(f"С учётом входных данных получена арифм. прогрессия -> {res}")

#############################################################################

first_elem = get_value_from_user("Введите значение первого элемента прогрессии: ")
step_value = get_value_from_user("Введите шаг арифм. прогрессии: ")
elem_count = get_value_from_user("Введите кол-во элементов арифм. прогрессии: ")

result = get_progression(first_elem, step_value, elem_count)

print()
print_report(result)