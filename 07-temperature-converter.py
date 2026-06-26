def celsius_to_fahrenheit(C):
    F = C * 1.8 + 32
    return F
if __name__ == '__main__':
    C = int(input('Enter Celsius'))
    print(celsius_to_fahrenheit(C))
