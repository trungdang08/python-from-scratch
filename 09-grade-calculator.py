def calculate_average(m, p, c):
    res = (m + p + c) / 3
    return res
def get_academic_score(n):
    if n >= 8:
        return 'Excellent'
    elif n >= 6.5 and n < 8:
        return 'Good'
    elif n >= 5 and n < 6.5:
        return 'Average'
    else:
        return 'Weak'
if __name__ == '__main__':
    m = float(input('Enter Math Score:'))
    p = float(input('Enter Physics Score:'))
    c = float(input('Enter Chemistry Score:'))
    avg = calculate_average(m, p, c)
    print(f"Average Score: {avg:.2f}")
    rank = get_academic_score(avg)
    print(f"Academic Rank: {rank}")
