#Data pengguna
namapengguna = "Annisa Nur Raidah"
nimpengguna = 2509106078

#Biaya langganan
biayalangganan = 1500000

#Biaya admin
biayaadminpaketbronze = biayalangganan*(1/100)
biayaadminpaketsilver = biayalangganan*(3/100)
biayaadminpaketgold = biayalangganan*(5/100)
biayaadminpaketplatinum = biayalangganan*(7/100)

#Total harga
totalhargapaketbronze = biayalangganan+biayaadminpaketbronze
totalhargapaketsilver = biayalangganan+biayaadminpaketsilver
totalhargapaketgold = biayalangganan+biayaadminpaketgold
totalhargapaketplatinum = biayalangganan+biayaadminpaketplatinum

bronze = "bronze"
silver = "silver"
gold = "gold"
platinum = "platinum"

#Keuntungan
keuntunganpaketbronze = "akses dasar ke lagu-lagu populer"
keuntunganpaketsilver = "akses lagu premium dan playlist kustom"
keuntunganpaketgold =  "akses lagu premium, playlist kustom, dan mode offline"
keuntunganpaketplatinum = "akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis"

print ("==== Selamat datang di aplikasi streaming musik ====")
nama = input("Masukkan nama anda: ") 
if nama != namapengguna:
    print ("Error: Nama yang anda masukkan salah")
    print ("Login gagal")
    exit ()
else:
    print ("Nama yang anda masukkan benar")

nim = int(input("Masukkan nim anda: "))
if nim != nimpengguna:
    print ("Eror: NIM yang anda masukkan salah")
    print ("Login gagal")
    exit ()
else:
    print ("NIM yang anda masukkan benar")

if nama == namapengguna and nim == nimpengguna:
    print ("="*60)
    print ("\nLogin berhasil")
    print (f"Selamat datang {nama} dengan NIM {nim}")
    print ()
    print ("="*60)
    print ("\nPilihlah opsi pembayaran biaya langganan streaming musik: ")
    print ("\nPaket Bronze: Biaya administrasi 1%, akses dasar ke lagu-lagu populer")
    print ("Paket Silver: Biaya administrasi 3%, akses lagu premium dan playlist kustom")
    print ("Paket Gold: Biaya administrasi 5%, akses lagu premium, playlist kustom, dan mode offline")
    print ("Paket Platinum: Biaya administrasi 7%, akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")

    from tabulate import tabulate  
    tabel = (
        ("\nPaket Bronze", f"Rp {biayalangganan}", "1%", f"Rp {biayaadminpaketbronze}", f"Rp {totalhargapaketbronze}", f"{keuntunganpaketbronze}"),
        ("Paket Silver", f"Rp {biayalangganan}", "3%", f"Rp {biayaadminpaketsilver}", f"Rp {totalhargapaketsilver}", f"{keuntunganpaketsilver}"),
        ("Paket Gold", f"Rp {biayalangganan}", "5%", f"Rp {biayaadminpaketgold}", f"Rp {totalhargapaketgold}", f"{keuntunganpaketgold}"),
        ("Paket Platinum", f"Rp {biayalangganan}", "7%", f"Rp {biayaadminpaketplatinum}", f"Rp {totalhargapaketplatinum}", f"{keuntunganpaketplatinum}")
)

    print (tabulate(tabel,
    headers = ("Opsi paket", "Biaya langganan", "Biaya administrasi (%)", "Biaya administrasi (Rp)", "Total harga (Rp)", "Keuntungan"),
    tablefmt = "grid",
    colalign = ("left", "right", "center", "right", "right", "left")
))

    paket = input("\nMasukkan paket yang anda inginkan: ")
    if paket == bronze:
        print (f"\n{nama} membeli paket Bronze, maka {nama} harus membayar Rp {totalhargapaketbronze} dengan biaya administrasi 1%.")
        print ("Keuntungan: akses dasar ke lagu-lagu populer")
    elif paket == silver:
        print (f"\n{nama} membeli paket Silver, maka {nama} harus membayar Rp {totalhargapaketsilver} dengan biaya administrasi 3%.")
        print ("Keuntungan: akses lagu premium dan playlist kustom")
    elif paket == gold:
        print (f"\n{nama} membeli paket Gold, maka {nama} harus membayar Rp {totalhargapaketgold} dengan biaya administrasi 5%.")
        print ("Keuntungan: akses lagu premium, playlist kustom, dan mode offline")
    elif paket == platinum:
        print (f"\n{nama} membeli paket Platinum, maka {nama} harus membayar Rp {totalhargapaketplatinum} dengan biaya administrasi 7%.")
        print ("Keuntungan: akses semua fitur, playlist kustom, mode offline, dan konten eksklusif artis")
    else:
        print ("Pilihan paket yang anda inginkan tidak ada")
else:
    print ("Login gagal")