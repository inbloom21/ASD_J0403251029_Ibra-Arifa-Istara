#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Studi Kasus: Generator PIN
#============================================================================

def buat_pin(panjang, hasil=""):
    if len(hasil) == panjang: # cek apakah hasil sama panjangnya dengan panjang yang sudah ada
        print("PIN: ", hasil) # jika iya, print hasil
        return
    
    for angka in ["0", "1", "2"]: #untuk setiap indeks pada list, akan dipanggil fungsi buat pin yang akan berekursi hingga panjang pin sesuai dengan hasil
        buat_pin(panjang, hasil + angka)

buat_pin(2)