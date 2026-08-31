import math
def giải_phương_trình_bậc_hai(a, b, c):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm" if c == 0 else "Phương trình vô nghiệm"
        return f"Phương trình bậc nhất có 1 nghiệm: x = {-c / b}"
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm thực"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Phương trình có nghiệm kép: x1 = x2 = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
print(giải_phương_trình_bậc_hai(1, -5, 6))