from socket import AF_INET, SOCK_STREAM, socket
import pickle
import time
import logging.config
from decorators import log


logger = logging.getLogger('messenger.client')

s = socket(AF_INET, SOCK_STREAM)


@log
def init_socket():
    try:
        s.connect(('localhost', 8733))
    except ConnectionRefusedError:
        logger.critical('Соединенте с сервером не установлено')
    except OSError as error:
        logger.critical(f'Инициализация не прошла ошибка: {error}')
    else:
        logger.info(f'Соединенте с сервером установлено.')
        return s


@log
def send_answer():
    msg ={
        "action": "authenticate",
        "time": time.time(),
        "user": {
                "account_name":  "C0deMaver1ck",
                "password":      "CorrectHorseBatteryStaple"
        }
    }
    try:
        return pickle.dumps(msg)
    except pickle.PicklingError:
        logger.error('Не удалось закодировать и отправить сообщни серверу')
    s.close()


if __name__ == '__main__':
    socket = init_socket()
    send = send_answer()
