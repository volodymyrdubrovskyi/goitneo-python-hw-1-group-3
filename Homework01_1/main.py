from datetime import datetime, timedelta
from collections import defaultdict

data = [
    {"name": "Kaitlyn Espinoza",    "birthday": datetime(1955, 10, 28)},
    {"name": "Cameron Vazquez",     "birthday": datetime(1952, 11, 27)},
    {"name": "Aliza Schmidt",       "birthday": datetime(1956, 7, 27)},
    {"name": "Sierra Jaramillo",    "birthday": datetime(1975, 12, 24)},
    {"name": "Yara Stein",          "birthday": datetime(1983, 1, 7)},
    {"name": "Creed Patel",         "birthday": datetime(2000, 4, 29)},
    {"name": "Madeline Nichols",    "birthday": datetime(1998, 8, 20)},
    {"name": "Sierra Jaramillo",    "birthday": datetime(1987, 10, 15)},
    {"name": "Atlas Moss",          "birthday": datetime(1999, 10, 14)},
    {"name": "Bianca McCullough",   "birthday": datetime(2002, 10, 18)},
    {"name": "Tessa Hernandez",     "birthday": datetime(1971, 10, 15)},
    {"name": "Celia Marquez",       "birthday": datetime(1991, 2, 15)}
]

# создаем список дней недели от текущего дня
def create_weekdays_order(today_date):
    weekdays_order_dict = defaultdict(list)
    for i in range(7):
        dt = today_date + timedelta(days=i)
        day = dt.strftime("%A")
        weekdays_order_dict[i] = day
    return weekdays_order_dict

# определяем интервал дат для празднования
def dates_for_party(data, start_date):
    day_of_week = int(start_date.strftime("%w"))
    if day_of_week == 1:  # понедельник. Нужно не забыть тех, кто в выходные родился
        start_date = start_date - timedelta(days=2)
    elif day_of_week == 0:  # воскресенье: считаем с субботы и до пятницы включительно
        start_date = start_date - timedelta(days=1)
    end_date = start_date + timedelta(days=6)
    return [start_date, end_date]

# список людей с днями рождения со start_date по end_date включительно
def get_party_people(data, start_date, end_date):
    party_people = list()
    for d in data:
        dt = d['birthday']
        current_year = int(start_date.strftime("%Y"))
        birthday_this_year = dt.replace(year=current_year)
        if start_date.strftime("%Y") != end_date.strftime("%Y"): # в неделе есть новый год
            if birthday_this_year.strftime("%m") == '01':
                birthday_this_year = dt.replace(year=current_year+1)
        if birthday_this_year >= start_date and birthday_this_year <= end_date:
            party_people.append(d)
    return party_people

# получаем распределение по дням недели
def get_birthday_per_week(data, start_date, end_date):
    res = defaultdict(list)
    for d in data:
        dt = d['birthday']
        current_year = int(start_date.strftime("%Y"))
        birthday_this_year = dt.replace(year=current_year)
        if start_date.strftime("%Y") != end_date.strftime("%Y"): # в неделе есть новый год
            if birthday_this_year.strftime("%m") == '01':
                birthday_this_year = dt.replace(year=current_year+1)
        day = birthday_this_year.strftime("%A")
        res[day].append(d["name"])
    return res

# вывод в консоль
def return_result(weekdays_order, group_week):
    group_week['Monday'] = group_week['Saturday'] + group_week['Sunday'] + group_week['Monday']
    for wd, wdn in weekdays_order.items():
        if group_week[wdn]:
            line_bearthday_people = ", ".join(group_week[wdn])
            if wdn != 'Saturday' and wdn != 'Sunday':
                print(f"{wdn:<9} : {line_bearthday_people}")
    

def main():
    # первоначально код писался от текущего дня включительно. Сегодня прочитал, что от "завтрашнего". Прибавим денек к текущей дате )
    today_date = datetime.now() + timedelta(days=1)
    #print(today_date)
    #today_date = datetime(2023, 10, 13)
    weekdays_order = (create_weekdays_order(today_date))
    #print(weekdays_order, '\n')
    start_date = dates_for_party(data, today_date)[0]
    end_date = dates_for_party(data, today_date)[1]
    party_people = get_party_people(data, start_date, end_date)
    #print(party_people, '\n')
    group_week = get_birthday_per_week(party_people, start_date, end_date)
    #print(group_week)
    return_result(weekdays_order, group_week)

if __name__ == "__main__":
    main()