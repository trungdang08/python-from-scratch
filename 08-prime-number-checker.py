def is_prime(n):
    if n <= 1: 
        return False
    for i in range (2, n):
        if n % i == 0:
            return False
    return True
if __name__ == '__main__':
    n = int(input())
    if is_prime(n) == True:
        print(n, 'is a prime number')
    else:
        print(n, 'is not a prime number')
