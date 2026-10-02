Oparater=input("Enter the Oparater(+,-,*,/):")
num1=float(input("Enter the number:"))
num2=float(input("Enter the number:"))

if Oparater== "+":
    result=num1+num2
    print(f"The output is:{result}")
elif Oparater == "-":
    result=num1-num2
    print(f"The output is:{result}")
elif Oparater == "*":
    result=num1*num2
    print(f"The output is:{result}") 
elif Oparater == "/":
    result=num1 / num2
    print(f"The output is:{result}") 
else:
    print("Ivalid Oparater!!!!")          