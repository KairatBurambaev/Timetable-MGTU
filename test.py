import requests
import json
import pytz
from datetime import datetime

def print_datetime():
    week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    tz = pytz.timezone('Asia/Yekaterinburg')
    day = datetime.now(tz)
    week_number = datetime.today().isocalendar()[1]
    today = week[day.weekday()]
    if week_number % 2:
        flag = 1
        print(f'Сегодня {today}   чётной недели')
    else:
        flag = 2
        print(f'Сегодня {today} нечётной недели')
    return today, flag

def group_name():
    name = str(input('Выберите Имя: '))
    s = requests.get(f'https://timetable.magtu.ru/api/v2/search?q={name}')
    data = s.json()
    if data == []:
        print('не найдено')
        exit()
    else:
        return data 

def nice_print(data):
    messege = '\n' + data['url'] + '\n' + 'Неделя: ' + data['schedule'][0]['week'] + '\n'
    for elem in data['schedule'][0]['days']:
        messege += '\n' + elem['day'] + '\n'
        for i in elem['events']:
            if elem['events'].count(i) > 0:
                messege += '-- ' + str(i['event_index']) + ' ' + i['course'] + ' ' + i['type'] + ' каб. ' + i['location'] + '\n'
            else: 
                messege += i + 'занятий нет' + '\n'

    messege1 = '\n' + 'Неделя: ' + data['schedule'][1]['week'] + '\n'
    for elem in data['schedule'][1]['days']:
        messege1 += '\n' + elem['day'] + '\n'
        for i in elem['events']:
            if elem['events'].count(i) > 0:
                messege1 += '-- ' + str(i['event_index']) + ' ' + i['course'] + ' ' + i['type'] + ' каб. ' + i['location'] + '\n'
            else:
                messege1 += i + 'занятий нет' + '\n'
    print('-'*31)
    print_datetime()
    print('-'*31)
    print(messege)
    print(messege1)

def print_res(data):
    messege = 'Результаты поиска:\n'
    if len(data) == 1:
        for elem in data:
            id = elem['id']
            if elem['url'][-1] not in 'АБВГДАЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                s = requests.get(f'https://timetable.magtu.ru/api/v2/groups/{id}/schedule')
                data = s.json()
            else:
                s = requests.get(f'https://timetable.magtu.ru/api/v2/teachers/{id}/schedule')
                data = s.json()
            nice_print(data)
            return data  
    else: 
        for elem in data:
            messege += elem['url'] + '\n'       
        print(messege)
        print_res(group_name())

print_res(group_name())