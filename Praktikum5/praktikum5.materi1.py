#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Contoh Rekursi 1: Faktorial
#============================================================================

def faktorial(n):
    # base case: berhenti ketika n = 0
    if n == 0:
        return 1 # jika nilai n adalah 0, kembalikan 1 (0!=1)
    
    # recursive case: masalah diperkecil menjadi faktorial(n-1)
    return n * faktorial(n - 1)

#contoh penggunaan (5!)
print(faktorial(5))