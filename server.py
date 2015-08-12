__author__ = 'andreanidouglas'
import socket
import constants
class server:
    _serv_socket = None
    def init_socket(self):
        self._serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._port = constants.get_random_port()
    def reset_port(self):
        self._port = constants.get_random_port()
    def _close_connection(self):
        self._serv_socket.close()
    def open_connection(self):
        if constants.debug:
            print ("Server on port:", self._port)
        self._serv_socket.bind((constants.server, self._port))
        self._serv_socket.listen(10)
        (clientsocket, address) = self._serv_socket.accept()
        clientsocket.send(bytes(constants.generic_buffer, 'UTF-8'))
        if constants.debug:
            print ("Connection acquired")
        self._close_connection()


if __name__ == "__main__":
    serv = server()
    while 1:
        serv.init_socket()
        serv.open_connection()
        serv.reset_port()

