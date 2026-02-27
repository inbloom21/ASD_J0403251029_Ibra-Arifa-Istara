#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Contoh Backtracking 2: Kombinasi Biner dengan Batas '1' (Pruning)
#============================================================================

def biner_batas(n, batas, hasil="", jumlah_1=0):
    # Pruning: jika jumlah_1 sudah melewati batas, berhenti
    if jumlah_1 > batas:
        return
    
    # base case
    if len(hasil) == n:
        print(hasil)
        return
    
    # pilih '0'
    biner_batas(n, batas, hasil + "0", jumlah_1)

    # pilih '0'
    biner_batas(n, batas, hasil + "1", jumlah_1 + 1)

biner_batas(4, 2)