print(f'+++++++++++++++++++GENERATING AWFUL POETRY++++++++++++++++++++++')
#  import random from random
import random
# declaring arrays
articles = ['the', 'an', 'a', 'those', 'that', 'these', 'this']
subjects = [ 'cat', 'puppy','friend', 'lover', 'woman', 'children', 'parents', 'relatives', 'neighibors' ]
verbs = ['eat', 'loves', 'run away', 'shows', 'picks', 'sit down', 'end up', 'turn out' ]
adverbs = ['loudly', 'well', 'badly','always', 'quietly', '']
# Entering required number of awful verses
inp = input('Enter how many awful poetry verses you need: ')
# Iterating until inp number of verses
try:
    for n in range(int(inp)) :
        if random.randint(0,1) == 1 :
            print(f'{n + 1} {random.choice(articles)} {random.choice(subjects)} {random.choice(verbs)} {random.choice(adverbs)}')
        else :
            print(f'{n + 1} {random.choice(articles)} {random.choice(subjects)} {random.choice(verbs)}')
except ValueError as  error:
    print('You have not entered a number!.')
