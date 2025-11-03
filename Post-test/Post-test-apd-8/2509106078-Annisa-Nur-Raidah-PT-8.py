from data import dataadmin, daftarmember, carimember, hitungharga, userterdaftar
from menu import tampilkanheader, tampilkanmember, tampilkanmenuadmin, tampilkanmenumember
from prettytable import PrettyTable
import inquirer
import os

statuslogin = False
useraktif = {"nama": "", "role": ""}

def ambiluser():
    return useraktif["nama"]

programaktif = True

while programaktif:
    if not statuslogin:
        tampilkanheader("SELAMAT DATANG DI KURSUS MUSIK H2H")
        questions = [
        inquirer.List('menu',
            message="Pilih opsi",
            choices=['Login', 'Register', 'Logout'])]
        opsimenu = {'Login': '1', 'Register': '2', 'Logout': '3'}
        pilih = opsimenu[inquirer.prompt(questions)['menu']]
        
        if pilih == '1':
            try:
                tampilkanheader("LAMAN LOGIN")
                nama = input("Username: ")
                if nama not in dataadmin and nama not in daftarmember:
                    raise ValueError("Username tidak ditemukan!")
                password = input("Password: ")
                if nama in dataadmin and password == dataadmin[nama]['password']:
                    statuslogin = True
                    userlogin = nama
                    rolelogin = dataadmin[nama]['role']
                    useraktif["nama"] = userlogin
                    useraktif["role"] = rolelogin
                    print("\nLogin berhasil sebagai", userlogin, "role:", rolelogin)
                    input("Klik Enter untuk melanjutkan...")
                elif nama in daftarmember and password == daftarmember[nama]['password']:
                    statuslogin = True
                    userlogin = nama
                    rolelogin = daftarmember[nama]['role']
                    useraktif["nama"] = userlogin
                    useraktif["role"] = rolelogin
                    print("\nLogin berhasil sebagai", userlogin, "role:", rolelogin)
                    input("Klik Enter untuk melanjutkan...")
                else:
                    raise ValueError("Password salah!")
            except ValueError as e:
                print(f"Error: {e}")
                input("Klik Enter untuk melanjutkan...")
            except KeyError:
                print("Error: Data pengguna tidak valid!")
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

        else:
            programaktif = False
            print("\nTERIMA KASIH SUDAH BERKUNJUNG DI KURSUS MUSIK H2H.")
    
    else:
        if useraktif["role"] == 'admin':
            tampilkanheader(f"MENU ADMIN - {useraktif['nama']}")
            questions = [
            inquirer.List('admin_menu',
                message="Pilih menu admin",
                choices=['Tambah Member', 'Tampilkan Member', 'Edit Member', 'Hapus Member', 'Logout'])]
            menu_map = {
                'Tambah Member': '1',
                'Tampilkan Member': '2',
                'Edit Member': '3',
                'Hapus Member': '4',
                'Logout': '5'}
            pilihan = menu_map[inquirer.prompt(questions)['admin_menu']]
            
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
                        raise ValueError("Nama tidak boleh kosong!")
                    elif namahapus not in daftarmember:
                        raise KeyError("Nama tidak ditemukan!")
                    else:
                        daftarmember.pop(namahapus)
                        print(f"Member '{namahapus}' dihapus.")
                        input("Klik Enter untuk melanjutkan...")
                except ValueError as e:
                    print(f"Error: {e}")
                    input("Klik Enter untuk melanjutkan...")
                except KeyError as e:
                    print(f"Error: {e}")
                    input("Klik Enter untuk melanjutkan...")

            else:
                statuslogin = False
                useraktif["nama"] = ""
                useraktif["role"] = ""
                print("Logout berhasil.")
                input("Klik Enter untuk melanjutkan...")
        
        else: 
            namauser = useraktif["nama"]
            tampilkanheader(f"MENU MEMBER - {namauser}")
            questions = [
            inquirer.List('member_menu',
                message=f"Pilih menu",
                choices=['Tampilkan Daftar Member', 'Cari Member', 'Logout'])]
            menu_map = {
            'Tampilkan Daftar Member': '1',
            'Cari Member': '2',
            'Logout': '3'}
            pilih = menu_map[inquirer.prompt(questions)['member_menu']]
            
            if pilih == '1':
                tampilkanheader("DAFTAR MEMBER")
                if len(daftarmember) == 0:
                    print("Belum ada member terdaftar.")
                else:
                    tampilkanmember()
                input("\nTekan Enter untuk melanjutkan...")
            
            elif pilih == '2':
                tampilkanheader("CARI MEMBER")
                cari = input("Cari nama atau instrumen: ")
                hasil = carimember(cari)
                
                if hasil:
                    print(f"\nDitemukan {len(hasil)} member:")
                    table = PrettyTable()
                    table.field_names = ["Nama", "Kontak", "Instrumen", "Harga"]
                    for nama, data in hasil:
                        table.add_row([
                            nama, 
                            data['password'], 
                            data['instrumen'], 
                            f"Rp {data['harga']:,}"])
                    print(table)
                else:
                    print("\nTidak ditemukan!")
                input("\nTekan Enter untuk melanjutkan...")
            
            else:
                statuslogin = False
                useraktif["nama"] = ""
                useraktif["role"] = ""
                print("\nLogout berhasil.")
                input("\nTekan Enter untuk melanjutkan...")