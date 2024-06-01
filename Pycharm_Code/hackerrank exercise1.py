##################################### Hackerrank exercise #####################################################

# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.


if __name__ == '__main__':
    N =int(input())
x=0
lst=[]

inp=list()
while(x<N):
    inp.append(input())
    #print(inp)
    x+=1

for x in inp:
    y=str(x)
    a=y.split()
    if(a[0]=='insert'):
        lst.insert(int(a[1]),int(a[2]))
    elif(a[0]=='append'):
        lst.append(int(a[1]))
    elif(a[0]=='remove'):
        lst.remove(int(a[1]))
    elif (a[0] == 'print'):
        print(lst)
    elif (a[0] == 'reverse'):
        lst.reverse()
    elif (a[0] == 'pop'):
        lst.pop()
    elif (a[0] == 'sort'):
        lst.sort()









