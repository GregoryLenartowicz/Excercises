#    Użytkownik wybiera czy obstawia resztę, czy orła (literka r – reszka, literka o – orzeł)
#    Po dokonaniu wybory, Komputer odlicza 3,2,1, a następnie dokonuje ‚rzutu’, czyli losowego wyboru orzeł / reszka.
#    Komputer wyświetla wynik rzutu.
#    Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli komputer to dodaje punkt dla komputera.
#    Wyświetla wyniki
#    Wracamy do punktu 1

# Next change 11/05/2020

import time
import random

choice = ('h', 't')

h = 'heads'
t = 'tails'

I = 0
bot = 0

while I < 3 and bot < 3:

    x = input('Make a choice: h - heads or t - tails: or "0" - to end the game ')
    print(x)

    if x == '0': break
    elif x == 'h': x = "head"
    elif x == 't': x = "tails"
    else:
        print('Tra again')
        continue

    # Random selection by bot
    random_select_bot = random.choice(['h','t'])

    # time countdown module
    for i in range(3):
        print(3 - i)
        time.sleep(1)

    print("bot choice:", random_select_bot)

    # point counter
    if  x == random_select_bot:
        I += 1
        print("another choice")
    else:
        bot += 1
        print("the same choice")
    print(f'I scored {I} points '
             f'bot scored {bot} points')

    if bot == 3:
        print('The winner is BOT')

    elif I == 3:
        print("I'm winner" )

