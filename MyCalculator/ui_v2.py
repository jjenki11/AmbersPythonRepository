#   Amber's Calculator
#       ui.py
#   Adding import statements
from Tkinter import *
#   for sqrt
import math

#   Construct the window
window = Tk()
#   Set the window's title
window.title("Calculator")
window.geometry("325x350")
window.configure(background="powder blue")

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


#   Define label to hold ongoing calculation
answer_label = Label(evaluation_container, text="0", bg="powder blue")

#   Define expression class to hold input(s) and operation prior to evaluation.
class Expression(object):
    input_number_1 = 0
    input_number_2 = 0
    operator = None
    #   Obligatory initialization
    def __init__(self):
        print("New expression created...")
    def set_input_1(self, num):
        self.input_number_1 = num
    def set_input_2(self, num):
        self.input_number_2 = num
    def set_operator(self, op):
        self.operator = op
    def evaluate_expression(self):
        print("What is the current operator?  " + str(self.operator))
        self.operator.replace('\'', "")
        result = 0
        if(self.operator.find('+') != -1):
            result = math.add(self.input_number_1, self.input_number_2)
            print( result )
        elif(self.operator.find('-') != -1):
            result = math.subtract(self.input_number_1, self.input_number_2)
            print( result )
        elif(self.operator.find('*') != -1):
            result = math.multiply(self.input_number_1, self.input_number_2) 
            print( result )
        elif(self.operator.find('/') != -1):
            result = math.divide(self.input_number_1, self.input_number_2)
            print( result )
        elif(self.operator.find('x*x') != -1):
            result = math.square_value(self.input_number_1)
            print( result )
        elif(self.operator.find('u"\u221A"') != -1):
            result = math.square_value(self.input_number_1)
            print( result )
        else:
            #   This should kick us out before overwriting the inputs
            print("bad expression)
            return        
        self.input_number_1 = self.input_number_2
        self.operator = None
        self.input_number_2 = None
        answer_label['text'] = str(result)            

#   Define operator class
class Operators(object):
    #   Obligatory initialization
    def __init__(self):
        print("New Operator created...")
    def add(self, in1, in2):
        return in1+in2
    def subtract(self, in1, in2):
        return (in1-in2)
    def multiply(self, in1, in2):
        return (in1*in2)
    def divide(self, in1, in2):
        return (in1/in2)    
    #   TBD impl
    #       square root 
    #       square value
    def square_root(self, in1):
        return math.sqrt(in1)
    def square_value(self, in1):
        return (in1 * in1)

#   DEFINE INPUT HANDLERS
    #   Define number callback
def number_callback(num):
    print("NUMBER = " + str(num))
    if((answer_label.cget("text") == str(0)) or (answer_label.cget("text") == 0)):
        answer_label['text'] = ""
        answer_label['text'] = str(num)
    else:
        print("Does THE LABEL HAVE A 0???? ->  " + answer_label.cget("text"))
        curr_label = answer_label.cget("text")
        curr_label = str(curr_label) + str(num)
        answer_label['text'] = curr_label
            
    #   Define operator callback
def operator_callback(op):
    print("OPERATOR = " + op)
    if((op == "clear") or (op ==  "<Delete>")):
        print("CLEAR called.")
        clear_callback(None)
    elif(op == "undo"):
        print("UNDO called.")    
    else:
        #this is where the arithmetic is done.
        expr.set_input_1(float(answer_label.cget("text")))
        expr.set_operator(op)
        answer_label['text'] = 0

#   This handles any key press (that has a standard unicode value) and performs proper action
def keypress_callback(key):
    print("KEY is -> " + str(key.char))
    if(str(key.char).isdigit()):
        print("It is a number.")
        number_callback(str(key.char))
    elif((repr(key.char) == "'+'") or (repr(key.char) == "'-'") or (repr(key.char) == "'*'") or (repr(key.char) == "'/'") or (repr(key.char) == "<Delete>")):
        print("It is an operator.")
        operator_callback(repr(key.char))
    elif(str(key.char) == "."):
        print("Decimal point pressed.")
        curr_label = answer_label.cget("text")
        if(curr_label.find('.') != -1):
            print("You already have a decimal point in your expression, ignoring this one.")
        else:
            curr_label = curr_label + str(".")
            answer_label['text'] = curr_label

#   This will revert the text label back to 0
def clear_callback(key):
    print("Clear pressed.")
    if not(float(answer_label.cget("text")) == 0):
        print("It is going to reset now.")
        answer_label['text'] = "0"
        expr = None
        expr = Expression()
        
#   Pretty self explanatory.
def evaluate_callback(key):
    print("Returning your answer...")
    expr.set_input_2(float(answer_label.cget("text")))
    #   If the expression is sqrt or square, then we only need the first input.
    if((expr.operator == "x*x") or (expr.operator == u"\u221A")):        
        expr.evaluate_expression()
    #   If the expression is anything else, set the 2nd input and then evaluate.
    else:
        expr.set_input_2(float(answer_label.cget("text")))
        expr.evaluate_expression()

#   Define buttons
button_0 = Button(number_container_r4, text="0", height=1, width=3, bg="powder blue", command=lambda:number_callback(0))
button_1 = Button(number_container_r3, text="1", height=1, width=3, command=lambda:number_callback(1))
button_2 = Button(number_container_r3, text="2", height=1, width=3, command=lambda:number_callback(2))
button_3 = Button(number_container_r3, text="3", height=1, width=3, command=lambda:number_callback(3))
button_4 = Button(number_container_r2, text="4", height=1, width=3, command=lambda:number_callback(4))
button_5 = Button(number_container_r2, text="5", height=1, width=3, command=lambda:number_callback(5))
button_6 = Button(number_container_r2, text="6", height=1, width=3, command=lambda:number_callback(6))
button_7 = Button(number_container_r1, text="7", height=1, width=3, command=lambda:number_callback(7))
button_8 = Button(number_container_r1, text="8", height=1, width=3, command=lambda:number_callback(8))
button_9 = Button(number_container_r1, text="9", height=1, width=3, command=lambda:number_callback(9))
button_decimal = Button(number_container_r4, text=".", height=1, width=3, command=lambda:operator_callback("."))
button_percent = Button(number_container_r4, text="%", height=1, width=3, command=lambda:operator_callback("%"))
button_divide = Button(operation_container, text="/", height=1, width=3, command=lambda:operator_callback("/"))
button_multiply = Button(operation_container, text="x", height=1, width=3, command=lambda:operator_callback("*"))
button_subtract = Button(operation_container, text="-", height=1, width=3, command=lambda:operator_callback("-"))
button_add = Button(operation_container, text="+", height=1, width=3, command=lambda:operator_callback("+"))
button_undo = Button(misc_container_r1, text="undo", height=1, width=5, state=DISABLED, command=lambda:operator_callback("undo"))   #TBD impl
button_clear = Button(misc_container_r1, text="clear", height=1, width=5, command=lambda:operator_callback("clear"))
button_Lparentheses = Button(misc_container_r2, text="(", height=1, width=5, state=DISABLED, command=lambda:operator_callback("("))   #TBD impl
button_Rparentheses = Button(misc_container_r2, text=")", height=1, width=5, state=DISABLED, command=lambda:operator_callback(")"))   #TBD impl
button_square = Button(misc_container_r3, text="x*x", height=1, width=5, command=lambda:operator_callback("x*x"))
button_root = Button(misc_container_r3, text=u"\u221A", height=1, width=5, command=lambda:operator_callback(u"\u221A"))
button_equal = Button(misc_container_r4, text="=", height=1, width=15, command=lambda:operator_callback("="))

#   Pack (bottom of tree) widgets
evaluation_container.pack(side=TOP)
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

#   Subscribe to 'keyboard press' events and handle above
window.bind("<Key>", keypress_callback)
window.bind("<Delete>", clear_callback)
#   these are the shortcut keys to evaluate the expression
window.bind("<Return>", evaluate_callback)
window.bind("<KP_Enter>", evaluate_callback)

#   These are the 'worker' classes that we will eventually  move into their own file(s).
math = Operators()
expr   = Expression()

#   Run the main loop
window.mainloop()
