questions=("1. What is the capital of India?",
          "2. What is the national bird of India? ",
          "3. Name the largest river of India?",
          "4. The hight of the MT.Evt?",
          "5. Total Number of Elemnt present in Periodic table?",
          "6. What  is the most abundant element in nature?")

option=(("A.Punjab","B.Delhi","C.Rajasthan","D.Chennai"),
        ("A.Pegion","B.Eagle","C.Peacock","D.Chicken"),
        ("A.Yamuna","B.Bhagirathi","C.Ganga","D.Bramhaputra"),
        ("A.8842 ft","B.8852 ft","C.8848 ft","D.8854 ft"),
        ("A.112","B.115","C.121","D.118"),
        ("A.N2","B.O2","C.CH4","D.NH3"))

answer=("B","C","C","C","D","A")
guesses=[]
score=0
que_num=0

for question in questions:
    print("-----------------")
    print(question)
    for opt in option[que_num]:
        print(opt)
    print() 
    guess=input("Enter(A ,B ,C ,B) :").upper()
    guesses.append(guess)
    score += 1
    if guess ==answer[que_num]:
        print("CORRECT")
    else:
        print("INCORRECT!")  
        print(f"{answer[que_num]} is the correct option")  
    
    que_num+=1

print('-----------------')
print("Result")
print("------------------")

for ans in answer:
    print(ans, end=" ")
print()

for guess in guesses:
    print(guess, end=" ")
print()


Total=int((score /len(questions)) *100)
print(f"The Total score is :{Total}%") 