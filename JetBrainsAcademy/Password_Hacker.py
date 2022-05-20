import socket
import argparse
import itertools


def return_word_in_list():
    file_password = open('/home/user/Downloads/passwords.txt')
    for password_word in file_password.read().split():
        password_list = []
        for password_alpha in password_word:
            if password_alpha.isdigit():
                password_list.append(password_alpha)
            else:
                password_list.append(password_alpha)
                password_list.append(password_alpha.upper())
        yield password_list, password_word


def generate_password():
    word = return_word_in_list()
    while True:
        passwords_list = []
        password = next(word)
        for psswrd in itertools.combinations(password[0], len(password[1])):
            if ''.join(psswrd).lower() == password[1]:
                if psswrd in passwords_list:
                    pass
                else:
                    passwords_list.append(psswrd)
                    yield ''.join(psswrd).encode()


# def generate_password():
#     password_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
#                       'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#                       'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     for r in range(1, 37):
#         for password in itertools.product(password_alpha, repeat=r):
#             yield str(''.join(password)).encode()


def send_password():
    generator = generate_password()
    while True:
        password = next(generator)
        client_socket.send(password)
        response = client_socket.recv(1024)
        response = response.decode()
        if response == 'Connection success!':
            print(password.decode())
            break


parser = argparse.ArgumentParser()
parser.add_argument('IP_address')
parser.add_argument('port')
args = parser.parse_args()
hostname = args.IP_address
port = int(args.port)
client_socket = socket.socket()
address = (hostname, port)
client_socket.connect(address)
send_password()
client_socket.close()
