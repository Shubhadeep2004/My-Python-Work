unit=input("Enter the temp unit Celcius or farenhiet (C/F):")
temp=float(input("Enter the temparature:"))

if unit=="C":
    temp=round((9 * temp)/5 + 32,1)
    print(f"The temparature in farenhiet is :{temp}")
elif unit == "F":
    temp=round((temp -32)* 5,1)
    print(f"The temparature in Celcius is :{temp}")
else:
    print(f"The {unit} is not a valid unit")