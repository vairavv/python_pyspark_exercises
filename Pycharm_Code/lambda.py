##################### lambda example 1 ############################
square_root = lambda x :x*(1/2)
print (square_root(2))

##################### simple interest calculation by lambda ################

si = lambda p , n , r : (p*n*r)/100
# 3 arguments and 1 expression ## satisfies lambda rule of 'n' number of arguments & only one expression
print(si(100000,2,5))

###################### map function with lambda #############################

num = {1,2,3,5,7,11,13,17}

add = lambda a : a+1
newlist= list(map(add , num ))

print(newlist)

#################### filter function with lambda ###############################


fltr = lambda b : (b%2 == 1)

fltrlist = list(filter(fltr , num))

print(fltrlist)

####################### reduce function with lambda ##############################
import functools
result = functools.reduce((lambda x,y:x+y) ,newlist)

print(result)

############## below & above snippet are the same #################################

from functools import reduce
result = reduce( (lambda x,y:x+y) ,newlist)

print(result)



