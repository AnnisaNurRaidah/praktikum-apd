print("=== WARUNG MAKAN NISA ===")

nama = input("Masukkan nama anda: ")
NIM = input("Masukkan NIM anda: ")
harga = float(input("Masukkan harga yang anda mau(tanpa pajak): Rp "))

pajakpecellele = harga*(5/100)
totalpecellele = harga+pajakpecellele

pajakmieayam = harga*(8/100)
totalmieayam = harga+pajakmieayam

pajaknasipadang = harga*(10/100)
totalnasipadang = harga+pajaknasipadang

print(f"\nSelamat datang {nama} dengan NIM {NIM} ingin membeli makanan seharga Rp {harga}")
print(f"Jika {nama} membeli Pecel Lele, maka {nama} harus membayar Rp {totalpecellele} setelah mendapat pajak 5%.")
print(f"Jika {nama} membeli Mie Ayam, maka {nama} harus membayar Rp {totalmieayam} setelah mendapat pajak 8%.")
print(f"Jika {nama} membeli Nasi Padang, maka {nama} harus membayar Rp {totalnasipadang} setelah mendapat pajak 10%.")


from tabulate import tabulate  
tabel = (
    ("Pecel Lele", f"Rp {harga}", "5%", f"Rp {pajakpecellele}", f"Rp {totalpecellele}"),
    ("Mie Ayam", f"Rp {harga}", "8%", f"Rp {pajakmieayam}", f"Rp {totalmieayam}"),
    ("Nasi Padang", f"Rp {harga}", "10%", f"Rp {pajaknasipadang}", f"Rp {totalnasipadang}")
)

print(tabulate(
    tabel,
    headers=("Menu", "Harga", "Pajak (%)", "Pajak (Rp)", "Total Bayar (Rp)"),
    tablefmt="grid"
))