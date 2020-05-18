#! usr/bin/python3

# which key is not a number?
z = {'ke' : 100, 'ke1' : 200, 1 : 'value1', 2 : 'value2', 'ke2' : 300}
f = ('fj','fd')

# use of the method: .items()
print(z)
print(z.items())
print(type(z.items()))  # class 'dict_items'

# dislay pars: key value
for k,v in z.items():
    print(k,':',v)

# check dict/tuple
if isinstance(f, dict):
    print('this is dictionary')
else:
    print('this is tuple')

# datacamp materials

s = {'cat':[4, 4.4, 'ir']}
print(s['cat'])






