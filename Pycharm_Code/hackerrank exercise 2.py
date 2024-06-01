# generate all combination of list using list comprehension

#You are given three integers  and  representing the dimensions of a cuboid along with an integer .
#Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to .
#Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.

# x = 0
# y=1
# z=2
# n=2

# all permutation of [x,y,z] are [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2]]
#Print an array of the elements that do not sum to n=3

#########################################################################################################################

x = int(input())
y = int(input())
z = int(input())
n = int(input())

lst1 =list(range(0,x+1))
lst2 = list(range(0,y+1))
lst3 =list(range(0,z+1))

result = [[a, b, c] for a in lst1 for b in lst2 for c in lst3 if (a+b+c) != n ]

print(result)

