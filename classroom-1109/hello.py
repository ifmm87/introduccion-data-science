print('######################### Hello from my second contact with python #############################')
print('############################################################################################')
# Python is a sequence focused language
print('the first element of the RAMMStein ("RAMMStein[0]")is:', "RAMMStein"[0])
print(int('56 '))
## references
print('Python is  a Object referenced languaje (as JS)')
x = 'blue'
y = 'green'
z = x; # I was expecting z = blue
x = 'blue changed'
print ('printing values ==>', x,y,z)
z = y
print ('printing values ==>', x,y,z)
x = z
print ('printing values ==>', x,y,z)
x = 'blue changed'
print ('printing values ==>', x,y,z)

## types
name = 'jorgito'
edad = 70
print(f'type(someting), name {name} type {type(name)}, edad {edad}, {type(edad)}' )
# Experimente with tuples, comma separated values
tuple = "one","two"
print(f'this is a {tuple} tuple ')
# LEN
# get the length from anything

print('we use len(object) to extract the length, len from string automatically ', len("automatically"))
print('we use len(object) to extract the length, len from tuple or array ', len(tuple))
print(len([0,5,6,'h']))

# operations with arrays
print('Operations with arrays, easier than JS')
a = [5,6]
b = [7,8]
print(f'I got a {a} and b {b}, both arrays, let\'s use append', a.append('appended element'), a)
print(f'I got a {a} and b {b}, both arrays, let\'s use append', list.append(a,b), a)
print(f'I got a {a} and b {b}, both arrays, let\'s use add')
a += b
print (a, '<== here we just use + operator>')
# python is referenced as js XD
a = [5,6]
b = [5,6]
print(f'Using boolean operators {a} is equal to {b} ?', a is b, 'Why?')
b = a
print(f'Using boolean operators {a} is equal to {b}?, no, but if b =a then :', a is b, 'Why?')
# Membership operator
print(f'If we got {a}, is 5 in {a}?', 5 in a)

# try except statement
print('Try except statement')

inp = input('enter a integer:')
try:
    i = int(inp)
    print(3 in b)
    print('the value is:', i)
except ValueError as error:
    print(error, 'a error ocurred')
