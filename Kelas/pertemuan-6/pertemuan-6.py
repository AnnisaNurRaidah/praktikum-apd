# nama = set ['dapupu', 'nisa', 'jiwoo']
# print(nama[1])

# buah = {"apel", "jeruk", "mangga", "apel"}
# print(buah)

# angka_ganjil = {1, 3, 5, 7, 9}
# for angka in angka_ganjil:
#     print(angka)

# print("menambahkan angka 11")
# angka_ganjil.add(11)

# angka_ganjil.remove(15)
# angka_ganjil.discard(15)
# print(angka_ganjil)

# set_A = {1, 2, {3, 4}}

# Daftar_buku = {
#     "Buku1" : "Bumi Manusia",
#     "Buku2" : "Laut Bercerita"
# }
# print(Daftar_buku["Buku1"]) 
# print(Daftar_buku)
# print(Daftar_buku.keys)
# for key in Daftar_buku.keys():
#     print(key)

# for value in Daftar_buku.values():
#     print(value)

# Biodata = {
#     "Nama" : "Ananda Daffa Harahap",
#     "NIM" : 2409106050,
#     "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
#     "Mahasiswa_Aktif" : True,
#     "Social Media" : {"Instagram" : "daffahrhap"
#     }
# }
# print(Biodata)

# list_mahasiswa = dict(nama="nisa", jurusan="informatika")
# print(list_mahasiswa)

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data", "algoritmaa", "jaringan komputer"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {"Instagram" : "daffahrhap"
# }
# }

# for i,j in Biodata.items:
#     print(f"{i} : {j}")

# print(f"nama saya adalah {Biodata["Nama"]}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")
# print(f"nama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("KRS")[1:5:3])

# Nilai = {
# "Matematika": 80,
# "B. Indonesia": 90,
# "B. Inggris": 81,
# "Kimia": 78,
# "Fisika": 80
# }
# Tanpa menggunakan items()
# for i in Nilai:
#     print(i)
    
# print("") # pemisah
# Menggunakan items()
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")

# Film = {
#     "Avenger Endgame" : "Action",
#     "Sherlock Holmes" : "Mystery",
#     "The Conjuring" : "Horror"}
# print(Film)

# Film["The Conjuring"] = "Comedy"
# Film.update({"Hours" : "Thriller"})
# print(Film)
# Film["Godzilla"] = "Action"

# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# print(Film)
# Film["Sherlock Holmes"] = "Action"
# Film.update({"The Conjuring" : "Tragedy"})
# print(Film)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print(data)
# del data["Nama"]
# print(data)
# print(data.get("Nama"))

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print(data)
# cache = data.pop("Nama")
# print(data)
# print(data.get("Nama"))
# print(cache)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print(data)
# data.clear()
# print(data)

# data = {
# "Nama" : "Daffa",
# "Umur" : 19,
# "Jurusan" : "Informatika"
# }
# print("Jumlah Data = ", len(data))

# buku = {
# "Buku1" : "Bumi Manusia",
# "Buku2" : "Laut Bercerita"
# }
# pinjam = buku.copy()
# print("Dictionary yang telah disalin : ", pinjam)

# Musik = {
# "The Chainsmoker" : ["All we Know", "The Paris"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
#     print("")