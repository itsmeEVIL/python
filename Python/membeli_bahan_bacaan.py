# Ralat logik
# Progam Python untuk mengira harga buku motivasi

# Pemboleh ubah
# Harga-harga buku
# Harga buku cerita
buku_cerita = float(39)
# Harga majalah
majalah = float(16)

# Proses
# Pengiraan
# Jumlah buku cerita dan majalah
jum1 = (buku_cerita * 2) + majalah
# Bayaran yang dibuat
bayaran = 200
# Baki yang tinggal
baki1 = 66

# Jumlah harga semua buku
jumlah_buku = bayaran - baki1
# Harga senaskah buku motivasi
buku_motisasi = (jumlah_buku - jum1) / 2 # Ralat ialah tiada tanda kurungan yang menyebabkan pengiraan tidak tepat # buku_motivasi = jum_buku - jumlah_buku / 2

# Semakan Pengiraan
# Jumlah harga semua buku
jum3 = jum1 + (2 * buku_motisasi)
# Baki
baki2 = 200 - jum3

# Output
# Bayaran yang dibuat
print('Bayaran yang dibuat: RM200')
# Harga 2 buku cerita
print('\nBuku cerita: RM', 2 * buku_cerita)
# Harga majalah
print('Majalah: RM', majalah)
# Harga senaskah buku motivasi
print('Buku motivasi: RM', buku_motisasi)
# Baki wang selepas pembayaran
print('\nBaki wang anda: RM', baki2, '\nSemakan adalah:', baki2==baki1) #True bermaksud semakan benar
