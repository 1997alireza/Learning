import socket
import threading
import os
import numpy as np
from gui import Window


class Proxy:
    webservers_categories = np.array([
        ['Sport',
         True,
         ['the-afc.com', 'espn.com']],
        ['Nature',
         False,
         ['solanaceaesource.org']]
    ], dtype=object)

    def __init__(self, host='localhost', port=7070):
        # Create a TCP socket
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Re-use the socket
        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # bind the socket to a public host, and a port
        self.serverSocket.bind((host, port))

        self.serverSocket.listen(10)  # become a server socket
        self.__clients = {}

    def wait_clients(self):
        waiting_loop = threading.Thread(name="wait_clients", target=self._wait_clients_loop)
        waiting_loop.setDaemon(True)
        waiting_loop.start()

    def _wait_clients_loop(self):
        while 1:
            (client_socket, client_address) = self.serverSocket.accept()
            print('--Got a request')
            self._make_thread(client_socket, client_address)

    def _make_thread(self, client_socket, client_address):
        thread = threading.Thread(name=client_socket.__str__() + ' ' + str(client_address), target=self._proxy_thread,
                                  args=(client_socket, client_address))
        thread.setDaemon(True)
        thread.start()

    def _proxy_thread(self, client_socket, client_address):
        request = client_socket.recv(4096)
        self._response(request, client_socket, client_address)
        client_socket.close()

    def _response(self, request, client_socket, client_address):
        try:
            request_str = request.decode()
        except:
            return  # ignore non utf-8 formats
        if len(request_str) == 0:
            return
        url = request_str.split(' ')[1]
        http_pos = url.find('://')
        if http_pos == -1:
            sep_url = url
        else:
            sep_url = url[http_pos + 3:]

        port_pos = sep_url.find(':')
        if port_pos == -1:
            port = 80
            sep_2_url = sep_url
        else:
            port = int(sep_url[port_pos + 1:])
            sep_2_url = sep_url[:port_pos]

        webserver_pos = sep_2_url.find('/')
        if webserver_pos == -1:
            webserver = sep_2_url
        else:
            webserver = sep_2_url[:webserver_pos]

        if 'www.' == webserver[:4]:
            webserver = webserver[4:]

        print('web server = ', webserver)
        if self._is_filtered(webserver):
            print("FILTER!")
            message = '<html><head></head><body style=\'color: red\'>Filter!</body></html>'
            header = 'HTTP/1.1 200 OK\r\n' \
                     'Content-Type: text/html; encoding=utf8\r\n' \
                     'Content-Length: ' + str(len(message)) + '\r\n' \
                     'Connection: close\r\n\r\n'
            client_socket.send(header.encode('ASCII'))
            client_socket.send(message.encode('utf8'))
        else:
            s = None
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((webserver, port))
                s.sendall(request)  # send request to webserver
                while 1:
                    data = s.recv(32768)
                    if len(data) > 0:
                        client_socket.send(data)
                    else:
                        break
                s.close()
            except socket.error as sock_err:
                print(os.strerror(sock_err.errno))
                print("Connection refused!")
                if s is not None:
                    s.close()

    def _is_filtered(self, webserver):
        for cat in self.webservers_categories:
            if cat[1]:
                for f_ws in cat[2]:
                    if f_ws == webserver[-len(f_ws):]:
                        return True
        return False

    def on_exit(self):
        if self.serverSocket is not None:
            self.serverSocket.close()


if __name__ == '__main__':
    proxy = Proxy()
    proxy.wait_clients()
    window = Window(proxy)
    window.show()
