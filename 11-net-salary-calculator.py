def calculate_net_salary(gross_salary):
    if gross_salary <= 11000000:
        tax = 0
    elif gross_salary <= 25000000:
        tax = (gross_salary - 11000000) * 0.1
    else:
        tax = 1400000 + (gross_salary - 25000000) * 0.2
        
    return gross_salary - tax

if __name__ == '__main__':
    while True:
        gross = float(input("Nhập lương Gross của bạn (Nhập 0 để thoát): "))
        if gross == 0:
            print("Tạm biệt!")

     
        net = calculate_net_salary(gross)
        print(f"Lương thực nhận (Net): {net:,.0f} VND\n") # Đoạn này giúp in ra có dấu phẩy phân tách hàng nghìn cho đẹp
