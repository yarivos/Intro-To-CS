account_balances = {}  # a dictionary mapping account numbers to a balance
account_histories = {}  # a dictionary mapping account numbers to a list of transfer records.
                        # transfer records are a list of [from, to, amount]

def open_account(account):
    """creates a new account in the system. assumes the account number does not exist."""
    account_balances[account] = 0
    account_histories[account] = []


def deposit(account, amount_in_cents):
    """Deposits or withdraws funds from the account (a negative ammound is a withdrawal).
    returns False if the account doesn't exist."""
    if account not in account_balances:
        return False
    if account_balances[account] + amount_in_cents < 0:
        return False

    # update the balance and history.
    account_balances[account] += amount_in_cents
    if amount_in_cents > 0:
        account_histories[account].append([None, account, amount_in_cents])
    else:
        account_histories[account].append([account, None, -amount_in_cents])
    return True


def transfer(source_account, target_account, amount_in_cents):
    """Transfers money between two accounts.
    For the transfer to succeed: The accounts should both exist, and amount should be positive,
    and source account should have funds.
    The function returns True if the transfer succeeds, False otherwise"""

    if source_account not in account_balances or target_account not in account_balances:
        return False
    if amount_in_cents > account_balances[source_account]:
        return False

    # update balances
    account_balances[source_account] -= amount_in_cents
    account_balances[target_account] += amount_in_cents

    # update account histories
    history_record = [source_account, target_account, amount_in_cents]
    account_histories[source_account].append(history_record)
    account_histories[target_account].append(history_record)


def close_account(account):
    """account should exist and be empty"""
    if account in account_balances and account_balances[account] == 0:
        del account_balances[account]
        del account_histories[account]
        return True
    return False


def print_history_item(item):
    """prints a single history item"""
    source, target, amount = item
    if source is None:
        print("Deposit of", amount)
    elif target is None:
        print("Withdrawal of", amount)
    else:
        print("Transfer of", amount, "from", source, "to", target)


def print_menu():
    """prints the menu"""
    print("Please enter an action:")
    print("1. Open an account")
    print("2. Get balance")
    print("3. Transfer funds")
    print("4. Close account")
    print("5. Account history")
    print("6. Deposit or withdraw cash")
    print("7. Quit")


def main():
    """the main function. Runs in a loop and asks the user for actions to perform"""
    next_account_num = 1
    while True:
        print_menu()
        action = int(input())
        if action == 1:
            open_account(next_account_num)
            print("Opened account", next_account_num)
            next_account_num += 1
        elif action == 2:
            account = int(input("Please enter the account number"))
            if account not in account_balances:
                print("No such account")
            else:
                print("The balance is:", account_balances[account], "cents")
        elif action == 3:
            account = int(input("Please Enter the number of the source account"))
            target = int(input("Please Enter the number of the target account"))
            amount = input("Please Enter the amount to transfer")
            if transfer(account, target, amount):
                print("Ok")
            else:
                print("Transfer could not be completed")
        elif action == 4:
            account = int(input("Enter the account number"))
            if close_account(account):
                print("Account closed.")
            else:
                print("Account could not be closed")
        elif action == 5:
            account = int(input("Please enter the account number"))
            if account not in account_histories:
                print("Account not found")
            else:
                for item in account_histories[account]:
                    print_history_item(item)
        elif action == 6:
            account = int(input("Please enter the account number"))
            amount = int(input("Please enter the amount in cents (use a negative amount to withdraw). "))
            if deposit(account, amount):
                print("OK")
            else:
                print("Deposit / Withdrawal falied.")
        elif action == 7:
            print("Goodbye!")
            break
        else:
            print("Illegal action.")


main()