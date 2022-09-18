import random as rn

print('Gambling Marbles')
# create a bag of ten marbles, 6 green and 4 red
bag = ['green'] * 5 + ['red'] * 3 + ['black'] + ['white']
# User starts with a grand (£1000)


def Marble():
    # User picks a marble at random
    purse = 1000
    print('To play, enter an amount you would like to bet. You will lose if your purse is £500 or less.\nTo exit game, enter a non-number as your bet.')
    while (purse > 500):
        # Exit the game if non-inter is entered
        try:
            bet = int(input('How many pounds would you like to bet?: '))
        except ValueError:
            print('You have exited the game')
            break
        # Bets must be placed within the confines of the purse
        if bet > purse:
            print('Your betting above your paygrade. Try again.')
            continue

        choice = rn.choice(bag)
        print(f'A {choice.capitalize()} marble was chosen.')
        # Green wins the bet
        if choice == 'green':
            purse = purse + bet
            print(f'You have won £{bet}. You now have £{purse}.')
        # Red loses the bet
        elif choice == 'red':
            # choice == 'red':
            purse = purse - bet
            print(f'You have lost £{bet}. You now have £{purse}.')
        # Black marble wins 10x the bet
        elif choice == 'black':
            purse = purse + (10 * bet)
            print(f'You have won £{bet*10}. You now have £{purse}.')
        # White marble loses 5x the bet
        elif choice == 'white':
            purse = purse - (5*bet)
            print(f'You have lost £{bet*5}. You now have £{purse}.')

    return print(f'You have finished with £{purse} left in your purse.')


Marble()
