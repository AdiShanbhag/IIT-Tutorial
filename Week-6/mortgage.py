def get_inputs():
    P = float(input("Loan amount (principal): "))
    r_annual = float(input("Annual interest rate (percent): "))
    years = int(input("Term in years: "))
    mp = input("Monthly payment (Enter to auto-compute): ").strip()
    if mp == "":
        i = (r_annual / 100.0) / 12.0
        n = years * 12
        if i == 0:
            M = P / n
        else:
            M = P * (i * (1 + i) * n) / ((1 + i) * n - 1)
    else:
        M = float(mp)
    return P, r_annual, years, M

def compute_schedule(P, r_annual, years, M):
    i = (r_annual / 100.0) / 12.0
    n = years * 12
    rows = []
    bal = P
    total_interest = 0.0
    total_paid = 0.0
    for m in range(1, n + 1):
        beg = bal
        interest = beg * i
        principal_reduction = M - interest
        if principal_reduction <= 0 and i > 0:
            raise ValueError("Monthly payment too low.")
        end = beg - principal_reduction
        payment_this_month = M
        if end < 0:
            principal_reduction += end
            payment_this_month = interest + principal_reduction
            end = 0.0
        total_interest += interest
        total_paid += payment_this_month
        rows.append((m, round(beg, 2), round(interest, 2),
                     round(principal_reduction, 2), round(payment_this_month, 2),
                     round(end, 2)))
        bal = end
        if bal <= 0:
            break
    return rows, round(total_interest, 2), round(total_paid, 2)

def print_schedule(rows, total_interest, total_paid):
    print("\nAmortization Schedule")
    print("-" * 80)
    print(f"{'Mo':>3} {'Beg Bal':>12} {'Interest':>10} {'Principal':>11} "
          f"{'Payment':>10} {'End Bal':>12}")
    print("-" * 80)
    for m, beg, intr, princ, pay, end in rows:
        print(f"{m:>3} {beg:>12,.2f} {intr:>10,.2f} {princ:>11,.2f} "
              f"{pay:>10,.2f} {end:>12,.2f}")
    print("-" * 80)
    print(f"{'TOTAL PAID:':>50} {total_paid:>10,.2f}")
    print(f"{'TOTAL INTEREST:':>50} {total_interest:>10,.2f}")

def main():
    P, r_annual, years, M = get_inputs()
    rows, total_interest, total_paid = compute_schedule(P, r_annual, years, M)
    print_schedule(rows, total_interest, total_paid)

if __name__ == "_main_":
    main()