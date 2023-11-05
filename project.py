from turtle import *
from superturtle.animation import animate
from settings import NUMFRAMES, LOOP, SCREENHEIGHT, SCREENWIDTH


def draw_animation(num_frames, is_loop):
    for frame in animate(frames=num_frames, loop=True):
        pass # delete this and write your own code!        

def main():
    # set up the screen
    screen = Screen()
    screen.setup(SCREENWIDTH,SCREENHEIGHT)

    # call the animation function
    draw_animation(NUMFRAMES, LOOP)
 
main()
