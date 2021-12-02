#input
mata_kuliah =[
    #Senin[0]
    ["1 Algoritma Graf", "3 Sistem Operasi", "4 PAK", "5 Praktikum INLAN"],
    #Selasa[1]
    ["2 Matematika Teknik", "4 Bhs Indonesia", "6 PKN"], 
    #Rabu 
    #Kamis[2]
    ["1 IMK", "3 LogMat", "4 Praktekkom"],
    #Jumat[3]
    ["2 Sistem Basis Data", "4 Praktikum Sistem Basis Data", "6 INLAN"]    
    ]

#proses
while True:
    Days = str(input("Hi Tutu, Silahkan Masukkan hari yang ingin Anda telusuri: ")).lower()    
    if Days == "senin" :
        for a in mata_kuliah [0]:
            print("kelas ke -",format(a))
    elif Days == "selasa" :
        for a in mata_kuliah [1]:
            print("kelas ke -",format(a))
    elif Days == "rabu" :
        print("Hari", Days, "Anda tidak ada kelas")
    elif Days == "kamis" :
        for a in mata_kuliah [2]:
            print("kelas ke -",format(a))
    elif Days == "jumat" :
        for a in mata_kuliah [3]:
            print("kelas ke -",format(a))