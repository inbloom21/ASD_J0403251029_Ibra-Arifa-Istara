#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Contoh Backtracking 1: Kombinasi Biner (n)
#============================================================================

def biner(n, hasil=""):
    # base case: jika panjang string sudah n, cetak hasil
    if len(hasil) == n:
        print(hasil)
        return
    
    # choose + explore: tambah '0'
    biner(n, hasil + "0")

    # choose + explore: tambah '1'
    biner(n, hasil + "1")

biner(3) 