# Домашнее задание по теме "Сложные моменты и исключения в стеке вызовов функции".
# Задача "План перехват".

def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            # Попытка добавить число
            if item == '' or item == None:
                raise ValueError('Некорректный тип данных для подсчёта суммы')
            result += float(item)
        except (ValueError, TypeError) as e:
            # Обработка некорректных данных
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')

    return result, incorrect_data


def calculate_average(numbers):
    try:
        # Проверка на корректность типа данных
        if not isinstance(numbers, (list, tuple)):
            raise TypeError('В numbers записан некорректный тип данных')

        # Подсчёт суммы и некорректных данных, используя personal_sum
        total_sum, incorrect_data_count = personal_sum(numbers)

        # Расчёт количества корректных чисел
        count_of_numbers = len(numbers) - incorrect_data_count

        # Обработка деления на ноль
        if count_of_numbers == 0:
            return 0

        return total_sum / count_of_numbers

    except ZeroDivisionError:
        return 0
    except TypeError as e:
        print(e)
        return None


# Примеры вызова функции calculate_average
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать