with open("nums.txt", 'r') as numbers:
    num_string = numbers.read()
    numbers_list = [int(number) for number in num_string.split(' ')]
    print(f'Сумма чисел: {sum(numbers_list)}')
    print(f'Среднее арифметическое: {sum(numbers_list) / len(numbers_list)}')