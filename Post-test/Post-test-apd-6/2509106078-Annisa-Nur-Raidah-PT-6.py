import os

# Data admin {username, password, role}
dataadmin = {
    'hatchu': {'password': 's2u', 'role': 'admin'}
}

# Data member {username, password (kontak), instrumen, harga, role}
daftarmember = {
    "carmen": {"password": "08123456789", "instrumen": "gitar", "harga": 750000, "role": "member"},
    "jiwoo": {"password": "0811112222", "instrumen": "piano", "harga": 1000000, "role": "member"},
    "juun": {'password': "0813334444", "instrumen": "gitar", "harga": 750000, "role": "member"}
}

programaktif = True
statuslogin = False
namamember = ""
role = ""

while programaktif:
    if not statuslogin:
        os.system("cls")
        print("="*40)
        print("SELAMAT DATANG DI KURSUS MUSIK H2H".center(40))
        print("="*40)
        print("1. Login")
        print("2. Register")
        print("3. Logout")
        pilih = input("\nPilih opsi (1/2/3): ")
        
        if pilih == '1':
            os.system("cls")
            print("-"*50)
            print("LAMAN LOGIN".center(50))
            print("-"*50)
            nama = input("Username: ")
            if nama not in dataadmin and nama not in daftarmember:
                print("Username tidak ditemukan!")
                input("Klik Enter untuk melanjutkan...")
                continue
            password = input("Password: ")
            if nama in dataadmin and password == dataadmin[nama]['password']:
                statuslogin = True
                namamember = nama
                role = dataadmin[nama]['role']
                print("\nLogin berhasil sebagai", namamember, "role:", role)
            elif nama in daftarmember and password == daftarmember[nama]['password']:
                statuslogin = True
                namamember = nama
                role = daftarmember[nama]['role']
                print("\nLogin berhasil sebagai", namamember, "role:", role)
            else:
                print("Password salah!")
            input("Klik Enter untuk melanjutkan...")
        
        elif pilih == '2':
            os.system("cls")
            print("-"*40)
            print("REGISTRASI AKUN".center(40))
            print("-"*40)
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
                    harga = 750000
                    daftarmember[namabaru] = {'password': passwordbaru, 'instrumen': instrumen, 'harga': harga, 'role': 'member'}
                    print("PENDAFTARAN AKUN ANDA SUKSES")
                    input("Klik Enter untuk melanjutkan...")
                elif instrumen == 'piano':
                    harga = 1000000
                    daftarmember[namabaru] = {'password': passwordbaru, 'instrumen': instrumen, 'harga': harga, 'role': 'member'}
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
        if role == 'admin':
            os.system("cls")
            print("="*40)
            print("MENU ADMIN".center(40))
            print("="*40)
            print("1. Tambah Member")
            print("2. Tampilkan Member")
            print("3. Edit Member")
            print("4. Hapus Member")
            print("5. Logout")
            pilihan = input("Pilih opsi (1-5): ")
            
            if pilihan == '1':
                os.system("cls")
                print("="*30)
                print("Tambah Member".center(30))
                print("="*30)
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
                            harga = 750000
                            daftarmember[nama] = {'password': kontak, 'instrumen': instrumen, 'harga': harga, 'role': 'member'}
                            print("Member berhasil ditambahkan.")
                            input("Klik Enter untuk melanjutkan...")
                        elif instrumen == 'piano':
                            harga = 1000000
                            daftarmember[nama] = {'password': kontak, 'instrumen': instrumen, 'harga': harga, 'role': 'member'}
                            print("Member berhasil ditambahkan.")
                            input("Klik Enter untuk melanjutkan...")
                        else:
                            print("Instrumen tidak valid!")
                            input("Klik Enter untuk melanjutkan...")
            
            elif pilihan == '2':
                os.system("cls")
                print("="*60)
                print("DAFTAR MEMBER".center(60))
                print("="*60)
                print(f"\n{'Nama':<15} {'Kontak':<15} {'Instrumen':<15} {'harga':<15}")
                print("-"*60)
                for nama, data in daftarmember.items():
                    print(f"{nama:<15}{data['password']:<20}{data['instrumen']:<15}Rp {data['harga']}")
                    print("-"*60)
                input("Klik Enter untuk melanjutkan...")
            
            elif pilihan == '3':
                os.system("cls")
                print("="*60)
                print("EDIT MEMBER".center(60))
                print("="*60)
                print(f"\n{'Nama':<15} {'Kontak':<15} {'Instrumen':<15} {'harga':<15}")
                for nama, data in daftarmember.items():
                    print(f"\n{nama:<15}{data['password']:<20}{data['instrumen']:<15}Rp {data['harga']}")
                    print("-"*60)
                namalama = input("\nMasukkan nama member: ")
                if namalama == "":
                    print("Nama tidak boleh kosong!")
                    input("Klik Enter untuk melanjutkan...")
                elif namalama not in daftarmember:
                    print("Nama tidak ditemukan!")
                    input("Klik Enter untuk melanjutkan...")
                else:
                    namabaru = input("Nama baru: ")
                    if namabaru in daftarmember or namabaru in dataadmin:
                        print("Nama sudah ada!")
                        input("Klik Enter untuk melanjutkan...")
                    else:
                        kontakbaru = input("Kontak baru: ")
                        if not kontakbaru.isdigit():
                            print("Kontak tidak valid! Harus angka.")
                            input("Klik Enter untuk melanjutkan...")
                        else:
                            instrumenbaru = input("Instrumen baru (gitar/piano): ")
                            if instrumenbaru == 'gitar':
                                hargabaru = 750000
                                if namabaru != namalama:
                                    daftarmember.pop(namalama, None)
                                daftarmember[namabaru] = {'password': kontakbaru, 'instrumen': instrumenbaru, 'harga': hargabaru, 'role': 'member'}
                                print("Data berhasil diubah.")
                                input("Klik Enter untuk melanjutkan...")
                            elif instrumenbaru == 'piano':
                                hargabaru = 1000000
                                if namabaru != namalama:
                                    daftarmember.pop(namalama, None)
                                daftarmember[namabaru] = {'password': kontakbaru, 'instrumen': instrumenbaru, 'harga': hargabaru, 'role': 'member'}
                                print("Data berhasil diubah.")
                                input("Klik Enter untuk melanjutkan...")
                            else:
                                print("Instrumen tidak valid!")
                                input("Klik Enter untuk melanjutkan...")                        

            elif pilihan == '4':
                os.system("cls")
                print("="*60)
                print("HAPUS MEMBER".center(60))
                print("="*60)
                print(f"\n{'Nama':<15} {'Kontak':<15} {'Instrumen':<15} {'harga':<15}")
                for nama, data in daftarmember.items():
                    print(f"\n{nama:<15}{data['password']:<20}{data['instrumen']:<15}Rp {data['harga']}")
                    print("-"*60)
                namahapus = input("\nMasukkan nama member yang ingin dihapus: ")
                if namahapus not in daftarmember:
                    print("Nama tidak ditemukan!")
                    input("Klik Enter untuk melanjutkan...")
                else:
                    daftarmember.pop(namahapus)
                    print(f"Member '{namahapus}' dihapus.")
                    input("Klik Enter untuk melanjutkan...")

            elif pilihan == '5':
                statuslogin = False
                namamember = ""
                role = ""
                print("Logout berhasil.")
                input("Klik Enter untuk melanjutkan...")
            else:
                print("Pilihan tidak valid!")
                input("Klik Enter untuk melanjutkan...")
        
        elif role == 'member':
            os.system("cls")
            print("="*30)
            print(("MENU MEMBER (" + namamember + ")").center(30))
            print("="*30)
            print("1. Tampilkan Daftar Member")
            print("2. Cari Peserta")
            print("3. Logout")
            pilih = input("Pilih (1-3): ")
            
            if pilih == '1':
                os.system("cls")
                print("="*50)
                print("Daftar Peserta".center(50))
                print("="*50)
                print(f"{'Nama':<15} {'Kontak':<15} {'Instrumen':<15}")
                print("-"*50)
                for nama, data in daftarmember.items():
                    print(f"{nama:<15}{data['password']:<15}{data['instrumen']}")
                input("Klik Enter untuk melanjutkan...")
            
            elif pilih == '2':
                os.system("cls")
                print("="*40)
                print("CARI Member".center(40))
                print("="*40)
                pencarian = input("Cari nama atau instrumen: ")
                pencarian = False
                for nama, data in daftarmember.items():
                    if pencarian in nama or pencarian in data['instrumen']:
                        print(f"{nama:<15}{data['password']:<15}{data['instrumen']}")
                        pencarian = True
                if not pencarian:
                    print("Tidak ditemukan!")
                input("Klik Enter untuk melanjutkan...")
            
            elif pilih == '3':
                statuslogin = False
                namamember = ""
                role = ""
                print("Logout berhasil.")
                input("Klik Enter untuk melanjutkan...")
            else:
                print("Pilihan tidak valid!")
                input("Klik Enter untuk melanjutkan...")
        else:
            print("Akun tidak terdaftar!")
            statuslogin = False