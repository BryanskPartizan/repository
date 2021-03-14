import math
import random

def geron_area(side_one, side_two, side_three):
    half_perimeter = 0.5 * (side_one + side_two + side_three)
    area = math.sqrt(half_perimeter * (half_perimeter - side_one) * (half_perimeter - side_two) * (half_perimeter - side_three))
    return round(area, 2)

def sin_area(side_one, side_two, degree):
    radian = (math.pi / 180) * degree
    area = 0.5 * side_one * side_two * math.sin(radian)
    return round(area, 2)

def number_from_interval(min_, max_):
    number = random.randint(min_, max_)
    print(f'Сформировано число: {number}')
    return number

if __name__ == "__main__":
    print(geron_area(3, 4, 5))
    print(sin_area(10, 12, 30))