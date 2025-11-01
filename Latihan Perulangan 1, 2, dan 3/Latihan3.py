# latihan3.py
def main():
    saldo = 1_000_000  # saldo awal
    print("=== SIMULASI ATM SEDERHANA ===")
    while True:
        print("\nSaldo saat ini: Rp {:,.0f}".format(saldo))
        print("Pilihan:")
        print("1. Tarik tunai")
        print("2. Cek saldo")
        print("3. Keluar")
        pilihan = input("Pilih (1/2/3): ").strip()

        if pilihan == "1":
            try:
                jumlah = int(input("Masukkan jumlah tarik (kelipatan 1000): "))
            except ValueError:
                print("Masukkan angka yang valid.")
                continue
            if jumlah <= 0:
                print("Jumlah harus > 0.")
                continue
            if jumlah % 1000 != 0:
                print("Harus kelipatan 1000.")
                continue
            if jumlah > saldo:
                print("Saldo tidak cukup.")
                continue
            saldo -= jumlah
            print(f"Berhasil! Anda menarik Rp {jumlah:,.0f}. Saldo sisa Rp {saldo:,.0f}")
            if saldo == 0:
                print("Saldo habis. Terima kasih telah menggunakan ATM.")
                break
        elif pilihan == "2":
            print("Saldo anda: Rp {:,.0f}".format(saldo))
        elif pilihan == "3":
            print("Keluar. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main()
