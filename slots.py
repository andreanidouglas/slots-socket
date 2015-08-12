__author__ = 'andreanidouglas'
import constants
import socket
import random
import time

class _client:
    def __init__(self):
        self._reset_port()
        self._init_socket()
    def _reset_port(self):
        self._port = constants.get_random_port()
    def _init_socket(self):
        self._cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def try_connection(self):
        connection_succesfull = False
        self._cli_socket.settimeout(constants.timeout)
        while not connection_succesfull:
            try:
                self._cli_socket.connect((constants.server, self._port))
                connection_succesfull = True
                if constants.debug == True:
                    print ("Connection succesfull", self._port)
                buffer = self._cli_socket.recv(1024)
                return self._port
            except ConnectionRefusedError as cre:
                #if constants.debug == True:
                 #   print ('connection refused reseting port', cre.strerror)
                self._reset_port()
            except ConnectionAbortedError as cae:
                #if constants.debug == True:
                    #print ('connection aborted reseting port', cae.strerror)
                self._reset_port()
            except socket.timeout as st:
                #print ('connection timedout reseting port', st.strerror)
                connection_succesfull = False
                self._reset_port()
            except OSError:
                connection_succesfull = False
                self._reset_port()



class slots:

    def random_generator(self):
        return random.randint(1,7)
    def _sleep(self):
        time.sleep(self.random_generator())
    def try_luck(self):
        cli = _client()
        luck_number = cli.try_connection()
        if constants.debug == True:
            print ("Luck_Number", luck_number)
        if (luck_number % 2) == 0:
            self._second_number = self.random_generator()
            self._third_number = self._second_number
        elif luck_number == constants.max_port:
            self._second_number = self._first_number
            self._third_number = self._first_number
        else:
            self._second_number = self.random_generator()
            self._third_number = self.random_generator()
            while self._third_number == self._second_number:
                self._third_number = self.random_generator()
    def run(self):
        self._first_number = self.random_generator()
        print ("First Number:", self._first_number)
        self.try_luck()
        print ("Second Number:", self._second_number)
        self._sleep()
        print ("Third Number:", self._third_number)

if __name__ == "__main__":
    slot = slots()
    slot.run()



