# =================================================================
# MODUL PRAKTIKUM 2: SISTEM KEAMANAN DASAR
# Mata Kuliah: Algoritma Pemrograman
# Prodi: D4 Rekayasa Keamanan Siber
# =================================================================

print("=" * 60)
print("SISTEM KEAMANAN DASAR")
print("D4 Rekayasa Keamanan Siber")
print("=" * 60)

# =================================================================
# DATABASE USER (3 User)
# =================================================================

database_user = [
    {
        "username": "admin",
        "password": "Admin123",
        "role": "admin",
        "ip": "192.168.1.100"
    },
    {
        "username": "user1",
        "password": "User123",
        "role": "user",
        "ip": "192.168.1.101"
    },
    {
        "username": "security",
        "password": "Secure@2024",
        "role": "security",
        "ip": "192.168.1.102"
    }
]

# Variabel untuk menyimpan data user yang login
user_login = None
role_login = None
ip_login = None

# =================================================================
# BAGIAN 1: FUNGSI LOGIN SEDERHANA
# =================================================================

print("\n")
print("=" * 60)
print("BAGIAN 1: FUNGSI LOGIN SEDERHANA")
print("=" * 60)

print("\n--- SILAKAN LOGIN KE SISTEM ---")

# Meminta input dari pengguna untuk proses login
username = input("Masukkan Username: ")
password = input("Masukkan Password: ")
ip_akses = input("Masukkan Alamat IP: ")

# Cari user di database
user_ditemukan = None

for user in database_user:
    if user["username"] == username:
        user_ditemukan = user
        break

if user_ditemukan is None:
    print("\nSTATUS: LOGIN GAGAL")
    print("- Username tidak terdaftar")
    print("\n" + "=" * 60)
    print("PROGRAM BERAKHIR")
    print("Username tidak terdaftar.")
    print("=" * 60)
    exit()

is_password_benar = password == user_ditemukan["password"]
is_ip_terdaftar = ip_akses == user_ditemukan["ip"]

if is_password_benar and is_ip_terdaftar:
    user_login = username
    role_login = user_ditemukan["role"]
    ip_login = ip_akses

    print("\n" + "=" * 60)
    print("STATUS: LOGIN BERHASIL")
    print(f"Selamat datang, {username}!")
    print(f"Role: {role_login}")
    print("=" * 60)

else:
    print("\nSTATUS: LOGIN GAGAL")
    print("Akses ditolak")

    if not is_password_benar:
        print("- Password salah")

    if not is_ip_terdaftar:
        print("- Alamat IP tidak terdaftar")

    print("\n" + "=" * 60)
    print("PROGRAM BERAKHIR")
    print("Login gagal.")
    print("=" * 60)
    exit()


# =================================================================
# BAGIAN 2: ANALISIS KEKUATAN PASSWORD
# =================================================================

print("\n")
print("=" * 60)
print("BAGIAN 2: ANALISIS KEKUATAN PASSWORD")
print("=" * 60)

# Menggunakan username yang sudah login untuk pengecekan
username_untuk_cek = user_login

print(
    f"\nUsername yang digunakan untuk pengecekan: "
    f"{username_untuk_cek}"
)

# Meminta input password dari pengguna
password = input("Masukkan password yang akan dianalisis: ")

# Menghitung panjang password menggunakan fungsi len()
panjang = len(password)

# Kriteria 1: Minimal 10 karakter
kriteria1 = panjang >= 10

# Kriteria 2: Minimal 2 huruf besar
jumlah_huruf_besar = sum(
    1 for c in password if c.isupper()
)
kriteria2 = jumlah_huruf_besar >= 2

# Kriteria 3: Minimal 2 huruf kecil
jumlah_huruf_kecil = sum(
    1 for c in password if c.islower()
)
kriteria3 = jumlah_huruf_kecil >= 2

# Kriteria 4: Minimal 2 angka
jumlah_angka = sum(
    1 for c in password if c.isdigit()
)
kriteria4 = jumlah_angka >= 2

# Kriteria 5: Minimal 2 karakter spesial
karakter_spesial = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

jumlah_spesial = sum(
    1 for c in password if c in karakter_spesial
)

kriteria5 = jumlah_spesial >= 2

# Kriteria 6: Tidak mengandung username
kriteria6 = username_untuk_cek.lower() not in password.lower()

# Menghitung skor kekuatan password
# Setiap kriteria yang terpenuhi bernilai 1 poin

skor = 0

if kriteria1:
    skor = skor + 1

if kriteria2:
    skor = skor + 1

if kriteria3:
    skor = skor + 1

if kriteria4:
    skor = skor + 1

if kriteria5:
    skor = skor + 1

if kriteria6:
    skor = skor + 1

# Menentukan level kekuatan password berdasarkan skor
# Skor maksimal adalah 6

if skor >= 6:
    level = "SANGAT KUAT"
elif skor >= 5:
    level = "KUAT"
elif skor >= 3:
    level = "SEDANG"
elif skor >= 1:
    level = "LEMAH"
else:
    level = "SANGAT LEMAH"

# Menampilkan hasil analisis password
print("\n--- HASIL ANALISIS PASSWORD ---")
print(f"Password : {'*' * panjang}")
print(f"Panjang : {panjang} karakter")
print(f"Skor     : {skor}/6")
print(f"Level    : {level}")

print("\nDetail Kriteria:")

print(
    f"- Minimal 10 karakter      : "
    f"{'YA' if kriteria1 else 'TIDAK'} ({panjang})"
)

print(
    f"- Minimal 2 Huruf Besar    : "
    f"{'YA' if kriteria2 else 'TIDAK'} "
    f"({jumlah_huruf_besar})"
)

print(
    f"- Minimal 2 Huruf Kecil    : "
    f"{'YA' if kriteria3 else 'TIDAK'} "
    f"({jumlah_huruf_kecil})"
)

print(
    f"- Minimal 2 Angka          : "
    f"{'YA' if kriteria4 else 'TIDAK'} "
    f"({jumlah_angka})"
)

print(
    f"- Minimal 2 Spesial        : "
    f"{'YA' if kriteria5 else 'TIDAK'} "
    f"({jumlah_spesial})"
)

print(
    f"- Tidak mengandung username : "
    f"{'YA' if kriteria6 else 'TIDAK'}"
)

# Memberikan rekomendasi perbaikan
print("\n--- REKOMENDASI PERBAIKAN ---")

if not kriteria1:
    print("- Tambah panjang password minimal 10 karakter")

if not kriteria2:
    print("- Tambahkan minimal 2 huruf besar (A-Z)")

if not kriteria3:
    print("- Tambahkan minimal 2 huruf kecil (a-z)")

if not kriteria4:
    print("- Tambahkan minimal 2 angka (0-9)")

if not kriteria5:
    print("- Tambahkan minimal 2 karakter spesial (!, @, #, $, %)")

if not kriteria6:
    print("- Password tidak boleh mengandung username")

if skor >= 5:
    print("\nPassword Anda sudah baik. Pertahankan keamanannya")


# =================================================================
# BAGIAN 3: ANALISIS JARINGAN DAN IP
# =================================================================

print("\n")
print("=" * 60)
print("BAGIAN 3: ANALISIS JARINGAN DAN IP")
print("=" * 60)

# Memasukkan data alamat IP untuk dianalisis
ip_address = input(
    "\nMasukkan alamat IP yang akan dianalisis: "
)

# Memisahkan alamat IP menjadi 4 bagian berdasarkan titik
# split('.') digunakan untuk memecah string menjadi list
# Contoh:
# "192.168.1.100"
# menjadi
# ["192", "168", "1", "100"]

bagian_ip = ip_address.split('.')

# Daftar IP yang dikenal sebagai IP berbahaya
ip_berbahaya = [
    "192.168.1.100",
    "10.0.0.1",
    "172.16.0.1"
]

# Daftar port berbahaya yang umum digunakan untuk serangan
port_berbahaya = [
    21,
    23,
    25,
    135,
    445,
    3389,
    1433,
    1434
]

port_aman = [
    80,
    443,
    22,
    3306,
    5432
]

# Analisis alamat IP
print("\n--- ANALISIS ALAMAT IP ---")

if len(bagian_ip) == 4:
    print(f"IP Address : {ip_address}")

    # Menampilkan setiap oktet dari IP
    print(f"Oktet 1     : {bagian_ip[0]}")
    print(f"Oktet 2     : {bagian_ip[1]}")
    print(f"Oktet 3     : {bagian_ip[2]}")
    print(f"Oktet 4     : {bagian_ip[3]}")

    # Mengecek apakah IP termasuk dalam daftar berbahaya
    is_ip_berbahaya = ip_address in ip_berbahaya

    if is_ip_berbahaya:
        print("\nSTATUS IP: BERBAHAYA")
        print("IP ini terdaftar dalam daftar IP berbahaya")
    else:
        print("\nSTATUS IP: AMAN")
        print("IP ini tidak terdaftar dalam daftar IP berbahaya")

else:
    print(
        "Format IP tidak valid. "
        "Gunakan format xxx.xxx.xxx.xxx"
    )


# Analisis port jaringan
print("\n--- ANALISIS PORT JARINGAN ---")

# Meminta input port dari pengguna
port_input = input(
    "Masukkan nomor port yang akan diperiksa: "
)

# Konversi input string ke integer
port = int(port_input)

# Mengecek status port
is_port_berbahaya = port in port_berbahaya
is_port_aman = port in port_aman

# Menentukan status port
if is_port_berbahaya:
    status_port = "BERBAHAYA"
    rekomendasi = (
        "Tutup port ini karena sering digunakan untuk serangan"
    )

elif is_port_aman:
    status_port = "AMAN"
    rekomendasi = "Port ini aman untuk digunakan"

else:
    status_port = "TIDAK DIKETAHUI"
    rekomendasi = "Perlu investigasi lebih lanjut"

print(f"\nPort        : {port}")
print(f"Status      : {status_port}")
print(f"Rekomendasi : {rekomendasi}")


# =================================================================
# BAGIAN 4: LAPORAN KEAMANAN LENGKAP
# =================================================================

print("\n")
print("=" * 60)
print("BAGIAN 4: LAPORAN KEAMANAN LENGKAP")
print("=" * 60)

# Menggabungkan semua data yang sudah dianalisis
print("\n--- LAPORAN KEAMANAN SISTEM ---")
print("Tanggal : 2024-09-03")
print("============================================================")

# Laporan Login
print("\n[1] LAPORAN LOGIN")

if user_login is not None:
    print(f"     Username       : {user_login}")
    print(f"     Role           : {role_login}")
    print(f"     IP Akses       : {ip_login}")
    print("     Status         : BERHASIL")
else:
    print("     Status         : GAGAL")


# Laporan Password
print("\n[2] LAPORAN PASSWORD")
print(f"     Password       : {'*' * len(password)}")
print(f"     Skor           : {skor}/6")
print(f"     Level          : {level}")


# Laporan Port
print("\n[3] LAPORAN PORT")
print(f"     Port           : {port}")
print(f"     Status         : {status_port}")


# Laporan IP
print("\n[4] LAPORAN IP")

if user_login is not None:
    print(f"     IP Address     : {ip_login}")

    # Cek apakah IP terdaftar di database
    ip_terdaftar = False

    for user in database_user:
        if user["ip"] == ip_login:
            ip_terdaftar = True
            break

    if ip_terdaftar:
        print("     Status         : TERDAFTAR")
    else:
        print("     Status         : TIDAK TERDAFTAR")

else:
    print("     Status         : BELUM LOGIN")


# Rekomendasi Kesimpulan
print("\n============================================================")
print("KESIMPULAN DAN REKOMENDASI")

if user_login is not None and skor >= 5 and is_port_aman:
    print(
        "SISTEM AMAN. Semua komponen dalam kondisi baik"
    )

elif user_login is not None and skor <= 2:
    print(
        "PERINGATAN: Password lemah. "
        "Segera ganti dengan password yang lebih kuat"
    )

elif user_login is None:
    print(
        "PERINGATAN: Upaya login gagal. "
        "Periksa kembali kredensial Anda"
    )

elif is_port_berbahaya:
    print(
        "PERINGATAN: Port berbahaya terdeteksi. "
        "Segera lakukan penutupan port"
    )

else:
    print(
        "Perlu dilakukan evaluasi keamanan lebih lanjut"
    )

print("=" * 60)
print("AKHIR LAPORAN")
print("=" * 60)