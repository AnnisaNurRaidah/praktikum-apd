# def perkenalan ():
#     print("haloo, aku nisa")
#     print("aku sedang belajar apd")
# perkenalan()

#return itu fungsi, selain itu prosedur. fungsinya untuk mengembalikan nilai yang diiput kedalam di menu

# def menu():
#     print("=== Menu Utama ===")
#     print("1. Tambah Data")
#     print("2. Hapus Data")
#     print("3. Tampilkan Data")
#     print("4. Keluar")
#     pilihan = input("Pilih menu (1-4): ")
#     return pilihan

# def tambah_data():
#     print("Menambahkan data")
#     print("Data berhasil ditambahkan")
    
# def hapus_data():
#     print("Menghapus data")
#     print("Data berhasil dihapus")

# def tampilkan_data():
#     print("Menampilkan data")
#     print("Data ditampilkan")

# while True:
#     pilihan = menu()
#     if pilihan == '1':
#         tambah_data()
#     elif pilihan == '2':
#         hapus_data()
#     elif pilihan == '3':
#         tampilkan_data()
#     elif pilihan == '4':
#         print("Keluar dari program")
#         break
#     else:
#         print("Pilihan tidak valid, silakan coba lagi.")

# def salam():
#     print("Halo, Ridho")
# def kali():
#     X = 5*5
#     print(X)

# salam()
# salam()
# salam()
# kali()
# kali()
# kali()

# def nama_fungsi(parameter):
#     print(parameter)
#     nama_fungsi("Selamat Pagi")

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("luas persegi panjang adalah", luas)

# luas_persegi_panjang(4, 5, 10)

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# print ("Luas persegi :", luas_persegi(8))

# def luaspersegipanjang(panjang, lebar):
#     luas = panjang * lebar
#     print("luaspersegi panjang adalah", luas)

# nama = "nisa"       #global, bisa dipakai di berbagai fungsi

# def salam():           #lokal
#     nama = "nica"
#     print ("halo", nama)

# print(nama)
# salam()

# def tambah(a, b):
#     return a - b

# tamabahlagi = tambah(3, 4)
# print(tamabahlagi)

# tamabahlagi -= 10
# print(tamabahlagi)

# def luaspersegi (s):
#     c = s * s
#     return c

# print (luaspersegi(6))

# def luaspersegi():
#     sisi = int(input("masukkan sisi: "))
#     luas = sisi * sisi
#     return luas

# s = int(input("masukkan sisi: "))
# print(luaspersegi(5.5))

# angka = int(input('Masukkan Angka : '))
# print(angka)

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else :
#     print(f'Angka yang kamu input : {angka}')

# try:
#     angka = int(input('Masukkan Angka : '))
# except ValueError:
#     print('input yang anda masukkan bukan Integer (angka)')
# else :
#     print(f'Angka yang kamu input : {angka}')
# finally :
#     print('Blok Try Selesai')

try:
    angka = input('Username yang diinginkan : ')
    if angka < 0:
        raise ValueError('Nama Minimal Memiliki 5 karakter')
except ValueError as e:
    print(valu)