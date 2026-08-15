def power_of_two(n):
    if n == 0:
        return 1
    else:
        return 2 * power_of_two(n-1)
if __name__ == '__main__':
    n = int(input('Enter n:'))
    result = power_of_two(n)
    print(result)
