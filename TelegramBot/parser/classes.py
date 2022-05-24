class Game:
    def __init__(self):
        self.__win = ''
        self.__player_name = ''
        self.__mmr = ''
        self.__start_items = []
        self.__items = []

    def get_win(self):
        return self.__win

    def set_win(self, text):
        self.__win = text

    def get_player_name(self):
        return self.__player_name

    def set_player_name(self, text):
        self.__player_name = text

    def get_mmr(self):
        return self.__mmr

    def set_mmr(self, text):
        self.__mmr = text

    def get_start_items(self):
        return self.__start_items

    def set_start_items(self, text):
        self.__start_items = text

    def get_items(self):
        return self.__items

    def set_items(self, text):
        self.__items = text


class Person:
    def __init__(self):
        self.__heroName = ''

    def get_name(self):
        return self.__heroName

    def set_name(self, name):
        self.__heroName = name


class Hero:
    def __init__(self):
        self.__hero_name = ''
        self.__win_rate = ''
        self.__matches = ''

    def get_hero_name(self):
        return self.__hero_name

    def set_hero_name(self, name):
        self.__hero_name = name

    def get_win_rate(self):
        return self.__win_rate

    def set_win_rate(self, name):
        self.__win_rate = name

    def get_matches(self):
        return self.__matches

    def set_matches(self, name):
        self.__matches = name


class Item:
    def __init__(self):
        self.__item_Name = ''
        self.__item_Win = ''
        self.__item_Count = '1x'
        self.__item_Time = ''

    def get_item_Name(self):
        return self.__item_Name

    def set_item_Name(self, name):
        self.__item_Name = name

    def get_item_Win(self):
        return self.__item_Win

    def set_item_Win(self, name):
        self.__item_Win = name

    def get_item_Count(self):
        return self.__item_Count

    def set_item_Count(self, name):
        self.__item_Count = name

    def get_item_Time(self):
        return self.__item_Time

    def set_item_Time(self, name):
        self.__item_Time = name