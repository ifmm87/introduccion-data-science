variable = "ivan"
print(type(variable))
edad = 32
estatura = 1.68
persona = { variable, edad, estatura }
print(type(variable), type(edad), type(estatura), type(persona))
print(f'aca numero {edad} y string {variable}')
import math as math
pi = math.pi
pi_redondeado = round(pi, 3)
print(pi_redondeado)


import random as random
random_array = random.randint(0, 10)
random_array =  random.sample(range(0,30),6)
random.random()
print(random_array)


string1 = 'ivan'
string2 = 'mujica'
string3 =  'mamani castillo'
edad =  '333333333333333333333333333333333333333333333333333333333333333333'
print(string3.count('a'))
print(string3.islower())
print(string3.find('ma'))
print(string3.title())
print(string3.upper())
print(edad.isnumeric())




