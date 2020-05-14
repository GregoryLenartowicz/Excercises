### Eexercise: Random letter
#!good habits!#

import random
#random choice
s = random.randint(97,97+25)
letter = chr(s)
print(letter)

#random letter from the generated alphabet

alphabet = []
for i in range(97,97+26):
    p = chr(i)
    alphabet += p
#    print(alphabet, end=' ')
rand_let = random.choice(alphabet)
print(rand_let)

print(chr(97+25))





