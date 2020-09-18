
"""
Hanged game
Created on 2020 wed 12 sept
@author: Ivan Mujica
"""
# welcome hanger
import random
# play function, well it plays
def play (word):
    hidden = []
    attempts = 0
    max_attempts = 4
    word = list (word)
    # let's create a result word
    for char in word :
        hidden.append('_')
    isGameOver = False
    # Iterating until game is over
    while not isGameOver:
        # first part
        print(f'You still have {max_attempts - attempts} attemps remaining')
        hiddenString = ''.join(hidden)
        print(f'The current word is : {hiddenString}')
        # second part
        print('   _________')
        print('    |     |')
        print('    |    ' + (' O' if attempts > 0 else  ''))
        print('    |    ' + ('/ \\' if attempts > 1 else ''))
        print('    |    ' + (' |' if attempts > 2 else ''))
        print('    |    ' + ('/ \\' if attempts > 3 else ''))
        print('-------- ')
        letterGuessed = input('Enter a letter:  ')
        print('\n\n\n')
        # third part
        if letterGuessed in word:
            print(f'Good, the letter {letterGuessed} is in the word.')
            for i in range(len(word)):
                if word[i] == letterGuessed:
                    hidden[i] = word[i]
                    word[i] = '_'
        else :
            if letterGuessed not in hidden:
                attempts += 1
                print(f'Wrong! The letter {letterGuessed} is not in the word.')
            else:
                print(f'You have already used letter {letterGuessed}')
        #  print(word, hidden)
        # fourth part
        # asking if there is any letter unguessed
        if all('_' == character for character in word):
            print (f'Contratulations, YOU WIN!!')
            isGameOver = True
        # asking if attemps are equal to max_attempts
        if attempts >= max_attempts :
            print(f'So sorry, YOU LOOSE!!')
            isGameOver = True
            print('   _________')
            print('    |     |')
            print('    |     O')
            print('    |    / \\')
            print('    |     |')
            print('    |    / \\')
            print('----------- ')
    main()
def main():
    yesNo = input('Wanna start the game?[Yes/No]: ')
    if yesNo.lower() in ['yes', 'no']:
        if yesNo.lower() == 'yes' :
            play('paciencia') # set dynamic spanish word generator
        if yesNo.lower() == 'no':
            print('Ok. Sorry for asking')
    else :
        print('Please answer Yes or No')
        main()

main()
