from math import ceil, log
from textwrap import dedent


def get_n_of_months() -> int:
    principal = float(input("Enter the loan principal:\n"))
    monthly_payment = float(input("Enter the monthly payment:\n"))
    monthly_interest = float(input("Enter the loan interest:\n")) / 12 / 100

    return ceil(log(monthly_payment / (monthly_payment - monthly_interest * principal), 1 + monthly_interest))


def get_monthly_payment() -> int:
    principal = float(input("Enter the loan principal:\n"))
    n_of_months = int(input("Enter the number of periods:\n"))
    monthly_interest = float(input("Enter the loan interest:\n")) / 12 / 100

    interest_compound_factor = monthly_interest * ((1 + monthly_interest) ** n_of_months)
    interest_growth_factor = ((1 + monthly_interest) ** n_of_months) - 1
    payment_per_dollar = interest_compound_factor / interest_growth_factor

    return ceil(principal * payment_per_dollar)


def get_principal() -> int:
    monthly_payment = float(input("Enter the monthly payment:\n"))
    n_of_months = int(input("Enter the number of periods:\n"))
    monthly_interest = float(input("Enter the loan interest:\n")) / 12 / 100

    interest_compound_factor = monthly_interest * ((1 + monthly_interest) ** n_of_months)
    interest_growth_factor = ((1 + monthly_interest) ** n_of_months) - 1
    payment_per_dollar = interest_compound_factor / interest_growth_factor

    return int(monthly_payment / payment_per_dollar)


def main():
    question = dedent("""
    What do you want to calculate?
    type "n" for number of monthly payments,
    type "a" for annuity monthly payment amount,
    type "p" for loan principal:
    """)

    if (to_calculate := input(question)) == "n":
        n_of_months = get_n_of_months()
        n_of_years = n_of_months // 12
        n_of_months %= 12
        years_str = f"{n_of_years} year{'s' if n_of_years > 1 else ''} " if n_of_years else ""
        and_str = "and " if n_of_months and n_of_years else ""
        months_str = f"{n_of_months} month{'s' if n_of_months != 1 else ''} " if n_of_months or not years_str else ""
        print(f"It will take {years_str}{and_str}{months_str}to repay the loan!")

    elif to_calculate == "a":
        print(f"Your monthly payment = {get_monthly_payment()}!")

    elif to_calculate == "p":
        print(f"Your loan principal = {get_principal()}!")

    else:
        print('You can only type "n", "a", or "p"')


if __name__ == "__main__":
    main()
