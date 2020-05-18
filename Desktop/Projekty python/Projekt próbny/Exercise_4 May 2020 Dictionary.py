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


nr = range(20)
new_dict = {}

# add values to for 'new_dict' using for loop (number divisible by three and 'value' multiplied by five)
for i in nr:
    if i == 3:
        new_dict[i] = i*5
print(new_dict)

# if - comdition



