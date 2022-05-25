from aiogram import types, Dispatcher
from create_bot import bot, hero, md, keyboards


async def start(message: types.Message):
    await bot.send_message(message.chat.id, "Что хотите узнать?", reply_markup=keyboards.start_menu)


async def user_text(message: types.Message):
    if md.hero_check(message.text):

        hero.hero_name = message.text

        md.create_files(hero.hero_name)

        list_win_rate = md.win_rate()

        await bot.send_message(message.chat.id, f'Ваш герой: {message.text}. '
                                                f'\nМатчи: {list_win_rate[0]}, Винрейт: {list_win_rate[1]}.'
                                                f'\nВыберите в меню то, что вас интересует?',
                               reply_markup=keyboards.hero_menu)


    elif message.text == '👱🏽 Выбрать героя':
        await bot.send_message(message.chat.id, "Напишите название вашего героя"
                                                "\nПример: "
                                                "\nTemplar Assassin"
                                                "\nTiny"
                                                "\nAnti-Mage")

    elif message.text == '🏹 Предметы':
        if hero.hero_name != '':


            await bot.send_message(message.chat.id, 'Выбирете в меню то, что вас интересует?',
                                   reply_markup=keyboards.menu_items)
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🛒 Предметы для покупки':
        if hero.hero_name != '':
            list_items = md.list_items(1)
            text = 'Предметы для покупки:\n'
            for item in list_items:
                text += f'{item._Item__item_name}\n'
            await bot.send_message(message.chat.id, text)
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🏁 Стартовый закуп':
        if hero.hero_name != '':
            list_items = md.list_items(2)
            text = 'Стартовый закуп:\n'
            for item in list_items:
                text += f'{item._Item__item_name} : {item._Item__item_count}, Частота выбора: {item._Item__item_win}\n'
            await bot.send_message(message.chat.id, text)
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '⚔ Доп. предметы':
        if hero.hero_name != '':
            list_items = md.list_items(3)
            text = 'Доп. предметы:\n'
            for item in list_items:
                text += f'{item._Item__item_name}, Частота выбора: {item._Item__item_win}\n'
            await bot.send_message(message.chat.id, text)
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🔙 Назад':
        if hero.hero_name != '':

            await bot.send_message(message.chat.id, '💬 Выбирете в меню то, что вас интересует?',
                                   reply_markup=keyboards.hero_menu)
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '😊 Кого контрит':
        if hero.hero_name != '':
            table_num = -2
            list_heroes = md.list_heros(table_num)
            list_heroes.sort(key=lambda heroes: heroes.win_rate, reverse=True)
            text_message = 'Вы сильны против:\n'
            for item in list_heroes:
                if len(item.hero_name) != 0:
                    text_message += f'{item.hero_name}: Вы побеждали в {round(float(item.win_rate[:-1]))}% игр за {item.matches} матчей\n'
            await bot.send_message(message.chat.id, text_message)

        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '😰 Контрпики':
        if hero.hero_name != '':
            table_num = -1
            list_heroes = md.list_heros(table_num)
            list_heroes.sort(key=lambda heroes: heroes.win_rate)
            text_message = 'Контрпики вашего героя:\n'
            for item in list_heroes:
                if len(item.hero_name) != 0:
                    text_message += f'{item.hero_name}: Вы побеждали в {round(float(item.win_rate[:-1]))}% игр за {item.matches} матчей\n'
            await bot.send_message(message.chat.id, text_message)

        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🏟 Последние игры':
        if hero.hero_name != '':

            await bot.send_message(message.chat.id, 'Сколько игр вы хотите посмотреть?',
                                   reply_markup=keyboards.menu_num)

        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '1' or message.text == '2' or message.text == '3' or message.text == '4' or message.text == '5':
        if hero.hero_name != '':
            list_last_games = md.last_games(int(message.text))
            for i in range(0, int(message.text)):
                text_start = ''
                text_mid = ''
                for item in list_last_games[i].start_items:
                    text_start += f"{item.item_name}, Кол-во: {item.item_count}\n"
                for item2 in list_last_games[i].items:
                    text_mid += f"{item2.item_name}, Тайминг: {item2.item_time}\n"

                await bot.send_message(message.chat.id, f'Игрок: {list_last_games[i].player_name}\n'
                                                        f'\n'
                                                        f'MMR: {list_last_games[i].mmr}\n'
                                                        f'\n'
                                                        f'{list_last_games[i].win}\n'
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

    elif message.text == '💪 Метовые герои':
        await bot.send_message(message.chat.id, 'Выбирете позицию', reply_markup=keyboards.menu_meta)

    elif message.text == '🗡️ Carry' or message.text == '🏹 Mid lane' or message.text == '🛡️ Off lane' or message.text == '🤝 Soft support (Pos 4)' or message.text == '🆘 Hard support (Pos 5)':
        text = ''
        list_meta_heroes = md.meta_heroes(message.text)
        list_meta_heroes.sort(key=lambda heroes: heroes.win_rate, reverse=True)
        for item in list_meta_heroes:
            text += f'{item.hero_name}: {item.matches} игр, {item.win_rate} побед\n'
        await bot.send_message(message.chat.id, text, reply_markup=keyboards.menu_meta)

    elif message.text == '🔙 Back':
        await bot.send_message(message.chat.id, 'Что хотите узнать', reply_markup=keyboards.start_menu)

    elif message.text == '🔙 Вернуться':
        if hero.hero_name != '':

            await bot.send_message(message.chat.id, '💬 Выбирете в меню то, что вас интересует?',
                                   reply_markup=keyboards.hero_menu)
        else:
            await bot.send_message(message.chat.id, "😧 Вы не выбрали героя")

    elif message.text == '🔄 Выбрать другого героя':
        await bot.send_message(message.chat.id, "Напишите название вашего героя"
                                                "\nПример: "
                                                "\nTemplar Assassin"
                                                "\nTiny"
                                                "\nAnti-Mage")


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start', 'info'])
    dp.register_message_handler(user_text, content_types=['text'])