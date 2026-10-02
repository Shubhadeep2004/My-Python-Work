import time
import datetime
import pygame

def set_alarm(alram_time):
    print(f"the set alram is {alram_time}")
    sound="my_music.mp3.wav"
    is_running=True

    while is_running:
        current_time=datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time==alram_time:
            print("WAKE UP!!")

            pygame.mixer.init()
            pygame.mixer.music.pygame.image.load(sound)
            pygame.mixer.music.play()

            while pygame.mixer.music.pygame.get_busy():
                time.sleep(1)
            is_running=False
        
        time.sleep(1)    
                    

if __name__=='__main__':
    time=input("Enter the alarm time in(HH:MM:SS)-->")
    set_alarm(time)