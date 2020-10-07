# Atur cara untuk mengira BMI (Body Mass Index)
# Kumpulan Syabil & Amir

print("***Atur Cara Untuk Mengira BMI Anda***\n")

# Input
tinggi = input("Masukkan ketinggian anda (Meter): ")
berat = input("Masukkan berat badan anda (KG): ")

# Jika tinggi atau berat tidak kosong
if tinggi or berat != "":
	# Proses
	# Formula untuk mengira BMI - berat × tinggi^2
	bmi = float(berat) / (float(tinggi) * float(tinggi))

	# Output
	print("\nBMI Anda: ", round(bmi, 2), "\nDan Anda: ", end="")

	# Jika bmi kurang daripada 18.5
	if (bmi < 18.5):
		print("Kurang Berat Badan")

	# Jika bmi lebih atau sama dengan 18.5 dan kurang daripada 24.9
	elif (bmi >= 18.5 and bmi < 24.9):
		print("Berat Badan Normal")

	# Jika bmi lebih atau sama dengan 25.0 dan kurang daripada 29.9
	elif (bmi >= 25.0 and bmi < 29.9):
		print("Lebih Berat Badan")

	# Jika bmi lebih atau sama dengan 30.0
	elif (bmi >= 30.0):
		print("Obesiti")

# Jika tinggi atau berat kosong
else:
	print("ERROR:\nMasukkan Ketinggian Dan Berat Dengan Betul!")
