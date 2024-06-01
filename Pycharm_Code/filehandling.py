########## reading a file #####################
x = open("muthu.txt", 'r')
# print(x.readline()) # reads first line from a file
print(x.read())  # reads entire file
x.close()

########## writing to a file ####################
y = open('muthu.txt', 'w')
y.write('muthuvairavan velikandan \n')  # overwrites the content
y.write('wanna become data analyst \n')
y.write('learning python \n')
y.close()     # once the file is closed, read/write operations are not allowed until the file is opened again.

########### appending data to a file ##############
z=open('muthu.txt','a')
z.write('currently learning file handling')
z.close()


