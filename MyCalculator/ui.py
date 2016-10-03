#   Amber's Calculator
#       ui.py

#   Adding import statements
from Tkinter import *




#   Construct the window
window = Tk()
#   Set the window's title
window.title("Calculator")
window.geometry("300x350")
window.configure(background="powder blue")


#   global variables
input_number_1 = 0
input_number_2 = 0

#   Define frames (containers)
widget_input_container = Frame(window, height=125, width=350)
number_container = Frame(widget_input_container, height=125, width=175)
number_container_r1 = Frame(number_container, height=1, width=175)
number_container_r2 = Frame(number_container, height=1, width=175)
number_container_r3 = Frame(number_container, height=1, width=175)
number_container_r4 = Frame(number_container, height=1, width=175)
operation_container = Frame(widget_input_container, height=125, width=58)
misc_container = Frame(widget_input_container, height=125, width=117)
misc_container_r1 = Frame(misc_container, height=1, width=175)
misc_container_r2 = Frame(misc_container, height=1, width=175)
misc_container_r3 = Frame(misc_container, height=1, width=175)
misc_container_r4 = Frame(misc_container, height=1, width=175)

evaluation_container = Frame(window, height=200, width=175)
evaluation_container.pack(side=TOP)
#   Define label
answer_label = Label(evaluation_container, text="0.00", bg="powder blue")

class Operators(object):
    def __init__(self):
        print("hi")
        
    def add(self, in1, in2):
        return in1+in2;        
    def divide(self, in1, in2):
        return (in1/in2);
        

#   DEFINE INPUT HANDLERS

#   Define number callback
def number_callback(num):
    print("NUMBER = " + str(num))
#   Define operator callback
def operator_callback(op):
    print("OPERATOR = " + op)
    if(op == "clear"):
        print("CLEAR called.")
    elif(op == "undo"):
        print("UNDO called.")        
    #this is where the arithmetic is done.
    elif(op == "+"):
        input_number_1 = float(answer_label.cget("text"));
        print( math.add(input_number_1, input_number_2));
    elif(op == "-"):
        input_number_1 = float(answer_label.cget("text"));
        print( math.subtract(input_number_1, input_number_2));
    elif(op == "/"):
        input_number_1 = float(answer_label.cget("text"));
        print( math.divide(input_number_1, input_number_2));

#   Argument command calling function "callback"
#   btn = Button(window, text="Click Me", command=callback)
#   btn.pack()

math = Operators()


#   Define buttons
button_0 = Button(number_container_r4, text="0", height=1, width=6, command=lambda:number_callback(0))
button_1 = Button(number_container_r3, text="1", height=1, width=6, command=lambda:number_callback(1))
button_2 = Button(number_container_r3, text="2", height=1, width=6, command=lambda:number_callback(2))
button_3 = Button(number_container_r3, text="3", height=1, width=6, command=lambda:number_callback(3))
button_4 = Button(number_container_r2, text="4", height=1, width=6, command=lambda:number_callback(4))
button_5 = Button(number_container_r2, text="5", height=1, width=6, command=lambda:number_callback(5))
button_6 = Button(number_container_r2, text="6", height=1, width=6, command=lambda:number_callback(6))
button_7 = Button(number_container_r1, text="7", height=1, width=6, command=lambda:number_callback(7))
button_8 = Button(number_container_r1, text="8", height=1, width=6, command=lambda:number_callback(8))
button_9 = Button(number_container_r1, text="9", height=1, width=6, command=lambda:number_callback(9))
button_decimal = Button(number_container_r4, text=".", height=1, width=6, command=lambda:operator_callback("."))
button_percent = Button(number_container_r4, text="%", height=1, width=6, command=lambda:operator_callback("%"))
button_divide = Button(operation_container, text="/", height=1, width=6, command=lambda:operator_callback("/"))
button_multiply = Button(operation_container, text="x", height=1, width=6, command=lambda:operator_callback("*"))
button_subtract = Button(operation_container, text="-", height=1, width=6, command=lambda:operator_callback("-"))
button_add = Button(operation_container, text="+", height=1, width=6, command=lambda:operator_callback("+"))
button_undo = Button(misc_container_r1, text="undo", height=1, width=5, command=lambda:operator_callback("undo"))
button_clear = Button(misc_container_r1, text="clear", height=1, width=5, command=lambda:operator_callback("clear"))
button_Lparentheses = Button(misc_container_r2, text="(", height=1, width=5, command=lambda:operator_callback("("))
button_Rparentheses = Button(misc_container_r2, text=")", height=1, width=5, command=lambda:operator_callback(")"))
button_square = Button(misc_container_r3, text="sq", height=1, width=5, command=lambda:operator_callback("sq"))
button_root = Button(misc_container_r3, text="sqrt", height=1, width=5, command=lambda:operator_callback("sqrt"))
button_equal = Button(misc_container_r4, text="=", height=1, width=12, command=lambda:operator_callback("="))

#   Pack (bottom of tree) widgets
answer_label.pack(side=LEFT)

button_0.pack(side=LEFT)
button_1.pack(side=LEFT)
button_2.pack(side=LEFT)
button_3.pack(side=LEFT)
button_4.pack(side=LEFT)
button_5.pack(side=LEFT)
button_6.pack(side=LEFT)
button_7.pack(side=LEFT)
button_8.pack(side=LEFT)
button_9.pack(side=LEFT)
button_decimal.pack(side=LEFT)
button_percent.pack(side=LEFT)
button_divide.pack()
button_multiply.pack()
button_subtract.pack()
button_add.pack()
button_undo.pack(side=LEFT)
button_clear.pack(side=LEFT)
button_Lparentheses.pack(side=LEFT)
button_Rparentheses.pack(side=LEFT)
button_square.pack(side=LEFT)
button_root.pack(side=LEFT)
button_equal.pack(side=LEFT)

#   Pack (next to last level of tree) widgets
evaluation_container.pack()
widget_input_container.pack(side=BOTTOM)
number_container.pack(side=LEFT)
number_container_r1.pack()
number_container_r2.pack()
number_container_r3.pack()
number_container_r4.pack()
operation_container.pack(side=LEFT)
misc_container.pack(side=LEFT)
misc_container_r1.pack()
misc_container_r2.pack()
misc_container_r3.pack()
misc_container_r4.pack()



#   Run the main loop
window.mainloop()
