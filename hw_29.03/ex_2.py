

dict_numbers = {'one': 'один', 'two' : 'два', 'three' : 'три', 'four' : 'четыре', 'five' : 'пять',
                'six' : 'шесть', 'seven' : 'семь', 'eight' : 'восемь', 'nine' : 'девять', 'ten' : 'десять'}

with open('numberE.txt', 'r') as numbers_eng, open('numberR.txt', 'w') as numbers_rus:
    for number in numbers_eng:
        numbers_rus.write(dict_numbers[number.strip()] + '\n')
