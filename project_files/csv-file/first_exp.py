import csv

class Company(object):
    def __init__(self, name, date, capital, owner):
        self.name = name
        self.date = date
        self.capital = capital
        self.owner = owner

    def snow_info(self):
        print(f'==========INFO-START=========')
        print(f'name is {self.name}')
        print(f'date of reg. is {self.date}')
        print(f'capital is {self.capital}')
        print(f'owner are: {self.owner}')
        print(f'==========INFO-END===========')


def reader(file_name):
    companies = []
    reader = csv.DictReader(file_name, delimiter=";")
    for line in reader:
        companies.append(Company(*line.values()))
    return companies


def sort_by_capital(companies):
    companies.sort(key=lambda company: int(company.capital), reverse=True)
    return companies   


def writer(path, fieldnames, data):
    with open(path, 'w', newline='') as out_file:
        writer = csv.DictWriter(out_file, delimiter=';', fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


def data_creator(companies):
    data = []
    result_data = []
    data.append('name;capital'.split(';'))

    for index in range(len(companies)):
        data_string = companies[index].name + ';' + companies[index].capital
        data.append(data_string.split(';'))

    fieldnames = data[0]
    for values in data[1:]:
        sub_dict = dict(zip(fieldnames, values))
        result_data.append(sub_dict)
    return fieldnames, result_data


if __name__ == "__main__":
    with open("datalist.csv", 'r') as file:
        companies = reader(file)

    fieldnames = data_creator(sort_by_capital(companies))[0]
    data = data_creator(sort_by_capital(companies))[1]
    path = 'result_data.csv'

    writer(path, fieldnames, data)
    




