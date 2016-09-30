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
number_container = Frame(window, height=125, width=175)
number_container_r1 = Frame(number_container, height=31, width=175)
number_container_r2 = Frame(number_container, height=31, width=175)
number_container_r3 = Frame(number_container, height=31, width=175)
number_container_r4 = Frame(number_container, height=31, width=175)

evaluation_container = Frame(window, height=200, width=175)
evaluation_container.pack(side=TOP)
#   Define label
answer_label = Label(evaluation_container, text="0.00")


#   Define buttons
button_0 = Button(number_container_r4, text="0")
button_1 = Button(number_container_r3, text="1")
button_2 = Button(number_container_r3, text="2")
button_3 = Button(number_container_r3, text="3")
button_4 = Button(number_container_r2, text="4")
button_5 = Button(number_container_r2, text="5")
button_6 = Button(number_container_r2, text="6")
button_7 = Button(number_container_r1, text="7")
button_8 = Button(number_container_r1, text="8")
button_9 = Button(number_container_r1, text="9")
button_decimal = Button(number_container_r4, text=".")
button_percent = Button(number_container_r4, text="%")

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

#   Pack (next to last level of tree) widgets
number_container.pack(side=BOTTOM)
number_container_r1.pack()
number_container_r2.pack()
number_container_r3.pack()
number_container_r4.pack()

#   Run the main loop
window.mainloop()





