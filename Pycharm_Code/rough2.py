### To find the greatest of 'n' numbers ####
import copy
n = int(input())

inp = (input())
lst = inp.split()
lst=list(map(int,lst)) # leveraged map() function to convert string to int
lstcopy1=copy.copy(lst)
lstcopy2=copy.copy(lst)
#print('the list copy is',lstcopy)

#print(lst)

if len(lst) != n:
    print('number of scores doesn\'t match with the given input')
    exit(1)
else:
    i = 0
    # abc =lst
    # print(abc)
    while i  < n-1:
        if (lstcopy1[i] > lstcopy1[i + 1]):
            temp = lstcopy1[i]
            lstcopy1[i + 1] = temp

    
        i += 1

#print('output of 1st iteration is',lstcopy1)
maxvalue = lstcopy1[i]

for z in range(0,len(lst)):
    if lst[z] == maxvalue:
        lstcopy2.remove(maxvalue)

m=len(lstcopy2)

#print('the input of 2nd iteration is',lstcopy2)
j = 0
while j < m - 1:
    if (lstcopy2[j] > lstcopy2[j + 1]):
        temp = lstcopy2[j]
        lstcopy2[j + 1] = temp

    j += 1

print( lstcopy2[j])