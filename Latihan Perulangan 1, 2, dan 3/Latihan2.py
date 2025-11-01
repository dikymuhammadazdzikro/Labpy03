modal = 100_000_000
rate = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]
total = 0

for i, r in enumerate(rate, 1):
    laba = modal * r
    total += laba
    print(f"Bulan {i}: laba = Rp {laba:,.0f}")

print(f"Total keuntungan: Rp {total:,.0f}")

