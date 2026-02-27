#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Latihan 4: Kombinasi Huruf
#============================================================================

def kombinasi(n, hasil=""):

    if len(hasil) == n:
        print(hasil)
        return
    
    kombinasi(n, hasil + "A")
    kombinasi(n, hasil + "B")

kombinasi(2)
# Jumlah kombinasi yang dihasilkan adalah 2 pangkat n karena pada setiap langkah rekursi, fungsi bercabang menjadi 2 pilihan, yaitu "A" dan "B"