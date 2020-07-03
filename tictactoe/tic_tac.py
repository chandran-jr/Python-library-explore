#importing required Libraries
import pygame as pg
import sys
import time
from pygame.locals import *

#declaring global variables

XO='x' #stores  x or o
win=None
draw=None
width=400
height=400
white=(255,255,255)
line_color=(0,0,0) #black

#sets up a 3*3 board on Canvas
board=[[None]*3,[None]*3,[None]*3]

#game display
pg.init()
fps=30 #frames per second
clock=pg.time.Clock()

screen=pg.display.set_mode((width,height+100),0,32)
#height+100 is to provide extra 100pc space to display game status

#name tag
pg.display.set_caption("Tic Tac Toe")

#load images
init_window=pg.image.load("images/cover_img.jpg")
x_img=pg.image.load("images/x_img.jpg")
o_img=pg.image.load("images/o_img.png")

#resizing images to required width and height
init_window=pg.transform.scale(init_window,(width,height+100))
x_img=pg.transform.scale(x_img,(80,80))
y_img=pg.transform.scale(o_img,(80,80))

def game_init_window():
    screen.blit(init_window,(0,0))
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

    #drawing 2 vertical lines that splits the canvas in three equal halves
    pg.draw.line(screen,line_color,(width/3,0),(width/3,height),7)
    pg.draw.line(screen,line_color,(width/3*2,0),(width/3*2,height),7)

    #drawing 2 horizontal lines that splits the canvas in three equal halves
    pg.draw.line(screen,line_color,(0,height/3),(width,height/3),7)
    pg.draw.line(screen,line_color,(0,height/3*2),(width,height/3*2),7)
    draw_status()

def draw_status():

    global drawing
    if win is None:
        msg=XO.upper()+"'s turn"
    else:
        msg=XO.upper()+" Won!"
    if draw:
        msg="Game Draw!"

    font=pg.font.Font(None,30)
    text=font.render(msg,1,white)

    #creating a small block at the bottom of the display
    screen.fill(line_color,(0,400,500,100))
    text_rect=text.get_rect(center=(width/2,450))
    screen.blit(text,text_rect)
    pg.display.update()

#main algorithm
def check_win():
    global board,win,draw

    #checking for wins in rows
    for row in range(3):
        if(board[row][0]==board[row][1]==board[row][2] and (board[row][0] is not None)):
            win=board[row][0]
            pg.draw.line(screen,(0,0,255),(0,(row+1)*height/3-height/6),(width,(row+1)*height/3-height/6),7)
            break

    #checking for wins in columns
    for column in range(3):
        if(board[0][column]==board[1][column]==board[2][column] and (board[0][column] is not None)):
            win=board[0][column]
            pg.draw.line(screen,(0,0,255),((col + 1)* width / 3 - width / 6, 0),((col + 1)* width / 3 - width / 6, height),7)
            break

    #checking for wins diagonally
    if (board[0][0]==board[1][1]==board[2][2] and (board[0][0] is not None)):
        #winning left to right
        win=board[0][0]
        pg.draw.line(screen,(0,0,255),(50,50),(350,350),4)
    elif(board[0][2]==board[1][1]==board[2][0] and (board[0][2] is not None)):
        #winning right to left
        win=board[0][2]
        pg.draw.line(screen,(0,0,255),(350,50),(50,350),4)

    if (all([all(row) for row in board]) and win is None):
        draw=True

    draw_status()

#displaying user input
def drawXO(row,col):
    global board,XO
    if row==1:
        posx=30
    elif row==2:
        posx=width/3+30
    elif row==3:
        posx=width/3*2+30

    if col==1:
        posy=30
    elif col==2:
        posy=height/3+30
    elif col==3:
        posy=height/3*2+30

    board[row-1][col-1]=XO
    #display the image
    if XO=='x':
        screen.blit(x_img,(posx,posy))
        XO='o'
    else:
        screen.blit(y_img,(posx,posy))
        XO='x'

    pg.display.update()

#getting user input
def user_click():

    #get coordinates of mouse user_click
    x,y=pg.mouse.get_pos()

    #finding column based on user_click
    if x < width/3:
        col=1
    elif x < width/3*2 :
        col=2
    elif x < width:
        col=3
    else:
        col=None

    #finding row based on user_click
    if y < height/3:
        row=1
    elif y < height/3*2:
        row=2
    elif y < height:
        row=3
    else:
        row=None

    if( row and col and board[row-1][col-1] is None):
        global XO
        drawXO(row,col)
        check_win()


def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_init_window()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]

game_init_window()

while(True):
    for event in pg.event.get():

        if event.type == QUIT:
            pg.quit()
            sys.exit()

        elif event.type is MOUSEBUTTONDOWN:
            user_click()

            if(win or draw):
                reset_game()

    pg.display.update()
    clock.tick(fps)
