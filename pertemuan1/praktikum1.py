#==================================================================
#Praktikum 1: Konsep ADT dan File Handling
#Latihan Dasar 1: Membaca seluruh isi file data
#==================================================================

print("===Membuka file dalam satu string===")
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    isi_file = file.read()
print(isi_file)

print("Tipe Data: ", type(isi_file))

print("===Membuka file per baris===")
jumlah_baris = 0
with open("data_mahasiswa.txt", "r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris
        print("Baris ke-", jumlah_baris)
        print("isinya : ", baris)
