#imports
from copy import deepcopy
from tkinter import *
import tkinter
import random
import sys

#variables
board = [[" "," "," "],[" "," "," "],[" "," "," "]]
tk = Tk()
canvas = Canvas(tk, width = 800, height = 800)
canvas.pack()

#test to see if someone has won 
def Test(board,symbol):
  if (board[0][0] == symbol and board[0][1] == symbol and board[0][2] == symbol) or (board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol) or (board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol) or (board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol) or (board[0][1] == symbol and board[1][1] == symbol and board[2][1] == symbol) or (board[0][2] == symbol and board[1][2] == symbol and board[2][2] == symbol) or (board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol) or (board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol):
    return True
#win checker
def Winner(board,person):
  if Test(board,person):
    return True
  return False
#board displaying function
def printBoard():
  #displays the board (lines)
  canvas.create_line(300,130,300,700, width = 5)
  canvas.create_line(500,130,500,700, width = 5)
  canvas.create_line(675,290,125,290, width = 5)
  canvas.create_line(675,490,125,490, width = 5)
  canvas.create_rectangle(675,130,125,700, width = 5)
  buttonPress(board)
def buttonPress(board):
  #displays button 1 if it has not already been taken by the user or computer
  if board[0][0] == " ":
    btn1 = tkinter.Button(tk, command = lambda: Btn_1("O"))
    btn1.pack()
    btn1.place(bordermode = OUTSIDE, height=145, width=165, x = 130 , y = 140)
  #displays button 2 if it has not already been taken by the user or computer
  if board[0][1] == " ":
    btn2 = tkinter.Button(tk, command = lambda: Btn_2("O"))
    btn2.pack()
    btn2.place(bordermode = OUTSIDE, height=145, width=190, x = 305 , y = 140)
  #displays button 3 if it has not already been taken by the user or computer
  if board[0][2] == " ":
    btn3 = tkinter.Button(tk, command = lambda: Btn_3("O"))
    btn3.pack()
    btn3.place(bordermode = OUTSIDE, height=145, width=165, x = 505 , y = 140)
  #displays button 4 if it has not already been taken by the user or computer
  if board[1][0] == " ":
    btn4 = tkinter.Button(tk, command = lambda: Btn_4("O"))
    btn4.pack()
    btn4.place(bordermode = OUTSIDE, height=190, width=165, x = 130 , y = 295)
  #displays button 5 if it has not already been taken by the user or computer
  if board[1][1] == " ":
    btn5 = tkinter.Button(tk, command = lambda: Btn_5("O"))
    btn5.pack()
    btn5.place(bordermode = OUTSIDE, height=190, width=190, x = 305 , y = 295)
  #displays button 6 if it has not already been taken by the user or computer
  if board[1][2] == " ":
    btn6 = tkinter.Button(tk, command = lambda: Btn_6("O"))
    btn6.pack()
    btn6.place(bordermode = OUTSIDE, height=190, width=165, x = 505 , y = 295)
  if board[2][0] == " ":
    btn7 = tkinter.Button(tk, command = lambda: Btn_7("O"))
    btn7.pack()
    btn7.place(bordermode = OUTSIDE, height=190, width=165, x = 130 , y = 495)
  #diplays button 8 if it has not already been taken by the user or computer
  if board[2][1] == " ":
    btn8 = tkinter.Button(tk, command = lambda: Btn_8("O"))
    btn8.pack()
    btn8.place(bordermode = OUTSIDE, height=190, width=190, x = 305 , y = 495)
  #displays button 9 if it has not already been taken by the user or computer
  if board[2][2] == " ":
    btn9 = tkinter.Button(tk, command = lambda: Btn_9("O"))
    btn9.pack()
    btn9.place(bordermode = OUTSIDE, height=190, width=165, x = 505 , y = 495)
def playAgain():
  sys.exit()
#users turn
def User():
  if Winner(board,"O"):
    canvas.create_text(400,50,text = "You win!", font = ("Impact",30))
    playAgain()
  if Winner(board,"X"):
    canvas.create_text(400,50,text = "You lose!", font = ("Impact",30))
    playAgain()
  if board[0].count(" ")+board[1].count(" ")+board[2].count(" ") == 0:
    canvas.create_text(400,50,text = "It's a tie!", font = ("Impact",30))
    playAgain()
  printBoard()
#computers turn 
def AI():
  bcount = 9-board[0].count(" ")-board[1].count(" ")-board[2].count(" ")
  coord = minimax(board,True,bcount,float("-inf"),float("inf"))[1]
  if coord[0] == 0 and coord[1] == 0:
    Btn_1("X")
  elif coord[0] == 0 and coord[1] == 1:
    Btn_2("X")
  elif coord[0] == 0 and coord[1] == 2:
    Btn_3("X")
  elif coord[0] == 1 and coord[1] == 0:
    Btn_4("X")
  elif coord[0] == 1 and coord[1] == 1:
    Btn_5("X")
  elif coord[0] == 1 and coord[1] == 2:
    Btn_6("X")
  elif coord[0] == 2 and coord[1] == 0:
    Btn_7("X")
  elif coord[0] == 2 and coord[1] == 1:
    Btn_8("X")
  elif coord[0] == 2 and coord[1] == 2:
    Btn_9("X")
  User()
#minimax algorithm
def minimax(board,turn,bcount,alpha,beta):
  if board[0].count(" ")+board[1].count(" ")+board[2].count(" ") == 0 or (Winner(board,"X") or Winner(board,"O")):
    return staticevaluation(board,bcount)
  if turn:
    maxevaluation = float("-inf")
    for i in range(len(board)):
      for x in range(len(board)):
        if board[i][x] == " ":
          child = deepcopy(board)
          child[i][x] = "X"
          evaluation = minimax(child,False,bcount,alpha,beta)
          if evaluation >= maxevaluation:
            coords = [i,x]
            maxevaluation = evaluation
          alpha = max(alpha,evaluation)
          if beta < alpha:
            break
      else:
        continue
      break
    return [maxevaluation,coords]
  else:
    minevaluation = float("inf")
    for i in range(len(board)):
      for x in range(len(board)):
        if board[i][x] == " ":
          child = deepcopy(board)
          child[i][x] = "O"
          evaluation = minimax(child,True,bcount,alpha,beta)
          if type(evaluation) != int:
            evaluation = evaluation[0]
          minevaluation = min(minevaluation, evaluation)
          beta = min(beta,evaluation)
          if beta < alpha:
            break
      else:
        continue
      break
    return minevaluation
#assigns a rating to all possible outcomes
def staticevaluation(board,bcount):
  if Winner(board,"X"):
    currentcount = 9-board[0].count(" ")-board[1].count(" ")-board[2].count(" ")
    return 1-(currentcount-bcount)
  if Winner(board,"O"):
    return -100000
  else:
    return -50000
#function called if button 1 had been pressed and displays the button
def Btn_1(symbol):
  board[0][0] = symbol
  Letter1 = tkinter.Label(tk, text = symbol, font = ("Ubuntu",150))
  Letter1.pack()
  Letter1.place(bordermode = OUTSIDE, height = 145, width = 165, x = 130, y = 140)
  if symbol == "O":
    AI()
  else:
    User()
        
#function called if button 2 had been pressed and displays the button
def Btn_2(symbol):
  board[0][1] = symbol
  Letter2 = tkinter.Label(tk, text = symbol, font = ("Ubuntu",150))
  Letter2.pack()
  Letter2.place(bordermode = OUTSIDE, height = 145, width = 190, x = 305, y = 140)
  if symbol == "O":
    AI()
  else:
    User()
        
#function called if button 3 had been pressed and displays the button
def Btn_3(symbol):
  board[0][2] = symbol
  Letter3 = tkinter.Label(tk, text = symbol, font = ("Ubuntu",150))
  Letter3.pack()
  Letter3.place(bordermode = OUTSIDE, height = 145, width = 165, x = 505, y = 140)
  if symbol == "O":
    AI()
  else:
    User()
        
#function called if button 4 had been pressed and displays the button
def Btn_4(symbol):
  board[1][0] = symbol
  Letter4 = tkinter.Label(tk, text = symbol, font = ("Ubuntu",150))
  Letter4.pack()
  Letter4.place(bordermode = OUTSIDE, height = 190, width = 165, x = 130, y = 295)
  if symbol == "O":
    AI()
  else:
    User()
        
#function called if button 5 had been pressed and displays the button
def Btn_5(symbol):
  board[1][1] = symbol
  Letter5 = tkinter.Label(tk, text = symbol, font = ("Ubuntu",150))
  Letter5.pack()
  Letter5.place(bordermode = OUTSIDE, height = 190, width = 190, x = 305, y = 295)
  if symbol == "O":
    AI()
  else:
    User()
        
#function called if button 6 had been pressed and displays the button
def Btn_6(symbol):
  board[1][2] = symbol
  Letter6 = tkinter.Label(tk, text = symbol, font = ("Ubuntu",150))
  Letter6.pack()
  Letter6.place(bordermode = OUTSIDE, height = 190, width = 165, x = 505, y = 295)
  if symbol == "O":
    AI()
  else:
    User()
        
#function called if button 7 had been pressed and displays the button
def Btn_7(symbol):
  board[2][0] = symbol
  Letter7 = tkinter.Label(tk, text = symbol, font = ("Ubuntu",150))
  Letter7.pack()
  Letter7.place(bordermode = OUTSIDE, height = 190, width = 165, x = 130, y = 495)
  if symbol == "O":
    AI()
  else:
    User()
        
#function called if button 8 had been pressed and displays the button
def Btn_8(symbol):
  board[2][1] = symbol
  Letter8 = tkinter.Label(tk, text = symbol, font = ("Ubuntu",150))
  Letter8.pack()
  Letter8.place(bordermode = OUTSIDE, height = 190, width = 190, x = 305, y = 495)
  if symbol == "O":
    AI()
  else:
    User()
        
#function called if button 9 had been pressed and displays the button
def Btn_9(symbol):
  board[2][2] = symbol
  Letter9 = tkinter.Label(tk, text = symbol, font = ("Ubuntu",150))
  Letter9.pack()
  Letter9.place(bordermode = OUTSIDE, height = 190, width = 165, x = 505, y = 495)
  if symbol == "O":
    AI()
  else:
    User()
#start the tictactoe game
def main():
  start = random.randint(1,2)
  if start == 1:
    User()
  else:
    AI()
main()
