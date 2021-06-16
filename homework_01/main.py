"""
Домашнее задание №1
Функции и структуры данных
"""
def power_numbers(num):
    print('num', num)
    return num ** 2

nums = (power_numbers(i) for i in range(5))
print(list(nums))


def filter_numbers(numbers):
    num_list = []
    for num in numbers:
        if num % 2 != 0:
            num_list.append(num)
    return num_list
odds = filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(odds)

def filter_numbers(numbers):
    num_list = []
    for num in numbers:
        if num % 2 == 0:
            num_list.append(num)
    return num_list
even = filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(even)

