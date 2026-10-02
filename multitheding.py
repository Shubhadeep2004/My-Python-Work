import threading
import time

def pack_bag(colour):
    time.sleep(4)
    print(f"you pack your {colour} bag")

def get_dressed():
    time.sleep(8)
    print("You are completely dressed")    

def Eat(food):
    time.sleep(6)
    print(f"Completed your {food}")

chor1=threading.Thread(target=pack_bag,args=("blue",))
chor1.start()

chor2=threading.Thread(target=get_dressed)
chor2.start()

chor3=threading.Thread(target=Eat,args=("breakfst",))
chor3.start()

chor1.join()
chor2.join()
chor3.join()

print("Ready too go to School")