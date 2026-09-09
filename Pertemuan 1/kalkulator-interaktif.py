def kalkulator():
    "Program kalkulator interaktif dengan menu"

    print("=" * 40)
    print("         KALKULATOR INTERAKTIF")
    print("=" * 40)

    # Input angka
    angka1 = int(input("\nMasukan angka pertama: "))
    angka2 = int(input("Masukan angka kedua : "))

    print("\n" + "=" * 40)
    print("Pilih operasi yang akan diinginkan: ")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (*)")
    print("4. Pembagian (/)")
    print("5. Pembagian Bulat (//)")
    print("6. Sisa Bagi (%)")
    print("7. Semua Operasi")
    print("=" * 40)

    # Input pilihan operasi
    pilihan = input("\nMasukan pilihan operasi (1-7): ")

    print("\n" + "=" * 40)
    print("Hasil Operasi: ")
    print("=" * 40)

    # Operasi berdasarkan pilihan
    if pilihan == "1":
        print(f"Hasil Penjumlahan: {angka1} + {angka2} = {angka1 + angka2}")
    elif pilihan == "2":
        print(f"Hasil Pengurangan: {angka1} - {angka2} = {angka1 - angka2}")
    elif pilihan == "3":
        print(f"Hasil Perkalian: {angka1} * {angka2} = {angka1 * angka2}")
    elif pilihan == "4":
        if angka2 != 0:
            print(f"Hasil Pembagian: {angka1} / {angka2} = {angka1 / angka2}")
        else:
            print("Error: Tidak dapat membagi dengan nol.")
    elif pilihan == "5":
        if angka2 != 0:
            print(f"Hasil Pembagian Bulat: {angka1} // {angka2} = {angka1 // angka2}")
        else:
            print("Error: Tidak dapat membagi dengan nol.")
    elif pilihan == "6":
        if angka2 != 0:
            print(f"Hasil Sisa Bagi: {angka1} % {angka2} = {angka1 % angka2}")
        else:
            print("Error: Tidak dapat menghitung sisa bagi dengan nol.")
    elif pilihan == "7":
        print(f"Hasil Penjumlahan: {angka1} + {angka2} = {angka1 + angka2}")
        print(f"Hasil Pengurangan: {angka1} - {angka2} = {angka1 - angka2}")
        print(f"Hasil Perkalian: {angka1} * {angka2} = {angka1 * angka2}")
        if angka2 != 0:
            print(f"Hasil Pembagian: {angka1} / {angka2} = {angka1 / angka2}")
            print(f"Hasil Pembagian Bulat: {angka1} // {angka2} = {angka1 // angka2}")
            print(f"Hasil Sisa Bagi: {angka1} % {angka2} = {angka1 % angka2}")
        else:
            print("Error: Tidak dapat melakukan operasi pembagian dengan nol.")
    else:
        print("Pilihan tidak valid")

    print("\n" + "=" * 40)

# Menjalankan program kalkulator
if __name__ == "__main__":
    while True:
        kalkulator()
        ulang = input("\nApakah Anda ingin melakukan operasi lain? (y/n): ").lower()
        if ulang != "y":
            print("Terima kasih telah menggunakan kalkulator interaktif.")
            break