age = int(input('Enter your age'))

if age >= 56:
    print('you are eligible for senior citizen quota')

else:
    print('you are not a senior citizen')

mark = int(input('Enter your mark'))

if mark >= 90 and mark < 100:
    print("grade is A")

elif mark >= 80 and mark < 90:
    print('grade is B')

elif mark >= 70 and mark < 80:
    print('grade is C')

elif mark < 70:
    print('grade is F')

else:
    print('invalid mark')
