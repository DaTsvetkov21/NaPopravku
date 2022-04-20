game = '_________'
count_x = game.count('X')
count_o = game.count('O')
result = ''
count_sum = 0
list_string1 = [game[:3]]
string1 = ''
for elements_string1 in list_string1:
    for element_string1 in elements_string1:
        string1 += element_string1
        string1 += ' '

list_string2 = [game[3:6]]
string2 = ''
for elements_string2 in list_string2:
    for element_string2 in elements_string2:
        string2 += element_string2
        string2 += ' '

list_string3 = [game[6:]]
string3 = ''
for elements_string3 in list_string3:
    for element_string3 in elements_string3:
        string3 += element_string3
        string3 += ' '
print('---------')

print('|', string1 + '|')
print('|', string2 + '|')
print('|', string3 + '|')
print('---------')

coordinates = input('Enter the coordinates: ').split()
q = ''

column1 = list_string1[0][0] + list_string2[0][0] + list_string3[0][0]
column2 = list_string1[0][1] + list_string2[0][1] + list_string3[0][1]
column3 = list_string1[0][2] + list_string2[0][2] + list_string3[0][2]
diagonal1 = list_string1[0][0] + list_string2[0][1] + list_string3[0][2]
diagonal2 = list_string1[0][2] + list_string2[0][1] + list_string3[0][0]


def location(string, column):
    global q
    string = coordinates[-2]
    column = coordinates[-1]
    if string == '1':
        string = string1
        q = '1'
    elif string == '2':
        string = string2
        q = '2'
    elif string == '3':
        string = string3
        q = '3'
    if column == '1':
        column = 0
    elif column == '2':
        column = 2
    elif column == '3':
        column = 4
    return [q, string, column]


def steps():
    count_x = game.count('X')
    count_o = game.count('O')
    if count_x > count_o:
        step = 'O'
    else:
        step = 'X'
    return step


def check():
    if 'XXX' in [column1, column2, column3, diagonal1, diagonal2] or 'X X X ' in [string1, string2, string3]:
        result = 'X wins'
        print(result)
        return result
    elif 'OOO' in [string1, string2, string3, column1, column2, column3, diagonal1, diagonal2] or 'O O O ' in [string1,
                                                                                                               string2,
                                                                                                               string3]:
        result = 'O wins'
        print(result)
        return result
    elif ('OOO' not in [string1, string2, string3, column1, column2, column3, diagonal1, diagonal2] and count_sum == 9 \
          or 'XXX' not in [string1, string2, string3, column1, column2, column3, diagonal1,
                           diagonal2] and count_sum == 9):
        result = 'Draw'
        print(result)
        return result


while True:
    if coordinates[-1].isdigit() == False or coordinates[-2].isdigit() == False:
        print('You should enter numbers!')
        coordinates = input('Enter the coordinates: ').split()
    elif int(coordinates[-1]) not in range(1, 4) or int(coordinates[-2]) not in range(1, 4):
        print('Coordinates should be from 1 to 3!')
        coordinates = input('Enter the coordinates: ').split()
    else:
        list_location = location(coordinates[-2], coordinates[-1])
        string, column = list_location[-2], list_location[-1]
        place = string[column]
        if place == 'X' or place == 'O':
            print('This cell is occupied! Choose another one!')
            coordinates = input('Enter the coordinates: ').split()
        else:
            if column == 4 and q == '1':
                step = steps()
                string1 = string1[:4] + step + ' '
                column3 = string1[4] + string2[4] + string3[4]
                diagonal1 = string1[0] + string2[1] + string3[2]
                diagonal2 = string1[2] + string2[1] + string3[0]
                game = string1 + string2 + string3
                print('---------')
                print('|', string1 + '|')
                print('|', string2 + '|')
                print('|', string3 + '|')
                print('---------')
                count_sum += 1
                result = check()
                if result == 'X wins' or result == 'O wins' or result == 'Draw':
                    break
                else:
                    coordinates = input('Enter the coordinates: ').split()
                    continue
            elif column == 2 and q == '1':
                step = steps()
                string1 = string1[:2] + step + ' ' + string1[4:]
                column2 = string1[2] + string2[2] + string3[2]
                diagonal1 = string1[0] + string2[1] + string3[2]
                diagonal2 = string1[2] + string2[1] + string3[0]
                game = string1 + string2 + string3
                print('---------')
                print('|', string1 + '|')
                print('|', string2 + '|')
                print('|', string3 + '|')
                print('---------')
                count_sum += 1
                result = check()
                if result == 'X wins' or result == 'O wins' or result == 'Draw':
                    break
                else:
                    coordinates = input('Enter the coordinates: ').split()
                    continue
            elif column == 0 and q == '1':
                step = steps()
                string1 = step + string1[1:]
                column1 = string1[0] + string2[0] + string3[0]
                diagonal1 = string1[0] + string2[2] + string3[4]
                diagonal2 = string1[4] + string2[2] + string3[0]
                game = string1 + string2 + string3
                print('---------')
                print('|', string1 + '|')
                print('|', string2 + '|')
                print('|', string3 + '|')
                print('---------')
                count_sum += 1
                result = check()
                if result == 'X wins' or result == 'O wins' or result == 'Draw':
                    break
                else:
                    coordinates = input('Enter the coordinates: ').split()
                    continue
            if column == 4 and q == '2':
                step = steps()
                string2 = string2[:4] + step + ' '
                column3 = string1[4] + string2[4] + string3[4]
                diagonal1 = string1[0] + string2[2] + string3[4]
                diagonal2 = string1[4] + string2[2] + string3[0]
                game = string1 + string2 + string3
                print('---------')
                print('|', string1 + '|')
                print('|', string2 + '|')
                print('|', string3 + '|')
                print('---------')
                count_sum += 1
                result = check()
                if result == 'X wins' or result == 'O wins' or result == 'Draw':
                    break
                else:
                    coordinates = input('Enter the coordinates: ').split()
                    continue

            elif column == 2 and q == '2':
                step = steps()
                string2 = string2[:2] + step + ' ' + string2[4:]
                column2 = string1[2] + string2[2] + string3[2]
                diagonal1 = string1[0] + string2[2] + string3[4]
                diagonal2 = string1[4] + string2[2] + string3[0]
                game = string1 + string2 + string3
                print('---------')
                print('|', string1 + '|')
                print('|', string2 + '|')
                print('|', string3 + '|')
                print('---------')
                count_sum += 1
                result = check()
                if result == 'X wins' or result == 'O wins' or result == 'Draw':
                    break
                else:
                    coordinates = input('Enter the coordinates: ').split()
                    continue
            elif column == 0 and q == '2':
                step = steps()
                string2 = step + string2[1:]
                column1 = string1[0] + string2[0] + string3[0]
                diagonal1 = string1[0] + string2[2] + string3[4]
                diagonal2 = string1[4] + string2[2] + string3[0]
                game = string1 + string2 + string3
                print('---------')
                print('|', string1 + '|')
                print('|', string2 + '|')
                print('|', string3 + '|')
                print('---------')
                count_sum += 1
                result = check()
                if result == 'X wins' or result == 'O wins' or result == 'Draw':
                    break
                else:
                    coordinates = input('Enter the coordinates: ').split()
                    continue
            if column == 4 and q == '3':
                step = steps()
                string3 = string3[:4] + step + ' '
                column3 = string1[4] + string2[4] + string3[4]
                diagonal1 = string1[0] + string2[2] + string3[4]
                diagonal2 = string1[4] + string2[2] + string3[0]
                game = string1 + string2 + string3
                print('---------')
                print('|', string1 + '|')
                print('|', string2 + '|')
                print('|', string3 + '|')
                print('---------')
                result = check()
                count_sum += 1
                coordinates = input('Enter the coordinates: ').split()
                if result == 'X wins' or result == 'O wins' or result == 'Draw':
                    break
                else:
                    continue
            elif column == 2 and q == '3':
                step = steps()
                string3 = string3[:2] + step + ' ' + string3[4:]
                column2 = string1[2] + string2[2] + string3[2]
                diagonal1 = string1[0] + string2[2] + string3[4]
                diagonal2 = string1[4] + string2[2] + string3[0]
                game = string1 + string2 + string3
                print('---------')
                print('|', string1 + '|')
                print('|', string2 + '|')
                print('|', string3 + '|')
                print('---------')
                result = check()
                count_sum += 1
                if result == 'X wins' or result == 'O wins' or result == 'Draw':
                    break
                else:
                    coordinates = input('Enter the coordinates: ').split()
                    continue
            elif column == 0 and q == '3':
                step = steps()
                string3 = step + string3[1:]
                column1 = string1[0] + string2[0] + string3[0]
                diagonal1 = string1[0] + string2[2] + string3[4]
                diagonal2 = string1[4] + string2[2] + string3[0]
                game = string1 + string2 + string3
                print('---------')
                print('|', string1 + '|')
                print('|', string2 + '|')
                print('|', string3 + '|')
                print('---------')
                result = check()
                count_sum += 1
                if result == 'X wins' or result == 'O wins' or result == 'Draw':
                    break
                else:
                    coordinates = input('Enter the coordinates: ').split()
                    continue
