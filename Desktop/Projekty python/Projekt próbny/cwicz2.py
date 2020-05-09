#    Użytkownik wybiera czy obstawia resztę, czy orła (literka r – reszka, literka o – orzeł)
#    Po dokonaniu wybory, Komputer odlicza 3,2,1, a następnie dokonuje ‚rzutu’, czyli losowego wyboru orzeł / reszka.
#    Komputer wyświetla wynik rzutu.
#    Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli komputer to dodaje punkt dla komputera.
#    Wyświetla wyniki
#    Wracamy do punktu 1

import time
#imort random

choice = ('h', 't')

a = 'heads'
t = 'tails'

I = 0
bot = 0

while I < 10 or bot < 6:
    my_choice = input('Make a choice: a - heads or t - tails: ')
    print(my_choice)
    remaining_time = 4

    while remaining_time >1:
        time.sleep(1)
        remaining_time -=1
        print(remaining_time)
    bot += 1
    print(bot)

