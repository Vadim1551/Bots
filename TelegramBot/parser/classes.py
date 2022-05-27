class Game:
    def __init__(self):
        self.__win = ''
        self.__player_name = ''
        self.__mmr = ''
        self.__start_items = []
        self.__items = []

    @property
    def win(self):
        return self.__win

    @win.setter
    def win(self, text):
        self.__win = text

    @property
    def player_name(self):
        return self.__player_name

    @player_name.setter
    def player_name(self, text):
        self.__player_name = text

    @property
    def mmr(self):
        return self.__mmr

    @mmr.setter
    def mmr(self, text):
        self.__mmr = text

    @property
    def start_items(self):
        return self.__start_items

    @start_items.setter
    def start_items(self, text):
        self.__start_items = text

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, text):
        self.__items = text


class Person:
    def __init__(self):
        self.__hero_name = ''

    @property
    def hero_name(self):
        return self.__hero_name

    @hero_name.setter
    def hero_name(self, name):
        self.__hero_name = name


class Hero(Person):
    def __init__(self):
        super().__init__()
        self.__win_rate = ''
        self.__matches = ''

    @property
    def win_rate(self):
        return self.__win_rate

    @win_rate.setter
    def win_rate(self, name):
        self.__win_rate = name

    @property
    def matches(self):
        return self.__matches

    @matches.setter
    def matches(self, name):
        self.__matches = name


class Item:
    def __init__(self):
        self.__item_name = ''
        self.__item_win = ''
        self.__item_count = '1x'
        self.__item_time = ''

    @property
    def item_name(self):
        return self.__item_name

    @item_name.setter
    def item_name(self, name):
        self.__item_name = name

    @property
    def item_win(self):
        return self.__item_win

    @item_win.setter
    def item_win(self, name):
        self.__item_win = name

    @property
    def item_count(self):
        return self.__item_count

    @item_count.setter
    def item_count(self, name):
        self.__item_count = name

    @property
    def item_time(self):
        return self.__item_time

    @item_time.setter
    def item_time(self, name):
        self.__item_time = name
