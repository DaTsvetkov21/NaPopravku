import random

list_words = ['python', 'java', 'swift', 'javascript']
list_alpha = 'abcdefghijklmnopqrstuvwxyz'
won = 0
lost = 0

print(f'H A N G M A N  ', '\n')
input_action = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ', )


def index_definition():
    i = 0
    list_index = []
    for alpha in selected_word:
        if selected_word[i] == input_alpha:
            list_index.append(i)
            i += 1
        else:
            i += 1
    return list_index


def replace_alpha():
    list_index = index_definition()
    for ind in list_index:
        word[ind] = input_alpha
    return word


while True:
    if input_action == 'play':
        number_of_attempts = 9
        selected_word = random.choice(list_words)
        word = list('-' * len(selected_word))
        set_alpha = set()
        input_alpha = input(f'{"".join(word)}\nInput a letter: > ', )
        if number_of_attempts == 1:
            lost += 1
            print('\n"You lost!"')
            input_action = input(
                'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ', )
            break
        while number_of_attempts > 0:
            if len(input_alpha) == 1:
                if input_alpha in list_alpha:
                    if input_alpha in set_alpha:
                        print("You've already guessed this letter.")
                        input_alpha = input(f'{"".join(word)}\nInput a letter: > ', )
                    else:
                        set_alpha.update(input_alpha)
                        if input_alpha not in selected_word:
                            print(f"That letter doesn't appear in the word.")
                            number_of_attempts -= 1
                            if number_of_attempts == 1:
                                print('\n"You lost!"')
                                lost += 1
                                input_action = input(
                                    'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ', )
                                break
                            else:
                                input_alpha = input(f'{"".join(word)}\nInput a letter: > ', )

                        else:
                            if input_alpha in word:
                                number_of_attempts -= 1
                                print('No improvements.')
                                if number_of_attempts == 1:
                                    print('\n"You lost!"')
                                    lost += 1
                                    input_action = input(
                                        'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ', )
                                    break
                                else:
                                    input_alpha = input(f'{"".join(word)}\nInput a letter: > ', )
                            else:
                                replace_alpha()
                                if selected_word == "".join(word):
                                    print(f'You guessed the word {selected_word}!\nYou survived!')
                                    won += 1
                                    input_action = input(
                                        'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ', )
                                    break
                                else:
                                    input_alpha = input(f'{"".join(word)}\nInput a letter: > ', )
                else:
                    print('Please, enter a lowercase letter from the English alphabet.')
                    input_alpha = input(f'{"".join(word)}\nInput a letter: > ', )
                    continue
            else:
                print('Please, input a single letter.')
                input_alpha = input(f'{"".join(word)}\nInput a letter: > ', )
                continue

    elif input_action == 'results':
        print(f'You won: {won} times.')
        print(f'You lost: {lost} times.')
        input_action = input(
            'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: > ', )
    else:
        break
