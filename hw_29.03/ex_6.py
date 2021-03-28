try:
    with open('asdjlakdjaslkdjals.txt', 'r') as file:
        pass
except FileNotFoundError:
    print('Запрашиваемый файл не найден')

try:
    with open('//', 'r') as file:
        pass
except IsADirectoryError:
    print('Вы ввели название директории, а не файла')
except OSError:
    print('Проверьте корректность введённого пути до файла')
