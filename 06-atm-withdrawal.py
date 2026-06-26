n = int(input())
bill100 = 0
bill50 = 0
bill20 = 0
bill10 = 0
bill1 = 0
while n > 0:
    if n >= 100:
        n = n - 100
        bill100 += 1
    elif n >= 50:
        n = n - 50
        bill50 += 1
    elif n >= 20:
        n = n - 20
        bill10 += 1
    elif n >= 10:
        n = n - 10
        bill10 += 1
    else:
        bill1 = n
        n = 0
print('n includes', bill100, 'of $100 bills', bill50, 'of $50 bills', bill20, 'of $20 bills', bill10, 'of $10 bills', bill1, 'of $1 bills')
