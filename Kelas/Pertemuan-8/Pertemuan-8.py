# num = int("42") 
# name = str(123) 
# data = list("abc") 
# data = dict(a=1, b=2) 
# print(type(num))

# listAngka = [1, 2, 2, 4, 6, 6]

# print (sorted(listAngka))

# a = "abc"
# print (len(a))
# if len == 0:
#     print ("data masih kosong")

# abs(-9) 
# max([1, 3, 7])
# min([1, 3, 7])
# round(3.14159,2)
# sum([1, 2, 3])

# for i, v in enumerate(['a', 'b']):
#     print(i, v)

# x = 42
# def fungsi():
#     x = 10
#     y = 20
#     z = 30
#     print(globals()['x']) # mendapatkan isi dari variabel x (global)
#     print(locals()['x']) # mendapatkan isi dari variabel x (lokal)
#     print(locals()) # {'x': 10, 'y': 20, 'z': 30}
# fungsi()

# pilihan = input("apakah kamu manusia? (ya/tidak)"). upper()

# if pilihan.lower == "YA":
#     print("terima kasih telah menggunakan program kami")
# elif pilihan.lower == "TIDAK":
#     print("program lanjut")
# else:
#     print("inputnya salah kocak")

# import math as m
# print(m.sqrt(16))
# print(m.factorial(4))

# import random
# # # print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4

# # pilih_acak = ["pisang", "rambutan", "manggis"]
# # acak = "apcb"
# # print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# # print(random.choice(acak)) # memilih 1 karakter acak pada string
# # memasukkan satu persatu nilai dari kumpulan_angka
# # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#     hasil += random.choice(kumpulan_angka)
# print(hasil)

# acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang
# berubah
# print(acak_kartu)

import inquirer

pertanyaan = [
    inquirer.List(
        'size',
        message="What size do you need?",
        choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
    ),
]
answer = inquirer.prompt(pertanyaan)
print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
print(answer['size'])