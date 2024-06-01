
################## list coding challenge ############################

food =['idly','roti','baby corn','dal','coffee']
print(food[2])
food.append('vadai')
print(food)
food.insert(3, 'tacos')
print(food)

###################for loop coding challenge ###########################

for a in range(5):
    print('i am a programmer')

def sqre():
    for a in range(1,10):
        print('square of a number ',a**2)

sqre()

#################Body Mass Index calculator #############################

weight =int(input("Enter the weight in KG"))

height =int(input("Enter the height in Meters"))

def fun(w,h):
    bmi=w/(h**2)
    return bmi

result = fun(weight , height)

print("BMI of given values is",result)

################# program to run a code until valid integer is given ##################
while True:
    try:
       x=int(input('Enter valid integer value'))
       break
    except (ValueError,NameError):
        print('Given input is not a valid integer')


############### program that handles divide by zero exception ###########################
a =int(input("Enter the numerator value"))

b =int(input("Enter the denominator value"))

def div(a,b):
    try:
        c=a/b
        return c
    except (ZeroDivisionError):
        print('please enter non zero value to avoid zero division exception')


result = div(a,b)

print ('division result is',result)


######### Write Python code which accepts name of a product and in turn returns their respective prices ##########

gunny = {
    'katti':40 ,
    'maavu':59,
    'seeni':55
}

product = input('Enter the input value')
print ('The price of',product,'is',gunny[product])
