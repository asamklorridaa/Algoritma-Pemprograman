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

    