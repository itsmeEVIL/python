# Ralat sintaks
# Program Python untuk mengira purata ketinggian 5 ahli

# Input
# Ketinggian ahli
pertama = float(input('Ketinggian ahli pertama: '))
kedua = float(input('Ketinggian ahli kedua: '))
ketiga = float(input('Ketinggian ahli ketiga: '))
keempat = float(input('Ketinggian ahli keempat: '))
kelima = float(input('Ketinggian ahli kelima: '))

# Proses 
# Jumlah semua ahli
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
print('\nPurata Ketinggian: ', round(purata, 2), 'm') # Ralat yang berlaku ialah ketiadan tanda "," sebelum fungsi round # ...Ketinggian: ' round...
