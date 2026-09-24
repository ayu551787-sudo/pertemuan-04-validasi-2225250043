sudut = float(input("besar sudut dalam derajat: "))
if sudut <= 0 or sudut >= 180:
    print("masukan ditolak: sudut harus lebih dari 0 dan kurang dari 180.")
elif sudut < 90:
    print("sudut lancip")
elif sudut == 90:
    print("sudut siku-siku")
else:
    print("sudut tumpul")