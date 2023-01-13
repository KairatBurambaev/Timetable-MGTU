import requests
import json
import pytz
from datetime import datetime

def get_datetime():
    week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
    tz = pytz.timezone('Asia/Yekaterinburg')
    day = datetime.now(tz)
    week_number = datetime.today().isocalendar()[1]
    today = week[day.weekday()]
    if week_number % 2:
        return (f'Сегодня {today}   чётной недели')
    else:
        return (f'Сегодня {today} нечётной недели')

def search_by_name(name):
    s = requests.get(f'https://timetable.magtu.ru/api/v2/search?q={name}')
    data = s.json()
    return data 

def nice_print_schedule(data):
    message = get_datetime() + '\n'
    message += '\n' + data['url'] + '\n' + 'Неделя: ' + data['schedule'][0]['week'] + '\n'
    for elem in data['schedule'][0]['days']:
        message += '\n' + elem['day'] + '\n'
        for i in elem['events']:
            if elem['events'].count(i) > 0:
                message += '* ' + str(i['event_index']) + ' ' + i['course'] + ' ' + i['type'] + ' каб. ' + i['location'] + '\n'
            else: 
                message += i + 'занятий нет' + '\n'

    message += '\n' + 'Неделя: ' + data['schedule'][1]['week'] + '\n'
    for elem in data['schedule'][1]['days']:
        message += '\n' + elem['day'] + '\n'
        for i in elem['events']:
            if elem['events'].count(i) > 0:
                message += '* ' + str(i['event_index']) + ' ' + i['course'] + ' ' + i['type'] + ' каб. ' + i['location'] + '\n'
            else:
                message += i + 'занятий нет' + '\n'
    return message

def get_group_schedule(group_id):
    s = requests.get(f'https://timetable.magtu.ru/api/v2/groups/{group_id}/schedule')
    data = s.json()
    return data

def get_teacher_schedule(teacher_id):
    s = requests.get(f'https://timetable.magtu.ru/api/v2/teachers/{teacher_id}/schedule')
    data = s.json()
    return data

def get_schedule_by_search_item(item):
    if item['type'] == 'group':
        return get_group_schedule(item['id'])
    else:
        return get_teacher_schedule(item['id'])

def nice_print_search_results(items):
    message = f'Найдено {len(items)} результатов:\n'
    for elem in items:
        message += elem['name'] + '\n'
    return message

def main(search_query):
    search_result = search_by_name(search_query)
    length = len(search_result)
    if length == 0:
        return 'не найдено'
    elif length == 1:
        schedule = get_schedule_by_search_item(search_result[0])
        return nice_print_schedule(schedule)
    else:
        return nice_print_search_results(search_result)

if __name__ == '__main__': 
    print(main(input('Введите имя: ')))