from aiogram import types, Dispatcher
from create_bot import bot, hero, md, keyboards


async def start(message: types.Message):
    await bot.send_message(message.chat.id, "Напишите название вашего героя"
                                            "\nПример: "
                                            "\nTemplar Assassin"
                                            "\nTiny"
                                            "\nAnti-Mage")


async def user_text(message: types.Message):
    if md.hero_check(message.text):

        hero.set_name(message.text)

        md.create_files(hero.get_name())

        list_win_rate = md.get_win_rate()

        await bot.send_message(message.chat.id, f'Ваш герой: {message.text}. '
                                                f'\nМатчи: {list_win_rate[0]}, Винрейт: {list_win_rate[1]}.'
                                                f'\nВыберите в меню то, что вас интересует?',
                               reply_markup=keyboards.get_start_menu())

    elif message.text == '🏹 Предметы':
        if hero.get_name() != '':


            await bot.send_message(message.chat.id, 'Выбирете в меню то, что вас интересует?',
                                   reply_markup=keyboards.get_menu_items())
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🛒 Предметы для покупки':
        if hero.get_name() != '':
            list_items = md.get_list_items(1)
            text = 'Предметы для покупки:\n'
            for item in list_items:
                text += f'{item._Item__item_Name}\n'
            await bot.send_message(message.chat.id, text)
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🏁 Стартовый закуп':
        if hero.get_name() != '':
            list_items = md.get_list_items(2)
            text = 'Стартовый закуп:\n'
            for item in list_items:
                text += f'{item._Item__item_Name} : {item._Item__item_Count}, Частота выбора: {item._Item__item_Win}\n'
            await bot.send_message(message.chat.id, text)
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '⚔ Доп. предметы':
        if hero.get_name() != '':
            list_items = md.get_list_items(3)
            text = 'Доп. предметы:\n'
            for item in list_items:
                text += f'{item._Item__item_Name}, Частота выбора: {item._Item__item_Win}\n'
            await bot.send_message(message.chat.id, text)
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🔙 Назад':
        if hero.get_name() != '':

            await bot.send_message(message.chat.id, '💬 Выбирете в меню то, что вас интересует?',
                                   reply_markup=keyboards.get_start_menu())
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '😊 Кого контрит':
        if hero.get_name() != '':
            table_num = -2
            list_heroes = md.get_list_heros(table_num)
            list_heroes.sort(key=lambda x: x.get_win_rate(), reverse=True)
            text_message = 'Вы сильны против:\n'
            for item in list_heroes:
                if len(item.get_hero_name()) != 0:
                    text_message += f'{item.get_hero_name()}: Вы побеждали в {round(float(item.get_win_rate()[:-1]))}% игр за {item.get_matches()} матчей\n'
            await bot.send_message(message.chat.id, text_message)

        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '😰 Контрпики':
        if hero.get_name() != '':
            table_num = -1
            list_heroes = md.get_list_heros(table_num)
            list_heroes.sort(key=lambda x: x.get_win_rate())
            text_message = 'Контрпики вашего героя:\n'
            for item in list_heroes:
                if len(item.get_hero_name()) != 0:
                    text_message += f'{item.get_hero_name()}: Вы побеждали в {round(float(item.get_win_rate()[:-1]))}% игр за {item.get_matches()} матчей\n'
            await bot.send_message(message.chat.id, text_message)

        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🏟 Последние игры':
        if hero.get_name() != '':

            await bot.send_message(message.chat.id, 'Сколько игр вы хотите посмотреть?',
                                   reply_markup=keyboards.get_menu_num())

        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '1' or message.text == '2' or message.text == '3' or message.text == '4' or message.text == '5':
        if hero.get_name() != '':
            list_last_games = md.get_last_games(int(message.text))
            for i in range(0, int(message.text)):
                text_start = ''
                text_mid = ''
                for item in list_last_games[i].get_start_items():
                    text_start += f"{item.get_item_Name()}, Кол-во: {item.get_item_Count()}\n"
                for item2 in list_last_games[i].get_items():
                    text_mid += f"{item2.get_item_Name()}, Тайминг: {item2.get_item_Time()}\n"

                await bot.send_message(message.chat.id, f'Игрок: {list_last_games[i].get_player_name()}\n'
                                                        f'\n'
                                                        f'MMR: {list_last_games[i].get_mmr()}\n'
                                                        f'\n'
                                                        f'{list_last_games[i].get_win()}\n'
                                                        f'\n'
                                                        'Стартовый закуп:\n'
                                                        '              ⬇\n'
                                                        f'{text_start}'
                                                        f'\n'
                                                        'Купленные предметы:\n'
                                                        '                 ⬇\n'
                                                        f'{text_mid}')
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🔙 Вернуться':
        if hero.get_name() != '':

            await bot.send_message(message.chat.id, '💬 Выбирете в меню то, что вас интересует?',
                                   reply_markup=keyboards.get_start_menu())
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🔙 Выбрать другого героя':
        await bot.send_message(message.chat.id, "💬 Напишите название вашего героя")

    else:
        await bot.send_message(message.chat.id, "😕 Нет такого героя")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'info'])
    dp.register_message_handler(user_text, content_types=['text'])