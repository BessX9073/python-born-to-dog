data = []
n =int(input())
for i in range(n):
    chapter = str(input())
    text = str(input())
    all = chapter + text
    data.append(all)
data.sort()
for i in range(n):
    print(f'Chapter {data[i][0]}')
    print(f'{data[i][1:]}')