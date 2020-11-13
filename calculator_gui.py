from tkinter import *

# function
def calculate(event=None):
    output_label.configure(text="hahaha")

# blank window
root = Tk()
root.title("Calculator")
root.geometry("400x500") # window size

# upper frame
upper_frame = Frame(root, bg="#a6a6a6", bd=10)
upper_frame.place(relx=0.5, rely=0, relwidth=1, relheight=0.2, anchor="n")

# lower frame
lower_frame = Frame(root, bg="#cccccc", bd=5)
lower_frame.place(relx=0.5, rely=1, relwidth=1, relheight=0.8, anchor="s")

# output / upper label
output_label = Label(upper_frame, text="Enter number here...", font=("roboto", 17, "bold"), bg="#88cc00", bd=5)
output_label.place(relwidth=1, relheight=1)

# input / lower button
button_1 = Button(lower_frame, text="1", font=("roboto", 18), command=calculate).place(relx=0, rely=0, relwidth=0.25, relheight=0.25)
button_2 = Button(lower_frame, text="2", font=("roboto", 18), command=calculate).place(relx=0.25, rely=0, relwidth=0.25, relheight=0.25)
button_3 = Button(lower_frame, text="3", font=("roboto", 18), command=calculate).place(relx=0.50, rely=0, relwidth=0.25, relheight=0.25)
button_plus = Button(lower_frame, text="+", font=("roboto", 18), command=calculate).place(relx=0.75, rely=0, relwidth=0.25, relheight=0.25)
button_4 = Button(lower_frame, text="4", font=("roboto", 18), command=calculate).place(relx=0, rely=0.25, relwidth=0.25, relheight=0.25)
button_5 = Button(lower_frame, text="5", font=("roboto", 18), command=calculate).place(relx=0.25, rely=0.25, relwidth=0.25, relheight=0.25)
button_6 = Button(lower_frame, text="6", font=("roboto", 18), command=calculate).place(relx=0.50, rely=0.25, relwidth=0.25, relheight=0.25)
button_minus = Button(lower_frame, text="-", font=("roboto", 18), command=calculate).place(relx=0.75, rely=0.25, relwidth=0.25, relheight=0.25)
button_7 = Button(lower_frame, text="7", font=("roboto", 18), command=calculate).place(relx=0, rely=0.50, relwidth=0.25, relheight=0.25)
button_8 = Button(lower_frame, text="8", font=("roboto", 18), command=calculate).place(relx=0.25, rely=0.50, relwidth=0.25, relheight=0.25)
button_9 = Button(lower_frame, text="9", font=("roboto", 18), command=calculate).place(relx=0.50, rely=0.50, relwidth=0.25, relheight=0.25)
button_multiply = Button(lower_frame, text="*", font=("roboto", 18), command=calculate).place(relx=0.75, rely=0.50, relwidth=0.25, relheight=0.25)
button_clear = Button(lower_frame, text="C", font=("roboto", 18), command=calculate).place(relx=0, rely=0.75, relwidth=0.25, relheight=0.25)
button_0 = Button(lower_frame, text="0", font=("roboto", 18), command=calculate).place(relx=0.25, rely=0.75, relwidth=0.25, relheight=0.25)
button_calc = Button(lower_frame, text="=", font=("roboto", 18), command=calculate).place(relx=0.50, rely=0.75, relwidth=0.25, relheight=0.25)
button_divide = Button(lower_frame, text="/", font=("roboto", 18), command=calculate).place(relx=0.75, rely=0.75, relwidth=0.25, relheight=0.25)

# loop through the program
root.mainloop()
