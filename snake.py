'''
 -- Snake Class 
 -- Contains all the functions of Snake

'''
import turtle
import random
import time


class Snake:
    def __init__(self,size,wn:turtle.Screen,pos=turtle.Vec2D(0,0)):
        '''
            input:
                size (int): size of the square that makes up the snake body (defalut value 20px)
                pos (Vec2d) : initial position of the snake head
                wn  (turtle.screen): window 
        '''
        self.size = size
        #contains the position of the all the body parts of the snake
        self.pos = [pos]
        self.body= [self.create_segment('#FC401A',self.pos[0])]

        #direction of the snake movement
        self.direction=turtle.Vec2D(0,0)
        #steps to be taken per frame
        self.steps=5 
      
        #TAKE KEYBOARD INPUT
        self.wn = wn
        self.wn.listen()
        self.take_input(self.wn)

        #THE FOOD
        self.food = None
        self.make_food()

        #IF GAME OVER OR NOT    
        self.GAMEOVER=False

        #SCORE OF THE GAME
        self.score=0
        self.HIGHSCORE=0

        self.pen= self.create_pen()



    def create_segment(self,color:str,pos:turtle.Vec2D):
        '''
        -- create body parts of the snake body and return it
        input:
            color (color): color of the segment created
            pos (vec2d)  : pos , where to position the segment

        output:
            return the a turtle object 

        '''
        s= turtle.Turtle()
        s.penup()
        s.speed(0)
        s.color('white',color)
        s.goto(pos)
        s.shape('square')
        s.shapesize(self.size, self.size, 3)
        return s
    

    def take_input(self,wn):    
        '''
        -- TAKES INPUT FROM KEYBOARD
        -- INPUT:
                WN (TURTLE.SCREEN) : WINDOW OF THE GAME
        '''        
        wn.onkeypress(lambda:self.change_direction(turtle.Vec2D(0,1)), "Up")
        wn.onkeypress(lambda:self.change_direction(turtle.Vec2D(0,-1)), "Down")
        wn.onkeypress(lambda:self.change_direction(turtle.Vec2D(-1,0)), "Left")
        wn.onkeypress(lambda:self.change_direction(turtle.Vec2D(1,0)), "Right")
    
    
    def change_direction(self,direction):
        '''
        -- CHANGES THE DIRECTION OF THE SNAKE HEAD
        INPUT:
            DIRECTION(VEC2D): NEW DIRECTION
        '''
        #if the current direction and new direction are not oposite , then change the direction
        if abs(self.direction+ direction) !=0:
            self.direction= direction


    def keep_the_snake_inside(self):
        '''
        -- IF THE SNAKE GO OUTSIDE OF THE SCREEN,THEN BRING IT BACK FROM THE OPPOSITE DIRECTION
        '''
        current_pos = self.body[0].pos()
        if current_pos[0]>= self.wn.window_width() /2 or current_pos[0]<= -self.wn.window_width()/2 :
            self.body[0].goto(self.direction[0]*-self.wn.window_width()/2,current_pos[1])

        if current_pos[1]>= self.wn.window_height() /2 or current_pos[1]<= -self.wn.window_height()/2 :
            self.body[0].goto(current_pos[0],self.direction[1]*-self.wn.window_height()/2)

    
    def make_food(self):
        '''
        -- CREATES FOOD  AND ADD NEW SEGMENT TO THE SNAKE EACH TIME IT EATS A FOOD
        
        '''
        #IF THERE IS NO FOOD THEN CREATE FOOD
        if self.food== None:
            self.food=self.create_segment('yellow',turtle.Vec2D(100,100))
        
        # IF THERE IS FOOD THEN JUST REPOSITON THE FOOD , WHEN SNAKE EATS THE FOOD
        else:
            self.food.goto(random.randint(-self.wn.window_width()/2 +10,self.wn.window_width()/2-10),
                           random.randint(-self.wn.window_height()/2 +10,self.wn.window_height()/2 -10))
            
            # GENERATE NEW SEGMENT AND ADD IT TO THE SANKE BODY
            self.body.append(self.create_segment('#019B18',self.pos[-1]))
            self.score += 1
            self.steps += .1
            self.Update_Score()
            

        

    def move(self):
        '''
        -- move the snake in the direction specified
            
        '''
        #UPDATE THE LOCATION OF THE EACH BODY SEGMENT 
        for segment in range(len(self.body)):
            if segment==0:
                self.body[segment].goto(self.body[segment].pos()+ self.steps*self.direction)

                #update the position .  for n body segments keep n+1 position.
                if abs(self.body[0].pos()-self.pos[0])>= 1/(10**self.steps):
                    self.pos.insert(0,self.body[0].pos())
                    self.pos= self.pos[0:len(self.body)+1]
            else:
                if len(self.pos)>1:
                    self.body[segment].goto(self.pos[segment])

            #IF THE HEAD OF THE SNAKE TOUCHES ITS BODY , THEN GAME OVER
                if self.body[0].distance(self.body[segment])<=5:
                    print('game over')
                    self.GAMEOVER= True

                    
        #keeps the snake inside the screen
        self.keep_the_snake_inside()


        #if snake head position is at the food position then make food
        if self.body[0].distance(self.food) <= 20:
            self.make_food()

            
    def restart(self):
        if self.GAMEOVER:
            for b in range(1,len(self.body)):
                self.body[b].hideturtle()
            
            self.body=[self.body[0]]
            self.pos.clear()
            self.pos=[turtle.Vec2D(0,0)]
            self.body[0].goto(self.pos[0])
            self.direction= turtle.Vec2D(0,0)
            self.GAMEOVER= False
            self.score=0
            time.sleep(2)


    def create_pen(self):
        # Pen
        pen = turtle.Turtle()
        pen.speed(0)
        pen.shape("square")
        pen.color("white")
        pen.penup()
        pen.hideturtle()
        pen.goto(0, 260)
        pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

        return pen
    
    def Update_Score(self):
        if self.score>self.HIGHSCORE:
            self.HIGHSCORE= self.score

        self.pen.clear()
        self.pen.write("Score: {}  High Score: {}".format(self.score,self.HIGHSCORE), align="center", font=("Lato", 24, "normal"))
        


