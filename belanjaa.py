belanja = int(input("dapat diskon jika belanja= "))
if belanja == 100:
    bayar = belanja - (belanja*0,10) + 2
elif belanja == 200:
    bayar = belanja - (belanja*0,15) + 2
elif belanja > 250:
    bayar = belanja - (belanja*0,20) + 2
else:
    bayar = belanja+2
print("membayar :", bayar)