a = int(input())
b = int(input())
plus = a + b
plus = list(str(plus))
plus.reverse()
for i in plus:
    print(i,end=' '.replace(' ',''))


