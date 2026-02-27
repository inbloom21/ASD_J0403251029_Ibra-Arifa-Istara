#============================================================================
# Nama        : Ibra Arifa Istara
# NIM         : J0403251029
# Kelas       : A1
#============================================================================

#============================================================================
# Latihan 3: Mencari Nilai Maksimum
#============================================================================

def cari_maks(data, index=0):
    # base case: jika rekursi sudah mencapai indeks terakhir dalam data, rekursi selesai dan mengembalikan nilai dari indeks terakhir
    if index == len(data) - 1:
        return data[index]
    
    # recursive case: fungsi akan merekursi hingga index terakhir. Ketika sudah mencapai indeks terakhir, kembalikan nilai indeks terakhir dan bandingkan dengan operator pembanding dibawah
    maks_sisa = cari_maks(data, index + 1)

    if data[index] > maks_sisa: # operator pembanding untuk menentukan nilai mana yang akan dikembalikan oleh fungsi cari_maks
        return data[index] # kalau data pada index yang sedang berjalan lebih tinggi dari nilai maks_sisa, kembalikan data tersebut
    else:
        return maks_sisa # kalau data pada nilai maks_sisa lebih tinggi daripada data pada index yang sedang berjalan, kembalikan nilai maks sisa
    
angka = [3, 7, 2, 9, 5]
print("Nilai maksimum:", cari_maks(angka))