from savings_account import create_savings_account
from cd_account import create_cd_account

def main():
    """Prompts the user to enter the savings and cd account details,
    calls the corresponding functions to calculate the interest earned and update the balances,
    and displays the results.
    """
    # Prompt the user for savings account details
    savings_balance = float(input("Enter the savings account balance: "))
    savings_interest = float(input("Enter the savings account annual interest rate (as a decimal): "))
    savings_maturity = int(input("Enter the number of months for the savings account: "))

    # Calculate and display the savings account details
    updated_savings_balance, interest_earned_savings = create_savings_account(savings_balance, savings_interest, savings_maturity)
    print(f"Interest earned on Savings Account: ${interest_earned_savings:.2f}")
    print(f"Updated Savings Account Balance: ${updated_savings_balance:.2f}")

    # Prompt the user for CD account details
    cd_balance = float(input("Enter the CD account balance: "))
    cd_interest = float(input("Enter the CD account annual interest rate (as a decimal): "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))

    # Calculate and display the CD account details
    updated_cd_balance, interest_earned_cd = create_cd_account(cd_balance, cd_interest, cd_maturity)
    print(f"Interest earned on CD Account: ${interest_earned_cd:.2f}")
    print(f"Updated CD Account Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()
