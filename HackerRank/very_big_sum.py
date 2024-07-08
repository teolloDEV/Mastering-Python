def aVeryBigSum(ar):
    return sum(ar)

if __name__ == '__main__':
    # Meminta pengguna untuk memasukkan jumlah elemen dalam array
    n = int(input("Masukkan jumlah elemen dalam array: "))

    # Meminta pengguna untuk memasukkan elemen-elemen array secara manual
    print("Masukkan elemen-elemen array, dipisahkan oleh spasi:")
    ar = list(map(int, input().split()))

    # Memanggil fungsi untuk menghitung jumlah elemen dalam array
    result = aVeryBigSum(ar)

    # Mencetak hasil
    print("Jumlah semua elemen dalam array adalah:", result)
