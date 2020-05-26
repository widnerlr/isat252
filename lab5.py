"""
lab 5
"""
#3.1

alien_color = 'green'

if alien_color == 'green':
    print("player earned 5 points")
    
#3.2

if alien_color == 'green':
    print('player earned 5 points')
else: 
    print('player earned 10 points')
    
#3.3
favorite_fruits = ['banana','kiwi','strawberry']
if 'banana' in favorite_fruits:
    print("i like bananas")
if 'kiwi'in favorite_fruits:
    print('i love kiwis')
if 'strawberry' in favorite_fruits:
    print('strawberries are yummy')
if "apple" in favorite_fruits:
    print('apples are okay')
if "raspberry" in favorite_fruits:
    print('you really like rasperries')

#3.4
age=17

if age <10:
    print('this person is a kid')
elif age <20: 
    print('this person is a teenager')
else:
    print('this person is an adult')
    if age >65:
        print('this person is an elder')
    
