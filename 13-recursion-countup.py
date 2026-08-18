def countup(m, n):
    if m == n or m > n:
        print('Done!')
        return
    if m < n:
        print(m)
        countup(m + 1, n)
if __name__ == '__main__':
    m = int(input('Enter countup number:'))
    n = int(input('Enter maximum number:'))
    countup(m, n)
