### Eexercise: Random letter
#!good habits!#

import random
#random choice
s = random.randint(97,97+25)
letter = chr(s)
#print(letter)

#random letter from the generated alphabet
alphabet = []
for i in range(97,97+26):
    p = chr(i)
    alphabet += p
#    print(alphabet, end=' ')
rand_let = random.choice(alphabet)
#print(rand_let)

# different approach
q = ('dfgfdsgargarcvfergserh')
w = random.choice(q)
print(w)
print(len(q))

# check if an element exists in the set
print('v' in q)

# drawing a square random size
n = random.randint(4,8)
print(n)
for i in range(1,n+1):  # height (y axis)
    print(w*n)            # width  (x axis)

# drawing an empty square
for i in range(1,n+1):
    print(w, w*(n-2) if i in (1,n) else ' '* (n-2),w)