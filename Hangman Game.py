# 32. Hangman (30 and 31)

import random

def word_pick():
    with open('C:\\Users\\amith\\Python Training\\Temp Files\\sowpods.txt', encoding = 'utf-8') as temp:
        return random.choice(temp.readlines())

def letter_check(guess_letter):
    global final, count, hang, incorrect
    j = 0
    if guess_letter in final or guess_letter in incorrect:
        print('Already guessed it!')
    else:
        if guess_letter in rand_word:
            for l in rand_word:
                if l == guess_letter:
                    final[j] = l
                    j += 1
                    count -= 1
                else:
                    j += 1
            print(' '.join(final))
        else:
            incorrect.append(guess_letter)
            print('Incorrect guess!!')
            print('Hangman:')
            hangman()
            hang -= 1
            print(f'You have only {hang} incorrect guesses left now!')
            if hang == 0:
                print('GAME OVER!')

def hangman():
    global hang
    if hang == 6:
        print(' O')
    elif hang == 5:
        print(' O\n |')
    elif hang == 4:
        print(' O\n/|')
    elif hang == 3:
        print(' O\n/|\\')
    elif hang == 2:
        print(' O\n/|\\\n/')
    elif hang == 1:
        print(' O\n/|\\\n/ \\')

if __name__ == "__main__":
    repeat = 'y'
    while repeat == 'y':
        count = 0; hang = 6; incorrect = []
        print('~~*~~'*16)
        print('HANGMAN GAME')
        print('Randomly picking a Word from the SOWPODS file!')
        rand_word = word_pick().strip()
        for i in rand_word:
            count += 1
        print('The Word has these many letters:'); print('_ ' * count)
        final = ['_'] * count
        print('Guess the Word, letter by letter!')
        while hang != 0 and count != 0:
            each_letter = input('Enter your guess: ')
            letter_check(each_letter.upper())
        print('The word is : ' + rand_word)
        repeat = input('Do you want to continue? Type (Y/N): ').lower()