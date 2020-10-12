# Atur cara untuk mengira BMI (Body Mass Index)
# Kumpulan Syabil & Amir

print("***Atur Cara Untuk Mengira BMI Anda***\n")

# Input
tinggi = input("Masukkan ketinggian anda (Meter): ")
berat = input("Masukkan berat badan anda (KG): ")

def kira_bmi():
	global tinggi, berat
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

		# Output
		print("\nBMI Anda:", bmi, "\nDan Anda:", end=" ")

		# Jika bmi kurang daripada 18.5
		if bmi < 18.5:
		  	# Output
			print("Kurang Berat Badan")

		# Jika bmi lebih atau sama dengan 18.5 dan kurang daripada 24.9
		elif bmi >= 18.5 and bmi < 24.9:
		  	# Output
			print("Berat Badan Normal")

		# Jika bmi lebih atau sama dengan 25.0 dan kurang daripada 29.9
		elif bmi >= 25.0 and bmi < 29.9:
		  	# Output
			print("Lebih Berat Badan")

		# Jika bmi lebih atau sama dengan 30.0
		elif bmi >= 30.0:
		 	# Output
			print("Obesiti")

	# Jika input tinggi tidak sama dengan "" dan berat sama dengan ""
	elif tinggi != "" and berat == "":
	  	# Output
	 	print("ERROR:\nMasukkan Berat Badan Anda!")

	# Jika input tinggi sama dengan "" dan berat tidak sama dengan ""
	elif tinggi == "" and berat != "":
	  	# Output
	  	print("ERROR:\nMasukkan Ketinggian Anda!")

	# Jika input tinggi sama dengan "" dan berat sama dengan ""
	else:
	  	# Output
	  	print("ERROR:\nMasukkan Ketinggian Dan Berat Badan Anda!")

# Jika tinggi dan berat tidak sama dengan ""
if tinggi != "" and berat != "":
	# Test input tinggi & berat jika boleh ditukarkan menjadi float 
	try:
		test_tinggi = float(tinggi)
		test_berat = float(berat)

	# Jika try == error
	except:
		print("ERROR:\nMasukkan Ketinggian Dan Berat Badan Anda Dengan Betul (Nombor)!")

	# Jika try != error
	else:
		kira_bmi()

# Jika tinggi tidak sama dengan ""
elif tinggi != "":
	# Test input tinggi jika boleh ditukarkan menjadi float 
	try:
		test_tinggi = float(tinggi)

	# Jika try == error
	except:
		print("ERROR:\nMasukkan Ketinggian Anda Dengan Betul (Nombor)!")

	# Jika try != error
	else:
		kira_bmi()

# Jika berat tidak sama dengan ""
elif berat != "":
	# Test input berat jika boleh ditukarkan menjadi float 
	try:
		test_berat = float(berat)

	# Jika try == error
	except:
		print("ERROR:\nMasukkan Berat Badan Anda Dengan Betul (Nombor)!")

	# Jika try != error
	else:
		kira_bmi()
