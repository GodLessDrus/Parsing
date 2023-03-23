from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd

# cookies = {
#     'anime_last_visit': '1363696017',
#     'anime_stashid': '%7B%22id%22%3A%222796e87f38853c5c9728ec70d8caa592d32458b9%22%2C%22dt%22%3A1679056017%7D',
#     '_ym_uid': '1679056019894890852',
#     '_ym_d': '1679056019',
#     '_ga': 'GA1.2.1830429246.1679056020',
#     'anime_csrf_token': '98b771d4829198815356473a5cfb7be87b381eb6',
#     '_ym_isad': '1',
#     '_gid': 'GA1.2.1255424304.1679486654',
#     '_gat_user': '1',
#     'anime_last_activity': '1679486659',
#     'anime_tracker': '%7B%220%22%3A%22top-100-anime%22%2C%221%22%3A%22index%22%2C%222%22%3A%22embeds%2Fplaylist-j.txt%2F14509%2F1%22%2C%223%22%3A%22anime%2Fgurren-lagann%2F1%2F2%22%2C%224%22%3A%22embeds%2Fplaylist-j.txt%2F14509%2F1%22%2C%22token%22%3A%22f5a12eb81c754a072cf17971367398d7408ad3419a1eac4b827759fd3f63c2422c94ba31043f10657d93daf050ab1f37%22%7D',
# }

# headers = {
#     'authority': 'online.animedia.tv',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
#     'cache-control': 'max-age=0',
#     'cookie': 'anime_last_visit=1363696017; anime_stashid=%7B%22id%22%3A%222796e87f38853c5c9728ec70d8caa592d32458b9%22%2C%22dt%22%3A1679056017%7D; _ym_uid=1679056019894890852; _ym_d=1679056019; _ga=GA1.2.1830429246.1679056020; anime_csrf_token=98b771d4829198815356473a5cfb7be87b381eb6; _ym_isad=1; _gid=GA1.2.1255424304.1679486654; _gat_user=1; anime_last_activity=1679486659; anime_tracker=%7B%220%22%3A%22top-100-anime%22%2C%221%22%3A%22index%22%2C%222%22%3A%22embeds%2Fplaylist-j.txt%2F14509%2F1%22%2C%223%22%3A%22anime%2Fgurren-lagann%2F1%2F2%22%2C%224%22%3A%22embeds%2Fplaylist-j.txt%2F14509%2F1%22%2C%22token%22%3A%22f5a12eb81c754a072cf17971367398d7408ad3419a1eac4b827759fd3f63c2422c94ba31043f10657d93daf050ab1f37%22%7D',
#     'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'none',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
# }

# response = requests.get('https://online.animedia.tv/top-100-anime', cookies=cookies, headers=headers)

# options = webdriver.ChromeOptions()
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
# try:
#     driver = webdriver.Chrome(
#         executable_path='C:\\Users\\1\\Desktop\\python\\chromedriver\\chromedriver.exe',
#         options=options)
#     driver.get(url='https://online.animedia.tv/top-100-anime')
#     sleep(20)

#     with open('animetop.html', 'w', encoding='utf-8') as file:
#         file.write(driver.page_source)
# except Exception as ex:
#     print(ex)
# finally:
#     driver.close()
#     driver.quit()
with open('animetop.html', encoding='utf-8') as file:
    src = file.read()


data = []
soup = BeautifulSoup(src, 'lxml')
anime = soup.select_one('.mains-container').select('.ads-list__item')
for i in anime:
    n, russian_name = i.select_one('.ads-list__item__title').stripped_strings
    anime_link = 'https://online.animedia.tv' + i.select_one('.ads-list__item__title').get('href')
    original_name = i.select_one('.original-title').text
    rate = i.select_one('.raitings').text
    tags = i.select_one('.genre-tags').stripped_strings


    data.append([n, russian_name, original_name, rate, tags, anime_link])

header = ['n', 'russian_name', 'original_name', 'rate', 'tags', 'anime_link']
df = pd.DataFrame(data, columns=header)
df.to_csv('topanime.csv', sep=';', encoding='utf-8')
    

