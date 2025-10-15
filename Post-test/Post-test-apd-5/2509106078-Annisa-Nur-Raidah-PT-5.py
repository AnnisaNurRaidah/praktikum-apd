import os

# Data admin (username, password, role)
dataadmin = [
    ('hatchu', 's2u', 'admin')
    ]
# Data member (username, password (kontak), instrumen, harga, role)
daftarmember = [
    ('carmen', '08123456789', 'gitar', 750000, 'member'),
    ('jiwoo', '0811112222', 'piano', 1000000, 'member'),
    ('juun', '0813334444', 'gitar', 750000, 'member')
    ]

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
            password = input("Password: ")
            for admin in dataadmin:
                if nama == admin[0] and password == admin[1]:
                    statuslogin = True
                    namamember = admin[0]
                    role = 'admin'
                    break
            for member in daftarmember:
                if nama == member[0] and password == member[1]:
                    statuslogin = True
                    namamember = member[0]
                    role = 'member'
                    break
            if statuslogin:
                print(f"\nLogin berhasil sebagai {namamember} ({role})")
                input("Klik Enter untuk melanjutkan...")
            else:
                print("Username atau Password salah!")
                input("Klik Enter untuk melanjutkan...")
        elif pilih == '2':
            os.system("cls")
            print("-"*40)
            print("REGISTRASI AKUN".center(40))
            print("-"*40)
            namabaru = input("Username: ")
            passwordbaru = input("Password (kontak): ")
            instrumen = input("Instrumen (gitar/piano): ")
            if instrumen == 'gitar':
                harga = 750000
            else:
                harga = 1000000
            daftarmember.append((namabaru, passwordbaru, instrumen, harga, 'member'))
            print("PENDAFTARAN AKUN ANDA SUKSES")
            input("Klik Enter untuk melanjutkan...")
        else: 
            pilih == '3'
            programaktif = False
            print("\nTERIMA KASIH SUDAH BERKUNJUNG DI KURSUS MUSIK H2H.")
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
                kontak = input("Kontak: ")
                instrumen = input("Instrumen (gitar/piano): ")
                if instrumen == 'gitar':
                    harga = 750000
                else:
                    harga = 1000000
                daftarmember.append((nama, kontak, instrumen, harga, 'member'))
                print("Member berhasil ditambahkan.")
                input("Klik Enter untuk melanjutkan...")
            elif pilihan == '2':
                os.system("cls")
                print("="*60)
                print("DAFTAR MEMBER".center(60))
                print("="*60)
                print(f"\n{'Nama':<15} {'Kontak':<15} {'Instrumen':<15} {'Harga':<15}")
                print("-"*60)
                for member in daftarmember:                    
                    print(f"{member[0]:<15} {member[1]:<15} {member[2]:<15} Rp {member[3]:<15,}")
                    print("-"*60)
                input("Klik Enter untuk melanjutkan...")
            elif pilihan == '3':
                os.system("cls")
                print("="*60)
                print("EDIT MEMBER".center(50))
                print("="*60)
                nomor = 1
                print(f"\n{'nomor':<10} {'Nama':<10} {'Kontak':<15} {'Instrumen':<10} {'Harga':<10}")
                print("-"*60)
                for member in daftarmember:                    
                    print(f"{nomor:<10} {member[0]:<10} {member[1]:<15} {member[2]:<10} Rp {member[3]:<10,}")
                    nomor = nomor + 1
                    jumlah = 0
                for member in daftarmember:
                    jumlah = jumlah + 1
                pilih = int(input("\nPilih nomor member: ")) - 1
                namabaru = input("Nama baru: ")
                kontakbaru = input("Kontak baru: ")
                instrumenbaru = input("Instrumen baru: ")
                if instrumenbaru == 'gitar':
                    hargabaru = 750000
                else:
                    hargabaru = 1000000
                daftarmember[pilih] = (namabaru, kontakbaru, instrumenbaru, hargabaru, 'member')
                print("Data berhasil diubah.")
                input("Klik Enter untuk melanjutkan...")
            elif pilihan == '4':
                os.system("cls")
                print("="*40)
                print("HAPUS MEMBER".center(40))
                print("="*40)
                nomor = 1
                for member in daftarmember:
                    print(f"{nomor:<10} {member[0]:<10} {member[2]:<10} Rp {member[3]:<10,}")
                    nomor = nomor + 1
                    jumlah = 0
                for member in daftarmember:
                    jumlah = jumlah + 1
                pilihhapus = int(input("Pilih nomor member: ")) - 1
                daftarmember.pop(pilihhapus)
                print("Member dihapus.")
                input("Klik Enter untuk melanjutkan...")
            else: 
                pilihan == '5'
                statuslogin = False
                namamember = ""
                role = ""
                print("Logout berhasil.")
                input("Klik Enter untuk melanjutkan...")
        elif role == 'member':
            os.system("cls")
            print("="*30)
            print(f"MENU MEMBER ({namamember})".center(30))
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
                print(member[0],        member[1],      member[2])
                print("-"*50)
                for member in daftarmember:
                    print(member[0],    member[1],      member[2])
                input("Klik Enter untuk melanjutkan...")
            elif pilih == '2':
                os.system("cls")
                print("="*40)
                print("CARI Member".center(40))
                print("="*40)
                pencarian = input("Cari nama atau instrumen: ")
                for member in daftarmember:
                    if pencarian in member[0] or pencarian in member[2]:
                        print("-"*40)
                        print(member[0],    member[1],      member[2])
                input("Klik Enter untuk melanjutkan...")
            else: 
                pilih == '3'
                statuslogin = False
                namamember = ""
                role = ""
                print("Logout berhasil.")
                input("Klik Enter untuk melanjutkan...")
        else:
            print("Akun tidak terdaftar!")