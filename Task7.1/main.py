import requests


ip = input('Введите IP-адрес: ')
response = requests.get('http://ip-api.com/json/' + ip)
response_json = response.json()
if 'country' in response_json:
    print('Страна IP-адреса:', response.json()['country'])
else:
    match response_json['message']:
        case 'invalid query':
            print('Таĸого IP не существует')
        case 'private range':
            print('IP-адрес не является публичным')
        case 'reserved range':
            print('IP-адрес находится в зарезервированном диапазоне')
        case _:
            print(response_json)
