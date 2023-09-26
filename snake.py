from turtle import Screen,Turtle

starting_position=[(0,0),(-20,0),(-40,0),(-60,0),(-80,0)]
moving_distance=20
up=90
down=270
left=180
right=0


class Snake:
    def __init__(self) :
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in starting_position:
            self.create_seg(position)
    def  create_seg(self,position):        
        new_segment=Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.create_seg(self.segment[-1].position())
    
    def move(self):
        for seg_num in range (len(self.segment)-1,0,-1):
            x_axis= self.segment[seg_num-1].xcor()
            y_axis= self.segment[seg_num-1].ycor()
            self.segment[seg_num].goto(x_axis,y_axis)
        self.head.forward(moving_distance)


    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)
    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)
    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    


