from math import ceil, log
import argparse


def get_periods(principal: float, monthly_payment: float, interest: float) -> int:
    monthly_interest = interest / 12 / 100

    return ceil(log(monthly_payment / (monthly_payment - monthly_interest * principal), 1 + monthly_interest))


def get_monthly_payment(principal: float, n_of_months: int, interest: float) -> int:
    monthly_interest = interest / 12 / 100

    interest_compound_factor = monthly_interest * ((1 + monthly_interest) ** n_of_months)
    interest_growth_factor = ((1 + monthly_interest) ** n_of_months) - 1
    payment_per_dollar = interest_compound_factor / interest_growth_factor

    return ceil(principal * payment_per_dollar)


def get_principal(monthly_payment: float, n_of_months: int, interest: float) -> int:
    monthly_interest = interest / 12 / 100

    interest_compound_factor = monthly_interest * ((1 + monthly_interest) ** n_of_months)
    interest_growth_factor = ((1 + monthly_interest) ** n_of_months) - 1
    payment_per_dollar = interest_compound_factor / interest_growth_factor

    return int(monthly_payment / payment_per_dollar)


def get_diff_payment(principal: float, n_of_months: int, interest: float, current_month: int) -> int:
    monthly_interest = interest / 12 / 100

    principal_payment = principal / n_of_months
    interest_payment = monthly_interest * (principal - (principal * (current_month - 1) / n_of_months))

    return ceil(principal_payment + interest_payment)


def print_overpayment(principal: float, monthly_payment: float, n_of_months: int) -> None:
    overpayment = int(abs(principal - monthly_payment * n_of_months))
    print(f"Overpayment = {overpayment}")


def main():
    parser = argparse.ArgumentParser(
        prog="Loan Calculator",
        description="This program calculates parameters of annuity and differentiated payments.",
    )
    parser.add_argument("--type",
                        choices=["annuity", "diff"],
                        help="You can calculate either the annuity or the differentiated payments.",
                        )
    parser.add_argument("--principal",
                        type=float
                        )
    parser.add_argument("--payment",
                        type=float,
                        )
    parser.add_argument("--periods",
                        type=int
                        )
    parser.add_argument("--interest",
                        type=float
                        )
    args = parser.parse_args()

    if args.interest is None or\
            args.type == "diff" and args.payment is not None or\
            any(value < 0 for key, value in vars(args).items() if value is not None and key != "type") or\
            len(empty_args := [key for key, value in vars(args).items() if value is None]) != 1:
        print("Incorrect parameters")

    else:
        to_calculate = empty_args[0]

        if args.type == "diff":
            overpayment = args.principal

            for current_month in range(1, args.periods + 1):
                current_payment = get_diff_payment(args.principal, args.periods, args.interest, current_month)
                print(f"Month {current_month}: payment is {current_payment}")
                overpayment -= current_payment

            print(f"\nOverpayment = {int(abs(overpayment))}")

        else:
            if to_calculate == "principal":
                principal = get_principal(args.payment, args.periods, args.interest)
                print(f"Your loan principal = {principal}!")

                print_overpayment(principal, args.payment, args.periods)

            elif to_calculate == "payment":
                monthly_payment = get_monthly_payment(args.principal, args.periods, args.interest)
                print(f"Your monthly payment = {monthly_payment}!")

                print_overpayment(args.principal, monthly_payment, args.periods)

            elif to_calculate == "periods":
                periods = get_periods(args.principal, args.payment, args.interest)
                n_of_years = periods // 12
                n_of_months = periods % 12

                years_str = f"{n_of_years} year{'s' if n_of_years > 1 else ''} " if n_of_years else ""
                and_str = "and " if n_of_months and n_of_years else ""
                months_str = f"{n_of_months} month{'s' if n_of_months != 1 else ''} " if n_of_months or not years_str else ""

                print(f"It will take {years_str}{and_str}{months_str}to repay the loan!")

                print_overpayment(args.principal, args.payment, periods)


if __name__ == "__main__":
    main()
