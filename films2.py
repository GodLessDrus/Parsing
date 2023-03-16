from bs4 import BeautifulSoup
import requests
from time import sleep
from selenium import webdriver
import pandas as pd

data = []

for p in range(1,6):
    url = f'https://www.kinopoisk.ru/lists/movies/top-250-2020/?page={p}'
    headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
        }
    r = requests.get(url=url, headers=headers)
    sleep(3)
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36')
    # try:
    #     driver = webdriver.Chrome(
    #         executable_path='C:\\Users\\1\\Desktop\\python\\chromedriver\\chromedriver.exe',
    #         options=options)
    #     driver.get(url=f'https://www.kinopoisk.ru/lists/movies/top-250-2020/?page={p}')
    #     sleep(20)

    #     with open(f'indexfilm{p}.html', 'w', encoding='utf-8') as file:
    #         file.write(driver.page_source)
    # except Exception as ex:
    #     print(ex)
    # finally:
    #     driver.close()
    #     driver.quit()
    with open(f'indexfilm{p}.html', encoding='utf-8') as file:
        src = file.read()


    soup = BeautifulSoup(src, 'lxml')
    film = soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').get('href')
    link = 'https://www.kinopoisk.ru'+ soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').get('href')
    russian_name = soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
    original_name = soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('div', class_='desktop-list-main-info_secondaryTitleSlot__mc0mI').text
    country = soup.find('div', class_='styles_root__ti07r').find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_truncatedText__IMQRP').text
    films = soup.find_all('div', class_='styles_root__ti07r')
    # print(country)


    for film in films:
        link = 'https://www.kinopoisk.ru'+ film.find('a', class_='base-movie-main-info_link__YwtP1').get('href')
        russian_name = film.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='styles_mainTitle__IFQyZ styles_activeMovieTittle__kJdJj').text
        original_name = film.find('a', class_='base-movie-main-info_link__YwtP1').find('div', class_='desktop-list-main-info_secondaryTitleSlot__mc0mI').text
        country = film.find('a', class_='base-movie-main-info_link__YwtP1').find('span', class_='desktop-list-main-info_truncatedText__IMQRP').text

        data.append([link, russian_name, original_name, country])
header = ['link', 'russian_name', 'original_name', 'country']
df = pd.DataFrame(data, columns=header)
df.to_csv('kinopoisk_data.csv', sep=';', encoding='utf-8')