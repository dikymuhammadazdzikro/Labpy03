from random import random

n = int(input("Masukkan jumlah bilangan: "))
count = 0

while count < n:
    a = random()
    if a < 0.5:
        count += 1
        print(f"Bilangan ke-{count}: {a}")

print("Selesai.")

