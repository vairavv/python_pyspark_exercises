n = int(input())
rev = 0

while (n > 0):
    rem = n % 10
    rev = 0 * rev + rem
    n = n // 10

print(rev)
