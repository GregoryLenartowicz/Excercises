### exercises for loops

for i in range(1,3):
    if i %2==0:
        print('first way', i, end=' ')

def EvenNumbersOnly(a,b):
    for i in range(a+1 if a%2 else a, b+1,2):
        print('second day', i, end=' ')


a,b = 1,2
EvenNumbersOnly(a,b)


