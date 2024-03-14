def hitung_ppn(nilai):
    ppn = nilai * 0.12
    return ppn

# Input nilai a dan b
a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))

# Cek apakah a lebih besar dari b
a_lebih_besar = a > b

# Cek apakah b lebih besar dari a
b_lebih_besar = b > a

# Cek apakah a sama dengan b
sama_dengan = a == b

# Hitung ppn a dan b jika sesuai kondisi
if a > 10000:
    ppn_a = hitung_ppn(a)
else:
    ppn_a = 0

if b > 50000:
    ppn_b = hitung_ppn(b)
else:
    ppn_b = 0

# Tambahkan kedua ppn a dan b
total_ppn = ppn_a + ppn_b

# Cek apakah total ppn lebih dari 0
ada_ppn = total_ppn > 0

# Hapus nilai a dan b
del a
del b

# Cek apakah nilai a dan b telah dihapus
nilai_terhapus = 'a' not in locals() and 'b' not in locals()

# Output hasil
print("a lebih besar dari b:", a_lebih_besar)
print("b lebih besar dari a:", b_lebih_besar)
print("a sama dengan b:", sama_dengan)
print("PPN a:", ppn_a)
print("PPN b:", ppn_b)
print("Total PPN:", total_ppn)
print("Ada PPN:", ada_ppn)
print("Nilai a dan b sudah terhapus:", nilai_terhapus)
