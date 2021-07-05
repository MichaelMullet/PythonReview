balance = 3926
annualInterestRate = 0.2

newBalance = balance
monthIntRate = (annualInterestRate)/12.0
epsilon = 0.01
low = newBalance / 12
high = (newBalance * (1 + monthIntRate)**12) / 12.0
monthlyPayment = (high + low) / 2.0

while abs(high - low) >= epsilon:
    for month in range(12):
        newBalance -= monthlyPayment
        newBalance += (annualInterestRate/12.0) * newBalance
    if newBalance > 0:
        month = 0
        newBalance = balance
        low = monthlyPayment
    else:
        month = 0
        newBalance = balance
        high = monthlyPayment
    monthlyPayment = (high+low)/2.0
print('Lowest Payment: ' + str(round(monthlyPayment, 2)))