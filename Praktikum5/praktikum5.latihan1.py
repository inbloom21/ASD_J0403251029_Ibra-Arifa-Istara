#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Latihan 1: Rekursi Pangkat
#============================================================================

def pangkat(a, n):
    # base case: mengembalikan  nilai 1 jika n sudah mencapai 0 dalam rekursi
    if n == 0: # jika n sudah mencapai 0, kondisi ini akan berjalan untuk menghentikan rekursi dan mengembalikan nilai berupa 1
        return 1
    
    # recursive case: mengalikan a terus menerus dengan fungsi yang menghasilkan jumlah angka selama rekursif dijalankan
    return a * pangkat(a, n - 1)

print(pangkat(2, 4)) # output: 16

# Alur program:
# 1. fungsi pertama, nilai n adalah 4
# 2. Setelah rekursi pertama, nilai n adalah 3
# 3. Setelah rekursi kedua, nilai n adalah 2
# 4. Setelah rekursi ketiga, nilai n adalah 1
# 5. Setelah rekursi keempat, nilai n adalah 0, base case tercapai, fungsi mengembalikan 1
# 6. Naik ke fungsi atasnya secara berulang, mengkalikan nilai a dengan nilai fungsi pada setiap rekursi hingga kembali ke rekursi pertama.