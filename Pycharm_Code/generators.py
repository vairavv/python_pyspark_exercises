################# fibonacci series using function #########################
def fibbonacci():
    a=1
    b=1
    print(a)
    print(b)
    i =0
    while i<100 :
        c = a+b
        print(c)
        a=b
        b=c
        i+=1

fibbonacci()

################ fibonacci series using generators ################

# generators are iterators

def fibbonacci():
    a=1
    b=1
    print(a)
    print(b)
    i =0
    while i<100 :
        c = a+b
        yield(c)
        a=b
        b=c
        i+=1

for x in fibbonacci() :
    print(x)






