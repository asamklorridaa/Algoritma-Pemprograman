# ============================================================
# SISTEM KEAMANAN DASAR
# D4 Rekayasa Keamanan Siber
# ============================================================

print("=" * 60)
print("SISTEM KEAMANAN DASAR")
print("D4 Rekayasa Keamanan Siber")
print("=" * 60)

# ============================================================
# BAGIAN 1: FUNGSI LOGIN SEDERHANA
# ============================================================
print("\n")
print("=" * 60)
print("BAGIAN 1: FUNGSI LOGIN SEDERHANA")
print("=" * 60)

# Mendeklarasikan variabel untuk menyimpan data kredensial
# Data ini berfungsi seperti database sederhana
username_valid = "admin"
password_valid = "Admin123!"
ip_terdaftar = "192.168.1.100"

print("\n--- SILAKAN LOGIN KE SISTEM ---")

# Meminta input dari pengguna untuk proses login
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")
ip_akses = input("Masukkan Alamat IP: ")

# Proses validasi login
# Operator perbandingan digunakan untuk memeriksa kesesuaian data
is_username_benar = username == username_valid
is_password_benar = password == password_valid
is_ip_terdaftar = ip_akses == ip_terdaftar

# Operator logika AND digunakan untuk memastikan semua kondisi terpenuhi
is_login_berhasil = is_username_benar and is_password_benar and is_ip_terdaftar

# Menampilkan hasil login
print("\n--- HASIL LOGIN ---")
print(f"Username : {username}")
print(f"Password : {'*' * len(password)}")
print(f"Alamat IP: {ip_akses}")

if is_login_berhasil:
    print("\nSTATUS: LOGIN BERHASIL")
    print("Selamat datang di Dashboard Keamanan Siber")
else:
    print("\nSTATUS: LOGIN GAGAL")
    print("Akses ditolak")

# Memberikan informasi spesifik penyebab kegagalan
if not is_username_benar:
    print("- Username tidak terdaftar")
if not is_password_benar:
    print("- Password salah")
if not is_ip_terdaftar:
    print("- Alamat IP tidak terdaftar")


# ============================================================
# BAGIAN 2: ANALISIS KEKUATAN PASSWORD
# ============================================================
print("\n")
print("=" * 60)
print("BAGIAN 2: ANALISIS KEKUATAN PASSWORD")
print("=" * 60)

# Meminta input password dari pengguna
password = input("\nMasukkan password yang akan dianalisis: ")

# Menghitung panjang password menggunakan fungsi len()
panjang = len(password)

# Mengecek karakteristik password menggunakan fungsi any() dan method string
# c.isupper() = mengecek apakah huruf besar
# c.islower() = mengecek apakah huruf kecil
# c.isdigit() = mengecek apakah angka
# c.isalnum() = mengecek apakah alfanumerik (huruf atau angka)
# not c.isalnum() = mengecek apakah karakter spesial

memiliki_huruf_besar = any(c.isupper() for c in password)
memiliki_huruf_kecil = any(c.islower() for c in password)
memiliki_angka = any(c.isdigit() for c in password)
memiliki_spesial = any(not c.isalnum() for c in password)

# Menghitung jumlah angka dalam password
jumlah_angka = sum(1 for c in password if c.isdigit())

# Perhitungan Skor
skor = 0

if panjang >= 8:
    skor = skor + 1
if memiliki_huruf_besar:
    skor = skor + 1
if memiliki_huruf_kecil:
    skor = skor + 1
if memiliki_angka:
    skor = skor + 1
if memiliki_spesial:
    skor = skor + 1

# Menentukan level kekuatan password berdasarkan skor (skor maksimal = 5)
if skor >= 5:
    level = "SANGAT KUAT"
elif skor >= 4:
    level = "KUAT"
elif skor >= 3:
    level = "SEDANG"
elif skor >= 2:
    level = "LEMAH"
else:
    level = "SANGAT LEMAH"

# Menampilkan hasil analisis password
print("\n--- HASIL ANALISIS PASSWORD ---")
print(f"Password : {'*' * panjang}")
print(f"Panjang  : {panjang} karakter")
print(f"Skor     : {skor}/5")
print(f"Level    : {level}")

print("\nDetail Kriteria:")
print(f"- Minimal 8 karakter     : {'YA' if panjang >= 8 else 'TIDAK'}")
print(f"- Mengandung Huruf Besar : {'YA' if memiliki_huruf_besar else 'TIDAK'}")
print(f"- Mengandung Huruf Kecil : {'YA' if memiliki_huruf_kecil else 'TIDAK'}")
print(f"- Mengandung Angka       : {'YA' if memiliki_angka else 'TIDAK'}")
print(f"- Mengandung Spesial     : {'YA' if memiliki_spesial else 'TIDAK'}")
print(f"- Jumlah Angka           : {jumlah_angka}")

# Memberikan rekomendasi perbaikan
print("\n--- REKOMENDASI PERBAIKAN ---")

if panjang < 8:
    print("- Tambah panjang password minimal 8 karakter")

if not memiliki_huruf_besar:
    print("- Tambahkan huruf besar seperti A, B, C")

if not memiliki_huruf_kecil:
    print("- Tambahkan huruf kecil seperti a, b, c")

if not memiliki_angka:
    print("- Tambahkan angka seperti 1, 2, 3")

if not memiliki_spesial:
    print("- Tambahkan karakter spesial seperti !, @, #, $")

if jumlah_angka < 2:
    print("- Tambahkan minimal 2 angka dalam password")

if skor >= 4:
    print("\nPassword Anda sudah baik. Pertahankan keamanannya")


# ============================================================
# BAGIAN 3: ANALISIS JARINGAN DAN IP
# ============================================================
print("\n")
print("=" * 60)
print("BAGIAN 3: ANALISIS JARINGAN DAN IP")
print("=" * 60)

# Memasukkan data alamat IP untuk dianalisis
ip_address = input("\nMasukkan alamat IP yang akan dianalisis: ")

bagian_ip = ip_address.split('.')

# Daftar IP yang dikenal sebagai IP berbahaya
ip_berbahaya = ["192.168.1.100", "10.0.0.1", "172.16.0.1"]

# Analisis alamat IP
print("\n--- ANALISIS ALAMAT IP ---")

if len(bagian_ip) == 4:
    print(f"IP Address : {ip_address}")
    
    # Menampilkan setiap oktet dari IP
    print(f"Oktet 1    : {bagian_ip}")
    print(f"Oktet 2    : {bagian_ip[1]}")
    print(f"Oktet 3    : {bagian_ip[2]}")
    print(f"Oktet 4    : {bagian_ip[3]}")
    
    # Mengecek apakah IP termasuk dalam daftar berbahaya
    is_ip_berbahaya = ip_address in ip_berbahaya
    
    if is_ip_berbahaya:
        print("\nSTATUS IP: BERBAHAYA")
        print("IP ini terdaftar dalam daftar IP berbahaya")
    else:
        print("\nSTATUS IP: AMAN")
        print("IP ini tidak terdaftar dalam daftar IP berbahaya")
else:
    print("Format IP tidak valid. Gunakan format xxx.xxx.xxx.xxx")


# Daftar port berbahaya dan aman
port_berbahaya = [21, 23, ]
port_aman = [80, 443, 53, 161]

# Analisis port jaringan
print("\n--- ANALISIS PORT JARINGAN ---")

# Meminta input port dari pengguna
port_input = input("Masukkan nomor port yang akan diperiksa: ")

# Konversi input string ke integer
port = int(port_input)

# Mengecek status port
is_port_berbahaya = port in port_berbahaya
is_port_aman = port in port_aman

# Menentukan status port
if is_port_berbahaya:
    status_port = "BERBAHAYA"
    rekomendasi = "Tutup port ini karena sering digunakan untuk serangan"
elif is_port_aman:
    status_port = "AMAN"
    rekomendasi = "Port ini aman untuk digunakan"
else:
    status_port = "TIDAK DIKETAHUI"
    rekomendasi = "Perlu investigasi lebih lanjut"

print(f"\nPort      : {port}")
print(f"Status      : {status_port}")
print(f"Rekomendasi : {rekomendasi}")


# ============================================================
# BAGIAN 4: LAPORAN KEAMANAN LENGKAP
# ============================================================
print("\n")
print("=" * 60)
print("BAGIAN 4: LAPORAN KEAMANAN LENGKAP")
print("=" * 60)

# Menggabungkan semua data yang sudah dianalisis
print("\n--- LAPORAN KEAMANAN SISTEM ---")
print("Tanggal : 2024-09-03")
print("=" * 60)

# Laporan Login
print("\n[1] LAPORAN LOGIN")
print(f"    Username    : {username}")
print(f"    IP Akses    : {ip_akses}")
if is_login_berhasil:
    print("    Status      : BERHASIL")
else:
    print("    Status      : GAGAL")

# Laporan Password
print("\n[2] LAPORAN PASSWORD")
print(f"    Password    : {'*' * len(password)}")
print(f"    Skor        : {skor}/5")
print(f"    Level       : {level}")

# Laporan Port
print("\n[3] LAPORAN PORT")
print(f"    Port        : {port}")
print(f"    Status      : {status_port}")

# Laporan IP
print("\n[4] LAPORAN IP")
print(f"    IP Address  : {ip_akses}")
if ip_akses == ip_terdaftar:
    print("    Status      : TERDAFTAR")
else:
    print("    Status      : TIDAK TERDAFTAR")

# Kesimpulan dan Rekomendasi
print("\n" + "=" * 60)
print("KESIMPULAN DAN REKOMENDASI")

if is_login_berhasil and level in ["KUAT", "SANGAT KUAT"] and is_port_aman:
    print("SISTEM AMAN. Semua komponen dalam kondisi baik")
elif is_login_berhasil and level in ["SANGAT LEMAH", "LEMAH"]:
    print("PERINGATAN: Password lemah. Segera ganti dengan password yang lebih kuat")
elif not is_login_berhasil:
    print("PERINGATAN: Upaya login gagal. Periksa kembali kredensial Anda")
elif is_port_berbahaya:
    print("PERINGATAN: Port berbahaya terdeteksi. Segera lakukan penutupan port")
else:
    print("Perlu dilakukan evaluasi keamanan lebih lanjut")

print("=" * 60)
print("AKHIR LAPORAN")
print("=" * 60)
