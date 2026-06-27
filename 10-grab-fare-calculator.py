def calculate_grab_fare(distance, is_rainy):
    if distance <= 1:
        base_fare = 20000
    else:
        base_fare = 20000 + (distance - 1) * 15000
    if is_rainy == True:
        total_fare = base_fare + 20000
    else: 
        total_fare = base_fare
    return total_fare
if __name__ == '__main__':
    distance = float(input('Enter distance'))
    print('Total fare on rainy days is:', calculate_grab_fare(distance, True))
    print('Total farre on normal days is:', calculate_grab_fare(distance, False))
