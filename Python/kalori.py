# Atur cara untuk mengetahui jumlah kalori yang dibenarkan berdasarkan jantina dan umur

# Output
print('***CADANGKAN JUMLAH KALORI YANG DIBERNARKAN BERDASARKAN JANTINA DAN UMUR***')

# Input
# Jantina (Ya = Lelaki, Tidak = Perempuan)
jantina = input('Adakah jantina anda lelaki? (YA atau TIDAK): ')

# Proses
# Jika input ialah Ya
if jantina == 'Ya' or jantina == 'ya' or jantina == 'YA':
	# Input
	# Umur
	umur = int(input('Berapakah Umur Anda?\n'))

	# Jika umur lebih atau sama dengan 60
	if (umur >= 60):
		# Output
		print('Nilai kalori yang dibenarkan ialah 2010')

	# Jika umur lebih atau sama dengan 30
	elif (umur >= 30):
		# Output
		print('Nilai kalori yang dibenarkan ialah 2460')

	# Jika umur lebih atau sama dengan 19
	elif (umur >= 19):
		# Output
		print('Nilai kalori yang dibenarkan ialah 2440')

	# Jika umur lebih atau sama dengan 16
	elif (umur >= 16):
		# Output
		print('Nilai kalori yang dibenarkan ialah 2840')

	# Jika umur lebih atau sama dengan 13
	elif (umur >= 13):
		# Output
		print('Nilai kalori yang dibenarkan ialah 2690')

	# Jika umur kurang daripada 13
	else:
	  # Output
		print('Maaf, had umur perlu 13 tahun ke atas.')

# Jika input ialah Tidak
elif jantina == 'Tidak' or jantina == 'tidak' or jantina == 'TIDAK':
	# Input
	# Umur
	umur = int(input('Berapakah Umur Anda?\n'))

	# Jika umur lebih atau sama dengan 60
	if (umur >= 60):
		# Output
		print('Nilai kalori yang dibenarkan ialah 1780')

	# Jika umur lebih atau sama dengan 30
	elif (umur >= 30):
		# Output
		print('Nilai kalori yang dibenarkan ialah 2180')

	# Jika umur lebih atau sama dengan 19
	elif (umur >= 19):
		# Output
		print('Nilai kalori yang dibenarkan ialah 2000')

	# Jika umur lebih atau sama dengan 16
	elif (umur >= 16):
		# Output
		print('Nilai kalori yang dibenarkan ialah 2050')

	# Jika umur lebih atau sama dengan 13
	elif (umur >= 13):
		# Output
		print('Nilai kalori yang dibenarkan ialah 2180')

	# Jika umur kurang daripada 13
	else:
	  # Output
		print('Maaf, had umur perlu 13 tahun ke atas.')

# Jika tiada input atau salah input
else:
  # Output
	print('Terima Kasih')
