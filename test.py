import requests
import json

def group_name():
    name = str(input('Введите Имя: '))
    s = requests.get(f'https://timetable.magtu.ru/api/v2/search?q={name}')
    data = s.json()
    if data == []:
        print('не найдено')
        exit()
    else:
        return data 

def print_result(data):
    messege = 'Результаты поиска:\n'
    if flag == 1:
        for elem in data:
            if elem['url'][-1] not in 'АБВГДАЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                messege += elem['url'] + ' id: ' + str(elem['id']) + '\n'
    elif flag == 2:
        for elem in data:
            if elem['url'][-1] in 'АБВГДАЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ':
                messege += elem['url'] + ' id: ' + str(elem['id']) + '\n'
    return messege

flag = int(input('1 - Поиск группы, 2 - Поиск преподавателя: '))

print(print_result(group_name()))

def schedule():
    id = int(input('Введите id: '))
    if flag == 1:
        s = requests.get(f'https://timetable.magtu.ru/api/v2/groups/{id}/schedule')
        data = s.json()
    elif flag == 2:
        s = requests.get(f'https://timetable.magtu.ru/api/v2/teachers/{id}/schedule')
        data = s.json()
    return data

def nice_print(data):
    messege = data['url'] + '\n' + 'Неделя: ' + data['schedule'][0]['week'] + '\n'
    for elem in data['schedule'][0]['days']:
        messege += elem['day'] + '\n'
        for i in elem['events']:
            if elem['events'].count(i) > 0:
                messege += str(i['event_index']) + ' ' + i['course'] + ' ' + i['type'] + ' каб. ' + i['location'] + '\n'
            else: 
                messege += 'занятий нет' + '\n'

    messege1 = 'Неделя: ' + data['schedule'][1]['week'] + '\n'
    for elem in data['schedule'][1]['days']:
        messege1 += elem['day'] + '\n'
        for i in elem['events']:
            if elem['events'].count(i) > 0:
                messege1 += str(i['event_index']) + ' ' + i['course'] + ' ' + i['type'] + ' каб. ' + i['location'] + '\n'
            else:
                messege1 += 'занятий нет' + '\n'

    print(messege)
    print(messege1)

print(nice_print(schedule()))