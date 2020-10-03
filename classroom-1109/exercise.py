# reading X = 3 elements
import numpy as np
n = 4
arr = [''] * (n)
print(f'array {arr}')
for k in range(n) :
    inp = input('Enter an element:')
    arr[k] = inp
# inverse
for k in range(round(n / 2)) :
    aux = arr[k]
    arr[k] = arr[n-k-1]
    arr[n-k-1] = aux
print (f'The inverted array is {arr} :)')

