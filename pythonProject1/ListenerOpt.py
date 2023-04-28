import time
import threading
from vk_api.longpoll import VkEventType
from RAW import read_and_write


#Каждые 5 секунд проверяет новые сообщения, если есть новые, для каждого в отдельном потоке запускает функцию run_selenium
def listen(longpoll, user_id):
    try:
        listEvents = longpoll.listen()
    except Exception:
        return

    if len(listEvents) == 0:
        time.sleep(5)
        return

    try:
        for event in listEvents:
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                threading.Thread(target=read_and_write, args=(event, user_id)).start()

    except Exception:
        return

