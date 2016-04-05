#/usr/bin/env python3

from tkinter import *
import tkinter.messagebox
import random

tictoe = Tk()
tictoe.title("Tic Tac Toe")

click = True

def tictactoe(buttons):
    global click
    marked_titles =[1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(marked_titles)
    print(marked_titles[0])
    if buttons["text"] == "" and click == True:
        for i in button_array:
            if button_array[i]["text"] == "X" or button_array[i]["text"] == "O":
                marked_titles.remove(i)
                print(marked_titles)

        buttons["text"] = "X"
        button_array[marked_titles[0]]["text"] = "O"
        click = True
    #elif buttons["text"] == "" and click == False:
     #   buttons["text"] = "O"
      #  click = True

    if(button_array[1]["text"] == "X" and button_array[2]["text"] == "X" and button_array[3]["text"] == "X" or
        button_array[4]["text"] == "X" and button_array[5]["text"] == "X" and button_array[6]["text"] == "X" or
        button_array[7]["text"] == "X" and button_array[8]["text"] == "X" and button_array[9]["text"] == "X" or
        button_array[1]["text"] == "X" and button_array[5]["text"] == "X" and button_array[9]["text"] == "X" or
        button_array[3]["text"] == "X" and button_array[5]["text"] == "X" and button_array[7]["text"] == "X" or
        button_array[1]["text"] == "X" and button_array[4]["text"] == "X" and button_array[7]["text"] == "X" or
        button_array[2]["text"] == "X" and button_array[5]["text"] == "X" and button_array[8]["text"] == "X" or
        button_array[3]["text"] == "X" and button_array[6]["text"] == "X" and button_array[9]["text"] == "X"):
        tkinter.messagebox.showinfo("The Winner...", "X just won the game!")
    elif(button_array[1]["text"] == "O" and button_array[2]["text"] == "O" and button_array[3]["text"] == "O" or
        button_array[4]["text"] == "O" and button_array[5]["text"] == "O" and button_array[6]["text"] == "O" or
        button_array[7]["text"] == "O" and button_array[8]["text"] == "O" and button_array[9]["text"] == "O" or
        button_array[1]["text"] == "O" and button_array[5]["text"] == "O" and button_array[9]["text"] == "O" or
        button_array[3]["text"] == "O" and button_array[5]["text"] == "O" and button_array[7]["text"] == "O" or
        button_array[1]["text"] == "O" and button_array[4]["text"] == "O" and button_array[7]["text"] == "O" or
        button_array[2]["text"] == "O" and button_array[5]["text"] == "O" and button_array[8]["text"] == "O" or
        button_array[3]["text"] == "O" and button_array[6]["text"] == "O" and button_array[9]["text"] == "O"):
        tkinter.messagebox.showinfo("The Winner...", "O just won the game!")

buttons=StringVar()

button_array = { 1: "button1", 2: "button2", 3: "button3", 4: "button4", 5: "button5", 6: "button6", 7: "button7", 8: "button8", 9: "button9"}

button_array[1]=Button(tictoe, text="",  font=('Arial 25 bold'), height=3, width=6, command=lambda:tictactoe(button_array[1]))
button_array[1].grid(row=1, column=0, sticky=S+N+E+W)
button_array[2]=Button(tictoe,  text="",  font=('Arial 25 bold'), height=3, width=6, command=lambda:tictactoe(button_array[2]))
button_array[2].grid(row=1, column=1, sticky=S+N+E+W)
button_array[3]=Button(tictoe, text="",  font=('Arial 25 bold'), height=3, width=6, command=lambda:tictactoe(button_array[3]))
button_array[3].grid(row=1, column=2, sticky=S+N+E+W)
button_array[4]=Button(tictoe, text="",  font=('Arial 25 bold'), height=3, width=6, command=lambda:tictactoe(button_array[4]))
button_array[4].grid(row=2, column=0, sticky=S+N+E+W)
button_array[5]=Button(tictoe, text="",  font=('Arial 25 bold'), height=3, width=6, command=lambda:tictactoe(button_array[5]))
button_array[5].grid(row=2, column=1, sticky=S+N+E+W)
button_array[6]=Button(tictoe, text="",  font=('Arial 25 bold'), height=3, width=6, command=lambda:tictactoe(button_array[6]))
button_array[6].grid(row=2, column=2, sticky=S+N+E+W)
button_array[7]=Button(tictoe, text="",  font=('Arial 25 bold'), height=3, width=6, command=lambda:tictactoe(button_array[7]))
button_array[7].grid(row=3, column=0, sticky=S+N+E+W)
button_array[8]=Button(tictoe, text="",  font=('Arial 25 bold'), height=3, width=6, command=lambda:tictactoe(button_array[8]))
button_array[8].grid(row=3, column=1, sticky=S+N+E+W)
button_array[9]=Button(tictoe, text="",  font=('Arial 25 bold'), height=3, width=6, command=lambda:tictactoe(button_array[9]))
button_array[9].grid(row=3, column=2, sticky=S+N+E+W)


tictoe.mainloop()