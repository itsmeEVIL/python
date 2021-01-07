# Atur cara untuk mengira Body Mass Index (BMI)
# Kumpulan Syabil & Amir
# Dibuat oleh Amir

# Output
print("***Atur Cara Untuk Mengira BMI Anda***\n")

# Input
tinggi = input("Masukkan ketinggian anda (Meter): ")
berat = input("Masukkan berat badan anda (KG): ")

# Function - mengetahui jika value ialah float atau tidak


def isfloat(value):
    # Jika value sama dengan float return true
    try:
        float(value)
        return True

    # Jika value tidak sama dengan float return false
    except ValueError:
        return False


# Note - != bermaksud tidak sama dengan
# Jika input tinggi tidak sama dengan "" dan berat tidak sama dengan ""
if tinggi != "" and berat != "":
    # Jika tinggi sama dengan float dan berat sama dengan float
    if isfloat(tinggi) == True and isfloat(berat) == True:
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

    # Jika tinggi tidak sama dengan float dan berat sama dengan float
    elif isfloat(tinggi) == False and isfloat(berat) == True:
        # Output
        print("ERROR:\nMasukkan Ketinggian Anda Dengan Betul (Nombor)!")

    # Jika tinggi sama dengan float dan berat tidak sama dengan float
    elif isfloat(tinggi) == True and isfloat(berat) == False:
        # Output
        print("ERROR:\nMasukkan Berat Badan Anda Dengan Betul (Nombor)!")

    # Jika tinggi tidak sama dengan float dan berat tidak sama dengan float
    else:
        # Output
        print("ERROR:\nMasukkan Ketinggian Dan Berat Badan Anda Dengan Betul (Nombor)!")


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
