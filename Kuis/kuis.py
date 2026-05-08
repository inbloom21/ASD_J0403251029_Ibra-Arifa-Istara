# ==============================================================================
# UJIAN TENGAH PRAKTIKUM - ALGORITMA & STRUKTUR DATA (TPL2106)
# Nama    : Ibra Arifa Istara
# NIM     : J0403251029
# Kelas   : A1
# ==============================================================================

# 1. FILE HANDLING & DICTIONARY (Sub-CPMK 1) [cite: 31]
def muat_data_buku(nama_file):
    """
    Fungsi untuk membaca 'buku.txt' dan menyimpannya ke Dictionary.
    Format file: kode_buku,judul,harga
    """
    database_buku = {}
    with open("buku.txt", "r", encoding="utf-8") as file: # membuka file buku.txt dan di-assign ke variabel file
        for baris in file: # untuk setiap baris di file, hilangkan karakter spasi lalu pisahkan string yang dipisah dengan "," dan masukkan masing-masing nilai ke variabel kode, judul, dan harga
            baris = baris.strip()
            kode, judul, harga = baris.split(",")
            database_buku[kode] = { # jadikan variabel kode sebagai key yang isinya adalah key judul dan harga, lalu masukkan ke dictionary
                "judul": judul,
                "harga": float(harga)
            }
    return database_buku # kembalikan dictionary yang sudah terisi

# 2. LINKED LIST - MANAJEMEN PROMOSI (Sub-CPMK 2) [cite: 32]
class Node: # buat class Node untuk buku yang mau dipromosikan
    def __init__(self, judul):
        self.judul = judul
        self.next = None

class LinkedListPromosi:
    def __init__(self):
         self.head = None

    def tambah_buku_promosi(self, judul): # masukkan objek buku ke dalam linked list
        """Menambahkan buku ke daftar promosi (Linked List)"""
        buku_baru = Node(judul) # memasukkan objek buku ke variabel buku_baru
        if not self.head: # kalau listnya masih kosong, jadikan buku yang baru di-assign menjadi head
            self.head = buku_baru
            return
        temp = self.head # jadikan headnya sebagai variabel temporary agar jika ingin menambahkan buku di list yang sudah terisi, headnya tidak berubah
        while temp.next: # pergi ke node paling terakhir
            temp = temp.next
        temp.next = buku_baru # tambahkan buku baru setelah node paling terakhir

    def tampilkan_promosi(self):
        """Menampilkan semua buku dalam daftar promosi"""
        temp = self.head # jadikan headnya sebagai variabel temporary agar jika ingin pergi ke node terakhir, headnya tidak berubah
        while temp: # print setiap buku di list
            print(temp.judul)
            temp = temp.next

# 3. QUEUE - ANTIREAN KASIR (Sub-CPMK 3) [cite: 33]
class AntreanKasir:
    def __init__(self):
        self.antrean = [] # inisiasi list queue

    def tambah_antrean(self, nama_pelanggan):
        """Menambah antrean (Enqueue)"""
        self.antrean.append(nama_pelanggan) # tambahkan pelanggan baru ke index paling belakang di list

    def layani_pelanggan(self):
        """Menghapus antrean (Dequeue)"""
        if len(self.antrean) == 0: # fungsi untuk memberitahu pengguna kalau antriannya kosong dan tidak ada yang dapat dilayani
            return "Tidak ada pelanggan yang dapat dilayani."
        return self.antrean.pop(0) # hapus index pertama dari antrean

# 4. SORTING - LAPORAN TRANSAKSI (Sub-CPMK 4) [cite: 34]
def urutkan_transaksi(list_harga): # mengurutkan transaksi dengan insertion sort
    """
    Mengurutkan list harga secara manual menggunakan 
    Insertion Sort atau Merge Sort.
    """
    for index in range(1, len(list_harga)): # membuat looping dengan panjang dari index kedua hingga terakhir dari data yang mau disortir
        nilai_posisi = list_harga[index] # buat variabel untuk menampung nilai yang ingin dibandingkan (mulai dari index kedua supaya bisa dibandingkan dengan index sebelumnya)
        posisi = index # simpan posisi dari nilai

        while posisi > 0 and list_harga[posisi - 1] > nilai_posisi: # jika nilai suatu index di posisi kurang satu lebih besar daripada nilai di posisi, tukar posisinya
            list_harga[posisi] = list_harga[posisi - 1]
            posisi = posisi - 1 # bandingkan lagi posisi yang sudah ditukar dengan posisi sebelumnya

        list_harga[posisi] = nilai_posisi # assign nilai yang sudah ditukar

    return list_harga # kembalikan list yang sudah terurut

# ==============================================================================
# MAIN PROGRAM - MENU ANTARMUKA
# ==============================================================================
def main():
    # Inisialisasi Data
    file_db = "buku.txt"
    data_buku = muat_data_buku(file_db)
    list_promosi = LinkedListPromosi()
    antrean_toko = AntreanKasir()
    riwayat_transaksi = [150000, 50000, 200000, 75000, 120000]

    while True:
        print("\n--- SISTEM MANAJEMEN TOKO BUKU ---")
        print("1. Lihat Katalog Buku (Dictionary/File)")
        print("2. Kelola Daftar Promosi (Linked List)")
        print("3. Kelola Antrean Kasir (Queue)")
        print("4. Lihat Laporan Penjualan Terurut (Sorting)")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == '1':
            print("\n======= KATALOG BUKU =======")
            print(f"{"KODE" : <10} | {"JUDUL" : <10} | {"HARGA" : >5}") # formating tabel agar rapih
            print("-" * 32)
            for kode in sorted(data_buku.keys()): # menampilkan setiap buku pada dictionary dengan rapih
                judul = data_buku[kode]["judul"]
                harga = data_buku[kode]["harga"]
                print(f"{kode:<10} | {judul:<12} | Rp{float(harga):>5}")
        
        elif pilihan == '2':
            judul_baru = input("Masukkan judul buku untuk promosi: ")
            for kode in data_buku: # looping untuk memastikan bahwa judul yang diinput ada di dalam katalog
                if data_buku[kode]["judul"] != judul_baru:
                    ada = False
                else:
                    ada = True

            if ada: # kalau ada di katalog, masukkan ke daftar promosi
                list_promosi.tambah_buku_promosi(judul_baru)
                list_promosi.tampilkan_promosi()
            else: # kalau tidak ada di katalog, beritahu pengguna
                print("Tidak terdapat buku dengan judul tersebut di katalog")

        elif pilihan == '3':
            nama = input("Nama Pelanggan: ")
            antrean_toko.tambah_antrean(nama) # tambahkan pelanggan yang sudah diinput ke list

            pilihan = input("Maukah kamu melayani antrean(y/n)? ")

            if pilihan == "y": # kalau pengguna memilih untuk melayani pelanggan, hapus index pertama pada list antrean
                antrean_toko.layani_pelanggan()
                for orang in antrean_toko.antrean:
                    print(orang)
            else:
                print("\n======= ANTREAN =======")
                for orang in antrean_toko.antrean:
                    print(orang)

        elif pilihan == '4':
            print("Harga Sebelum Urut:", riwayat_transaksi) # tampilkan harga sebelum urut
            hasil_sort = urutkan_transaksi(riwayat_transaksi) # lakukan sorting
            print("Harga Sesudah Urut:", hasil_sort) # tampilkan harga sesudah urut

        elif pilihan == '5': # keluar dari looping main
            print("Program selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__": # jalankan main
    main()