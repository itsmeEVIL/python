# import sys module untuk check python version
import sys
# Import module Tkinter
if sys.version_info[0] == 3: # check jika version python sama dengan 3
    # Untuk Python3
    from tkinter import * ## 't'kinter
else:
    # Untuk Python2
    from Tkinter import * ## 'T'kinter

# Window
window = Tk()
# Title window
window.title("pengiraan_bmi")
# Size window
window.geometry("400x250")

# Functions
# function untuk menukarkan text pada widget label
def clicked():
	# Mendapatkan input dari pemboleh ubah input_user
	input_text = input_user.get()
	# Configure widget label untuk ditukarkan dengan input_texts
	label.configure(text=input_text)

# function untuk close window
def close_window():
	window.destroy()


# Widget label
label = Label(
	window, # letak widget dimana
	text="Hello!", # text
	font=("Arial Bold", 40), # font type & size
	fg="black", # foreground/text color
	bg="blue" # background color
)

# Widget Button
button1 = Button(
	window,
	text="this is clickable!",
	fg="black",
	bg="red",
	command=clicked # call function
)
button2 = Button(
	window,
	text="close window",
	command=close_window # call function
)

# Widget input
input_user = Entry(
	window,
	# state="disabled", # disable widget daripada digunakan
	width=10, # lebar widget
	height=1 # tinggi widget 
)

# Meletakkan widget di dalam grid tertentu
label.grid(row=0, column=0)
button1.grid(row=1, column=1)
button2.grid(row=2, column=2)
input_user.grid(row=3, column=3)

# Focus kepada sesuatu widget
input_user.focus() # focus ke widget entry

# Loop the window
window.mainloop()
