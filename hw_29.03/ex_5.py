import random

number_list = [random.randint(-1000000, 10000000) for i in range(20)]

with open('numbers.txt', 'w') as result_file:
    for number in number_list:
        result_file.write(str(number) + ' ')

with open('numbers.txt', 'r') as log_file:
    num_string = log_file.read()
    numbers_list = [int(number) for number in num_string.split()]
    print(f'Сумма чисел: {sum(numbers_list)}')
    print(f'Среднее арифметическое: {sum(numbers_list) / len(numbers_list)}')