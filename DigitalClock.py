import time

my_time=int(input("Enter the time in second's::"))

for x in reversed(range(1, my_time)):
    seconds=x % 60
    minutes=int(x / 60) % 60
    hour=int(x / 3600)

    print(f"{hour:02}::{minutes:02}::{seconds:02}")
    time.sleep(1)
print("TIMES UP !!!!")    