# Atur cara untuk mengira purata ketinggian 5 ahli

# Input
# Ketinggian ahli pertama
pertama = float(input('Ketinggian ahli pertama: '))
# Ketinggian ahli kedua
kedua = float(input('Ketinggian ahli kedua: '))
# Ketinggian ahli ketiga
ketiga = float(input('Ketinggian ahli ketiga: '))
# Ketinggian ahli keempat
keempat = float(input('Ketinggian ahli keempat: '))
# Ketinggian ahli kelima
kelima= float(input('Ketinggian ahli kelima: '))

# Proses
# Jumlah ketinggian semua ahli
jumlah = pertama + kedua + ketiga + keempat + kelima
# Purata ketinggian semua ahli
purata = jumlah / 5

# Output
print('\nUkuran Ketinggian Yang Dimasukkan:')
# Ketinggian ahli pertama
print('Ahli pertama: ', pertama, 'm')
# Ketinggian ahli kedua
print('Ahli kedua: ', kedua, 'm')
# Ketinggian ahli ketiga
print('Ahli ketiga: ', ketiga, 'm')
# Ketinggian ahli keempat
print('Ahli keempat: ', keempat, 'm')
# Ketinggian ahli kelima
print('Ahli kelima: ', kelima, 'm')
# Purata ketinggian semua ahli
print('\nPurata Ketinggian: ', round(purata, 2), 'm')
