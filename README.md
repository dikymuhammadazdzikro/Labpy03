# LabPy03 - Perulangan (Praktikum 3)

## Isi repositori
- `latihan1.py` : Menghasilkan n bilangan acak < 0.5 (n input runtime). Menggunakan kombinasi while + for.
- `latihan2.py` : Menghitung total keuntungan usaha selama 8 bulan berdasarkan perubahan persentase per bulan.
- `latihan3.py` : Simulasi mesin ATM sederhana (saldo awal Rp 1.000.000).

## Algoritma singkat
### latihan1.py
1. Minta input n (jumlah bilangan).
2. Inisialisasi counter.
3. Loop `while` sampai counter == n:
   - Dalam loop gunakan `for` untuk menghasilkan bilangan acak.
   - Jika bilangan < 0.5, tampilkan dan tambah counter.
4. Selesai.

### latihan2.py
1. Tetapkan modal awal Rp 100.000.000.
2. Tentukan daftar rate per bulan: [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03].
3. Hitung keuntungan tiap bulan = modal_awal * rate.
4. Jumlahkan keuntungan tiap bulan → total keuntungan 8 bulan.
5. (Opsional) Hitung saldo akhir jika keuntungan direinvestasikan.

### latihan3.py
1. Inisialisasi saldo = Rp 1.000.000.
2. Tampilkan menu: tarik tunai, cek saldo, keluar.
3. Proses input user; validasi jumlah tarik (kelipatan 1000 & saldo cukup).
4. Perbarui saldo dan ulangi sampai user keluar atau saldo habis.

## Hasil screenshoot
Latihan1.py

<img width="258" height="221" alt="Hasil_run_Latihan1 py" src="https://github.com/user-attachments/assets/cef465e2-8717-49b1-b4b2-2f9860dd393e" />

Latihan2.py

<img width="233" height="249" alt="Hasil_run_Latihan2 py" src="https://github.com/user-attachments/assets/d51b5722-a70e-4666-9aaa-5c685733316c" />

Latihan3.py

<img width="265" height="311" alt="Hasil_run_Latihan3 py" src="https://github.com/user-attachments/assets/c00e11e1-de1a-424d-b5ce-13987c89d8dc" />




