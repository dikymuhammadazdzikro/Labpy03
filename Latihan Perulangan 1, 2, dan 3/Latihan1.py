# latihan1.py
# Menampilkan n bilangan acak yang < 0.5
from random import random

def main():
    try:
        n = int(input("Masukkan jumlah bilangan (n): "))
        if n <= 0:
            print("Masukkan bilangan > 0.")
            return
    except ValueError:
        print("Masukkan angka bulat.")
        return

    count = 0
    hasil = []
    # Gunakan while untuk loop sampai kita mengumpulkan n angka < 0.5
    while count < n:
        # di setiap iterasi while kita bisa menghasilkan beberapa bilangan (contoh pakai for)
        for _ in range(1):  # satu perulangan for — bisa diubah jika mau generate batch
            a = random()
            if a < 0.5:
                hasil.append(a)
                count += 1
                print(f"Bilangan ke-{count}: {a}")
            # jika sudah cukup, break dari for
            if count >= n:
                break

    print("Selesai. Total bilangan yang dihasilkan:", len(hasil))

if __name__ == "__main__":
    main()
