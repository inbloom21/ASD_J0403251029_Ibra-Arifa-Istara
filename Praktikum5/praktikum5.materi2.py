#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Contoh Rekursi 2: Tracing Masuk/Keluar
#============================================================================

def hitung(n):
    # base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk: ", n) # fase stacking
    hitung(n - 1) # pemanggilan rekursif
    print("Keluar: ", n) # fase unwinding

hitung(3)