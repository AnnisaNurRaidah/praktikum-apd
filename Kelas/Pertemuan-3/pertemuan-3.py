totalbelanja = int(input("Masukkan total belanja"))

if (totalbelanja > 100000):
    print("Dapat diskon 20%")
elif (totalbelanja >50000):
    print("Dapat diskon 10%")
else:
    print("Tidak dapat diskon")