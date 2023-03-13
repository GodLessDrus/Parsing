import requests
from bs4 import BeautifulSoup

url = requests.get('https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0_%D0%B2_%D0%A7%D0%B5%D1%80%D0%B5%D0%BF%D0%BE%D0%B2%D1%86%D0%B5')
res = url.status_code
html = url.content


soup = BeautifulSoup(html, 'html.parser')

add = soup.find(class_='round-5')

result = add.text

weather = soup.find(class_='ArchiveTemp',).find('span')
temp = weather.text

print(f'Сейчас температура на улице в городе Череповец: {temp}. {result}' )