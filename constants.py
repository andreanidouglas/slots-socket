__author__ = 'andreanidouglas'

import random
min_port = 1000
max_port = 65535
server = "localhost"
timeout = 1.0
_str = 'A'
generic_buffer = _str*1000

debug = True
port_list=[]
def get_random_port():
    port = random.randint(min_port, max_port)
    if port_list.count(port) == 0:
        port_list.insert(0, port)
        return (port)
    else:
        return (get_random_port())



if __name__ == "__main__":
    print("Hello, this is the constant module, please import it to use")
