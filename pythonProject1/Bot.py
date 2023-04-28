import vk_api
import os
from dotenv import load_dotenv,find_dotenv
from vk_api.longpoll import VkLongPoll
from ListenerOpt import listen


def main():
    while True:
        # Работа с ВК
        load_dotenv(find_dotenv())
        session = vk_api.VkApi(token=os.getenv('TOKEN'))
        vk = session.get_api()
        longpoll = VkLongPoll(session)
        user_id = 419661764  # id человека сообщения которого хотим брать сообщения
        listen(longpoll, user_id)

if __name__ == '__main__':
    main()



