# Progam Python untuk mengira jumlah kos perkhemahan unit beruniform 

# Kos tetap
peribadi = float(13.50)
pakaian = float(105.90)
khemah = float(12.00)

# Kos tetap
kos_tetap = peribadi + pakaian + khemah
# Kos masak
kos_masak = float(input('\nMasukkan kos untuk barangan memasak: RM'))
# Jumlah kos
jumlah_kos = kos_tetap + kos_tetap

# Output
print('\n***Pengiraan Kos Perkhemahan Unit Beruniform***')
# Jumlah kos tetap
print('\nJumlah bagi Kos Tetap: RM', kos_tetap)
# Jumlah kos berubah
print('Jumlah bagi Kos Berubah : RM', kos_masak)
# Jumlah semua kos
print('Jumlah Kos: RM', round(jumlah_kos, 2))
