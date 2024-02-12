#------------------CONSTANTS-------------------#
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#------------------Decorators------------------#
print("-----------------------------")
print("Welcome to the Casino! ")
print("You have €1000 in your account.")
print("You can bet on 1-3 lines.")
print("You can bet between €1-€100.")
print("Good luck!")
print("-----------------------------")
print ()

#------------------Balance input------------------#
def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: €€")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a valid amount.")
        else:
            print("Please enter a number.")
    return amount

#------------------Number of lines input------------------#
def get_number_of_lines():
    while True:
        lines = input("Enter the amount of lines you want to bet on: (1-" + str(MAX_LINES) + "?) ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Please enter a valid number of lines.")
        else:
            print("Please enter a number.")
    return lines

#------------------Bet input------------------#
def get_bet():
    while True:
        bet = input("Enter the amount you want to bet: (€€" + str(MIN_BET) + "-€€" + str(MAX_BET) + ") ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Please enter a valid bet between €€{MIN_BET} - €€{MAX_BET}.")
        else:
            print("Please enter a number.")
    return bet

#------------------Main------------------#
def main():
    balance = deposit()
    lines = get_number_of_lines()
    bet = get_bet()
    print(balance, lines, bet)







main()