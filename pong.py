import simpleguitk as simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
width = 800
half_width = width / 2
height = 500   
half_height = height / 2
ball_radius = 20
pad_width = 8
pad_height = 80
LEFT = False
RIGHT = True

#paddles
paddle1_pos = height / 2.5
paddle2_pos = height / 2.5
paddle1_vel = 0
paddle2_vel = 0
paddle_vel = 5


# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [half_width, half_height]
ball_vel = [0,1]

# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    
    ball_pos = [half_width, half_height]	
    
    ball_vel[0] = -random.randrange(120,240) / 100 
    if direction == True:
        ball_vel[0] *= -1
    ball_vel[1] = -random.randrange(10,120) / 100
   
   
   
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball(12)
    paddle1_pos = height / 2.5
    paddle2_pos = height / 2.5
      

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    c.draw_line([half_width, 0],[half_width, height], 2, "white")
    c.draw_line([pad_width, 0],[pad_width, height], 2, "white") #left pad
    c.draw_line([width - pad_width, 0],[width - pad_width, height], 2, "white") #right  pad 
        
    # update ball
    ball_pos[0] += ball_vel[0] # horizontal
    ball_pos[1] += ball_vel[1] #vertical
    
    #keeping the  ball inside the frame [HORIZONTAL]
    if ball_pos[0] <= (ball_radius + pad_width) or ball_pos[0] >= (width - pad_width - ball_radius):        
        ball_vel[0] *= -1
      
       
        
        score(10)   
   
   
    #keeping the  ball inside the frame [VERTICAL]     
    if ball_pos[1] <= ball_radius or ball_pos[1] >= (height - ball_radius):
       ball_vel[1] *= -1
  
    
    # draw ball
    c.draw_circle(ball_pos, ball_radius, 2, "White", "Green")
    
    
    
    # update paddle's vertical position, keep paddle on the screen
  
    global paddle1_vel, paddle2_vel
    
    if (paddle1_pos <= height - pad_height and paddle1_vel > 0) or (paddle1_pos >= 0 and paddle1_vel < 0) :
        paddle1_pos += paddle1_vel    
    
    elif (paddle2_pos <= height - pad_height and paddle2_vel > 0) or (paddle2_pos >= 0 and paddle2_vel < 0) :
        paddle2_pos += paddle2_vel  
    
    
    
    # draw paddles
    c.draw_polygon([[0, paddle1_pos], [pad_width, paddle1_pos],[pad_width, (paddle1_pos) + pad_height ],[0, (paddle1_pos) + pad_height]],1, "green", "white") #left pad
    c.draw_polygon([[width, paddle2_pos], [width - pad_width, paddle2_pos], [width - pad_width, paddle2_pos + pad_height], [width, paddle2_pos + pad_height]],1, "green", "white")
    
    # draw scores
    c.draw_text(str(score1), [300, 100], 100, "pink")    
    c.draw_text(str(score2), [440, 100], 100, "pink")   

def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_vel
    
    #player1    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -paddle_vel     
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = paddle_vel  
      
    #player2
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = paddle_vel    
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -paddle_vel 
      
    
    
    
    
def keyup(key):
    global paddle1_vel, paddle2_vel, paddle_vel
    
     #player1
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 0
        
    #player2
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0     
        
def score(s):
        global score1, score2
        if (ball_pos[0] > half_width):    #right part of the board         
            if (ball_pos[1] < paddle2_pos or ball_pos[1] > paddle2_pos + pad_height):
                score1 += 1 
                spawn_ball(LEFT) 
            else: ball_vel[0] += .20 * ball_vel[0]
            
        if (ball_pos[0] < half_width):
            if (ball_pos[1] < paddle1_pos or ball_pos[1] > paddle1_pos + pad_height ):
                score2 += 1
                spawn_ball(RIGHT)
            else: ball_vel[0] += .20 * ball_vel[0]    


# create frame
frame = simplegui.create_frame("Pong", width, height)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)


# start frame
new_game()
frame.start()
