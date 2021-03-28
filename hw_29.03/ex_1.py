
days = []

with open("weekday_Eng.txt", 'r') as week_days:    
    for day in week_days:
        days.append(day.strip())
    days.sort()

        
with open("sort_weekday_Eng.txt", 'w') as result_file:
    for day in days:
        result_file.write(day + '\n')
