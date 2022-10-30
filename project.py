from turtle import *
import settings
import time

def draw_animation(num_frames, sleeptime):
    for i in range(num_frames):
        

        update()
        time.sleep(sleeptime)
    clear()

def main():
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)

    for i in range(settings.NUMREPEATS):
        draw_animation(settings.NUMFRAMES, settings.SLEEPTIME)



    
main()
