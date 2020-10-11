# GUI atur cara untuk mengira BMI (Body Mass Index)
# Kumpulan Syabil & Amir

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
	# Dapatkan input daripada entry input_ketinggian
	tinggi = input_ketinggian.get()
	# Dapatkan input daripada entry input_berat
    berat = input_berat.get()
    
    # Note - != bermaksud tidak sama dengan
    # Jika input tinggi tidak sama dengan "" dan berat tidak sama dengan ""
    if tinggi != "" and berat != "":
    	
        # Proses
	    # Tukar string kepada nombor
	    berat = float(berat)
	    tinggi = float(tinggi)
	    # Formula untuk mengira BMI - berat ÷ tinggi^2
	    bmi = berat / (tinggi * tinggi)
	    # Bundarkan bmi kepada 2 tempat perpuluhan
	    bmi = round(bmi, 2)
	    # Tukar bmi *float* menjadi string
	    bmi = str(bmi)
	
	    # Jika bmi kurang daripada 18.5
	    if bmi < 18.5:
	        status = "Kurang Berat Badan"

	    # Jika bmi lebih atau sama dengan 18.5 dan kurang daripada 24.9
	    elif bmi >= 18.5 and bmi < 24.9:
	        status = "Berat Badan Normal"

	    # Jika bmi lebih atau sama dengan 25.0 dan kurang daripada 29.9
	    elif bmi >= 25.0 and bmi < 29.9:
	        status = "Lebih Berat Badan"

	    # Jika bmi lebih atau sama dengan 30.0
	    elif bmi >= 30.0:
	    	status = "Obesiti"
	    
	    # Output
	    # Configure/Edit Label output_bmi
        output_bmi.configure(text="\nBMI Anda:" + bmi + "\nDan Anda:" + status)

    # Jika input tinggi tidak sama dengan "" dan berat sama dengan ""
    elif tinggi != "" and berat == "":
        # Output
        output_bmi.configure(text="ERROR:\nMasukkan Berat Badan Anda!")

    # Jika input tinggi sama dengan "" dan berat tidak sama dengan ""
    elif tinggi == "" and berat != "":
        # Output
        output_bmi.configure(text="ERROR:\nMasukkan Ketinggian Anda!")

    # Jika input tinggi sama dengan "" dan berat sama dengan ""
    else:
        # Output
        output_bmi.configure(text="ERROR:\nMasukkan Ketinggian Dan Berat Badan Anda!")


# Window
window = tk.Tk()
window.title('Atur Cara Untuk Mengira BMI Anda')

# Canvas
canvas = tk.Canvas(
    window, # Diletakkan di dalam window
    bg='#0099ff', # Background color
    width=600, # Lebar
    height=500 # Tinggi
    )
canvas.pack() # Pack canvas

# Frame
frame_input = tk.Frame(
    window, # Diletakkan di dalam window
    bg='#99d6ff', # Background color
    bd=5 # Border
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
    font=10,
    command=button_clicked
    )
button.place(
    relx=0.7,
    relheight=1,
    relwidth=0.3
    )

# Frame
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

# Label
output_bmi = tk.Label( # 
    frame_output # Diletakkan di dalam Frame frame_ouput
    )
output_bmi.place(
    relwidth=1,
    relheight=1
    )

# Jalankan program
window.mainloop()
