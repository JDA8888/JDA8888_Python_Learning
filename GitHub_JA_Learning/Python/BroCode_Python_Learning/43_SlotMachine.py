# Python Slot Machine
import random

def spin_row():
    symbols = ['🍒', '🍉','🍋', '🔔', '🌟']
    
    return [random.choice(symbols) for _ in range(3)]
    
    

def print_row(row):
    print("-------------")
    print(" | ".join(row))
    print("-------------")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 2
        elif row[0] == '🍉':
            return bet * 3
        elif row[0] == '🍋':
            return bet * 4
        elif row[0] == '🔔':
            return bet * 8
        elif row[0] == '🌟':
            return bet * 20
    return 0
    

def main():
    balance = 100
    print("--------------------------------")
    print(" Welcome to Python Fruity Slots ")
    print("    Symbols: 🍒 🍉 🍋 🔔 🌟    ")
    print("--------------------------------")
    
    while balance > 0:
        print(f"  Current Balance: ${balance}  ")
        print("--------------------------------")
        
        bet = input("  Please your bet amount: ")
        
        if not bet.isdigit():
            print("--------------------------------")
            print("   Please enter a Valid number  ")
            print("--------------------------------")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("--------------------------------")
            print("     Insufficient Funds         ")
            print("--------------------------------")
            continue
        
        if bet <= 0:
            print("--------------------------------")
            print("   Bet must be greater than 0   ")
            print("--------------------------------")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("-------------")
        print("Spinning.....")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You Won ${payout}")
        else:
            print("Sorry you lost this round")
        
        balance += payout
        
        play_again = input("Do you want to sping again? (Y/N): ").upper()
        if play_again != 'Y':
            break
    print("--------------------------------------------")
    print(f"Game Over! Your Final Balance Is ${balance}")
    print("--------------------------------------------")




if __name__ == '__main__':
    main()