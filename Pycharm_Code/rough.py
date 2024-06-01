
###### List out  all the odd numbers from 1 to 100 using lists in Python #####

odd = [x for x in range(1,100) if x%2==1]

print(odd)




x = open("muthu.txt", 'r')
# print(x.readline()) # reads first line from a file
print(x.read())  # reads entire file
x.close()

# Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression

result = (lambda x :x*(x+5)**2)(5)

print(result)


############################### printing numbers without delimiter #####################################
#solution 1 : using str method

n=int(input())

num = list(range(1,n+1))

def listtostring(num):
    str1=""
    for x in num:
        str1+=str(x)
    print(str1)

listtostring(num)










