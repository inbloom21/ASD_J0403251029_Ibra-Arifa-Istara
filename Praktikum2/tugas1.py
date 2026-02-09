# ================================================================
# TUGAS HANDS-ON MODUL 1
# Studi Kasus: Sistem Stok Barang Kantin (Berbasis File .txt)
#
# Nama: Ibra Arifa Istara
# NIM: J0403251029
# Kelas: A/P1
# ================================================================

# --------------------------------------
# Konstanta nama file
# --------------------------------------
nama_file = "stok_barang.txt"

# --------------------------------------
# Fungsi: Membaca data dari file
# --------------------------------------
def baca_stok(nama_file):
    stok_dict = {} # inisialisasi dictionary untuk menyimpan data stok
    with open(nama_file, "r", encoding="utf-8") as file:
        for baris in file:
            baris = baris.strip() # menghapus karakter newline di setiap baris
            kode, barang, jumlah = baris.split(",") # memisahkan kata di baris dan memasukkannya ke variabel terkait
            stok_dict[kode] = {"nama": barang, "jumlah": int(jumlah)}
            # menambah index baru di stok_dict dengan key "kode" yang bernilai sebuah dictionary yang memiliki key "nama" dengan value nama barang dan "jumlah" dengan value stok barang
    return stok_dict

# --------------------------------------
# Fungsi: Menyimpan data ke file
# --------------------------------------
def simpan_stok(nama_file, stok_dict): # mengubah dictionary menjadi teks yang dapat ditulis ke file .txt
    with open(nama_file, "w", encoding="utf-8") as file:
        for kode in sorted(stok_dict.keys()):
            barang = stok_dict[kode]["nama"] # mengambil nama barang dari dict
            jumlah = stok_dict[kode]["jumlah"] # mengambil stok barang dari dict
            file.write(f"{kode},{barang},{jumlah}\n") 

# --------------------------------------
# Fungsi: Menampilkan semua data
# --------------------------------------
def tampilkan_semua(stok_dict):
    print("\n=========== DATA BARANG ===========")
    print(f"{"Kode" : <10} | {"Nama Barang" : <12} | {"Jumlah" : >5}") # pengformatan agar teks terlihat seperti tabel yang rapi
    print("-" * 35) #membuat garis

    #menampilkan isi datanya
    for kode in sorted(stok_dict.keys()):
        barang = stok_dict[kode]["nama"]
        jumlah = stok_dict[kode]["jumlah"]
        print(f"{kode:<10} | {barang:<12} | {int(jumlah):>5}")

# --------------------------------------
# Fungsi: Cari barang berdasarkan kode
# --------------------------------------
def cari_barang(stok_dict):
    kode_barang = input("Masukkan kode barang yang ingin dicari: ").strip() # meminta user mengetikkan kode barang yang ingin dicari

    if kode_barang in stok_dict: # jika kode barang ditemukan, tampilkan barang beserta keterangan terkait
        barang = stok_dict[kode_barang]["nama"]
        jumlah = stok_dict[kode_barang]["jumlah"]

        print("\n===== Data Barang Ditemukan =====")
        print(f"Kode         : {kode_barang}")
        print(f"Nama Barang  : {barang}")
        print(f"Jumlah       : {jumlah}")
    else:
        print("Data tidak ditemukan. Pastikan kode barang yang dimasukkan benar!")

# --------------------------------------
# Fungsi: Tambah barang baru
# --------------------------------------
def tambah_barang(stok_dict):
    kode_barang = input("Masukkan kode barang baru yang ingin ditambahkan: ").strip()
    if kode_barang in stok_dict: # kalau kode sudah terpakai, user akan diberi tahu
        print("Kode sudah digunakan.")
    else:
        try: # try dan except sebagai error handler ketika user mengetikkan karakter yang tidak bisa diubah menjadi integer
            nama_barang = input("Masukkan nama barang baru yang ingin ditambahkan: ")
            jumlah_barang = int(input("Masukkan stok awal barang yang ingin ditambahkan: "))

            if jumlah_barang < 0: # jika stok awal yang diinput user bernilai negatif, peringati user dan jangan jalankan penambahan barang
                print("Stok tidak boleh negatif. Penambahan barang dibatalkan.")
            else: # jika stok awal yang diinput tidak negatif, tambahkan barang
                stok_dict[kode_barang] = {"nama": nama_barang, "jumlah": jumlah_barang}
                print("Barang berhasil ditambahkan")
        except ValueError:
            print("Stok awal harus berupa angka")

# --------------------------------------
# Fungsi: Update stok barang
# --------------------------------------
def update_stok(stok_dict):
    kode_barang = input("Masukkan kode barang yang ingin diubah stoknya: ").strip() # simpan input user di variabel

    if kode_barang in stok_dict: # jika kode yang diinput ada di dictionary, jalankan
        print("1. Tambah stok")
        print("2. Kurangi stok")
        pilihan_update = input("Pilih opsi: ").strip() # simpan input user di variabel

        try: # try dan except untuk mengantisipasi jika user menginput karakter yang tidak bisa diubah menjadi integer
            if pilihan_update == "1": # menjalankan kode di bawah berdasarkan input user
                tambah_input = int(input("Berapa jumlah stok yang ingin ditambah: "))
                stok_dict[kode_barang]["jumlah"] += tambah_input
                print("Stok berhasil diupdate!")
            elif pilihan_update == "2":
                kurang_input = int(input("Berapa jumlah stok yang ingin dikurangi: "))

                if (stok_dict[kode_barang]["jumlah"] - kurang_input) < 0: # mengantisipasi agar stok tidak bernilai negatif
                    print("Stok tidak boleh bernilai negatif. Update dibatalkan!")
                else:
                    stok_dict[kode_barang]["jumlah"] -= kurang_input
                    print("Stok berhasil diupdate!")
            else:
                print("Pilih opsi 1-2!")
        except ValueError:
            print("Ketikkan angka!")
    else: # jika kode yang diinput tidak ada di dictionary, peringatkan user
        print("Barang tidak ditemukan")

# --------------------------------------
# Program Utama
# --------------------------------------
def main():
    stok_barang = baca_stok(nama_file)

    while True: # program akan berjalan terus kecuali jika dihentikan paksa atau user menginput "0" (break akan dijalankan)
        print("\n=== MENU STOK KANTIN ===")
        print("1. Tampilkan semua barang")
        print("2. Cari barang berdasarkan kode")
        print("3. Tambah barang baru")
        print("4. Update stok barang")
        print("5. Simpan ke file")
        print("0. Keluar")

        pilihan = input("Pilih Menu: ").strip() # masukkan input user ke variabel

        # berdasarkan variabel pilihan akan ditentukan fungsi mana yang akan dijalankan
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
        else: # jika input tidak sesuai, peringatkan user
            print("Pilihan Tidak Valid. Silakan Coba Lagi")

# Menjalankan program utama
if __name__ == "__main__":
    main()