print("=" * 70)
print("LATIHAN PRAKTIKUM KOMPREHENSIF")
print("SISTEM KEAMANAN SIBER TERINTEGRASI")
print("D4 Rekayasa Keamanan Siber")
print("=" * 70)
print("\n")
print("=" * 70)
print("BAGIAN 1: VARIABEL, TIPE DATA, DAN OPERATOR")
print("=" * 70)

nama_analis = "Budi Santoso"
role_analis = "Security Analyst"
ip_workstation = "192.168.1.50"
jumlah_insiden = 15
port_default = 443
skor_keamanan = 85
rating_risiko = 7.5
persentase_aman = 92.75
is_authorized = True
is_incident_resolved = False

print("\n--- DATA ANALIS DALAM SISTEM ---")
print(f"Nama Analis          : {nama_analis}")
print(f"Role                 : {role_analis}")
print(f"IP Workstation       : {ip_workstation}")
print(f"Jumlah Insiden       : {jumlah_insiden}")
print(f"Port Default         : {port_default}")
print(f"Skor Keamanan        : {skor_keamanan}")
print(f"Rating Risiko        : {rating_risiko}")
print(f"Persentase Aman      : {persentase_aman}%")
print(f"Status Otorisasi     : {is_authorized}")
print(f"Insiden Selesai      : {is_incident_resolved}")

print("\n--- OPERATOR ARITMATIKA ---")
total_log = 1500
log_berbahaya = 47
log_aman = total_log - log_berbahaya

print(f"Total Log            : {total_log}")
print(f"Log Berbahaya        : {log_berbahaya}")
print(f"Log Aman             : {log_aman}")

penjumlahan = total_log + 500
pengurangan = total_log - log_berbahaya
perkalian = log_berbahaya * 2
pembagian = total_log / 2
pembagian_bulat = total_log // 7
modulus = total_log % 7
pangkat = 2 ** 10

print(f"\nPenjumlahan (total_log + 500) : {penjumlahan}")
print(f"Pengurangan (total - bahaya)  : {pengurangan}")
print(f"Perkalian (bahaya * 2)         : {perkalian}")
print(f"Pembagian (total / 2)          : {pembagian}")
print(f"Pembagian Bulat (total // 7)   : {pembagian_bulat}")
print(f"Modulus (total % 7)            : {modulus}")
print(f"Pangkat (2 ** 10)              : {pangkat}")

persentase_berbahaya = (log_berbahaya / total_log) * 100
print(f"\nPersentase Log Berbahaya      : {persentase_berbahaya:.2f}%")

print("\n--- OPERATOR PERBANDINGAN ---")
threshold_insiden = 10
insiden_terdeteksi = 15

print(f"Threshold Insiden    : {threshold_insiden}")
print(f"Insiden Terdeteksi   : {insiden_terdeteksi}")

print(f"\ninsiden == threshold  : {insiden_terdeteksi == threshold_insiden}")
print(f"insiden != threshold  : {insiden_terdeteksi != threshold_insiden}")
print(f"insiden > threshold   : {insiden_terdeteksi > threshold_insiden}")
print(f"insiden < threshold   : {insiden_terdeteksi < threshold_insiden}")
print(f"insiden >= threshold  : {insiden_terdeteksi >= threshold_insiden}")
print(f"insiden <= threshold  : {insiden_terdeteksi <= threshold_insiden}")

print("\n--- OPERATOR LOGIKA ---")
is_login_valid = True
is_ip_trusted = True
is_password_kuat = False
is_mfa_enabled = True

print(f"Login Valid          : {is_login_valid}")
print(f"IP Trusted           : {is_ip_trusted}")
print(f"Password Kuat        : {is_password_kuat}")
print(f"MFA Enabled          : {is_mfa_enabled}")

akses_diberikan = is_login_valid and is_ip_trusted and is_password_kuat
print(f"\nAkses Diberikan (AND): {akses_diberikan}")

perlu_perbaikan = not is_password_kuat or not is_mfa_enabled
print(f"Perlu Perbaikan (OR) : {perlu_perbaikan}")

sistem_aman = not (not is_login_valid or not is_ip_trusted)
print(f"Sistem Aman (NOT)    : {sistem_aman}")

print("\n--- OPERATOR PENUGASAN ---")
insiden_counter = 0
print(f"Nilai awal insiden_counter: {insiden_counter}")

insiden_counter += 5
print(f"Setelah += 5         : {insiden_counter}")

insiden_counter -= 2
print(f"Setelah -= 2         : {insiden_counter}")

insiden_counter *= 3
print(f"Setelah *= 3         : {insiden_counter}")

insiden_counter //= 2
print(f"Setelah //= 2        : {insiden_counter}")

print("\n")
print("=" * 70)
print("BAGIAN 2: INPUT, OUTPUT, DAN F-STRING")
print("=" * 70)

print("\n--- INPUT DATA ANALIS ---")
nama_input = input("Masukkan Nama Analis: ")
shift_input = input("Masukkan Shift (Pagi/Siang/Malam): ")
jumlah_log_input = input("Masukkan Jumlah Log yang Diperiksa: ")
jumlah_log_int = int(jumlah_log_input)

print("\n--- HASIL INPUT DENGAN F-STRING ---")
print(f"Nama Analis          : {nama_input}")
print(f"Shift                : {shift_input}")
print(f"Jumlah Log           : {jumlah_log_int}")
print(f"Rata-rata per Jam    : {jumlah_log_int / 8:.0f} log")

rata_rata = jumlah_log_int / 8
print(f"Rata-rata (2 desimal): {rata_rata:.2f}")

print(f"\n{'Nama':<15}: {nama_input}")
print(f"{'Shift':<15}: {shift_input}")
print(f"{'Jumlah Log':<15}: {jumlah_log_int}")

print("\n")
print("=" * 70)
print("BAGIAN 3: STRUKTUR KONTROL PERCABANGAN")
print("=" * 70)

print("\n--- 3.1 PERCABANGAN IF-ELSE ---")
ip_cek = input("Masukkan IP untuk diklasifikasi: ")

if ip_cek in ["192.168.1.100", "10.0.0.1", "172.16.0.1"]:
    status_ip = "BERBAHAYA"
    rekomendasi_ip = "Blokir IP ini segera!"
elif ip_cek.startswith("192.168.") or ip_cek.startswith("10.") or ip_cek.startswith("172."):
    status_ip = "IP PRIVAT"
    rekomendasi_ip = "Pantau aktivitas"
else:
    status_ip = "IP PUBLIK"
    rekomendasi_ip = "Lakukan verifikasi"

print(f"\nIP Address           : {ip_cek}")
print(f"Status IP            : {status_ip}")
print(f"Rekomendasi          : {rekomendasi_ip}")

print("\n--- 3.2 PERCABANGAN ELIF ---")
port_cek = int(input("Masukkan nomor port (0-65535): "))

if 0 <= port_cek <= 1023:
    klasifikasi = "Well-known Port"
elif 1024 <= port_cek <= 49151:
    klasifikasi = "Registered Port"
elif 49152 <= port_cek <= 65535:
    klasifikasi = "Dynamic/Private Port"
else:
    klasifikasi = "PORT TIDAK VALID"

print(f"\nPort                 : {port_cek}")
print(f"Klasifikasi          : {klasifikasi}")

print("\n--- 3.3 PERCABANGAN BERSARANG ---")
username_login = input("Masukkan Username: ")
password_login = input("Masukkan Password: ")
ip_login = input("Masukkan IP Address: ")

db_admin = {"username": "admin", "password": "Admin123", "ip": "192.168.1.100"}
db_user = {"username": "user1", "password": "User123", "ip": "192.168.1.101"}

if username_login == db_admin["username"]:
    if password_login == db_admin["password"]:
        if ip_login == db_admin["ip"]:
            hasil_login = "LOGIN BERHASIL. Selamat datang Admin!"
            akses_level = "FULL ACCESS"
        else:
            hasil_login = "LOGIN GAGAL: IP tidak terdaftar untuk admin"
            akses_level = "DITOLAK"
    else:
        hasil_login = "LOGIN GAGAL: Password admin salah"
        akses_level = "DITOLAK"
elif username_login == db_user["username"]:
    if password_login == db_user["password"]:
        if ip_login == db_user["ip"]:
            hasil_login = "LOGIN BERHASIL. Selamat datang User!"
            akses_level = "LIMITED ACCESS"
        else:
            hasil_login = "LOGIN GAGAL: IP tidak terdaftar"
            akses_level = "DITOLAK"
    else:
        hasil_login = "LOGIN GAGAL: Password user salah"
        akses_level = "DITOLAK"
else:
    hasil_login = "LOGIN GAGAL: Username tidak ditemukan"
    akses_level = "DITOLAK"

print(f"\nUsername             : {username_login}")
print(f"IP Address           : {ip_login}")
print(f"Hasil Login          : {hasil_login}")
print(f"Akses Level          : {akses_level}")

print("\n--- 3.4 OPERATOR TERNARY ---")
password_test = input("Masukkan password untuk dicek panjangnya: ")
panjang_password = len(password_test)

status_panjang = "PANJANG" if panjang_password >= 8 else "PENDEK"
kategori = "AMAN" if panjang_password >= 12 else "SEDANG" if panjang_password >= 8 else "LEMAH"

print(f"\nPassword             : {'*' * panjang_password}")
print(f"Panjang              : {panjang_password} karakter")
print(f"Status               : {status_panjang}")
print(f"Kategori             : {kategori}")

print("\n")
print("=" * 70)
print("BAGIAN 4: STRUKTUR KONTROL PERULANGAN")
print("=" * 70)

print("\n--- 4.1 PERULANGAN FOR DENGAN RANGE() ---")
print("\nSimulasi Monitoring 8 Jam Kerja:")
total_log_monitoring = 0

for jam in range(1, 9):
    log_per_jam = jam * 10
    total_log_monitoring += log_per_jam
    print(f"Jam ke-{jam}: {log_per_jam} log diproses (Total: {total_log_monitoring})")

print(f"\nTotal log diproses: {total_log_monitoring}")

print("\n--- 4.2 PERULANGAN FOR DENGAN LIST ---")
daftar_ip = [
    "192.168.1.100",
    "10.0.0.1",
    "8.8.8.8",
    "172.16.0.1",
    "1.1.1.1"
]
ip_berbahaya = ["192.168.1.100", "10.0.0.1", "172.16.0.1"]

print("\nAnalisis Daftar IP:")
for ip in daftar_ip:
    if ip in ip_berbahaya:
        status = "BERBAHAYA - BLOKIR!"
    else:
        status = "AMAN"
    print(f"IP: {ip:18} | {status}")

print("\n--- 4.3 PERULANGAN FOR DENGAN STRING ---")
password_analisis = "Secure@2024!"
print(f"\nAnalisis karakter password: {password_analisis}")

huruf_besar = 0
huruf_kecil = 0
angka = 0
spesial = 0

for karakter in password_analisis:
    if karakter.isupper():
        huruf_besar += 1
        tipe = "Huruf Besar"
    elif karakter.islower():
        huruf_kecil += 1
        tipe = "Huruf Kecil"
    elif karakter.isdigit():
        angka += 1
        tipe = "Angka"
    else:
        spesial += 1
        tipe = "Karakter Spesial"
    print(f"  '{karakter}' -> {tipe}")

print(f"\nRingkasan:")
print(f"  Huruf Besar     : {huruf_besar}")
print(f"  Huruf Kecil     : {huruf_kecil}")
print(f"  Angka           : {angka}")
print(f"  Karakter Spesial: {spesial}")

print("\n--- 4.4 PERULANGAN WHILE ---")
print("\nSimulasi Countdown Maintenance:")
waktu_maintenance = 5

while waktu_maintenance > 0:
    print(f"  Sistem maintenance dalam {waktu_maintenance} detik...")
    waktu_maintenance -= 1

print("  Sistem siap digunakan!")

print("\n--- 4.5 KONTROL ALUR: BREAK, CONTINUE, PASS ---")
daftar_port = [21, 22, 80, -1, 443, 70000, 3306, 8080, 0]

print("\nSimulasi pencarian port berbahaya (break):")
for port in daftar_port:
    if port in [21, 23, 25, 445, 3389]:
        print(f"  Port {port}: BERBAHAYA! Menghentikan scan.")
        break
    print(f"  Port {port}: aman")

print("\nSimulasi filter port valid (continue):")
for port in daftar_port:
    if port < 1 or port > 65535:
        print(f"  Port {port}: TIDAK VALID (dilewati)")
        continue
    print(f"  Port {port}: valid")

print("\nSimulasi pass sebagai placeholder:")
for port in daftar_port[:3]:
    if port == 22:
        pass
        print(f"  Port {port}: [Fitur analisis SSH belum tersedia]")
    else:
        print(f"  Port {port}: dianalisis")

print("\n--- 4.6 PERULANGAN BERSARANG ---")
zona_keamanan = [
    [1, 2, 3, 4],
    [2, 5, 6, 3],
    [3, 6, 9, 4],
    [4, 3, 4, 2]
]

print("\nMatriks Zona Keamanan:")
for i in range(len(zona_keamanan)):
    for j in range(len(zona_keamanan[i])):
        print(f"{zona_keamanan[i][j]:4}", end="")
    print()

tertinggi = 0
posisi_tertinggi = (0, 0)

for i in range(len(zona_keamanan)):
    for j in range(len(zona_keamanan[i])):
        if zona_keamanan[i][j] > tertinggi:
            tertinggi = zona_keamanan[i][j]
            posisi_tertinggi = (i, j)

print(f"\nNilai tertinggi: {tertinggi}")
print(f"Posisi: Baris {posisi_tertinggi[0]}, Kolom {posisi_tertinggi[1]}")

print("\n")
print("=" * 70)
print("BAGIAN 5: STUDI KASUS TERINTEGRASI")
print("=" * 70)
print("\n--- SISTEM DETEKSI ANCAMAN LOGIN ---")

database_user = [
    {"username": "admin", "password": "Admin123", "role": "admin", "ip": "192.168.1.100"},
    {"username": "user1", "password": "User123", "role": "user", "ip": "192.168.1.101"},
    {"username": "security", "password": "Secure@2024", "role": "security", "ip": "192.168.1.102"}
]

ip_berbahaya = ["192.168.1.100", "10.0.0.1", "172.16.0.1"]
username_mencurigakan = ["admin", "root", "guest"]

print("\n--- INPUT DATA LOGIN ---")
username_login = input("Masukkan Username: ")
ip_login = input("Masukkan Alamat IP: ")
password_login = input("Masukkan Password: ")

if ip_login in ip_berbahaya:
    status_ip = "BERBAHAYA"
    is_ip_berbahaya = True
else:
    status_ip = "AMAN"
    is_ip_berbahaya = False

if username_login in username_mencurigakan:
    status_username = "MENCURIGAKAN"
    is_username_mencurigakan = True
else:
    status_username = "NORMAL"
    is_username_mencurigakan = False

panjang = len(password_login)
kriteria1 = panjang >= 12
jumlah_huruf_besar = sum(1 for c in password_login if c.isupper())
kriteria2 = jumlah_huruf_besar >= 2
kriteria3 = any(c.islower() for c in password_login)
jumlah_angka = sum(1 for c in password_login if c.isdigit())
kriteria4 = jumlah_angka >= 3
karakter_spesial = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
kriteria5 = any(c in karakter_spesial for c in password_login)
kriteria6 = username_login.lower() not in password_login.lower()

skor_password = 0
if kriteria1:
    skor_password += 1
if kriteria2:
    skor_password += 1
if kriteria3:
    skor_password += 1
if kriteria4:
    skor_password += 1
if kriteria5:
    skor_password += 1
if kriteria6:
    skor_password += 1

if skor_password >= 6:
    level_password = "SANGAT KUAT"
    is_password_lemah = False
elif skor_password >= 5:
    level_password = "KUAT"
    is_password_lemah = False
elif skor_password >= 3:
    level_password = "SEDANG"
    is_password_lemah = False
elif skor_password >= 1:
    level_password = "LEMAH"
    is_password_lemah = True
else:
    level_password = "SANGAT LEMAH"
    is_password_lemah = True

if is_ip_berbahaya:
    if is_username_mencurigakan:
        if is_password_lemah:
            tingkat_ancaman = "TINGGI"
            rekomendasi = "Segera blokir IP dan lakukan investigasi menyeluruh"
        else:
            tingkat_ancaman = "SEDANG"
            rekomendasi = "Lakukan monitoring ketat dan verifikasi dengan user"
    else:
        if is_password_lemah:
            tingkat_ancaman = "SEDANG"
            rekomendasi = "Lakukan monitoring ketat dan verifikasi dengan user"
        else:
            tingkat_ancaman = "RENDAH"
            rekomendasi = "Pantau aktivitas user dan catat dalam log"
else:
    if is_username_mencurigakan:
        if is_password_lemah:
            tingkat_ancaman = "SEDANG"
            rekomendasi = "Lakukan monitoring ketat dan verifikasi dengan user"
        else:
            tingkat_ancaman = "RENDAH"
            rekomendasi = "Pantau aktivitas user dan catat dalam log"
    else:
        if is_password_lemah:
            tingkat_ancaman = "RENDAH"
            rekomendasi = "Pantau aktivitas user dan catat dalam log"
        else:
            tingkat_ancaman = "AMAN"
            rekomendasi = "Tidak ada tindakan yang diperlukan"

print("\n--- ANALISIS IP ---")
print(f"IP Address           : {ip_login}")
print(f"Status IP            : {status_ip}")

print("\n--- ANALISIS USERNAME ---")
print(f"Username             : {username_login}")
print(f"Status Username      : {status_username}")

print("\n--- ANALISIS PASSWORD ---")
print(f"Password             : {'*' * panjang}")
print(f"Panjang              : {panjang} karakter")
print(f"Skor                 : {skor_password}/6")
print(f"Level                : {level_password}")

print("\nDetail Kriteria:")
print(f"- Minimal 12 karakter        : {'YA' if kriteria1 else 'TIDAK'} ({panjang})")
print(f"- Minimal 2 Huruf Besar      : {'YA' if kriteria2 else 'TIDAK'} ({jumlah_huruf_besar})")
print(f"- Mengandung Huruf Kecil     : {'YA' if kriteria3 else 'TIDAK'}")
print(f"- Minimal 3 Angka            : {'YA' if kriteria4 else 'TIDAK'} ({jumlah_angka})")
print(f"- Mengandung Simbol Khusus   : {'YA' if kriteria5 else 'TIDAK'}")
print(f"- Tidak mengandung username  : {'YA' if kriteria6 else 'TIDAK'}")

print("\n--- REKOMENDASI PERBAIKAN PASSWORD ---")
if not kriteria1:
    print("- Tambah panjang password minimal 12 karakter")
if not kriteria2:
    print("- Tambahkan minimal 2 huruf besar (A-Z)")
if not kriteria3:
    print("- Tambahkan huruf kecil (a-z)")
if not kriteria4:
    print("- Tambahkan minimal 3 angka (0-9)")
if not kriteria5:
    print("- Tambahkan simbol khusus (!@#$%^&*...)")
if not kriteria6:
    print("- Password tidak boleh mengandung username")

print("\n--- PENENTUAN TINGKAT ANCAMAN ---")
print(f"Tingkat Ancaman      : {tingkat_ancaman}")
print(f"Rekomendasi          : {rekomendasi}")

print("\n")
print("=" * 70)
print("LAPORAN AKHIR DETEKSI ANCAMAN LOGIN")
print("=" * 70)
print(f"Username             : {username_login}")
print(f"IP Address           : {ip_login}")
print(f"Status IP            : {status_ip}")
print(f"Status Username      : {status_username}")
print(f"Skor Password        : {skor_password}/6")
print(f"Level Password       : {level_password}")
print(f"Tingkat Ancaman      : {tingkat_ancaman}")
print(f"Rekomendasi          : {rekomendasi}")
print("=" * 70)

print("\n")
print("=" * 70)
print("BAGIAN 7: SIMULASI ANALISIS MULTI-LOG")
print("=" * 70)

daftar_log = [
    {"username": "admin", "ip": "192.168.1.100", "status": "success"},
    {"username": "user1", "ip": "192.168.1.101", "status": "success"},
    {"username": "unknown", "ip": "10.0.0.1", "status": "failed"},
    {"username": "admin", "ip": "10.0.0.1", "status": "failed"},
    {"username": "root", "ip": "172.16.0.1", "status": "failed"},
    {"username": "security", "ip": "192.168.1.102", "status": "success"},
    {"username": "guest", "ip": "8.8.8.8", "status": "failed"}
]

total_log = 0
login_sukses = 0
login_gagal = 0
log_mencurigakan = 0

print("\nMemproses log login...\n")

for log in daftar_log:
    total_log += 1
    username = log["username"]
    ip = log["ip"]
    status = log["status"]

    if status == "success":
        login_sukses += 1
        status_text = "BERHASIL"
    else:
        login_gagal += 1
        status_text = "GAGAL"

    if ip in ip_berbahaya or username in username_mencurigakan:
        log_mencurigakan += 1
        peringatan = "[MENCURIGAKAN]"
    else:
        peringatan = ""

    print(f"Log #{total_log}: {username:10} | {ip:15} | {status_text} {peringatan}")

print("\n" + "=" * 70)
print("RINGKASAN ANALISIS LOG")
print("=" * 70)
print(f"Total Log            : {total_log}")
print(f"Login Sukses         : {login_sukses}")
print(f"Login Gagal          : {login_gagal}")
print(f"Log Mencurigakan     : {log_mencurigakan}")

print("\n--- REKOMENDASI ---")
if log_mencurigakan >= 3:
    print("PERINGATAN TINGGI: Banyak aktivitas mencurigakan terdeteksi!")
    print("Segera lakukan investigasi menyeluruh.")
elif log_mencurigakan > 0:
    print("PERINGATAN SEDANG: Terdapat aktivitas mencurigakan.")
    print("Lakukan monitoring ketat.")
else:
    print("SISTEM AMAN: Tidak ada aktivitas mencurigakan.")

print("\n")
print("=" * 70)
print("BAGIAN 8: ANALISIS PASSWORD BANYAK USER")
print("=" * 70)

daftar_password = [
    {"user": "admin", "password": "admin"},
    {"user": "user1", "password": "User123"},
    {"user": "security", "password": "Secure@2024"},
    {"user": "root", "password": "P@ssword!2024"},
    {"user": "guest", "password": "12345678"}
]

print("\n--- ANALISIS KEKUATAN PASSWORD ---")
print(f"{'User':<12} | {'Password':<20} | {'Skor':<5} | {'Level':<15}")
print("-" * 70)

for data in daftar_password:
    user = data["user"]
    pwd = data["password"]
    panjang = len(pwd)

    k1 = panjang >= 12
    k2 = sum(1 for c in pwd if c.isupper()) >= 2
    k3 = any(c.islower() for c in pwd)
    k4 = sum(1 for c in pwd if c.isdigit()) >= 3
    k5 = any(c in karakter_spesial for c in pwd)
    k6 = user.lower() not in pwd.lower()

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

    pwd_tampil = "*" * panjang
    print(f"{user:<12} | {pwd_tampil:<20} | {skor}/6   | {level:<15}")

print("\n")
print("=" * 70)
print("PRAKTIKUM KOMPREHENSIF SELESAI")
print("=" * 70)
print("\nTerima kasih telah mengikuti praktikum ini.")
print("Pastikan Anda telah memahami:")
print("  1. Variabel dan tipe data primitif")
print("  2. Operator aritmatika, perbandingan, logika, penugasan")
print("  3. Fungsi input(), print(), dan f-string")
print("  4. Percabangan (if, if-else, elif, nested if, ternary)")
print("  5. Perulangan (for, while, break, continue, pass, nested loop)")
print("=" * 70)