import sys
# Import module Tkinter
if sys.version_info[0] == 3:
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

# Widget label
label = Label(
	window,
	text="Hello!",
	font=("Arial Bold", 40),
	foreground="black",
	background="blue"
)
# Widget Button
button = Button(
	text="this is clickable!",
	foreground="black",
	background="red"
)

# Meletakkan widget di dalam grid tertentu
label.grid(row=0, column=0)
button.grid(row=1, column=0)

# Loop the window
window.mainloop()
