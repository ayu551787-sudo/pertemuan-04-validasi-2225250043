teks = input("jumlah soal benar dari 20: ") .strip()
try:
    benar = int(teks)
except valueError:
    print("masukan ditolak: jumlah harus berupa bilangan bulat.")
else:
    if benar < 0 or benar > 20:
        print("masukan ditolak: jumlah harus berada pada rentang 0 sampai 20.")
    else:
        persen = benar / 20 * 100
        print(f"persentase = (persen:.2f) persen")
        if persen >= 75:
            print("tuntas")
        else: 
            print("belum tuntas")