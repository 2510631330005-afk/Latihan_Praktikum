def input_matriks(baris, kolom, nama):
    print(f"\nMasukkan elemen matriks {nama} ({baris}x{kolom}):")
    matriks = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            while True:
                try:
                    val = float(input(f"Elemen [{i+1},{j+1}]: "))
                    row.append(val)
                    break
                except ValueError:
                    print("Input harus angka!")
        matriks.append(row)
    return matriks

def print_matriks(matriks):
    for row in matriks:
        print("\t".join(f"{elemen:.2f}" for elemen in row))

def penjumlahan_matriks(A, B):
    baris = len(A)
    kolom = len(A[0])
    C = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

def perkalian_matriks(A, B):
    m = len(A)
    p = len(A[0])
    n = len(B[0])
    C = []

    for i in range(m):
        row = []
        for j in range(n):
            total = 0
            for k in range(p):
                total += A[i][k] * B[k][j]
            row.append(total)
        C.append(row)
    return C

def transpose_matriks(A):
    baris_A = len(A)
    kolom_A = len(A[0])
    T = []

    for j in range(kolom_A):
        new_row = []
        for i in range(baris_A):
            new_row.append(A[i][j])
        T.append(new_row)
    return T


def main_menu(m_A, p_A, m_B, n_B):

    A = input_matriks(m_A, p_A, "A")
    B = input_matriks(m_B, n_B, "B")

    while True:
        print("\n" + "="*40)
        print(f"Pilihan Operasi untuk Matriks A ({m_A}x{p_A}) dan B ({m_B}x{n_B})")
        print("1. Penjumlahan dua matriks (A + B)")
        print("2. Perkalian dua matriks (A x B)")
        print("3. Transpose matriks (Matriks A)")
        print("4. Keluar")
        print("="*40)

        pilihan = input("Masukkan pilihan (1-4): ")

        try:
            pilihan = int(pilihan)
        except ValueError:
            print("Pilihan tidak valid. Masukkan angka 1-4.")
            continue

        if pilihan == 1:
            if m_A == m_B and p_A == n_B:
                C_jumlah = penjumlahan_matriks(A, B)
                print("\n--- Hasil Penjumlahan Matriks A + B ---")
                print_matriks(C_jumlah)
            else:
                print("\n--- Penjumlahan Gagal ---")
                print("Penjumlahan matriks hanya bisa dilakukan jika ukuran kedua matriks SAMA.")
                print(f"Ukuran A: {m_A}x{p_A}, Ukuran B: {m_B}x{n_B}")

        elif pilihan == 2:
            if p_A == m_B:
                C_kali = perkalian_matriks(A, B)
                print("\n--- Hasil Perkalian Matriks A x B ---")
                print_matriks(C_kali)
            else:
                print("\n--- Perkalian Gagal ---")
                print("Perkalian matriks hanya bisa dilakukan jika jumlah kolom matriks pertama (A) sama dengan jumlah baris matriks kedua (B).")
                print(f"Ukuran A: {m_A}x{p_A}, Ukuran B: {m_B}x{n_B}")

        elif pilihan == 3:
            A_transpose = transpose_matriks(A)
            print("\n--- Hasil Transpose Matriks A ---")
            print_matriks(A_transpose)

        elif pilihan == 4:
            print("\nTerima kasih! Keluar dari program.")
            break

        else:
            print("Pilihan tidak ada. Silakan pilih antara 1 hingga 4.")

def jalankan_kasus():

    kasus_data = {
        "Kasus 1": {"A": (2, 2), "B": (2, 2)},
        "Kasus 2": {"A": (2, 3), "B": (3, 2)},
        "Kasus 3": {"A": (3, 3), "B": (3, 3)},
        "Kasus 4": {"A": (3, 2), "B": (3, 2)}
    }

    print("PROGRAM OPERASI DASAR MATRIKS (Penjumlahan, Perkalian, Transpose)")

    while True:
        print("\nSilakan pilih Kasus yang ingin dijalankan:")
        for i, nama_kasus in enumerate(kasus_data.keys(), 1):
            data = kasus_data[nama_kasus]
            print(f"{i}. {nama_kasus}: Matriks A ({data['A'][0]}x{data['A'][1]}), Matriks B ({data['B'][0]}x{data['B'][1]})")
        print("5. Keluar Program Utama")

        pilihan_kasus = input("Masukkan nomor Kasus (1-5): ")

        if pilihan_kasus == '5':
            print("Keluar dari program utama.")
            break

        try:
            pilihan_int = int(pilihan_kasus)
            if 1 <= pilihan_int <= 4:
                nama_kasus = list(kasus_data.keys())[pilihan_int - 1]
                data = kasus_data[nama_kasus]

                print(f"\n======== {nama_kasus} Dijalankan ========")
                print(f"Ukuran Matriks: A({data['A'][0]}x{data['A'][1]}) dan B({data['B'][0]}x{data['B'][1]})")

                main_menu(data['A'][0], data['A'][1], data['B'][0], data['B'][1])

            else:
                print("Pilihan kasus tidak valid.")
        except ValueError:
            print("Input harus berupa angka.")


if __name__ == "__main__":
    jalankan_kasus()
