taxable_income = int(input("State your taxble income: "))
tax = 0
if taxable_income <= 20000:
    tax = taxable_income * 0.02
elif taxable_income <= 50000:
    tax = 400 + 0.25 * (taxable_income - 20000)
else:
    tax = 1150 + 0.35 * (taxable_income - 50000)

print(tax)