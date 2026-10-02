# Create a python compound intrest calculator

principle=0
time=0
rate=0

while principle <= 0 :
    principle=float(input("Enter the Principle ammount:"))
    if principle <= 0:
        print("Principle Can't be less or equal to zero")

while rate <= 0 :
    rate=float(input("Enter the Interest rate:"))
    if rate <= 0:
        print("Rate Can't be less or equal to zero")

while time <= 0 :
    time=int(input("Enter the total time in years::"))
    if time <= 0:
        print("time Can't be less or equal to zero")

print(f"The Principle is: {principle}")
print(f"The rate is: {rate}")
print(f"The time is: {time}")

Total=round(float(principle * pow((1+ rate/100),time)),3)

print(f"The Balancing ammount after {time} years is : {Total}")