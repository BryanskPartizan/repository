

def bmi_count(mass, height):
    bmi = round(mass / (height ** 2), 1)
    return bmi

def bmi_analysis(bmi):
    if bmi < 16:
        answer = 'Выраженный дефицит массы тела'
    elif 16 <= bmi < 18.5:
        answer = 'Недостаточная масса тела'
    elif 18.5 <= bmi < 25:
        answer = 'Нормальная масса тела'
    elif 25 <= bmi < 30:
        answer = 'Избыточная масса тела'
    elif 30 <= bmi < 35:
        answer = 'Ожирение 1-ой степени'
    elif 35 <= bmi < 40:
        answer = 'Ожирение 2-ой степени'
    elif bmi >= 40:
        answer = 'Ожирение 3-ей степени'
    return answer
