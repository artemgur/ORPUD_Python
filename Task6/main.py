import re


url = input('Введите ссылĸу на видео в YouTube: ')

regex = r'^https://((www\.youtube\.com/watch\?v=[A-Za-z\-0-9]+(&t=[0-9]+)?)|(youtu\.be/[A-Za-z\-0-9]+(\?t=[0-9]+)?))$'

if re.match(regex, url):
    print('Ссылка ĸорреĸтна')
else:
    print('Ссылка неĸорреĸтна')
