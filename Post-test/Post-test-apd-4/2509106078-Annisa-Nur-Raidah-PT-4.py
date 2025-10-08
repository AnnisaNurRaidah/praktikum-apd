# Nama dan Password yang benar
nama = "Annisa Nur Raidah"
nim = "2509106078"

bataspercobaan = 3
percobaan = 0
loginsukses = False

print("=" * 60)
print(" " * 15 + "BIOSKOP XXO")
print(" " * 10 + "Sistem Pembelian Tiket Online")
print("=" * 60)

print("\n--- LOGIN SISTEM ---")
print("Silakan login untuk melanjutkan")
print("-" * 40)

while percobaan < bataspercobaan:
    print(f"\nPercobaan ke-{percobaan + 1} dari {bataspercobaan}")
    username = input("Username: ")
    password = input("Password: ")
    
    if username == nama and password == nim:
        print("\nLOGIN BERHASIL!")
        print(f"Selamat datang, {nama}!")
        loginsukses = True
        break
    else:
        percobaan = percobaan + 1
        if percobaan < bataspercobaan:
            print("Login gagal! Username atau Password salah.")
            print(f"Sisa percobaan: {bataspercobaan - percobaan}")
        else:
            print("\nLOGIN GAGAL!")
            print("Anda telah melebihi batas percobaan login.")

if not loginsukses:
    print("\nProgram berhenti.")
else:
    while True:
        print("\n" + "=" * 60)
        print(" " * 15 + "MENU PEMBELIAN TIKET")
        print("=" * 60)
        print("1. Tiket Reguler  : Rp 50.000")
        print("2. Tiket VIP      : Rp 100.000")
        print("3. Tiket VVIP     : Rp 150.000")
        print("4. Keluar")
        print("-" * 60)
        
        pilihan = input("Pilih jenis tiket (1-4): ")
        
        if pilihan == "1" or pilihan == "2" or pilihan == "3":
            if pilihan == "1":
                jenistiket = "Reguler"
                hargapertiket = 50000
            elif pilihan == "2":
                jenistiket = "VIP"
                hargapertiket = 100000
            else:
                jenistiket = "VVIP"
                hargapertiket = 150000
            
            print(f"\nAnda memilih: Tiket {jenistiket}")
            print(f"Harga per tiket: Rp {hargapertiket:}")
            
            jumlahtiket = False
            while not jumlahtiket:
                jumlahtiket = input("Masukkan jumlah tiket: ")
                jumlahtiket = int(jumlahtiket)
                if jumlahtiket > 0:
                    jumlahtiket_valid = True
                else:
                    print("Error: Jumlah tiket harus lebih dari 0!")
            
            totalbayar = 0
            for i in range(jumlahtiket):
                totalbayar = totalbayar + hargapertiket
            
            totalsebelumdiskon = totalbayar
            persendiskon = 0
            dapatposter = False
            
            if totalbayar >= 300000:
                persendiskon = 12
            elif totalbayar >= 200000:
                persendiskon = 8
            elif totalbayar >= 150000:
                dapatposter = True
            
            if persendiskon > 0:
                diskon = totalbayar * persendiskon / 100
                totalbayar = totalbayar - diskon
            else:
                diskon = 0
            
            print("\n" + "=" * 60)
            print(" " * 20 + "STRUK PEMBELIAN")
            print("=" * 60)
            print(f"Nama Pembeli            : {nama}")
            print(f"Jenis Tiket             : {jenistiket}")
            print(f"Harga per Tiket         : Rp {hargapertiket:}")
            print(f"Jumlah Tiket            : {jumlahtiket}")
            print("-" * 60)
            print(f"Harga sebelum diskon    : Rp {totalsebelumdiskon:}")
            
            if persendiskon > 0:
                print(f"Diskon ({persendiskon}%)            : Rp {diskon:}")
                print("-" * 60)
                print(f"TOTAL BAYAR             : Rp {totalbayar:}")
                print("=" * 60)
                print(f"Selamat! Anda mendapat diskon {persendiskon}%!")
            elif dapatposter:
                print("-" * 60)
                print(f"TOTAL BAYAR             : Rp {totalbayar:}")
                print("=" * 60)
                print("Selamat! Anda mendapat Poster Film Eksklusif!")
            else:
                print("-" * 60)
                print(f"TOTAL BAYAR             : Rp {totalbayar:}")
                print("=" * 60)
            
            print("\nTerima kasih atas pembelian Anda!")
            print("Selamat menonton!")
            print("=" * 60)
            
            input("\nTekan Enter untuk kembali ke menu...")
            
        elif pilihan == "4":
            print("\n" + "=" * 60)
            print("Terima kasih telah menggunakan layanan kami!")
            print("Sampai jumpa di Bioskop XXO!")
            print("=" * 60)
            break 
        else:
            print("\nError: Pilihan tidak valid! Pilih angka 1-4.")
            input("Tekan Enter untuk mencoba lagi...")