
# Variabel untuk menyimpan data file
nama_file = "stok_barang.txt"

# Fungsi untuk load data dari file
def baca_stok(nama_file):
    stok_dict = {}
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip()
            kode, barang, jumlah = baris.split(",")
            stok_dict[kode] = {"nama": barang, "jumlah": int(jumlah)}
    return stok_dict

def simpan_stok(nama_file, stok_dict):
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            barang = stok_dict[kode]["nama"]
            jumlah = stok_dict[kode]["jumlah"]
            file.write(f"{kode},{barang},{jumlah}\n")

# Fungsi untuk menampilkan data
def tampilkan_semua(stok_dict):
    print("\n=========== DATA BARANG ===========")
    print(f"{"Kode" : <10} | {"Nama Barang" : <12} | {"Jumlah" : >5}")
    print("-" * 35) #membuat garis

    #menampilkan isi datanya
    for kode in sorted(stok_dict.keys()):
        barang = stok_dict[kode]["nama"]
        jumlah = stok_dict[kode]["jumlah"]
        print(f"{kode:<10} | {barang:<12} | {int(jumlah):>5}")

# Fungsi untuk mencari data
def cari_barang(stok_dict):
    kode_barang = input("Masukkan kode barang yang ingin dicari: ")

    if kode_barang in stok_dict:
        barang = stok_dict[kode_barang]["nama"]
        jumlah = stok_dict[kode_barang]["jumlah"]

        print("\n===== Data Barang Ditemukan =====")
        print(f"Kode         : {kode_barang}")
        print(f"Nama Barang  : {barang}")
        print(f"Jumlah       : {jumlah}")
    else:
        print("Data tidak ditemukan. Pastikan kode barang yang dimasukkan benar!")

# Fungsi untuk menambah barang
def tambah_barang(stok_dict):
    kode_barang = input("Masukkan kode barang baru yang ingin ditambahkan: ")
    if kode_barang in stok_dict:
        print("Kode sudah digunakan.")
    else:
        try:
            nama_barang = input("Masukkan nama barang baru yang ingin ditambahkan: ")
            jumlah_barang = int(input("Masukkan stok awal barang yang ingin ditambahkan: "))

            if jumlah_barang < 0:
                print("Stok tidak boleh negatif. Penambahan barang dibatalkan.")
            else:
                stok_dict[kode_barang] = {"nama": nama_barang, "jumlah": jumlah_barang}
                print("Barang berhasil ditambahkan")
        except ValueError:
            print("Stok awal harus berupa angka")

# Fungsi untuk update stok barang
def update_stok(stok_dict):
    kode_barang = input("Masukkan kode barang yang ingin diubah stoknya: ")

    if kode_barang in stok_dict:
        print("1. Tambah stok")
        print("2. Kurangi stok")
        pilihan_update = input("Pilih opsi: ")

        try:
            if pilihan_update == "1":
                tambah_input = int(input("Berapa jumlah stok yang ingin ditambah: "))
                stok_dict[kode_barang]["jumlah"] += tambah_input
                print("Stok berhasil diupdate!")
            elif pilihan_update == "2":
                kurang_input = int(input("Berapa jumlah stok yang ingin dikurangi: "))

                if (stok_dict[kode_barang]["jumlah"] - kurang_input) < 0:
                    print("Stok tidak boleh bernilai negatif. Update dibatalkan!")
                else:
                    stok_dict[kode_barang]["jumlah"] -= kurang_input
                    print("Stok berhasil diupdate!")
            else:
                print("Pilih opsi 1-2!")
        except ValueError:
            print("Ketikkan angka!")

def main():
    stok_barang = baca_stok(nama_file)

    while True:
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip()

        if pilihan == "1":
            tampilkan_semua(stok_barang)
        elif pilihan == "2":
            cari_barang(stok_barang)
        elif pilihan == "3":
            tambah_barang(stok_barang)
        elif pilihan == "4":
            update_stok(stok_barang)
        elif pilihan == "5":
            simpan_stok(nama_file, stok_barang)
            print("Data berhasil disimpan.")
        elif pilihan == "0":
            print("Program Selesai")
            break
        else:
            print("Pilihan Tidak Valid. Silakan Coba Lagi")

if __name__ == "__main__":
    main()