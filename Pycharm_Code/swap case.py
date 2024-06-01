str_inp=input()
#str_inp='This is a string'
out=''
for i in str_inp:
    if(i.isupper()==True):
        out+=i.lower()
    elif(i.islower()==True):
        out+=i.upper()
    else:
        out+=i
print(out)