K0 = float(input("Enter the initial balance (K0): "))
interest_rate = float(input("Enter the interest rate(percentage): "))
K1 = K0 * (1 + interest_rate / 100)
print("Capital after one year (K1): ",K1)
n = int(input("Enter the number of years: "))
Kn = K0
year = 0
while year < n:
    Kn = Kn * (1 + interest_rate / 100)
    year += 1
print("Capital after",n," years:",Kn)
