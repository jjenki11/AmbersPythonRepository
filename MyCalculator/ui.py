#   Amber's Calculator
#       ui.py

#   Adding import statements
from tkinter import *

#   Construct the window
window = Tk()
#   Set the window's title
window.title("THIS IS MY WINDOW!")
window.geometry("325x350")

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
answer_label = Label(evaluation_container, text="0.00")


#   Define buttons
button_0 = Button(number_container_r4, text="0", height=1, width=3)
button_1 = Button(number_container_r3, text="1", height=1, width=3)
button_2 = Button(number_container_r3, text="2", height=1, width=3)
button_3 = Button(number_container_r3, text="3", height=1, width=3)
button_4 = Button(number_container_r2, text="4", height=1, width=3)
button_5 = Button(number_container_r2, text="5", height=1, width=3)
button_6 = Button(number_container_r2, text="6", height=1, width=3)
button_7 = Button(number_container_r1, text="7", height=1, width=3)
button_8 = Button(number_container_r1, text="8", height=1, width=3)
button_9 = Button(number_container_r1, text="9", height=1, width=3)
button_decimal = Button(number_container_r4, text=".", height=1, width=3)
button_percent = Button(number_container_r4, text="%", height=1, width=3)
button_divide = Button(operation_container, text="/", height=1, width=3)
button_multiply = Button(operation_container, text="x", height=1, width=3)
button_subtract = Button(operation_container, text="-", height=1, width=3)
button_add = Button(operation_container, text="+", height=1, width=3)
button_undo = Button(misc_container_r1, text="undo", height=1, width=3)
button_clear = Button(misc_container_r1, text="clear", height=1, width=3)
button_Lparentheses = Button(misc_container_r2, text="(", height=1, width=3)
button_Rparentheses = Button(misc_container_r2, text=")", height=1, width=3)
button_square = Button(misc_container_r3, text="sq", height=1, width=3)
button_root = Button(misc_container_r3, text="sqrt", height=1, width=3)
button_equal = Button(misc_container_r4, text="=", height=1, width=10)

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
