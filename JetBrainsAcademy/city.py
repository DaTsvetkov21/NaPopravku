import itertools


def return_login_in_list():
    file_password = open('/home/user/Downloads/logins.txt')
    for password_word in file_password.read().split():
        password_list = []
        for password_alpha in password_word:
            if password_alpha.isdigit():
                password_list.append(password_alpha)
            else:
                password_list.append(password_alpha)
                password_list.append(password_alpha.upper())
        yield password_list, password_word


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


def generate_password():
    password_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                      'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                      'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                      'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                      '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for r in range(1, 37):
        for password in itertools.product(password_alpha, repeat=r):
            yield str(''.join(password))

login = generate_login()
password = generate_password()
while True:
    print(next(password))