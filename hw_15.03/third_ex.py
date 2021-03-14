import health

if __name__ == "__main__":
    mass = float(input('input a mass in kg: '))
    height = float(input('input a height in meter: '))
    bmi = health.bmi_count(mass, height)

    print(f'ИМТ тела составил: {bmi}')
    print(f'Вывод: {health.bmi_analysis(bmi)}')
