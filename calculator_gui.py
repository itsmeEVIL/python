# graphical user interface (GUI) of a calculator using tkinter
# made by itsmeEVIL

from tkinter import *

# function
expression = ""

def press(num):
    global expression

    expression = expression + str(num)
    output_label.configure(text=expression)

def operator(symbol):
    global expression

    expression = expression + " " + str(symbol) + " "
    output_label.configure(text=expression)

def equal():
    try:
        global expression

        total = str(round(eval(expression), 3))
        output_label.configure(text=expression + " = " + total)
        expression = ""

    except:
        output_label.configure(text="ERROR")
        expression = ""

def clear():
    global expression

    expression = ""
    output_label.configure(text="Enter the number here...")

# blank window
root = Tk()
root.title("Calculator")
root.geometry("400x500") # window size

# upper frame
upper_frame = Frame(root, bg="#A5BACB", bd=10)
upper_frame.place(relx=0.5, rely=0, relwidth=1, relheight=0.2, anchor="n")

# lower frame
lower_frame = Frame(root, bg="#D8E0E2", bd=5)
lower_frame.place(relx=0.5, rely=1, relwidth=1, relheight=0.8, anchor="s")

# output / upper label
output_label = Label(upper_frame, text="Enter the number here...", font=("roboto", 17, "bold"), bg="#D1DCBA", fg="#64773c", bd=5)
output_label.place(relwidth=1, relheight=1)

# input / lower button
# first row
button_7 = Button(lower_frame, text="7", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(7)).place(relx=0, rely=0, relwidth=0.2, relheight=0.25)
button_8 = Button(lower_frame, text="8", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(8)).place(relx=0.2, rely=0, relwidth=0.2, relheight=0.25)
button_9 = Button(lower_frame, text="9", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(9)).place(relx=0.4, rely=0, relwidth=0.2, relheight=0.25)
button_power = Button(lower_frame, text="^", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:operator("**")).place(relx=0.6, rely=0, relwidth=0.2, relheight=0.25)
button_clear = Button(lower_frame, text="C", font=("roboto", 18), bg="#4D738A", fg="#f2f2f2", activebackground="#405f72", activeforeground="#f2f2f2", relief="flat", command=clear).place(relx=0.8, rely=0, relwidth=0.2, relheight=0.25)
# second row
button_4 = Button(lower_frame, text="4", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(4)).place(relx=0, rely=0.25, relwidth=0.2, relheight=0.25)
button_5 = Button(lower_frame, text="5", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(5)).place(relx=0.2, rely=0.25, relwidth=0.2, relheight=0.25)
button_6 = Button(lower_frame, text="6", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(6)).place(relx=0.4, rely=0.25, relwidth=0.2, relheight=0.25)
button_multiply = Button(lower_frame, text="×", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:operator("*")).place(relx=0.6, rely=0.25, relwidth=0.2, relheight=0.25)
button_divide = Button(lower_frame, text="÷", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:operator("/")).place(relx=0.8, rely=0.25, relwidth=0.2, relheight=0.25)
# third row
button_1 = Button(lower_frame, text="1", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(1)).place(relx=0, rely=0.5, relwidth=0.2, relheight=0.25)
button_2 = Button(lower_frame, text="2", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(2)).place(relx=0.2, rely=0.5, relwidth=0.2, relheight=0.25)
button_3 = Button(lower_frame, text="3", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(3)).place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.25)
button_plus = Button(lower_frame, text="+", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:operator("+")).place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.25)
utton_minus = Button(lower_frame, text="-", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:operator("-")).place(relx=0.8, rely=0.5, relwidth=0.2, relheight=0.25)
# fourth row
button_0 = Button(lower_frame, text="0", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(0)).place(relx=0, rely=0.75, relwidth=0.2, relheight=0.25)
button_dot = Button(lower_frame, text=".", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(".")).place(relx=0.2, rely=0.75, relwidth=0.2, relheight=0.25)
button_bracket1 = Button(lower_frame, text="(", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press("(")).place(relx=0.4, rely=0.75, relwidth=0.2, relheight=0.25)
button_bracket2 = Button(lower_frame, text=")", font=("roboto", 18), bg="#7998AC", fg="#f2f2f2", activebackground="#61869e", activeforeground="#f2f2f2", relief="flat", command=lambda:press(")")).place(relx=0.6, rely=0.75, relwidth=0.2, relheight=0.25)
button_calc = Button(lower_frame, text="=", font=("roboto", 18), bg="#FD8103", fg="#f2f2f2", activebackground="#e37302", activeforeground="#f2f2f2", relief="flat", command=equal).place(relx=0.8, rely=0.75, relwidth=0.2, relheight=0.25)

# loop through the program
root.mainloop()
