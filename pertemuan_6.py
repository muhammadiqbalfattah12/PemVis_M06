def tampilkan_catalog():
    print("Selamat datang di toko aksesoris Pak Yeru!")
    print("Inilah catalog aksesoris kami:")
    for item in catalog_aksesoris:
        print("-", item)

def beli_produk():
    produk = input("Masukkan nama produk yang ingin Anda beli: ")
    if produk in catalog_aksesoris:
        print("Terima kasih telah membeli", produk)
        catalog_aksesoris.remove(produk)
    else:
        print("Maaf, produk tersebut tidak tersedia di toko kami")

def tambah_produk():
    produk_baru = input("Masukkan nama produk baru: ")
    catalog_aksesoris.append(produk_baru)
    print(produk_baru, "telah ditambahkan ke dalam catalog aksesoris")

def update_catalog():
    produk_lama = input("Masukkan nama produk lama yang ingin diubah: ")
    if produk_lama in catalog_aksesoris:
        index = catalog_aksesoris.index(produk_lama)
        produk_baru = input("Masukkan nama produk baru: ")
        catalog_aksesoris[index] = produk_baru
        print("Catalog telah diperbarui")
    else:
        print("Maaf, produk tersebut tidak ditemukan di dalam catalog")

def hapus_semua_produk():
    catalog_aksesoris.clear()
    print("Semua produk telah dihapus dari catalog")

def tampilkan_jumlah_produk():
    print("Jumlah produk dalam catalog:", len(catalog_aksesoris))

# Pendefinisian catalog
catalog_aksesoris = ["Gelang Mutiara", "Gelang Kopel", "Kalung Hijrah", "Kalung Rantai", "Kalung Anak"]

while True:
    # Langkah 1: Menampilkan catalog
    tampilkan_catalog()

    # Langkah 2: Pelanggan memilih dan membeli aksesoris
    beli_produk()

    # Langkah 3: Menambahkan produk baru ke dalam catalog
    tambah_produk()

    # Langkah 4: Memperbarui catalog
    update_catalog()

    # Langkah 5: Menampilkan jumlah produk dalam catalog
    tampilkan_jumlah_produk()

    # Langkah 6: Menghapus semua produk dari catalog
    hapus_semua_produk()

    # Pengecekan apakah pengguna ingin keluar dari loop
    lanjutkan = input("Apakah Anda ingin melanjutkan (ya/tidak)? ")
    if lanjutkan.lower() != "ya":
        break


