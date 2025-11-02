from data import daftarmember
from prettytable import PrettyTable
import os

def tampilkanheader(judul):
    os.system("cls")
    print("="*50)
    print(judul.center(50))
    print("="*50)

def tampilkanmember():
    table = PrettyTable()
    table.field_names = ["Nama", "Kontak", "Instrumen", "Harga"]
    for nama, data in daftarmember.items():
        table.add_row([nama, data['password'], data['instrumen'], f"Rp {data['harga']:,}"])
    print(table)

def tampilkanmenuadmin():
    print("\nMENU ADMIN")
    print("=" * 30)
    print("1. Tambah Member")
    print("2. Tampilkan Member")
    print("3. Edit Member")
    print("4. Hapus Member")
    print("5. Logout")

def tampilkanmenumember():
    print("\nMENU MEMBER")
    print("=" * 30)
    print("1. Tampilkan Daftar Member")
    print("2. Cari Member")
    print("3. Logout")