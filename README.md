

Nama: Ayu Syarifatu Zahra
NIM: 2225250043
Kelas: 3B

## Tujuan
Membangun program validasi dan klasifikasi dengan rantai if-elif-else.

## Cara Menjalankan
python3 praktik/validasi_klasifikasi_nilai.py

## Tabel Keputusan
| Kategori | Syarat | Contoh Masukan |
| --- | --- | --- |
| Penolakan Tipe | Input bukan angka / float | `ujian = "abc"` |
| Penolakan Rentang | Nilai < 0 atau Nilai > 100 | `ujian = 105` atau `tugas = -5` |
| Tidak Memenuhi Kehadiran | Kehadiran < 80% | `ujian = 90, tugas = 90, hadir = 75` |
| Predikat A | Nilai Akhir >= 85 (Hadir >= 80%) | `ujian = 90, tugas = 80, hadir = 95` |
| Predikat B | Nilai Akhir >= 70 (Hadir >= 80%) | `ujian = 75, tugas = 70, hadir = 85` |
| Predikat C | Nilai Akhir >= 60 (Hadir >= 80%) | `ujian = 60, tugas = 60, hadir = 80` |
| Predikat D | Nilai Akhir >= 50 (Hadir >= 80%) | `ujian = 55, tugas = 50, hadir = 90` |
| Predikat E | Nilai Akhir < 50 (Hadir >= 80%) | `ujian = 40, tugas = 30, hadir = 100` |

## Hasil Pengujian
| Ujian | Tugas | Kehadiran | Nilai Akhir | Keluaran Diharapkan | Status |
| --- | --- | --- | --- | --- | --- |
| 90 | 80 | 95 | 86.00 | Predikat A, Lulus | Sesuai |
| 75 | 70 | 85 | 73.00 | Predikat B, Lulus | Sesuai |
| 60 | 60 | 80 | 60.00 | Predikat C, Lulus | Sesuai |
| 55 | 50 | 90 | 53.00 | Predikat D, Belum lulus | Sesuai |
| 40 | 30 | 100 | 36.00 | Predikat E, Belum lulus | Sesuai |
| 90 | 90 | 75 | 90.00 | Nilai akhir tetap tampil, status Tidak memenuhi syarat kehadiran | Sesuai |
| 105 | 80 | 90 | - | Pesan penolakan rentang nilai ujian | Sesuai |
| 80 | -5 | 90 | - | Pesan penolakan rentang nilai tugas | Sesuai |
| 80 | 80 | abc | - | Pesan penolakan tipe | Sesuai |

## Refleksi
Salah satu masukan tidak valid yang semula terlewat adalah ketika pengguna memasukkan teks/string alih-alih angka (seperti `"abc"`). Hal ini ditangani menggunakan struktur penanganan eksepsi `try-except ValueError` untuk menangkap kesalahan konversi tipe data sebelum dilakukan kalkulasi matematika.
"""
