a = float(input("sudut A: "))
b = float(input("sudut B: "))
c = float(input("sudut C: "))
if a <= 0 or b <= 0 or c <= 0:
    print("masukan ditolak: setiap sudut harus lebih dari 0 derajat.")
elif abs (a + b + c - 180) > le-9:
    print("masukan tolak: jumlah ketiga sudut harus 180 derajat.")
else:
    terbesar = max(a, b, c)
    if terbesar > 90:
        print("segitiga tumpul")
    elif terbesar == 90:
        print("segitiga siku-siku")
    else:
        print("segitiga lancip")