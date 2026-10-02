#Banking System 

def show_balance(balance):
    print("*************")
    print(f"The Balance in your account is {balance:.2f}")
    print("*************")
def withdraw(balance):
    print("*************")
    ammount=float(input("Enter the withdrawn ammount:"))

    if ammount > balance:
        print("Insufficient ammount")
        return 0
    elif ammount < 0:
        print("The +Ammount is invalid")
        return 0
    else:
        return ammount    
def deposite():
    print("*************")
    ammount=float(input("Enter the deposite2 ammount:"))

    if ammount > 0:
        return ammount
    else:
        print("The Ammount is invalid")
        return 0
    
def main():
    balance=0
    is_running=True

    while is_running:
        print("---Bank details---")
        print("1.Show Balance:")
        print("2.Deposite money:")
        print("3.Withdraw money:")
        print("4.Exit")

        Choice=int(input("Enter the coice (1-4):"))

        if Choice==1:
            show_balance(balance)
        if Choice==2:
            balance +=deposite()
        if Choice ==3:
            balance -=withdraw(balance)
        if  Choice ==4:
            is_running =False
            
        print("*************")
        print("Thank You For Connecting")         
        print("*************") 
if __name__=='__main__':
    main()        