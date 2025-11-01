saldo = 1_000_000
while True:
    print(f"\nSaldo: Rp {saldo:,.0f}")
    print("1. Tarik tunai\n2. Cek saldo\n3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        tarik = int(input("Jumlah tarik: "))
        if tarik > saldo or tarik <= 0 or tarik % 1000 != 0:
            print("Jumlah tidak valid.")
        else:
            saldo -= tarik
            print(f"Berhasil tarik Rp {tarik:,.0f}")
            if saldo == 0:
                print("Saldo habis.")
                break
    elif pilih == "2":
        continue
    elif pilih == "3":
        print("Terima kasih.")
        break
    else:
        print("Pilihan salah.")

