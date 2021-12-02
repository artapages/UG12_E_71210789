#input
panjang = int(input("Masukkan Angka: "))

#proses
for x in range (panjang) :
    str(print(" "*(panjang - x)+" *"*(x + 1) ) )
for y in range (panjang-1) :
    str(print(" "*(y + 2)+" *"*(panjang - 1 - y) ) )