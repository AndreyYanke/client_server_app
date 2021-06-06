from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import pickle

s = socket(AF_INET, SOCK_STREAM)

def init_socket():
    s.bind(('', 8733))
    s.listen(6)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

def main():
    while True:
        client, addr = s.accept()
        print('Получен запрос на соединение от %s' % str(addr))
        data = client.recv(1024)
        response = {
            'response': 200,
            'alert': 'Позравляю Вы вошли в систему'
        }
        client.send(pickle.dumps(response))

        client.close()


if __name__ == '__main__':
    socket = init_socket()
    try:
        main()
    except Exception as text:
        print('Сервер не запустился')
