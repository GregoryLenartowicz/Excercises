# from: /www.w3schools.com/python/python

# 25/05/2020
# 26/05/2020


# repetition of previous lessons

# Strings

# lenght
txt = 'Use negative indexes to start the slice from the end of the string. '
print(len(txt))

# count how many letters are in a sentence
# number of characters in a sentence
num_characters = len(txt)
# number of spaces
num_of_spac = txt.count(' ')

print(f'There are { num_characters - num_of_spac } letters the sentence')

# megative indexing
print(txt[-10:-6])
print(txt[-50:-30])

# strip() removes whitespace (from the beginning or the end, or both)
print(txt.strip())
print(txt[60:70])

# lower()  upper() title() method
print(txt.lower())
print(txt.upper())
print(txt.title())

# count()
print(txt.count(" "), 'spaces in this sentence')
print(txt.count('a'))
word_in_sentence = (txt.count(' '))
print(word_in_sentence ,' word in sentence')
print(type(word_in_sentence))
 # syntax string.cound( to search for , start of search , end of search)
print(txt.count('t', 1 , 60))


# replace() method
print(txt.replace('t', '1'))

# split() method (splits string into substring)
print(txt.split())

# check string
x = 'the' in txt
print(x)
x = 'the' not in txt
print(x)

# string concatenation
word = 'add'
print(txt + word)
print(txt+' any info str '+word)

# check if object is...
x = 200
print(isinstance(x , str))
print(isinstance(x, bool))
print(isinstance(x, complex))
print(isinstance(x, int))

# Lists

sample_list = [ 'zero', 'one', 'two', 'three']
print(sample_list[2])
print(sample_list[1:3])
print(sample_list[:])
print(sample_list[:2])
sample_list[3] = 'four'
sample_list.append('five')
print(sample_list)

