print("=" * 70)
print("SISTEM AUDIT KEAMANAN PASSWORD SECUREPASS")
print("D4 Rekayasa Keamanan Siber")
print("=" * 70)


def tampilkan_header():
    """Menampilkan header sistem."""
    print("\n" + "=" * 70)
    print("SISTEM AUDIT KEAMANAN PASSWORD SECUREPASS")
    print("=" * 70)

# Pemanggilan fungsi
tampilkan_header()


def validasi_ip(ip):
    bagian = ip.split(".")
    if len(bagian) != 4:
        return False
    for b in bagian:
        if not b.isdigit():
            return False
        if int(b) < 0 or int(b) > 255:
            return False
    return True


def klasifikasi_ip(ip, daftar_berbahaya):
    if ip in daftar_berbahaya:
        return "BERBAHAYA"
    elif (
        ip.startswith("192.168")
        or ip.startswith("10.")
        or ip.startswith("172.")
    ):
        return "IP PRIVAT"
    else:
        return "IP PUBLIK"


# Data untuk pengujian
ip_berbahaya = ["192.168.1.100", "10.0.0.1", "172.16.0.1"]

# Pemanggilan positional
print("\n--- PENGUJIAN FUNGSI POSITIONAL ---")
ip_test1 = "192.168.1.100"
ip_test2 = "8.8.8.8"
print(f"IP {ip_test1} valid? {validasi_ip(ip_test1)}")
print(f"IP {ip_test2} valid? {validasi_ip(ip_test2)}")
print(f"Klasifikasi {ip_test1}: {klasifikasi_ip(ip_test1, ip_berbahaya)}")
print(f"Klasifikasi {ip_test2}: {klasifikasi_ip(ip_test2, ip_berbahaya)}")


def validasi_login(username, password, ip):
    database = {
        "admin": {"password": "Admin123", "ip": "192.168.1.100"},
        "user1": {"password": "User123", "ip": "192.168.1.101"},
    }
    if username not in database:
        return "GAGAL Username tidak terdaftar"
    if password != database[username]["password"]:
        return "GAGAL Password salah"
    if ip != database[username]["ip"]:
        return "GAGAL IP tidak terdaftar"
    return f"BERHASIL Selamat datang {username}!"


# Pemanggilan keyword (urutan bebas)
print("\n--- PENGUJIAN FUNGSI KEYWORD ---")
hasil1 = validasi_login(
    username="admin", password="Admin123", ip="192.168.1.100"
)
hasil2 = validasi_login(ip="192.168.1.101", username="user1", password="User123")
hasil3 = validasi_login(username="admin", password="salah", ip="192.168.1.100")

print(f"Login 1: {hasil1}")
print(f"Login 2: {hasil2}")
print(f"Login 3: {hasil3}")


def scan_port(ip, port=80, protokol="TCP"):
    port_berbahaya = [21, 23, 25, 135, 445, 3389]
    if port in port_berbahaya:
        status = "TERBUKA BERBAHAYA"
    elif port < 1024:
        status = "TERBUKA PERLU VERIFIKASI"
    else:
        status = "TERTUTUP"
    return f"{ip}:{port}/{protokol} -> {status}"


# Pemanggilan dengan default
print("\n--- PENGUJIAN FUNGSI DEFAULT ---")
print(scan_port("192.168.1.100"))  # Pakai default port 80, TCP
print(scan_port("192.168.1.100", 443))  # Pakai default protokol TCP
print(scan_port("192.168.1.100", 21, "UDP"))  # Semua argumen diberikan


def pindai_banyak_port(ip, *ports):
    port_berbahaya = [21, 23, 25, 135, 445, 3389]
    jumlah_berbahaya = 0
    print(f"\nMemindai IP: {ip}")
    print(f"Total port yang dipindai: {len(ports)}")
    for port in ports:
        if port in port_berbahaya:
            status = "BERBAHAYA"
            jumlah_berbahaya += 1
        else:
            status = "AMAN"
        print(f" - Port {port}: {status}")
    return jumlah_berbahaya


# Pemanggilan dengan *args
print("\n--- PENGUJIAN FUNGSI ARGS ---")
total_bahaya = pindai_banyak_port("192.168.1.100", 21, 22, 80, 443, 445)
print(f"Total port berbahaya: {total_bahaya}")


def profil_analis(**data):
    print("\n--- PROFIL ANALIS ---")
    for key, value in data.items():
        # Mengubah format key dari underscore ke spasi
        label = key.replace("_", " ").title()
        print(f"{label:<20} : {value}")

    # Mengembalikan nama jika ada
    if "nama" in data:
        return data["nama"]
    return "Unknown"


# Pemanggilan dengan **kwargs
print("\n--- PENGUJIAN FUNGSI **KWARGS ---")
nama1 = profil_analis(
    nama="Budi Santoso", role="Security Analyst", shift="Malam", level=5
)
nama2 = profil_analis(nama="Siti Aminah", role="Penetration Tester")
print(f"\nAnalis yang bertugas: {nama1} dan {nama2}")


def analisis_password(password, username=""):
    karakter_spesial = "!@#$%^&*()_+-=[]{};:,.<>/?~"

    # Cek 6 kriteria
    k1 = len(password) >= 12
    k2 = sum(1 for c in password if c.isupper()) >= 2
    k3 = any(c.islower() for c in password)
    k4 = sum(1 for c in password if c.isdigit()) >= 3
    k5 = any(c in karakter_spesial for c in password)
    k6 = username.lower() not in password.lower() if username else True

    # Hitung skor
    skor = 0
    if k1:
        skor += 1
    if k2:
        skor += 1
    if k3:
        skor += 1
    if k4:
        skor += 1
    if k5:
        skor += 1
    if k6:
        skor += 1

    # Tentukan level
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

    # Detail kriteria sebagai list
    detail = [k1, k2, k3, k4, k5, k6]
    return skor, level, detail


# Pemanggilan dengan multiple return
print("\n--- PENGUJIAN MULTIPLE RETURN ---")
password_test = "Secure@2024!"
skor, level, detail = analisis_password(password_test, "admin")

print(f"Password                : {'*' * len(password_test)}")
print(f"Skor                    : {skor}/6")
print(f"Level                   : {level}")
print(f"Detail Kriteria:")
print(f" - Minimal 12 karakter  : {'YA' if detail[0] else 'TIDAK'}")
print(f" - Minimal 2 huruf besar: {'YA' if detail[1] else 'TIDAK'}")
print(f" - Mengandung huruf kecil : {'YA' if detail[2] else 'TIDAK'}")
print(f" - Minimal 3 angka      : {'YA' if detail[3] else 'TIDAK'}")
print(f" - Mengandung simbol khusus: {'YA' if detail[4] else 'TIDAK'}")
print(f" - Tidak mengandung username: {'YA' if detail[5] else 'TIDAK'}")


total_audit_global = 0
log_audit = []


def catat_audit(username, skor, level):
    # Menggunakan global untuk mengubah variabel global
    global total_audit_global

    # Variabel lokal (hanya ada di dalam fungsi ini)
    status_aman = skor >= 5

    # Menambah counter global
    total_audit_global += 1

    # Menambah entri ke log global
    entri = {
        "no": total_audit_global,
        "username": username,
        "skor": skor,
        "level": level,
        "aman": status_aman,
    }
    log_audit.append(entri)

    # Return status lokal
    return status_aman


def tampilkan_log_audit():
    """Menampilkan seluruh log audit dari variabel global."""
    print("\n--- LOG AUDIT ---")
    print(
        f"{'No':<4} | {'Username':<12} | {'Skor':<6} | {'Level':<15} | {'Status':<10}"
    )
    print("-" * 60)
    for entri in log_audit:
        status = "AMAN" if entri["aman"] else "PERLU PERBAIKAN"
        print(
            f"{entri['no']:<4} | {entri['username']:<12} | "
            f"{entri['skor']}/6 | {entri['level']:<15} | {status:<10}"
        )


# Pengujian scope variabel
print("\n--- PENGUJIAN SCOPE VARIABEL ---")
print(f"Total audit sebelum: {total_audit_global}")

# Audit beberapa user
users = [
    ("admin", "Admin123"),
    ("user1", "User1Pass!"),
    ("security", "Secur3P@ssword2024"),
    ("guest", "guest"),
]

for user, pwd in users:
    skor_u, level_u, _ = analisis_password(pwd, user)
    status = catat_audit(user, skor_u, level_u)
    print(f"Audit {user}: skor {skor_u}/6, level {level_u}, aman={status}")

print(f"\nTotal audit setelah: {total_audit_global}")
tampilkan_log_audit()


def deteksi_ancaman_login():
    print("\n")
    print("=" * 70)
    print("DETEKSI ANCAMAN LOGIN TERINTEGRASI")
    print("=" * 70)

    # Input
    username = input("Masukkan Username: ")
    ip_input = input("Masukkan Alamat IP: ")
    password = input("Masukkan Password: ")

    # 1. Validasi IP
    if not validasi_ip(ip_input):
        print("\nERROR: Format IP tidak valid!")
        return

    # 2. Klasifikasi IP
    status_ip = klasifikasi_ip(ip_input, ip_berbahaya)

    # 3. Analisis Password
    skor, level, detail = analisis_password(password, username)

    # 4. Penentuan tingkat ancaman (nested if)
    is_ip_berbahaya = status_ip == "BERBAHAYA"
    is_password_lemah = skor < 3
    is_username_mencurigakan = username in ["admin", "root", "guest"]

    if is_ip_berbahaya and is_username_mencurigakan and is_password_lemah:
        tingkat = "TINGGI"
        rekomendasi = "Segera blokir IP dan lakukan investigasi menyeluruh"
    elif is_ip_berbahaya and (is_username_mencurigakan or is_password_lemah):
        tingkat = "SEDANG"
        rekomendasi = "Lakukan monitoring ketat dan verifikasi dengan user"
    elif is_ip_berbahaya:
        tingkat = "RENDAH"
        rekomendasi = "Pantau aktivitas user dan catat dalam log"
    elif is_username_mencurigakan and is_password_lemah:
        tingkat = "SEDANG"
        rekomendasi = "Verifikasi identitas user dan sarankan ganti password"
    elif is_username_mencurigakan or is_password_lemah:
        tingkat = "RENDAH"
        rekomendasi = "Pantau aktivitas user"
    else:
        tingkat = "AMAN"
        rekomendasi = "Tidak ada tindakan yang diperlukan"

    # 5. Tampilkan laporan
    print("\n" + "=" * 70)
    print("LAPORAN ANALISIS ANCAMAN")
    print("=" * 70)
    print(f"Username              : {username}")
    print(f"IP Address            : {ip_input}")
    print(f"Status IP             : {status_ip}")
    print(f"Password              : {'*' * len(password)}")
    print(f"Skor Password         : {skor}/6")
    print(f"Level Password        : {level}")
    print(f"Tingkat Ancaman       : {tingkat}")
    print(f"Rekomendasi           : {rekomendasi}")
    print("=" * 70)

    # Catat ke log
    catat_audit(username, skor, level)


# Jalankan studi kasus terintegrasi (komentar jika dijalankan otomatis)
# deteksi_ancaman_login()


def audit_batch(daftar_pengguna):
    statistik = {
        "total": 0,
        "sangat_kuat": 0,
        "kuat": 0,
        "sedang": 0,
        "lemah": 0,
        "sangat_lemah": 0,
    }

    print("\n--- HASIL AUDIT BATCH ---")
    print(
        f"{'User':<12} | {'Password':<18} | {'Skor':<6} | {'Level':<15}"
    )
    print("-" * 65)

    for pengguna in daftar_pengguna:
        user = pengguna["username"]
        pwd = pengguna["password"]
        skor, level, _ = analisis_password(pwd, user)

        statistik["total"] += 1
        if level == "SANGAT KUAT":
            statistik["sangat_kuat"] += 1
        elif level == "KUAT":
            statistik["kuat"] += 1
        elif level == "SEDANG":
            statistik["sedang"] += 1
        elif level == "LEMAH":
            statistik["lemah"] += 1
        else:
            statistik["sangat_lemah"] += 1

        pwd_tampil = "*" * len(pwd)
        print(f"{user:<12} | {pwd_tampil:<18} | {skor}/6 | {level:<15}")

    return statistik


# Data pengguna
daftar_pengguna = [
    {"username": "admin", "password": "admin"},
    {"username": "user1", "password": "User123"},
    {"username": "security", "password": "Secur3P@ssword2024"},
    {"username": "manager", "password": "M@nager2024!X"},
    {"username": "guest", "password": "12345678"},
]

statistik = audit_batch(daftar_pengguna)
print("\n--- STATISTIK AUDIT ---")
print(f"Total pengguna        : {statistik['total']}")
print(f"Sangat Kuat           : {statistik['sangat_kuat']}")
print(f"Kuat                  : {statistik['kuat']}")
print(f"Sedang                : {statistik['sedang']}")
print(f"Lemah                 : {statistik['lemah']}")
print(f"Sangat Lemah          : {statistik['sangat_lemah']}")


def laporan_analis(nama, role, *keahlian, level=1, **info_tambahan):
    laporan = {
        "nama": nama,
        "role": role,
        "keahlian": list(keahlian),
        "level": level,
        "info": info_tambahan,
    }

    print(f"\n--- LAPORAN ANALIS: {nama} ---")
    print(f"Role                  : {role}")
    print(f"Level                 : {level}")
    print(f"Keahlian              : {', '.join(keahlian)}")
    if info_tambahan:
        print("Info Tambahan:")
        for key, value in info_tambahan.items():
            label = key.replace("_", " ").title()
            print(f" - {label} : {value}")
    return laporan


# Pemanggilan dengan semua jenis parameter
print("\n--- PENGUJIAN KOMBINASI PARAMETER LENGKAP ---")
laporan1 = laporan_analis(
    "Budi Santoso",
    "Senior Analyst",
    "Penetration Testing",
    "Incident Response",
    "Forensik Digital",
    level=5,
    sertifikasi="CEH, OSCP",
    tahun_bergabung=2018,
)

laporan2 = laporan_analis("Siti Aminah", "Junior Analyst", "Network Security", level=2)


print("\n")
print("=" * 70)
print("PRAKTIKUM FUNGSI SELESAI")
print("=" * 70)
print("\nMateri yang telah dipraktikkan:")
print(" 1. Fungsi sederhana tanpa parameter")
print(" 2. Fungsi dengan positional argument")
print(" 3. Fungsi dengan keyword argument")
print(" 4. Fungsi dengan default argument")
print(" 5. Fungsi dengan *args (variadic positional)")
print(" 6. Fungsi dengan **kwargs (variadic keyword)")
print(" 7. Fungsi dengan multiple return values")
print(" 8. Ruang lingkup variabel (local vs global)")
print(" 9. Studi kasus terintegrasi")
print(" 10. Kombinasi lengkap semua parameter")
print("=" * 70)