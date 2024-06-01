import random

name = input('Hello. What is your name?\n')

print('Well, %s, I am thinking of a number between 1 and 20.' %name)
guess =random.randint(1,20)
print("Take a guess")
for i in range (0,6):
    inp = int(input())
    if inp==guess:
        print('you made it')
        break
    elif inp>guess:
        print('your guess is high.\nTake a guess')
    elif inp<guess:
        print('your guess is low.\nTake a guess')

if inp!=guess:
    print('Nope.Number i was thinking is %s'%guess)




