print("/033c")
#Import Libraries
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import time

#Tentukam Wilayah (domain) diagram

x = np.linspace(-10,10,1000)
plt.figure (figsize=(4,15))

# Draw a Small Circle
plt.plot(x, (0.05 - x*2)* 0.5,    '-k')
plt.plot(x, ((0.05 - x*2)*0.5),  '-k')


# Tentukan persamaan matematika yang diingnakn
y1 = x - x - 0
y2 = 0.5 * x
y3 = x
y4 = 2*x
y5 = -0.5 * x
y6 = -x
y7 = -2*x

plt.plot(x, y1, '-k', label='y1')
plt.plot(x, y2, '-r', label='y2')
plt.plot(x, y3, '-g', label='y3')
plt.plot(x, y4, '-b', label='y4')
plt.plot(x, y5, '-y', label='y5')
plt.plot(x, y6, '-m', label='y6')
plt.plot(x, y7, '-c', label='y7')

plt.legend(loc='upper left')
plt.grid()
plt.show()


# Koordinat titik untuk garis pertama
x1, y1 = 5, 2
x2, y2 = 3, 4

# Koordinat titik untuk garis kedua
x3, y3 = 2, 1
x4, y4 = 4, 3

# Menggunakan numpy untuk membuat array dari koordinat x dan y
x_values1 = np.array([x1, x2])
y_values1 = np.array([y1, y2])

x_values2 = np.array([x3, x4])
y_values2 = np.array([y3, y4])

# Membuat array dari koordinat x untuk plot garis
x_plot = np.linspace(0, 5, 100)  # Mulai dari 0 hingga 5 dengan 100 titik

# Menghitung nilai y untuk garis pertama dan garis kedua
m1 = (y2 - y1) / (x2 - x1)
c1 = y1 - m1 * x1
y_plot1 = m1 * x_plot + c1

m2 = (y4 - y3) / (x4 - x3)
c2 = y3 - m2 * x3
y_plot2 = m2 * x_plot + c2

# Plot titik-titik
plt.scatter([x1, x2, x3, x4], [y1, y2, y3, y4], color='red', label='Titik')

# Tambahkan label sumbu
plt.xlabel('X')
plt.ylabel('Y')

# Tambahkan judul
plt.title('Visualisasi Dua Garis')

# Tampilkan legenda
plt.legend()

# Tampilkan plot
plt.grid(True)
plt.show()

# Koordinat titik untuk garis pertama
x1, y1 = 1, 2
x2, y2 = 3, 4

# Koordinat titik untuk garis kedua
x3, y3 = 2, 1
x4, y4 = 4, 3

# Menggunakan numpy untuk membuat array dari koordinat x dan y
x_values1 = np.array([x1, x2])
y_values1 = np.array([y1, y2])

x_values2 = np.array([x3, x4])
y_values2 = np.array([y3, y4])

# Membuat array dari koordinat x untuk plot garis
x_plot = np.linspace(0, 5, 100)  # Mulai dari 0 hingga 5 dengan 100 titik

# Menghitung nilai kemiringan dan perpotongan sumbu-y untuk garis pertama
m1 = (y2 - y1) / (x2 - x1)
c1 = y1 - m1 * x1
y_plot1 = m1 * x_plot + c1

# Menghitung nilai kemiringan dan perpotongan sumbu-y untuk garis kedua
m2 = (y4 - y3) / (x4 - x3)
c2 = y3 - m2 * x3
y_plot2 = m2 * x_plot + c2

# Plot garis pertama
plt.plot(x_plot, y_plot1, label=f'Garis 1: y={m1:.2f}x+{c1:.2f}')

# Plot garis kedua
plt.plot(x_plot, y_plot2, label=f'Garis 2: y={m2:.2f}x+{c2:.2f}')

# Plot titik-titik
plt.scatter([x1, x2, x3, x4], [y1, y2, y3, y4], color='red', label='Titik')

# Tambahkan label sumbu
plt.xlabel('X')
plt.ylabel('Y')

# Tambahkan judul
plt.title('Visualisasi Dua Garis dengan Dua Titik')

# Tampilkan legenda
plt.legend()

# Tampilkan plot
plt.grid(True)
plt.show()

# Titik-titik
ya, xa = 200, 200
yb, xb = 200, 600
yc, xc = 600, 600
yd, xd = 600, 200

# Warna dan lebar garis
pd, lw = int(8), int(8)
pr, pg, pb = 255, 0, 255  # Warna magenta
lr, lg, lb = 255, 0, 255  # Warna magenta

# Ukuran gambar
col, row = int(800), int(800)
print('col - row', col, ',', row)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    # Membuat gambar kosong
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2 - y1
    dx = x2 - x1

    # Buat titik pertama
    for i in range(x1 - hd, x1 + hd):
        for j in range(y1 - hd, y1 + hd):
            if (i - x1) ** 2 + (j - y1) ** 2 < hd ** 2:
                Gambar[j, i] = [pr, pg, pb]

    # Buat titik kedua
    for i in range(x2 - hd, x2 + hd):
        for j in range(y2 - hd, y2 + hd):
            if (i - x2) ** 2 + (j - y2) ** 2 < hd ** 2:
                Gambar[j, i] = [pr, pg, pb]

    # Buat garis cendrung horizontal
    if dy <= dx:
        my = dy / dx
        for i in range(x1, x2):
            j = int(my * (i - x1) + y1)
            x, y = i, j
            print('x,y =', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if (i - x) ** 2 + (j - y) ** 2 < hw ** 2:
                        Gambar[j, i] = [lr, lg, lb]

    # Buat garis cendrung vertikal
    if dy > dx:
        mx = dx / dy
        for j in range(y1, y2):
            i = int(mx * (j - y1) + x1)
            x, y = i, j
            print('x,y =', x, ',', y)
            for i in range(x - hw, x + hw):
                for j in range(y - hw, y + hw):
                    if (i - x) ** 2 + (j - y) ** 2 < hw ** 2:
                        Gambar[j, i] = [lr, lg, lb]

    return Gambar

hasil = buat_garis(ya, xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)

# Menampilkan gambar
plt.figure()
plt.imshow(hasil)

# Titik-titik
ya, xa = 200, 200
yb, xb = 200, 600
yc, xc = 600, 600
yd, xd = 600, 200

# Warna dan lebar garis
pd, lw = int(8), int(8)
pr, pg, pb = 255, 0, 255  # Warna magenta
lr, lg, lb = 255, 255, 0  # Warna kuning

# Ukuran gambar
col, row = int(800), int(800)

def buat_garis(y1, x1, y2, x2, pd, lw, pr, pg, pb, lr, lg, lb):
    # Membuat gambar kosong
    Gambar = np.zeros(shape=(row, col, 3), dtype=np.uint8)

    hd = int(pd/2)
    hw = int(lw/2)
    dy = y2 - y1
    dx = x2 - x1

    # Buat titik-titik
    for i, j in [(x1, y1), (x2, y2)]:
        for k in range(i - hd, i + hd):
            for l in range(j - hd, j + hd):
                if (k - i) ** 2 + (l - j) ** 2 < hd ** 2:
                    Gambar[l, k] = [pr, pg, pb]

    # Buat garis vertikal
    if dx == 0:
        for j in range(min(y1, y2), max(y1, y2)):
            for i in range(x1 - hw, x1 + hw):
                for j in range(j - hw, j + hw):
                    if (i - x1) ** 2 + (j - y1) ** 2 < hw ** 2:
                        Gambar[j, i] = [lr, lg, lb]

    return Gambar

hasil = buat_garis(ya, xa, yb, xb, pd, lw, pr, pg, pb, lr, lg, lb)

# Menampilkan gambar
plt.figure()
plt.imshow(hasil)
plt.show()
