n = int(input())
a = list(map(int, input().split()))
k = int(input())
xuathien = False
for i in range(len(a)):
    if k == a[i]:
        xuathien = True
        break
if xuathien is True:
    print('YES')
else:
    print('NO')
