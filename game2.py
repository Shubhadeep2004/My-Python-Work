#python SLOT MACHINE
import random

def spin_row():
    symbols=['🍒' ,'🍉' ,'⭐' ,'🥭' ,'🔔']

    result=[]
    [result.append(random.choice(symbols)) for _ in range(3)]

    return result
def print_row(row):
    
    print("***********")
    print(" | ".join(row))
    print("***********")

def get_payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0] == '🍒':
            return bet*2; 
        elif row[0] == '🍉':
            return bet*3;
        elif row[0] == '⭐':
            return bet*4;
        elif row[0] == '🥭':
            return bet*8;
        elif row[0] == '🔔':
            return bet*10;
    return 0    
def main():
    balance=int(input("Enter Your balance:"))

    print("**********************")
    print("Welcome to slot machine")
    print("symbols:🍒 🍉 ⭐ 🥭 🔔")
    print("**********************")

    while balance > 0:
        print(f"Your balance is ${balance}")

        bet=int(input("Enter your bet:"))
        
        if bet > balance:
            print("Insufficient balance")
            continue

        if bet <= 0:
            print("THe bet sahould be above 0:")
            continue

        balance -=bet
        row=spin_row()
        print("Spinning...\n")
        print_row(row)    
        payout=get_payout(row,bet)

        if payout > 0:
            print(f"Your payout is {payout}")
        else:
            print("sorry you lostv this round")    

        balance +=payout
        play_again=input("Do you want tio paly again (Y/N)").upper()    
if __name__ == '__main__':
    main()