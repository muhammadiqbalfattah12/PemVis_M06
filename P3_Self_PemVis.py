import matplotlib.pyplot as plt

# Meminta pengguna untuk memasukkan bilangan bulat positif
bilangan = int(input("Masukkan bilangan bulat positif: "))

# Inisialisasi variabel untuk menyimpan jumlah bilangan ganjil
jumlah_ganjil = 0

# Inisialisasi list untuk menyimpan nomor bilangan ganjil
bilangan_ganjil = []

# Memeriksa setiap bilangan dari 1 hingga bilangan yang dimasukkan pengguna
for i in range(1, bilangan + 1):
    # Memeriksa apakah bilangan tersebut ganjil
    if i % 2 != 0:
        # Menambahkan bilangan ganjil ke jumlah_ganjil
        jumlah_ganjil += 1
        # Menambahkan nomor bilangan ganjil ke dalam list
        bilangan_ganjil.append(i)

# Menampilkan hasil
print("Jumlah bilangan ganjil dari rentang 1 hingga", bilangan, "adalah", jumlah_ganjil)

# Visualisasi data menggunakan Matplotlib
plt.bar(range(1, jumlah_ganjil + 1), bilangan_ganjil, color='skyblue')
plt.xlabel('Nomor Bilangan Ganjil')
plt.ylabel('Jumlah')
plt.title('Jumlah Bilangan Ganjil dari 1 hingga {}'.format(bilangan))
plt.grid(True)
plt.show()
