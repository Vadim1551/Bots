import re
from SeleniumRun import run_selenium


def read_and_write(event, user_id):

            message = event.text  # текст смс
            user = event.user_id  # id профиля кто отправил смс

            if user == user_id:
                print(message)
                with open('log.txt', 'a', encoding='utf-8') as f:
                    f.write(message + '\n')

                with open("log.txt", "r", encoding="utf-8") as f:
                    text = f.read()

                # Извлечение названия команд
                teams = re.findall(r' ([A-Z]{1,2}) ', text)
                teams_str = " ".join(teams)

                # Извлечение прогноза
                forecast = re.findall(r'Прогноз:\s(.+)', text)[0]
                forecast = re.sub(r'[🇪🇺\s]+', '', forecast)  # Убираем эмодзи и пробельные символы

                # Извлечение суммы ставки
                bet_amount = re.findall(r'Сумма ставки:\s(\d+)%', text)[0]

                print("Переменная с командами:", teams_str)
                print("Переменная с прогнозом:", forecast)
                print("Переменная с суммой ставки:", bet_amount, "%")