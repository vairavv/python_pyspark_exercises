lst =[0 ,5,6,5,2]

n = len(lst)
# snippet for sorting a list
j=0
while (j < n-1):
    i=0
    while (i< n-1):
        if (lst[i] > lst[i+1]):
            temp=lst[i]
            lst[i] = lst[i + 1]
            lst[i+1] = temp

        i+=1
    j+=1

print(lst)
