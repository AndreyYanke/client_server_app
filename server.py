import select
from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import pickle
import logging.config
from decorators import log

logger = logging.getLogger('messenger.server')

s = socket(AF_INET, SOCK_STREAM)


@log
def init_socket():
    address = ('', 8733)
    clients = []
    s.bind(address)
    s.listen(6)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    try:
        s.listen()
    except OSError as error:
        logger.critical(f'Инициализация не прошла ошибка: {error}')
    else:
        logger.info(f'Сервер запустился.')

    while True:
        try:
            conn, addr = s.accept()
        except OSError as e:
            pass
        else:
            print("Получен запрос на соединение от %s" % str(addr))
            clients.append(conn)
        finally:
            wait = 3
            r = []
            w = []
            try:
                r, w, e = select.select(clients, clients, [], wait)
            except:
                pass  # Ничего не делать, если какой-то клиент отключился

            requests = requests_client(r, clients)  # Сохраним запросы клиентов
            if requests:
                write_responses(requests, w, clients)  # Выполним отправку ответов клиентам


@log
def requests_client(r_clients, all_clients):
    requests ={}
    for sock in r_clients:
        try:
            data = sock.recv(1024)
            requests[sock] = data
        except:
            print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился ')
            all_clients.remove(sock)
    return requests

@log
def write_responses(requests, w_clients, all_clients):
    for sock in w_clients:
        if sock in requests:
            data = sock.recv(1024)
            resp = requests[sock] = data
            try:
                for sock in all_clients:
                    sock.send(pickle.dumps(resp))
            except:
                print(f'Клиент {sock.fileno()} {sock.getpeername()} отключился ')
                sock.close()
                all_clients.remove(sock)


if __name__ == '__main__':
    socket = init_socket()
    try:
        requests_client()
    except Exception as text:
        print('Сервер не запустился')
    else:
        print('Сервер запущен!')


