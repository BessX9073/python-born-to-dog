wdata = []
n = input()
n_list = input().split(' ')
w = input()
wdata.append(w)
true = 'No'
for i in n_list:
    if i == w:
        true = 'Yes'
print(true)

