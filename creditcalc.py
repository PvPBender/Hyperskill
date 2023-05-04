from math import ceil

enter_principal = "Enter the loan principal:"
question = """
    What do you want to calculate?
    type "m" - for number of monthly payments,
    type "p" - for the monthly payment:
    """
enter_payment = "Enter the monthly payment:"
enter_months = "Enter the number of months:"


def ask_principal():
    print(enter_principal)
    return float(input())


def ask_which():
    print(question)
    return input()


def get_months():
    print(enter_payment)
    payments = float(input())
    return principal / payments


def get_payment():
    print(enter_months)
    months = int(input())
    return ceil(principal / months), int(principal % ceil(principal / months))


principal = ask_principal()
if ask_which() == "m":
    months = get_months()
    if months == 1:
        print("It will take 1 month to repay the loan")
    else:
        print(f"It will take {ceil(months)} months to repay the loan")
else:
    months = get_payment()
    payments = months[0]
    last_payment = months[1]
    if last_payment != 0:
        print(f"Your monthly payment = {payments} and the last payment = {last_payment}")
    else:
        print(f"Your monthly payment = {payments}")
