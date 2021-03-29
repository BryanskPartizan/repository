import csv

data = open('data.csv', 'r')
data_csv  = csv.reader(data, delimiter=';')
data_list = [row for row in data_csv]

print(data_list)