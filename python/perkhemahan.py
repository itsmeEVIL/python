# Ralat masa larian
# Progam Python untuk mengira jumlah kos perkhemahan unit beruniform 

# Kos item-item dalam kos tetap
# Kos kelengkapan peribadi
peribadi = float(13.50) # Ralat ialah menggunakan fungsi float secara tidak betul # float(peribadi = 13.50)
# Kos pakaian
pakaian = float(105.90) # Ralat ialah menggunakan fungsi float secara tidak betul # float(pakaiam = 105.90)
# Kos sewaan khemah
khemah = float(12.00) # Ralat ialah menggunakan fungsi float secara tidak betul # float(khemah = 12.00)

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
