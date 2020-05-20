#! usr/bin/python3
# from datacamp

a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
a['doughnut'] = 'snack'  # add key and value to dictionary
#print(a['apple'])
#print(a)

a = {'one': 1, 'two': 'to', 'three': 3.0, 'four': [4,4.0]}
#add element
a[1] = 1
a['jf'] = 2
a[4]='fj'
#print(a)

# delete element
del a['jf']
#print(a)
#del a['two']
#print(a)

#delete all elements
#a.clear()
#print(a)

#delete the directory
#del a
#print(a)   # //error: name 'a' is not defined//

# (key) no duplicates are allowed  LAST instance to be VALID

# 18/05/2020

f = dict.keys(a)
print(f)
g = dict.values(a)
print(g)
h = dict.items(a)
print(h)

# tripling each value in dict
a  = {'a': 1, 'b': 2, 'c': 3}
at = {k:v*3 for (k,v) in a.items()}
print(at)

import time

nr = range(2000000)
new_dict = {}

# add values to for 'new_dict' using for loop (number divisible by three and 'value' multiplied by five)
t1 = time.time()
for i in nr:
    if i%3 == 0:
        new_dict[i] = i*5
#print(new_dict)
t2 = time.time()
print(f'start loop method {t1}'
      f' finish loop method {t2} '
      f'The time it took: {t2-t1}')
loop_time = t2-t1

# 18/05/2020
# 19/05/2020 construction of the dict method and attempt to count the speed of action
# 20/05/2020 complete attempt to compare two methods

# adding values using dictionary comprehension
t3 = time.time()
new_dict_dick = {i:i*5 for i in nr if i%3 == 0}
#print(new_dict_dick)
t4 = time.time()
dict_time = t4 - t3
print(f'start dict method {t3} finish dict method {t4} The time it took {dict_time}')

a = dict_time
b = loop_time

# calculation of the time difference
the_times_difference = a-b if a>b else b-a

# Comparsion of the speed of the task performed
# establishing a faster method
faster_method = a if a>b else b

# statment
if  faster_method == b:
    print(f'The dict method {the_times_difference} seconds faster then the loop method.')
else:
    print(f'The loop method {the_times_difference} seconds  faster then the dict method.')




