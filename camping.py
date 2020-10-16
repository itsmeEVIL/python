# program to calculate the total cost of camping in uniformed units  

# variables
# cost of items in fixed cost
# cost of personal equipment
personal = float(13.50)
# cost of clothing
clothing = float(105.90)
# tent rental costs
tent = float(12.00)

# process
# fixed cost
kos_tetap = peribadi + pakaian + khemah
# cooking costs
kos_masak = float(input('\nMasukkan kos untuk barangan memasak: RM'))
# total cost
jumlah_kos = kos_tetap + kos_masak

# output
print('\n***Pengiraan Kos Perkhemahan Unit Beruniform***')
# total fixed cost
print('\nJumlah bagi Kos Tetap: RM', kos_tetap)
# total costs change
print('Jumlah bagi Kos Berubah : RM', kos_masak)
# total of all costs
print('Jumlah Kos: RM', round(jumlah_kos, 2))
