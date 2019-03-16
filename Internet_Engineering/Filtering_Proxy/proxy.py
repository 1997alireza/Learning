import socket
import threading
import os


class Proxy:
    filtered_categuries = []
    def __init__(self, host='localhost', port=7575):
        # Create a TCP socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Re-use the socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind the socket to a public host, and a port
        self.serverSocket.bind((host, port))

        self.serverSocket.listen(10)  # become a server socket
        self.__clients = {}

    def wait_clients(self):
        waiting_loop = threading.Thread(name="wait_clients", target=self._wait_clients_loop())
        waiting_loop.setDaemon(True)
        waiting_loop.start()

    def _wait_clients_loop(self):
        while 1:
            (client_socket, client_address) = self.serverSocket.accept()
            self._make_thread(client_socket, client_address)

    def _make_thread(self, client_socket, client_address):
        thread = threading.Thread(name=client_socket.__str__() + ' ' + str(client_address), target=self._proxy_thread,
                                  args=(client_socket, client_address))
        thread.setDaemon(True)
        thread.start()

    def _proxy_thread(self, client_socket, client_address):
        request = client_socket.recv(4096)
        request_str = request.decode()
        url = request_str.split(' ')[1]
        http_pos = url.find('://')
        if http_pos == -1:
            sep_url = url
        else:
            sep_url = url[http_pos+3:]

        port_pos = sep_url.find(':')
        if port_pos == -1:
            port = 80
        else:
            port = sep_url[]

        if self._is_filtered(url):
            print("xxx")
        else:
            s = None
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect(('google.com', 80))
                s.sendall(request)  # send request to webserver
                print("asda")
                while 1:
                    data = s.recv(32768)
                    if len(data) > 0:
                        client_socket.send(data)
                    else:
                        break
                s.close()
            except socket.error as sock_err:
                print(os.strerror(sock_err.errno))
                if s is not None:
                    s.close()
                print("Connection refused")
        client_socket.close()

    def _is_filtered(self, url):
        return False


if __name__ == '__main__':
    proxy = Proxy()
    proxy.wait_clients()
