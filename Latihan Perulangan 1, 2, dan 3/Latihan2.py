# latihan2.py
# Hitung total keuntungan selama 8 bulan
def main():
    modal_awal = 100_000_000  # 100 juta
    # Daftar persentase per bulan (dalam desimal)
    monthly_rates = [
        0.00,  # bulan 1
        0.00,  # bulan 2
        0.01,  # bulan 3
        0.01,  # bulan 4 (diasumsikan tetap 1%)
        0.05,  # bulan 5
        0.05,  # bulan 6
        0.05,  # bulan 7
        0.03   # bulan 8 (5% - 2% = 3%)
    ]

    total_keuntungan = 0.0
    saldo = modal_awal

    print(f"Modal awal: Rp {modal_awal:,.0f}\n")
    for bulan, rate in enumerate(monthly_rates, start=1):
        keuntungan_bulan = modal_awal * rate  # menghitung berdasarkan modal awal
        total_keuntungan += keuntungan_bulan
        # jika ingin menampilkan saldo jika di-reinvest:
        saldo += keuntungan_bulan
        print(f"Bulan {bulan}: rate={rate*100:.2f}% -> keuntungan = Rp {keuntungan_bulan:,.0f}")

    print("\nTotal keuntungan 8 bulan: Rp {:,.0f}".format(total_keuntungan))
    print("Saldo akhir jika keuntungan direinvestasikan: Rp {:,.0f}".format(saldo))

if __name__ == "__main__":
    main()
