#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Latihan 2: Tracing Rekursi
#============================================================================

def countdown(n):
    # base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk: ", n)

    # recursive case
    countdown(n - 1) # fungsi countdown akan terus berekursi dan mencetak print masuk sampai base case tercapai

    print("Keluar: ", n) # output keluar muncul terbalik karena rekursi countdown dijalankan hingga base case sebelum print keluar dijalankan

countdown(3)