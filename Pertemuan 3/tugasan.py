# ==========================================
# 1. Database Global
# ==========================================

database_user = []

IP_BERBAHAYA = ["192.168.1.100", "192.186.1.100", "129.168.1.100",
                "10.0.0.1", "172.16.0.1"]

USERNAME_MENCURIGAKAN = ["admin", "root", "guest"]


# ==========================================
# 1. Utility Functions
# ==========================================

def tanya_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(" [!] input harus berupa angka")

def garis(panjang=70, karakter="="):
    print(karakter * panjang)

def judul(teks):
    garis()
    print(f"  {teks}")
    garis()

def sub(teks):
    print(f"\n[ {teks} ]")
    garis(70, "-")

def validasi_format_ip(ip):
    oktet = ip.split(".")
    if len(oktet) != 4:
        return False
    for o in oktet:
        if not o.isdigit():
            return False
        if not (0 <= int(o) <= 255):
            return False
    return True

def input_ip_valid(prompt=" Alamat IP (xxx.xxx.xxx.xxx): "):
    while True:
        ip = input(prompt).strip()
        if validasi_format_ip(ip):
            return ip
        print(" [!] Format IP tidak valid, gunakan format xxx.xxx.xxx.xxx")


# ==========================================
# 2. Registrasi User
# ==========================================

def registrasi_user():
    judul("REGISTRASI USER BARU")

    sub("Input Data User")
    username = input(" Username baru : ").strip()
    password = input(" Password baru : ")
    ip = input_ip_valid(" Alamat IP     : ")

    database_user.append({
        "username": username,
        "password": password,
        "ip": ip
    })

    sub("Hasil Registrasi")
    print(f" Registrasi user '{username}' BERHASIL disimpan ke database_user")
    print(f" Total user terdaftar saat ini: {len(database_user)}")
    return username


# ==========================================
# 3. Login User
# ==========================================

def cari_user(username):
    for user in database_user:
        if user["username"] == username:
            return user
    return None

def login_user(username=None, password=None, ip=None, tampilkan_judul=True):
    if tampilkan_judul:
        judul("LOGIN USER")
        sub("Input Kredensial")

    if username is None:
        username = input(" Username : ").strip()
    if password is None:
        password = input(" Password : ")
    if ip is None:
        ip = input_ip_valid(" Alamat IP: ")

    sub("Proses Validasi")
    user = cari_user(username)
    status = "GAGAL"
    alasan = ""

    if user is None:
        alasan = "Username tidak ditemukan"
    elif user["password"] != password:
        alasan = "Password salah"
    elif user["ip"] != ip:
        alasan = "IP tidak terdaftar"
    else:
        status = "BERHASIL"

    print(f" Username : {username}")
    print(f" Alamat IP: {ip}")
    print(f" Status Login: {status}")
    if status == "GAGAL":
        print(f" Alasan      : {alasan}")
    else:
        print(f" Login user '{username}' berhasil, selamat datang!")

    return status, alasan, username, password, ip


# ==========================================
# 4. Lupa Password / Reset Password
# ==========================================

def lupa_password():
    judul("LUPA / RESET PASSWORD")

    sub("Verifikasi Identitas")
    username = input(" Username: ").strip()
    ip = input_ip_valid(" Alamat IP (verifikasi): ")

    user = cari_user(username)

    if user is None:
        print(f" [X] Username '{username}' tidak ditemukan di database_user")
        return
    if user["ip"] != ip:
        print(f" [X] Alamat IP tidak sesuai dengan data terdaftar user '{username}'")
        return

    print(f" [OK] Identitas user '{username}' terverifikasi")

    sub("Input Password Baru")
    password_baru = input(" Password baru: ")
    user["password"] = password_baru

    sub("Hasil Reset Password")
    print(f" Password untuk user '{username}' BERHASIL direset")


# ==========================================
# 5. Analisis IP
# ==========================================

def analisis_ip(ip):
    sub("Analisis IP")
    berbahaya = ip in IP_BERBAHAYA
    status_ip = "BERBAHAYA" if berbahaya else "AMAN"
    print(f" IP diperiksa : {ip}")
    print(f" Status IP    : {status_ip}")
    return berbahaya, status_ip


# ==========================================
# 6. Analisis Username
# ==========================================

def analisis_username(username):
    sub("Analisis Username")
    mencurigakan = username.lower() in USERNAME_MENCURIGAKAN
    status_username = "MENCURIGAKAN" if mencurigakan else "NORMAL"
    print(f" Username diperiksa : {username}")
    print(f" Status Username    : {status_username}")
    return mencurigakan, status_username


# ==========================================
# 7. Analisis Password
# ==========================================

def analisis_password(password, username):
    sub("Analisis Password")

    panjang = len(password)
    print(f" Password (disamarkan): {'*' * panjang}")
    print(f" Panjang password     : {panjang} karakter")

    jumlah_upper = sum(1 for c in password if c.isupper())
    jumlah_digit = sum(1 for c in password if c.isdigit())
    ada_lower = any(c.islower() for c in password)
    ada_simbol = any(not c.isalnum() for c in password)
    mengandung_username = username != "" and username.lower() in password.lower()

    kriteria = [
        ("Panjang password >= 12 karakter", panjang >= 12),
        ("Huruf besar <= 2 huruf", jumlah_upper <= 2),
        ("Mengandung huruf kecil", ada_lower),
        ("Angka >= 3 angka", jumlah_digit >= 3),
        ("Mengandung simbol khusus", ada_simbol),
        ("Tidak mengandung username", not mengandung_username),
    ]

    sub("Detail Kriteria Password (Ternary)")
    skor = 0
    kriteria_terpenuhi = []
    kriteria_tidak_terpenuhi = []

    for i, (nama, kondisi) in enumerate(kriteria, start=1):
        status = "YA" if kondisi else "TIDAK"
        print(f" {i}. {nama:<32}: {status}")
        skor += 1 if kondisi else 0
        if kondisi:
            kriteria_terpenuhi.append(nama)
        else:
            kriteria_tidak_terpenuhi.append(nama)

    if skor == 6:
        level_password = "SANGAT KUAT"
    elif skor == 5:
        level_password = "KUAT"
    elif skor >= 3:
        level_password = "SEDANG"
    elif skor >= 1:
        level_password = "LEMAH"
    else:
        level_password = "SANGAT LEMAH"

    sub("Skor & Level Kekuatan Password")
    print(f" Skor password : {skor}/6")
    print(f" Level password: {level_password}")

    sub("Kriteria Terpenuhi")
    if kriteria_terpenuhi:
        for k in kriteria_terpenuhi:
            print(f" [OK] {k}")
    else:
        print(" Tidak ada kriteria yang terpenuhi")

    sub("Kriteria Tidak Terpenuhi")
    if kriteria_tidak_terpenuhi:
        for k in kriteria_tidak_terpenuhi:
            print(f" [X] {k}")
    else:
        print(" Semua kriteria terpenuhi")

    sub("Rekomendasi Perbaikan Password")
    if not kriteria_tidak_terpenuhi:
        print(" Password sudah memenuhi seluruh kriteria keamanan")
    else:
        for k in kriteria_tidak_terpenuhi:
            print(f" - Perbaiki agar memenuhi: {k}")

    return skor, level_password


# ==========================================
# 8. Deteksi Tingkat Ancaman & Rekomendasi SOC
# ==========================================

def tentukan_tingkat_ancaman(ip_berbahaya, username_mencurigakan, level_password):
    """
    Menggabungkan 3 parameter (IP, username, password) menjadi skor risiko,
    lalu memetakannya ke 4 tingkat ancaman: AMAN, RENDAH, SEDANG, TINGGI.
    """
    skor_risiko = 0
    skor_risiko += 2 if ip_berbahaya else 0
    skor_risiko += 1 if username_mencurigakan else 0
    skor_risiko += 2 if level_password in ["SANGAT LEMAH", "LEMAH"] else \
                   (1 if level_password == "SEDANG" else 0)

    if skor_risiko >= 4:
        tingkat = "TINGGI"
    elif skor_risiko >= 2:
        tingkat = "SEDANG"
    elif skor_risiko >= 1:
        tingkat = "RENDAH"
    else:
        tingkat = "AMAN"

    return tingkat, skor_risiko

def rekomendasi_soc(tingkat_ancaman):
    peta_rekomendasi = {
        "TINGGI": "Segera blokir IP dan lakukan investigasi menyeluruh",
        "SEDANG": "Lakukan monitoring ketat dan verifikasi dengan user",
        "RENDAH": "Pantau aktivitas user dan catat dalam log",
        "AMAN": "Tidak ada tindakan yang diperlukan",
    }
    return peta_rekomendasi[tingkat_ancaman]


# ==========================================
# 9. Deteksi Ancaman Login (Integrasi Penuh) + Laporan Akhir
# ==========================================

def deteksi_ancaman_login(username=None, password=None, ip=None):
    judul("DETEKSI ANCAMAN LOGIN")

    if username is None or password is None or ip is None:
        sub("Input Percobaan Login")
        username = input(" Username : ").strip()
        password = input(" Password : ")
        ip = input_ip_valid(" Alamat IP: ")

    # 1. Cek status login terhadap database_user
    status_login, alasan, _, _, _ = login_user(username, password, ip,
                                                 tampilkan_judul=False)

    # 2. Analisis IP
    ip_berbahaya, status_ip = analisis_ip(ip)

    # 3. Analisis Username
    username_mencurigakan, status_username = analisis_username(username)

    # 4. Analisis Password
    skor_password, level_password = analisis_password(password, username)

    # 5. Deteksi Tingkat Ancaman
    tingkat_ancaman, skor_risiko = tentukan_tingkat_ancaman(
        ip_berbahaya, username_mencurigakan, level_password
    )

    # 6. Rekomendasi Tindakan SOC
    tindakan = rekomendasi_soc(tingkat_ancaman)

    # 7. LAPORAN AKHIR - seluruh komponen ditampilkan berurutan
    judul("LAPORAN AKHIR TRIAGE LOGIN")
    print(f" Username         : {username}")
    print(f" Alamat IP        : {ip}")
    print(f" Status Login     : {status_login}" +
          (f" ({alasan})" if status_login == "GAGAL" else ""))
    garis(70, "-")
    print(f" Status IP        : {status_ip}")
    print(f" Status Username  : {status_username}")
    print(f" Level Password   : {level_password} (skor {skor_password}/6)")
    garis(70, "-")
    print(f" Skor Risiko Total: {skor_risiko}")
    print(f" TINGKAT ANCAMAN  : {tingkat_ancaman}")
    print(f" REKOMENDASI SOC  : {tindakan}")
    garis()

    return tingkat_ancaman


# ==========================================
# 10. Skenario Uji (Beberapa Skenario Login)
# ==========================================

def siapkan_data_uji():
    database_user.clear()
    database_user.append({"username": "budi",  "password": "Budi!2024Kuat99", "ip": "192.168.1.10"})
    database_user.append({"username": "admin", "password": "admin123",        "ip": "192.168.1.100"})
    database_user.append({"username": "siti",  "password": "S1t1Aman#2024",   "ip": "10.10.10.5"})
    print(f" {len(database_user)} akun uji telah dimuat ke database_user")

def jalankan_skenario_uji():
    judul("SKENARIO UJI - BEBERAPA KASUS LOGIN")
    siapkan_data_uji()

    skenario = [
        ("Login normal, IP & password aman",
         "budi", "Budi!2024Kuat99", "192.168.1.10"),
        ("Login dengan username & IP mencurigakan, password lemah",
         "admin", "admin123", "192.168.1.100"),
        ("Login dengan IP berbahaya, password kuat, username normal",
         "siti", "S1t1Aman#2024", "10.0.0.1"),
        ("Login gagal - password salah",
         "budi", "salahpassword", "192.168.1.10"),
        ("Login gagal - username tidak terdaftar",
         "unknown_user", "sembarang123", "192.168.1.10"),
    ]

    for nomor, (deskripsi, user, pwd, ip) in enumerate(skenario, start=1):
        print(f"\n>>> SKENARIO {nomor}: {deskripsi}")
        deteksi_ancaman_login(user, pwd, ip)
        input("\n[ENTER untuk lanjut ke skenario berikutnya]")

    judul("SKENARIO UJI SELESAI")


# ==========================================
# 11. Menu Utama
# ==========================================

def menu():
    print()
    garis()
    print("      TUGAS PRAKTIKUM 03 - SISTEM AKUN & DETEKSI ANCAMAN LOGIN")
    print("                 D4 Rekayasa Keamanan Siber")
    garis()
    print(" [1] Registrasi User")
    print(" [2] Login User")
    print(" [3] Lupa / Reset Password")
    print(" [4] Deteksi Ancaman Login (Laporan Akhir)")
    print(" [5] Jalankan Skenario Uji (beberapa kasus login)")
    print(" [6] Tampilkan Total User Terdaftar")
    print(" [Q] Keluar")
    garis()

def tampilkan_total_user():
    judul("TOTAL USER TERDAFTAR")
    print(f" Total user pada database_user: {len(database_user)}")
    for i, user in enumerate(database_user, start=1):
        print(f" {i}. {user['username']} - IP: {user['ip']}")

def main():
    aksi = {
        "1": registrasi_user,
        "2": login_user,
        "3": lupa_password,
        "4": deteksi_ancaman_login,
        "5": jalankan_skenario_uji,
        "6": tampilkan_total_user,
    }

    while True:
        menu()
        pilihan = input("Pilih [1-6/Q]: ").strip().upper()
        if pilihan == "Q":
            print("\nKeluar dari program. Sampai jumpa!")
            break
        elif pilihan in aksi:
            aksi[pilihan]()
            input("\n[ENTER untuk kembali ke menu]")
        else:
            print("\nPilihan tidak valid.")


if __name__ == "__main__":
    main()