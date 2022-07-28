n = int(input("Enter the number : "))
s = 0
while n > 0:
    r = n % 10
    s = s * 10 + r
    n //= 10
print(f"Reverse : {s}")
