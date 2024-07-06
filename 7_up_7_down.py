import random

def roll_dice():
    return random.randint(1, 6), random.randint(1, 6)

def play_game():
    balance = 100
    choice = '0'
    while balance != 0:
        print(f"Current Balance: {balance} Rs")
        if(choice != '1'):
            play = input("Press 'P' to Play or 'Q' to Quit: ").strip().lower()
            
            if play == 'q':
                print("Thanks for playing!")
                break
            elif play != 'p':
                print("Invalid input. Try again.")
                continue
        
        balance -= 10
        print("10 Rs deducted from your balance.")
        print("Select your bet:")
        print("1. Below 7")
        print("2. Lucky 7")
        print("3. Above 7")
        
        bet = input("Enter your choice (1, 2, or 3): ").strip()
        
        if bet not in ['1', '2', '3']:
            print("Invalid choice. Try again.")
            balance += 10
            continue
        
        print("Rolling the dice...")
        die1, die2 = roll_dice()
        total = die1 + die2
        print(f"Dice rolled: {die1} and {die2}. Total: {total}")
        
        if (bet == '1' and total < 7) or (bet == '2' and total == 7) or (bet == '3' and total > 7):
            if bet == '2' and total == 7:
                balance += 30
                print("Congratulations! Lucky 7! You Win 30 Rs.")
            else:
                balance += 20
                print("Congratulations! You Win 20 Rs.")
        else:
            print("Sorry, you lost this round.")
        
        print(f"New Balance: {balance} Rs")
        print("1. Continue")
        print("2. Reset and Continue")
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == '2':
            balance = 100
            print("Balance reset to 100 Rs.")
        elif choice != '1':
            print("Invalid input. Continuing with current balance.")
    else:
        print("You have insufficient balance.")
if __name__ == "__main__":
    play_game()
