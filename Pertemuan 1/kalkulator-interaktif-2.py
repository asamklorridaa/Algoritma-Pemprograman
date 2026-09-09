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
    if pilihan not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Pilihan tidak valid. Silakan masukan angka dari 1-7.")
        ulang = input("Apakah Anda ingin mencoba lagi? (y/n): ")
        if ulang.lower() == "y":
            kalkulator()

    print("\n" + "=" * 40)
    print("Hasil Operasi: ")
    print("=" * 40)

    # Operasi berdasarkan pilihan
    if pilihan == "1":
        hasil = angka1 + angka2
        print(f"Hasil Penjumlahan: {angka1} + {angka2} = {hasil}")
    elif pilihan == "2":
        hasil = angka1 - angka2
        print(f"Hasil Pengurangan: {angka1} - {angka2} = {hasil}")
    elif pilihan == "3":
        hasil = angka1 * angka2
        print(f"Hasil Perkalian: {angka1} * {angka2} = {hasil}")
    elif pilihan == "4":
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"Hasil Pembagian: {angka1} / {angka2} = {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    elif pilihan == "5":
        if angka2 != 0:
            hasil = angka1 // angka2
            print(f"Hasil Pembagian Bulat: {angka1} // {angka2} = {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan.")
    elif pilihan == "6":
        if angka2 != 0:
            hasil = angka1 % angka2
            print(f"Hasil Sisa Bagi: {angka1} % {angka2} = {hasil}")
        else:
            print("Error: Sisa bagi dengan nol tidak diperbolehkan.")
    elif pilihan == "7":
        print(f"Hasil Penjumlahan: {angka1} + {angka2} = {angka1 + angka2}")
        print(f"Hasil Pengurangan: {angka1} - {angka2} = {angka1 - angka2}")
        print(f"Hasil Perkalian: {angka1} * {angka2} = {angka1 * angka2}")
        if angka2 != 0:
            print(f"Hasil Pembagian: {angka1} / {angka2} = {angka1 / angka2}")
            print(f"Hasil Pembagian Bulat: {angka1} // {angka2} = {angka1 // angka2}")
            print(f"Hasil Sisa Bagi: {angka1} % {angka2} = {angka1 % angka2}")
        else:
            print("Error: Operasi pembagian dengan nol tidak diperbolehkan.")

    # Menanyakan apakah ingin melakukan perhitungan lagi
    ulang = input("\nApakah Anda ingin melakukan perhitungan lagi? (y/n): ")
    if ulang.lower() == "y":
        kalkulator()
    else:
        print("\nTerima kasih telah menggunakan kalkulator interaktif ini!")
        
    # Menjalankan program kalkulator
if __name__ == "__main__":
    kalkulator()