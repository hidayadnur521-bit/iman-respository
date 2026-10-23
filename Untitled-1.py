hasil = int(input("jika saya lulus: "))
if hasil == 100:
    print("lulus")
elif hasil >= 80:
    print("mengulang")
else:
    print("tidak lulus")

diskon = int(input("dapat diskon jika belanja= "))
if diskon == 100:
    print(10/100+2)