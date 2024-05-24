from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class
    account = Account(balance, 0)

    # Calculate interest earned
    monthly_interest_rate = interest_rate / 12
    interest_earned = balance * ((1 + monthly_interest_rate) ** months - 1)

    # Update the balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Pass the updated balance and interest to the Account instance
    account.set_balance(updated_balance)
    account.set_interest(interest_earned)

    return updated_balance, interest_earned
