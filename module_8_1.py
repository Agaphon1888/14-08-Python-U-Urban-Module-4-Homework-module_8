# Домашнее задание по уроку "Try и Except".
# Задание "Программистам всё можно".

def add_everything_up(a, b):
    try:
        # Проверка типов a и b
        if a is None or b is None:
            raise TypeError("Одно или оба аргумента равны None")

        if isinstance(a, str) and isinstance(b, str):
            return a + b  # Сложение двух строк
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = a + b
            # Возвращаем результат с тремя знаками после запятой
            return f'{result:.3f}'  # Форматирование числа
        else:
            # Если типы разные, возвращаем строковое представление
            return str(a) + str(b)

    except TypeError as e:
        return f'Ошибка: Неподдерживаемый тип данных - {e}'


# Примеры использования
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215
print(add_everything_up(123.456, 7))  # Вывод: 130.456
print(add_everything_up(None, 5))  # Вывод: Ошибка: Неподдерживаемый тип данных - Одно или оба аргумента равны None
print(add_everything_up(3, None))  # Вывод: Ошибка: Неподдерживаемый тип данных - Одно или оба аргумента равны None
