#input
awal = int(input("Masukkan awal deret: "))
akhir = int(input("Masukkan ahkir deret: "))

#objek
kyungsoo = []

#proses
if ((awal + 1) % 2 == 0):
    for yayy in range (awal + 1, akhir, 2):
        if (yayy % 5 == 0) or (yayy % 9 == 0): continue
        print (yayy, end = " ")

else:
    for yayy in range (awal, akhir, 2):
        if (yayy % 5 == 0) or (yayy % 9 == 0) : continue
        print (yayy, end = " ")