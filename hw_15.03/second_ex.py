import math
import helpfmodel

def f(min_, max_):
    x = helpfmodel.number_from_interval(min_, max_)
    a = helpfmodel.number_from_interval(min_, max_)
    b = helpfmodel.number_from_interval(min_, max_)

    y = round(math.log(x**2 + a* b))
    print(f'Значение функции: {y}')
    return y % 7

def day_count(number):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']
    numbers = [i for i in range(1, 8)]
    day_dict = {number: day for (number, day) in zip(numbers, days)}

    if number == 0:
        number = 7
    return day_dict[number]


if __name__ == "__main__":
    min_ = int(input('write a min number of interval: '))
    max_ = int(input('write a max number of interval: '))

    print(day_count(f(min_, max_)))
