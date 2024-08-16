# Author: Trak
# Date: Friday 13, 2023
# Purpose: Create a functioning Pong Game

#Import all the functions from cs1lib
from cs1lib import *
import random
from playsound import playsound
from pong_utility import *

# SET CONSTANTS FOR WIN SIZE, HEIGHT, WIDTH, LEFT_X, RIGHT_X, change
WIN_SIZE= 400
HEIGHT=80
WIDTH=20
LEFT_X= 0
RIGHT_X= WIN_SIZE - WIDTH
change= 10
# Ball Variables
RADIUS= 10
posx= 200
posy= 200
ball_speed= 3
p1=0
p2=0
# Set variables for left_y, right_y, a_press, z_press, K_press, m_press
left_y= 0
right_y= WIN_SIZE - HEIGHT
# Set boolean values to check for conditions
# key Booleans
a_press= False
b_press= False
z_press= False
k_press= False
m_press= False
q_press= False
sp_press= False
# Condition updates boolean values
inner_collide= False
t_collide= False
b_collide= False
vert_collide= False
right_touch= False
left_touch= False

x1=load_image("Photos/1.png")
#x2=load_image("Photos/2.png")
x3=load_image("Photos/3.png")
x4=load_image("Photos/4.png")
x5=load_image("Photos/5.png")
x6=load_image("Photos/6.png")
x7=load_image("Photos/7.png")
x8=load_image("Photos/8.png")
x9=load_image("Photos/9.png")
x10=load_image("Photos/10.png")
x11=load_image("Photos/11.png")
x12=load_image("Photos/12.png")
x13=load_image("Photos/13.png")
x14=load_image("Photos/14.png")
x15=load_image("Photos/15.png")
x16=load_image("Photos/16.png")
x17=load_image("Photos/17.png")
x18=load_image("Photos/18.png")
x19=load_image("Photos/19.png")
x20=load_image("Photos/20.png")
x21=load_image("Photos/21.png")
x22=load_image("Photos/22.png")
x23=load_image("Photos/23.png")
x24=load_image("Photos/24.png")
x25=load_image("Photos/25.png")
x26=load_image("Photos/26.png")
x27=load_image("Photos/27.png")
x28=load_image("Photos/28.png")
x29=load_image("Photos/29.png")
x30=load_image("Photos/30.png")
x31=load_image("Photos/31.png")
x32=load_image("Photos/32.png")
x33=load_image("Photos/33.png")
x34=load_image("Photos/34.png")
x35=load_image("Photos/35.png")
x36=load_image("Photos/36.png")
x37=load_image("Photos/37.png")
x38=load_image("Photos/38.png")
x39=load_image("Photos/39.png")
x40=load_image("Photos/40.png")
x41=load_image("Photos/41.png")
x42=load_image("Photos/42.png")
x43=load_image("Photos/43.png")
x44=load_image("Photos/44.png")
x45=load_image("Photos/45.png")
x46=load_image("Photos/46.png")
x47=load_image("Photos/47.png")
x48=load_image("Photos/48.png")
x49=load_image("Photos/49.png")
x50=load_image("Photos/50.png")
x51=load_image("Photos/51.png")
x52=load_image("Photos/52.png")
x53=load_image("Photos/53.png")
x54=load_image("Photos/54.png")
x55=load_image("Photos/55.png")
x56=load_image("Photos/56.png")
x57=load_image("Photos/57.png")
x58=load_image("Photos/58.png")
x59=load_image("Photos/59.png")
x60=load_image("Photos/60.png")
x61=load_image("Photos/61.png")
bcount=0

list1= [x1,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,x16,x17,x18,x19,x20,x21,x22,x23,x24]
list2= [x28,x29,x30,x31,x32,x33,x34,x35,x36,x37,x38,x39,x40,x41,x42,x43,x44,x45,x46,x47,x48,x49,x50,x51,x52,x53,x54,x55,x56,x57,x58,x59,x60,x61]
list3= [x25]
list4=[x26]
ll= [list1,list2,list3,list4]
newb= list1



# If the key is pressed, set the value to True
def my_key_press(value):
    global a_press,z_press, k_press, m_press, q_press, sp_press, b_press
    if value == "a":
        a_press = True
    if value == "b":
        b_press = True
    if value == "z":
        z_press = True
    if value == "k":
        k_press = True
    if value == "m":
        m_press = True
    if value == "q":
        q_press = True
    if value == " ":
        sp_press = True

# If the key is released, set the value to False
def my_key_release(value):
    global a_press, z_press, k_press, m_press, q_press, b_press
    if value == "a":
        a_press = False
    if value == "b":
        b_press = False
    if value == "z":
        z_press = False
    if value == "k":
        k_press = False
    if value == "m":
        m_press = False
    if value == "q":
        q_press = False


# If the key is pressed, moved it in that direction.
def key_helper():
    global  left_y, right_y
    if a_press == True:
        if left_y - change >= 0:
            left_y -= change
    if z_press == True:
        if left_y - change < 310:
            left_y += change
    if k_press == True:
        if right_y- change >= 0:
            right_y -= change
    if m_press == True:
        if right_y - change < 310:
            right_y += change
    # If q is pressed, quit the program
    if q_press == True:
        cs1_quit()
    # If space is pressed and game is not over, run the ball_runner function
    if sp_press == True:
        ball_runner()

# Resets the game and reset all the variables when called
def game_reset():
    global game_over, posx, posy, game_start, inner_collide, t_collide, b_collide, vert_collide, right_touch, left_touch, sp_press, ball_speed
    posx= 200
    posy= 200
    ball_speed= 3
    game_over = False
    inner_collide = False
    t_collide = False
    b_collide = False
    vert_collide = False
    right_touch = False
    left_touch = False
    sp_press = False
    playsound("restart.mp3",False)


# Updates the location of the ball according to the conditions of the current positions.
def ball_runner():
    global posx, posy, vert_collide
    if inner_collide == False and (left_touch == False or right_touch == False) and t_collide== False and b_collide == False and vert_collide== False:
        move_up_right()
    elif inner_collide == True and left_touch == True and t_collide== False and b_collide == False and vert_collide== False:
        move_up_left()
    elif inner_collide == True and right_touch == True and t_collide== False and b_collide == False and vert_collide== False:
        move_down_right()
    elif t_collide == True and left_touch == True:
        move_down_left()
    elif t_collide == True and right_touch == True:
        move_down_right()
    elif b_collide == True and right_touch == True:
        move_up_right()
    elif b_collide == True and left_touch == True:
        move_up_left()

def sound_runner():
    if inner_collide == True:
        playsound("paddleHit.mp3",False)
    elif t_collide == True:
        playsound("wallHit.mp3",False)
    elif b_collide == True:
        playsound("wallHit.mp3",False)




# Checks whether the ball has hit the inner sie of the paddle board and from which paddle.
def inner_checker(posx,posy):
    global inner_collide, left_touch, right_touch,ball_speed
    if posx == 20 and (posy >= left_y and posy <= left_y+HEIGHT):
        inner_collide = True
        left_touch = True
        right_touch = False
        playsound("paddleHit.mp3", False)
    if posx == 380 and (posy >= right_y and posy <= right_y+HEIGHT):
        inner_collide = True
        left_touch = False
        right_touch = True
        playsound("paddleHit.mp3", False)

# Checks whether the ball has hit the top wall or bottom wall. Set the boolean values as such.
def tb_checker():
    global t_collide, b_collide, ball_speed
    if posy == 2 and vert_collide == False:
        t_collide= True
        b_collide= False
        playsound("wallHit.mp3", False)
    elif posy == 401 and vert_collide == False:
        b_collide = True
        t_collide= False
        playsound("wallHit.mp3", False)

# Checks whether the ball has hit the vertical walls. If it did, game resets.
def vert_checker():
    global p1,p2
    global game_over
    if posx <= 2 :
        p2 += 1
        game_reset()
    elif posx >= 400:
        p1 += 1
        game_reset()


# Define ball movement when it is coming down from the left side.
def move_down_left():
    global posx, posy
    if right_touch == False or game_over == False:
        posx+= ball_speed
        posy+= ball_speed

# Define ball movement when it is coming down from the right side.
def move_down_right():
    global posx, posy
    if left_touch == False or game_over == False:
        posx-= ball_speed
        posy+= ball_speed

# Define ball movement when it is coming up from the left side.
def move_up_left():
    global posx, posy
    if right_touch == False or game_over == False:
        posx+= ball_speed
        posy-= ball_speed

# Define ball movement when it is coming up from the right side.
def move_up_right():
    global posx, posy
    if left_touch == False or game_over == False:
        posx-= ball_speed
        posy-= ball_speed

def music():
    playsound("song1.mp3")

def background_change():
    global newb,bcount

    if b_press == True:
        bcount += 1
        if bcount >= len(ll)-1:
            newb=0
            bcount=0
        newb = ll[bcount]
    return newb

def theme():
    if bcount == 0:
        set_clear_color(0.98, 0.93, 0.819)
        disable_stroke()
        enable_fill()
        set_fill_color(0.3764, 0.447, 0.454)
        draw_rectangle(LEFT_X, left_y, WIDTH, HEIGHT)
        draw_rectangle(RIGHT_X, right_y, WIDTH, HEIGHT)
        set_fill_color(0.698, 0.647, 0.607)
        draw_circle(posx, posy, RADIUS)
    elif bcount ==1:
        set_clear_color(0.091, 0, 0.819)
        set_stroke_width(3)
        set_stroke_color(0.6, 0.6, 0.6)
        enable_fill()
        set_fill_color(0.5254, 0.5254, 0.5254)
        draw_rectangle(LEFT_X, left_y, WIDTH, HEIGHT)
        draw_rectangle(RIGHT_X, right_y, WIDTH, HEIGHT)
        set_fill_color(0.6, 0.6, 0.6)
        draw_circle(posx, posy, RADIUS)
    elif bcount ==2:
        set_clear_color(0.091, 0, 0.819)
        disable_stroke()
        enable_fill()
        set_fill_color(0.2158, 0.3529, 0.49411)
        draw_rectangle(LEFT_X, left_y, WIDTH, HEIGHT)
        draw_rectangle(RIGHT_X, right_y, WIDTH, HEIGHT)
        set_fill_color(0.533, 0.6, 0.7254)
        draw_circle(posx, posy, RADIUS)












# Main draw function sets the background, the recetangle, and calls the move_helper() function
# The Main function also constantly checks whether conditions are met or not.

play_music()
x= 125
y=100
rnum = 0




def my_maindraw():
    global x,y,rnum
    set_font_size(13)
    clear()
    newb= background_change()
    if rnum>= len(ll[bcount])-1:
        rnum=0
    stri = rnum
    rnum+=1
    draw_image(newb[stri], 0, 0)
    theme()
    # Run the checker functions
    key_helper()
    inner_checker(posx, posy)
    vert_checker()
    tb_checker()
    enable_stroke()
    set_stroke_color(0, 0, 0)
    set_font("Public Pixel")
    draw_text("Pong Game", 125, 50)
    str2c= random.randint(1,100)
    if str2c == 25:
        x= 800
        y=900
    draw_text("LOADING...", x, y)
    set_font_size(6)
    draw_text("P1:"+str(p1),90,30)
    draw_text("P2:" + str(p2), 250, 30)

# Start the graphics
start_graphics(my_maindraw, key_press=my_key_press, key_release=my_key_release)