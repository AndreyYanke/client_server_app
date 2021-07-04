from socket import AF_INET, SOCK_STREAM, socket

from client_server_app import client


def main():
    test_start_server()
    test_send_answer()


def test_start_server():
    start_server = client.init_socket()
    start_server('error_localhost', 'error_port')

def test_send_answer():
    error_data = client.send_answer()
    error_data.s.recv(msg={})



if __name__ == '__main__':
    try:
        main()
    except  Exception as error_test:
        print(error_test)
