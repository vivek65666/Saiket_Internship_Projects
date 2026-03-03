P = float(input("Enter Loan Amount: "))
rate = float(input("Enter Annual Interest Rate (%): "))
years = int(input("Enter Loan Tenure (years): "))

R = rate / (12 * 100)
N = years * 12

EMI = (P * R * (1 + R)**N) / ((1 + R)**N - 1)

print("\nMonthly EMI:", round(EMI, 2))