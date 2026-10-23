diskon = int(input("dapat diskon jika belanja= "))
if diskon == 100:
    print(0,10+2)
elif diskon == 200:
    print(0,15+2)
elif diskon > 250:
    print(0,20+2)
elif diskon != 100: 
    print("tidak dapat diskon", +2)
elif diskon != 200:
    print("tidak dapat diskon", +2)
elif diskon != 250:
    print("tidak dapat diskon", +2)
else:
    print(2)