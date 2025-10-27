import os

# Data admin
dataadmin = {
    'hatchu': {'password': 's2u', 'role': 'admin'}
}

# Data member {username, password (kontak), instrumen, harga, role}
daftarmember = {
    "carmen": {"password": "08123456789", "instrumen": "gitar", "harga": 750000, "role": "member"},
    "jiwoo": {"password": "0811112222", "instrumen": "piano", "harga": 1000000, "role": "member"},
    "juun": {'password': "0813334444", "instrumen": "gitar", "harga": 750000, "role": "member"}
}
statuslogin = False
useraktif = {"nama": "", "role": ""}

def hitungharga(instrumen):
    if instrumen == 'gitar':
        return 750000
    else:
        return 1000000

def carimember(keyword):
    hasil = []
    for nama, data in daftarmember.items():
        if keyword in nama or keyword in data['instrumen']:
            hasil.append((nama, data))
    return hasil

def userterdaftar():
    jumlah = len(daftarmember)
    return jumlah

def ambiluser():
    return useraktif["nama"]

def tampilkanheader(judul):
    os.system("cls")
    print("="*60)
    print(judul.center(60))
    print("="*60)

def tampilkanmember():
    print(f"\n{'Nama':<15} {'Kontak':<15} {'Instrumen':<15} {'Harga':<15}")
    print("-"*60)
    for nama, data in daftarmember.items():
        print(f"{nama:<15}{data['password']:<15}{data['instrumen']:<15}Rp {data['harga']:<15}")
    print("-"*60)

def tampilkanmenuadmin():
    os.system("cls")
    print("="*60)
    print("MENU ADMIN".center(60))
    print("="*60)
    print("1. Tambah Member")
    print("2. Tampilkan Member")
    print("3. Edit Member")
    print("4. Hapus Member")
    print("5. Logout")
    return input("Pilih opsi (1-5): ")

def tampilkanmenumember(namauser):
    os.system("cls")
    print("="*60)
    print(f"MENU MEMBER ({namauser})".center(60))
    print("="*60)
    print("1. Tampilkan Daftar Member")
    print("2. Cari Member")
    print("3. Logout")
    return input("Pilih (1-3): ")

programaktif = True

while programaktif:
    if not statuslogin:
        tampilkanheader("SELAMAT DATANG DI KURSUS MUSIK H2H")
        print("1. Login")
        print("2. Register")
        print("3. Logout")
        pilih = input("\nPilih opsi (1/2/3): ")
        
        if pilih == '1':
            tampilkanheader("LAMAN LOGIN")
            nama = input("Username: ")
            if nama not in dataadmin and nama not in daftarmember:
                print("Username tidak ditemukan!")
                input("Klik Enter untuk melanjutkan...")
                continue
            password = input("Password: ")
            if nama in dataadmin and password == dataadmin[nama]['password']:
                statuslogin = True
                userlogin = nama
                rolelogin = dataadmin[nama]['role']
                useraktif["nama"] = userlogin
                useraktif["role"] = rolelogin
                print("\nLogin berhasil sebagai", userlogin, "role:", rolelogin)
            elif nama in daftarmember and password == daftarmember[nama]['password']:
                statuslogin = True
                userlogin = nama
                rolelogin = daftarmember[nama]['role']
                useraktif["nama"] = userlogin
                useraktif["role"] = rolelogin
                print("\nLogin berhasil sebagai", userlogin, "role:", rolelogin)
            else:
                print("Password salah!")
            input("Klik Enter untuk melanjutkan...")
        
        elif pilih == '2':
            tampilkanheader("REGISTRASI AKUN")
            namabaru = input("Username: ")
            if namabaru in daftarmember or namabaru in dataadmin:
                print("Username sudah ada!")
                input("Klik Enter untuk melanjutkan...")
                continue
            passwordbaru = input("Password (kontak): ")
            if not passwordbaru.isdigit():
                print("Password tidak valid! Harus berupa angka.")
                input("Klik Enter untuk melanjutkan...")
            else:
                instrumen = input("Instrumen (gitar/piano): ")
                if instrumen == 'gitar':
                    daftarmember[namabaru] = {'password': passwordbaru, 'instrumen': instrumen, 'harga': 750000, 'role': 'member'}
                    print("PENDAFTARAN AKUN ANDA SUKSES")
                    input("Klik Enter untuk melanjutkan...")
                elif instrumen == 'piano':
                    daftarmember[namabaru] = {'password': passwordbaru, 'instrumen': instrumen, 'harga': 1000000, 'role': 'member'}
                    print("PENDAFTARAN AKUN ANDA SUKSES")
                    input("Klik Enter untuk melanjutkan...")
                else:
                    print("Instrumen tidak valid! Pilih gitar atau piano.")
                    input("Klik Enter untuk melanjutkan...")

        elif pilih == '3':
            programaktif = False
            print("\nTERIMA KASIH SUDAH BERKUNJUNG DI KURSUS MUSIK H2H.")
        else:
            print("Pilihan tidak valid!")
            input("Klik Enter untuk melanjutkan...")
    
    else:
        if useraktif["role"] == 'admin':
            pilihan = tampilkanmenuadmin()
            
            if pilihan == '1':
                tampilkanheader("Tambah Member")
                nama = input("Nama: ")
                if nama in daftarmember:
                    print("Username sudah ada!")
                    input("Klik Enter untuk melanjutkan...")
                else:
                    kontak = input("Kontak: ")
                    if not kontak.isdigit():
                        print("Kontak tidak valid! Harus angka.")
                        input("Klik Enter untuk melanjutkan...")
                    else:
                        instrumen = input("Instrumen (gitar/piano): ")
                        if instrumen == 'gitar':
                            daftarmember[nama] = {'password': kontak, 'instrumen': instrumen, 'harga': 750000, 'role': 'member'}
                            print("Member berhasil ditambahkan.")
                            input("Klik Enter untuk melanjutkan...")
                        elif instrumen == 'piano':
                            daftarmember[nama] = {'password': kontak, 'instrumen': instrumen, 'harga': 1000000, 'role': 'member'}
                            print("Member berhasil ditambahkan.")
                            input("Klik Enter untuk melanjutkan...")
                        else:
                            print("Instrumen tidak valid!")
                            input("Klik Enter untuk melanjutkan...")
            
            elif pilihan == '2':
                tampilkanheader("DAFTAR MEMBER")
                tampilkanmember()
                input("Klik Enter untuk melanjutkan...")
            
            elif pilihan == '3':
                tampilkanheader("EDIT MEMBER")
                tampilkanmember()
                namalama = input("\nMasukkan nama member: ")
                if namalama == "":
                    print("Nama tidak boleh kosong!")
                    input("Klik Enter untuk melanjutkan...")
                elif namalama not in daftarmember:
                    print("Nama tidak ditemukan!")
                    input("Klik Enter untuk melanjutkan...")
                else:
                    namabaru = input("Nama baru: ")
                    kontakbaru = input("Kontak baru: ")
                    if not kontakbaru.isdigit():
                        print("Kontak tidak valid! Harus angka.")
                        input("Klik Enter untuk melanjutkan...")
                    else:
                        instrumenbaru = input("Instrumen baru (gitar/piano): ")
                        if instrumenbaru == 'gitar':
                            if namabaru != namalama:
                                daftarmember.pop(namalama, None)
                            daftarmember[namabaru] = {'password': kontakbaru, 'instrumen': instrumenbaru, 'harga': 750000, 'role': 'member'}
                            print("Data berhasil diubah.")
                            input("Klik Enter untuk melanjutkan...")
                        elif instrumenbaru == 'piano':
                            if namabaru != namalama:
                                daftarmember.pop(namalama, None)
                            daftarmember[namabaru] = {'password': kontakbaru, 'instrumen': instrumenbaru, 'harga': 1000000, 'role': 'member'}
                            print("Data berhasil diubah.")
                            input("Klik Enter untuk melanjutkan...")
                        else:
                            print("Instrumen tidak valid!")
                            input("Klik Enter untuk melanjutkan...")

            elif pilihan == '4':
                try:
                    tampilkanheader("HAPUS MEMBER")
                    tampilkanmember()
                    namahapus = input("\nMasukkan nama member yang ingin dihapus: ")
                    if namahapus == "":
                        print("Nama tidak boleh kosong!")
                        input("Klik Enter untuk melanjutkan...")
                    elif namahapus not in daftarmember:
                        print("Nama tidak ditemukan!")
                        input("Klik Enter untuk melanjutkan...")
                    else:
                        daftarmember.pop(namahapus)
                        print(f"Member '{namahapus}' dihapus.")
                        input("Klik Enter untuk melanjutkan...")
                except KeyError:
                    print("Error: Data member tidak ditemukan!")
                    input("Klik Enter untuk melanjutkan...")

            elif pilihan == '5':
                statuslogin = False
                useraktif["nama"] = ""
                useraktif["role"] = ""
                print("Logout berhasil.")
                input("Klik Enter untuk melanjutkan...")
            else:
                print("Pilihan tidak valid!")
                input("Klik Enter untuk melanjutkan...")
        
        else: 
            namauser = useraktif["nama"]
            pilih = tampilkanmenumember(namauser)
            
            if pilih == '1':
                tampilkanheader("Daftar Member")
                print(f"{'Nama':<20} {'Kontak':<20} {'Instrumen':<20}")
                print("-"*60)
                for nama, data in daftarmember.items():
                    print(f"{nama:<20}{data['password']:<20}{data['instrumen']:<20}")
                input("Klik Enter untuk melanjutkan...")
            
            elif pilih == '2':
                tampilkanheader("CARI Member")
                cari = input("Cari nama atau instrumen: ")
                hasil = carimember(cari)
                if hasil:
                    for nama, data in hasil:
                        print(f"{nama:<20}{data['password']:<20}{data['instrumen']:<20}")
                else:
                    print("Tidak ditemukan!")
                input("Klik Enter untuk melanjutkan...")
            
            elif pilih == '3':
                statuslogin = False
                print("Logout berhasil.")
                input("Klik Enter untuk melanjutkan...")
            else:
                print("Pilihan tidak valid!")
                input("Klik Enter untuk melanjutkan...")