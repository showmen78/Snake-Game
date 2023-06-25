import turtle
import time
from snake import Snake

WIDTH=800
HEIGHT=600

fps = 30
STEPS=5

#creating a window
wn = turtle.Screen()
#setting the width and height of the screen
wn.setup(width=WIDTH,height=HEIGHT)
#background color of the screen
wn.bgcolor("#034787")
#setting the animation on this window off
wn.tracer(0)


#take input


#snake object
snake= Snake(.85,wn=wn)





while True:

    if not snake.GAMEOVER:
        wn.update()

        snake.move()  
        time.sleep(1/fps)

    else:
        snake.restart()



wn.mainloop()