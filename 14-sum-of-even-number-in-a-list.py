n = int(input())
a = list(map(int, input().split()))
tong = 0
for i in a:
    if i % 2 == 0:
        tong += i
print(tong)
