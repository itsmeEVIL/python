# Ralat sintaks
# Program Python untuk mengira purata ketinggian 5 ahli

# Input ketinggian ahli
pertama = float(input('Ketinggian ahli pertama: '))
kedua = float(input('Ketinggian ahli kedua: '))
ketiga = float(input('Ketinggian ahli ketiga: '))
keempat = float(input('Ketinggian ahli keempat: '))
kelima = float(input('Ketinggian ahli kelima: '))

# Jumlah semua ahli
jumlah = pertama + kedua + ketiga + keempat + kelima
# Purata ketinggian semua ahli
purata = jumlah / 5

# Print input ketinggian ahli
print('\nUkuran Ketinggian Yang Dimasukkan:')
print('Ahli pertama: ', pertama, 'm')
print('Ahli kedua: ', kedua, 'm')
print('Ahli ketiga: ', ketiga, 'm')
print('Ahli keempat: ', keempat, 'm')
print('Ahli kelima: ', kelima, 'm')

# Print purata semua ketinggian ahli
print('\nPurata Ketinggian: ', round(purata, 2), 'm')
