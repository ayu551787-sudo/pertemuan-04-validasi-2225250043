x = int(input("Masukan bilangan bulat: "))
if x < 0:
    print("bilangan negatif")
elif x == 0:
    print("nol")
elif x % 2 == 0:
    print("bilangan positif genap")
else:
    print("bilangan positif ganjil")