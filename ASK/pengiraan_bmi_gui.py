# Import module sys untuk periksa versi Python
import sys
# Import module Tkinter
if sys.version_info[0] == 3: # Periksa jika versi Python sama dengan 3
    # Untuk Python3
    import tkinter as tk ## 't'kinter
else:
    # Untuk Python2
    import Tkinter as tk ## 'T'kinter
    
# Functions
def button_clicked():
	tinggi = input_ketinggian.get()
    berat = input_berat.get()
    bmi = berat / (tinggi * tinggi)
    bmi = str(bmi)
    output_bmi.configure(text=bmi)


window = tk.Tk()

canvas = tk.Canvas(
    window,
    bg='#0099ff',
    width=600,
    height=500
    )
canvas.pack()

frame_input = tk.Frame(
    window,
    bg='#99d6ff',
    bd=5
    )
frame_input.place(
    relx=0.5,
    rely=0.1,
    relwidth=0.75,
    relheight=0.1,
    anchor='n'
    )

input_ketinggian = tk.Entry(
    frame_input,
    font=40
    )
input_ketinggian.place(
    relwidth=0.65,
    relheight=1
    )

input_berat = tk.Entry(
    frame_input,
    font=40
    )
input_berat.place(
    relx=0.15,
    relwidth=0.65,
    relheight=1
    )

button = tk.Button(
    frame_input,
    text="OK",
    font=40,
    command=button_clicked
    )
button.place(
    relx=0.7,
    relheight=1,
    relwidth=0.3
    )

frame_output = tk.Frame(
    window,
    bg='#99d6ff',
    bd=5
    )
frame_output.place(
    relx=0.5,
    rely=0.25,
    relwidth=0.75,
    relheight=0.6,
    anchor='n'
    )

output_bmi = tk.Label(
    frame_output
    )
output_bmi.place(
    relwidth=1,
    relheight=1
    )

window.mainloop()
