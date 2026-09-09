# ============================================================
# SISTEM KEAMANAN DASAR
# TUGAS KE 2
# D4 Rekayasa Keamanan Siber
# ============================================================

print("=" * 60)
print("SISTEM KEAMANAN DASAR")
print("D4 Rekayasa Keamanan Siber")
print("=" * 60)

# ============================================================
# DATABASE USER
# ============================================================

database_user = [
    {"username": "admin", "password": "Admin123", "role": "admin", "ip": "192.168.1.100"},
    {"username": "user1", "password": "User123", "role": "user", "ip": "192.168.1.101"},
    {"username": "security", "password": "Secure@2024", "role": "security", "ip": "192.168.1.102"},
]

# Variable untuk menyimpan data user yang login
user_login = None
role_login = None
ip_login = None

# ============================================================
# BAGIAN 1: FUNGSI LOGIN
# ============================================================

print("\n")
print("=" * 60)
print("BAGIAN 1: FUNGSI LOGIN")
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
    print("Username tidak terdaftar")
    exit()

is_password_benar = password == user_ditemukan["password"]
is_ip_terdaftar = ip_akses == user_ditemukan["ip"]

if is_password_benar and is_ip_terdaftar:
    user_login = username
    role_login = user_ditemukan["role"]
    ip_login = ip_akses
    print("\n""STATUS: LOGIN BERHASIL")
    print(f"Selamat datang, {username}")
    print(f"Role: {role_login}")
else:
    print("\nSTATUS: LOGIN GAGAL")
    print("Akses ditolak")
    if not is_password_benar:
        print("- Password salah")
    if not is_ip_terdaftar:
        print("- Alamat IP tidak terdaftar")
    print("\n" + "=" * 60)
    print("PROGRAM BERAKHIR")
    print("Login gagal")
    print("=" * 60)
    exit()

# ============================================================
# BAGIAN 2: ANALISIS KEKUATAN PASSWORD
# ============================================================

print("\n")
print("=" * 60)
print("BAGIAN 2: ANALISIS KEKUATAN PASSWORD")
print("=" * 60)

# Menggunakan username yang sudah login untuk pengecekan
username_untuk_cek = user_login
print(f"\nUsername yang digunakan untuk pengecekan: {username_untuk_cek}")

# Meminta input password dari pengguna
password = input("Masukkan password yang akan dianalisis: ")

# Menhitung panjang password
panjang = len(password)

# Kriteria 1: Minimal 10 karakter
kriteria1 = panjang >= 10

# Kriteria 2: Minimal 2 huruf besar
jumlah_huruf_besar = sum(1 for c in password if c.isupper())
kriteria2 = jumlah_huruf_besar >= 2

# Kriteria 3: Minimal 2 huruf kecil
jumlah_huruf_kecil = sum(1 for c in password if c.islower())
kriteria3 = jumlah_huruf_kecil >= 2

# Kriteria 4: Minimal 2 angka
jumlah_angka = sum(1 for c in password if c.isdigit())
kriteria4 = jumlah_angka >= 2

# Kriteria 5: Minimal 2 karakter spesial
karakter_spesial = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
jumlah_spesial = sum(1 for c in password if c in karakter_spesial)
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

if skor == 6:
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
print(f"Panjang  : {panjang} karakter")
print(f"Skor     : {skor}/6")
print(f"Level    : {level}")

print("\nDetail Kriteria:")
print(f"- Minimal 10 karakter        : {'YA' if kriteria1 else 'TIDAK'} ({panjang})")
print(f"- Minimal 2 huruf besar      : {'YA' if kriteria2 else 'TIDAK'} ({jumlah_huruf_besar})")
print(f"- Minimal 2 huruf kecil      : {'YA' if kriteria3 else 'TIDAK'} ({jumlah_huruf_kecil})")
print(f"- Minimal 2 angka            : {'YA' if kriteria4 else 'TIDAK'} ({jumlah_angka})")
print(f"- Minimal 2 karakter spesial : {'YA' if kriteria5 else 'TIDAK'} ({jumlah_spesial})")
print(f"- Tidak mengandung username  : {'YA' if kriteria6 else 'TIDAK'}")

# Memberikan rekomendasi perbaikan
print("\n--- REKOMENDASI PERBAIKAN ---")

if not kriteria1:
    print("- Tambah panjang password minimal 10 karakter")

if not kriteria2:
    print("- Tambahkan minimal 2 huruf besar (A-Z)")

if not kriteria3:
    print("- Tambahkan minimal 2 huruf kecil (a-z)")

if not kriteria4:
    print("- Tambah jumlah angka minimal 2")

if not kriteria5:
    print("- Tambah jumlah karakter spesial minimal 2")

if not kriteria6:
    print("- Ubah password untuk tidak mengandung username")
if skor >= 5:
    print("\nPassword Anda sudah baik. Pertahankan keamanannya")