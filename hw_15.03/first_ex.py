import helpfmodel

if __name__ == "__main__":

    side_one = float(input('write a first side: '))
    side_two = float(input('wtire a second side: '))
    side_three = float(input('write a third side: '))
    degree = float(input('write a degree between the first and second sides: '))

    print(f'area of triangle with sides {side_one}, {side_two}, {side_three} are: {helpfmodel.geron_area(side_one, side_two, side_three)} with Geron-method')
    print(f'area of triangle with sides {side_one}, {side_two} and {degree} degrees between them are: {helpfmodel.sin_area(side_one, side_two, degree)}')