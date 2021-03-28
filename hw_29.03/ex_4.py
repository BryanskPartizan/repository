import csv


class Human(object):
    def __init__(self, first_name, last_name, father_name, gender, height, weight, age):
        self.first_name = first_name
        self.last_name = last_name
        self.father_name = father_name
        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.power_factor = self.height + self.weight

    def snow_info(self, file_name=None):
        print(f'==================START-INFO==============', file=file_name)
        print(f'ФИО: {self.first_name} {self.last_name[0]}. {self.father_name[0]}.', file=file_name)
        print(f'Пол: {self.gender}, Рост: {self.height}, Вес: {self.weight}, Возраст: {self.age}', file=file_name)
        print(f'Коэффициент силы: {self.power_factor}', file=file_name)
        print(f'==================END-INFO================', file=file_name)
        print(f'\n', file=file_name)
        return '\n'


def reader(file):
    reader = csv.DictReader(file, delimiter = ';')
    first_names = []
    last_names = []
    father_names = []
    genders = []
    heights = []
    weights = []
    ages = []
    for line in reader:
        first_names.append(line['\ufeffФамилия'])
        last_names.append(line['Имя'])
        father_names.append(line['Отчество'])
        genders.append(line['Пол'])
        heights.append(int(line['Рост']))
        weights.append(int(line['Вес']))
        ages.append(int(line['Возраст']))
    data = [first_names, last_names, father_names, genders, heights, weights, ages]
    return data

def object_creator(data):
    objects = []
    for index in range(len(data[0])):
        objects.append(Human(data[0][index], data[1][index], data[2][index], data[3][index],
        data[4][index], data[5][index], data[6][index]))
    return objects

def max_pow_fact(objects):
    max_object_pf = 0
    for object_ in objects:
        if max_object_pf < object_.power_factor:
            max_object_pf = object_.power_factor
            max_object = object_
    return max_object

def the_youngest_woman(objects):
    min_age = 100
    for object_ in objects:
        if object_.gender == 'Ж':
            if min_age > object_.age:
                min_object = object_
                min_age = object_.age
    return min_object

def the_highest_woman(objects):
    max_height = 0
    for object_ in objects:
        if object_.gender == 'Ж':
            if max_height < object_.height:
                max_height = object_.height
                max_object = object_
    return max_object


if __name__ == "__main__":
    with open("human.csv", 'r', encoding='utf8') as file:
        data = reader(file)
    human_list = object_creator(data)
    
    with open("results.txt", 'w') as result_file:
        print(f'Самый максимальный коэффициент силы: ', file=result_file)
        result_file.write(max_pow_fact(human_list).snow_info(result_file))
        print(f'Самая молодая женщина: ', file=result_file)
        result_file.write(the_youngest_woman(human_list).snow_info(result_file))
        print(f'Самая высокая женщина: ', file=result_file)
        result_file.write(the_highest_woman(human_list).snow_info(result_file))


