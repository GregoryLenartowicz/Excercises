# from datacamp

a = {'apple': 'fruit', 'beetroot': 'vegetable', 'cake': 'dessert'}
a['doughnut'] = 'snack'  # add key and value to dictionary
print(a['apple'])
print(a)

a = {'one': 1, 'two': 'to', 'three': 3.0, 'four': [4,4.0]}
#add element
a[1] = 1
a['jf'] = 2
a[4]='fj'
print(a)

# delete element
del a['jf']
print(a)
del a['two']
print(a)

#delete all elements
a.clear()
print(a)

#delete the directory
del a
print(a)   # //error: name 'a' is not defined//

# (key) no duplicates are allowed  LAST instance to be VALID
