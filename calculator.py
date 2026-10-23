import tkinter #GUI Library

#Structure of the calculator's buttons

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]  #Figure out how to do the sqaure root function on your own

#Row and column count

row_count = len(button_values) #5 - How many lists in total 
column_count = len(button_values[0]) #4 - this is how many that are in the list from the very first row

right_symbols = ["÷", "×", "-", "+", "="] #Operators
top_symbols = ["AC", "+/-", "%"] #Functions

#Colours to use for calculator (you can search them up)
colour_grey = "#3b3b3b"
colour_black = "#000000"
colour_red = "#ff0000"
colour_orange = "#ffa500"
colour_lightgrey =  "#6e6e6e"	
colour_white = "white"

#Window set up
window = tkinter.Tk() #creates the window
window.title("First Calculator")
window.resizeable(False, False) #This is so the user doesn't resize the calculator (Width, Height)
window.mainloop() #So the window does not shut down and it keeps running




