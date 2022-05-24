import requests
import re
import threading
from bs4 import BeautifulSoup
from parser.classes import Game, Item, Hero
from fake_useragent import UserAgent


class Methods:
    UA = UserAgent()
    HEADERS = {
        "Accept": "*/*",
        "User-Agent": f"{UA.random}"
    }

    def hero_check(self, text):  # Проверка на существование имени героя
        list_names = open('list_hero_names.txt', encoding='utf-8')
        count = 0
        hero_name = text.replace(' ', '-')
        for row_name in list_names:
            if re.search(hero_name, row_name):
                count += 1
                return True
            else:
                continue
        if count == 0:
            return False

    def create_files(self, name_hero):
        t1 = threading.Thread(target=self.get_html(name_hero, 1))
        t2 = threading.Thread(target=self.get_html(name_hero, 2))

        t1.start()
        t2.start()

        t1.join()
        t2.join()

    def get_html(self, name_hero, num_site):  # Получение html кода страницы с одного из двух сайтов
        if num_site == 1:
            URL = 'https://www.dota2protracker.com/hero/'
            req = requests.get(URL + name_hero.replace(' ', '%20'), headers=self.HEADERS)
            src = req.text
            with open("dotapro.html", "w", encoding='utf-8') as file:
                file.write(src)
        elif num_site == 2:
            URL = 'https://ru.dotabuff.com/heroes/'
            req = requests.get(URL + name_hero.lower().replace(' ', '-'), headers=self.HEADERS)
            src = req.text
            with open("dotabuff.html", "w", encoding='utf-8') as file:
                file.write(src)

    def get_soup(self, site_name):

        if site_name == "pro":
            with open("dotapro.html", encoding='utf-8') as file:
                src = file.read()

        if site_name == "buff":
            with open("dotabuff.html", encoding='utf-8') as file:
                src = file.read()

        soup = BeautifulSoup(src, "lxml")
        return soup

    def get_list_heros(self, table_num):  # Получение списка героев с их показателями
        soup = get_soup("buff")
        list_section = soup.find(class_="col-8").find_all("section")
        list_heroes = list_section[table_num].find_all("tr")
        list_objects = []
        for item in list_heroes:
            hero = Hero()
            list_item_characteristics = item.find_all("td")  # Список показателей героя
            x = 0
            for items in list_item_characteristics:
                if len(items.text) != 0:
                    x += 1
                    if x == 1:
                        hero.set_hero_name(items.text)
                    if x == 3:
                        hero.set_win_rate(items.text)
                    if x == 4:
                        hero.set_matches(items.text)
            list_objects.append(hero)
        return list_objects

    def set_item_name_and_win(self, item_name, skip, list_win, i):  # Получение названия и винрейта предмета
        name = item_name.replace('item_', '')
        name = name.replace('_', ' ')
        name = name[:1].upper() + name[1:]
        thing = Item()
        thing.set_item_Name(name)
        if skip == 2 or skip == 3:
            win = list_win[i].get_text().strip()
            thing.set_item_Win(win)
        return thing

    def get_list_items(self, count):  # Получаем список предметов из нужной таблицы
        soup = get_soup("pro")
        list_item_tables = soup.find("div", class_="content-box-body").find_all("div", class_="inner-box")
        list_item = []
        skip = 0  # Пропуск ненужных таблиц элементов
        for item in list_item_tables:
            if item.find("div", class_="inner-box-header").text.strip() != "Top Ability Build":
                if skip == 1 and count == skip:       # Таблица предметов для покупки
                    list_items = item.find_all("div", class_="item-row-top")
                    for items in list_items:
                        item_name = items.get('title')  # Получение названия предмета
                        list_item.append(set_item_name_and_win(item_name, skip, list_item, 0))
                    return list_item
                elif skip == 2 and count == skip:     # Таблица предметов стартового закупа
                    list_items = item.find_all("div", class_="item-row-top")
                    list_win = item.find_all("div", class_="item-row-bottom")
                    for i in range(0, 11):
                        try:
                            item_name = list_items[i].get("title")  # Получение названия предмета
                            thing = set_item_name_and_win(item_name, skip, list_win, i)
                            count = list_items[i].find('div', class_="item-charges")
                            if count is not None:
                                thing.set_item_Count(count.text.strip())
                            list_item.append(thing)
                        except IndexError:
                            pass
                    return list_item
                elif skip == 3 and count == skip:        # Таблица доп. предметов
                    list_items = item.find_all("div", class_="item-row-top")
                    list_win = item.find_all("div", class_="item-row-bottom")
                    for i in range(0, 11):
                        try:
                            item_name = list_items[i].get("title")  # Получение названия предмета
                            thing = set_item_name_and_win(item_name, skip, list_win, i)
                            list_item.append(thing)
                        except IndexError:
                            pass
                    return list_item
            skip += 1

    def get_win_rate(self):
        soup = get_soup("pro")
        list_data = []
        list_win_and_matches = soup.find("div", class_="hero-header-stats-detailed").find_all('span')
        m = list_win_and_matches[0].get_text()
        w = list_win_and_matches[1].get_text()
        list_data.append(m)
        list_data.append(w)
        return list_data

    def get_last_games(self, count_games):  # Получаем список последних игр про-игроков на этом герое
        soup = get_soup("pro")
        list_last_games = []
        list_games = soup.find('table', class_='alx_table sort-fd').find('tbody').find_all('tr')

        count = 0  # Счетчик игр

        for item in list_games:
            if count < count_games:  # Парсим столько игр, сколько запросил пользователь

                game = Game()

                list_start_items = item.find("div", class_='item-inventory-start').find_all('div', class_='inventory-item')

                if len(list_start_items) == 0:  # Проверяем что игра не пустая
                    count_games += 1
                    continue
                list_item_build = item.find("div", class_='item_build').find_all('div', class_='inventory-item')

                set_game_start_items(list_start_items, game)
                set_game_end_items(list_item_build, game)

                win = ''.join(item.td['class'])
                game.set_win(win)

                player_name = item.find("div", class_='pros-stats').find('a').text
                game.set_player_name(player_name)

                mmr = item.find('td', class_='td-mmr').text
                game.set_mmr(mmr)

                list_last_games.append(game)
            count += 1
        return list_last_games


def set_item_name_and_win(item_name, skip, list_win, i):  # Получение названия и винрейта предмета
    name = item_name.replace('item_', '')
    name = name.replace('_', ' ')
    name = name[:1].upper() + name[1:]
    thing = Item()
    thing.set_item_Name(name)
    if skip == 2 or skip == 3:
        win = list_win[i].get_text().strip()
        thing.set_item_Win(win)
    return thing


def set_game_end_items(list_item_build, game):
    list_middle = []
    for items2 in list_item_build:  # Все купленные предметы к концу игры
        pr = Item()
        pr.set_item_Name(items2.get("title"))
        pr.set_item_Time(items2.get_text().strip())
        list_middle.append(pr)
    game.set_items(list_middle)


def set_game_start_items(list_start_items, game):
    list_start = []
    for items in list_start_items:  # Начальные предметы
        pr = Item()
        name = ''.join(
            ''.join(items.get('style').split('.jpg')[:-1]).split("background-image:url('/static/items_jpg_res/"))
        name = name[:1].upper() + name[1:]
        pr.set_item_Name(name.replace('_', ' '))
        counts = items.get_text().strip()
        if counts == '' or counts == '1':
            pr.set_item_Count(1)
        else:
            pr.set_item_Count(counts)
        list_start.append(pr)
    game.set_start_items(list_start)


def get_soup(site_name):
    if site_name == "pro":
        with open("dotapro.html", encoding='utf-8') as file:
            src = file.read()

    if site_name == "buff":
        with open("dotabuff.html", encoding='utf-8') as file:
            src = file.read()

    soup = BeautifulSoup(src, "lxml")
    return soup
