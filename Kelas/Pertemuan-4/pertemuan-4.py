for i in range (10, 1, -1):
    print(f'Perulangan ke {i}')

# print(f'Perulangan)

mahasiswa = ["anhap", "dapupu", 10, 102.54, "jarvis"]

for i in "mahasiswa":
    print(i)

for i in range(1, 10):
    for j in range(1, i+1):
        print("#", end="@")
    print("")

jawab = 'ya'
hitung = 0
while(jawab == 'ya'):
    hitung += 1
    jawab = input("Ulang lagi? ")
print(f"Total perulangan: {hitung}")

angka = [2, 5, 8, 12, 15, 7, 20]
print("Mencari angka pertama yang lebih besar dari 10...")
for n in angka:
    print(f"Sekarang memeriksa angka: {n}")
    if n > 10:
        print(f"Angka {n} lebih besar dari 10, Perulangan berhenti.")
        break
print("Program selesai.")

for i in range(1, 11):
    if i % 2 != 0:
        continue
        print(f"Angka genap ditemukan: {i}")
print("\nProgram selesai.")

while True:
    print("MENU")
    print("1. fitur 1")
    print("2. fitur 2")
    print("3. fitur 3")
    opsi = int(input("Masukkan opsi: "))
    if opsi == 1:
        print("1. Fitur 1")
    elif opsi == 2:
        print("2. Fitur 2")
    elif opsi == 3:
        break
    else:
        print("Pilihan invalid")