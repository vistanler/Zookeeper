a = int(input())
b = int(input())
c = 0

while a >= b:
    a = (a + 1) // 2
    c += 1

print(c * 12)