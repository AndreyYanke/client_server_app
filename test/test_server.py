from client_server_app import server


def main():
    test_start_server()


def test_start_server():
    start_server = server.init_socket()
    start_server('error_localhost', 'error_port')



if __name__ == '__main__':
    try:
        main()
    except  Exception as error_test:
        print(error_test)



