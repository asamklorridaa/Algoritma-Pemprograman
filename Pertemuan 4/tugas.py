print("=" * 70)
print("TUGAS PRAKTIKUM IV")
print("SISTEM MONITORING KEAMANAN JARINGAN KAMPUS")
print("D4 Rekayasa Keamanan Siber")
print("=" * 70)
print("\n")

print("=" * 70)
print("BAGIAN 1: REGISTRASI DATA ANALIS")
print("=" * 70)

print("\n--- INPUT DATA ANALIS ---")
nama_analis = input("Masukkan Nama Lengkap Analis      : ")
nim_analis = input("Masukkan NIM Analis               : ")
shift_kerja = input("Masukkan Shift (Pagi/Siang/Malam) : ")
jumlah_log = int(input("Masukkan Jumlah Log yang Dianalisis: "))

tingkat_kewaspadaan = int(input("Masukkan Tingkat Kewaspadaan (1-10): "))
while tingkat_kewaspadaan < 1 or tingkat_kewaspadaan > 10:
    print("  Input tidak valid! Tingkat kewaspadaan harus 1-10.")
    tingkat_kewaspadaan = int(input("Masukkan Tingkat Kewaspadaan (1-10): "))

print("\n--- DATA ANALIS TERDAFTAR ---")
print(f"Nama Lengkap         : {nama_analis}")
print(f"NIM                  : {nim_analis}")
print(f"Shift Kerja          : {shift_kerja}")
print(f"Jumlah Log           : {jumlah_log}")
print(f"Tingkat Kewaspadaan  : {tingkat_kewaspadaan}")

print("\n--- TIPE DATA VARIABEL ---")
print(f"nama_analis          : {type(nama_analis).__name__}")
print(f"nim_analis           : {type(nim_analis).__name__}")
print(f"shift_kerja          : {type(shift_kerja).__name__}")
print(f"jumlah_log           : {type(jumlah_log).__name__}")
print(f"tingkat_kewaspadaan  : {type(tingkat_kewaspadaan).__name__}")

print("\n")
print("=" * 70)
print("BAGIAN 2: OPERATOR ARITMATIKA DAN PENUGASAN")
print("=" * 70)

JAM_SHIFT = 8
DETIK_PER_LOG = 30
KAPASITAS_MAKS = 2000

print("\n--- PERHITUNGAN ---")

# 1. Rata-rata log per jam (operator pembagian /)
rata_log_per_jam = jumlah_log / JAM_SHIFT
print(f"Rata-rata Log per Jam      : {rata_log_per_jam:.2f} log/jam")

# 2. Estimasi waktu analisis (operator pembagian bulat //)
total_detik = jumlah_log * DETIK_PER_LOG
estimasi_jam = total_detik // 3600
estimasi_menit = (total_detik % 3600) // 60
estimasi_detik = total_detik % 60
print(f"Total Waktu Analisis       : {total_detik} detik")
print(f"Estimasi Waktu Analisis    : {estimasi_jam} jam {estimasi_menit} menit {estimasi_detik} detik")
print(f"Estimasi dalam Menit (//)  : {total_detik // 60} menit")

# 3. Persentase kapasitas (operator modulus % dan pembagian /)
sisa_kapasitas_log = jumlah_log % KAPASITAS_MAKS
persentase_kapasitas = (jumlah_log / KAPASITAS_MAKS) * 100
print(f"Persentase Kapasitas       : {persentase_kapasitas:.2f}% dari {KAPASITAS_MAKS} log")
print(f"Sisa Log (modulus)         : {sisa_kapasitas_log} (jumlah_log % {KAPASITAS_MAKS})")

# 5. Pangkat
nilai_pangkat = 2 ** tingkat_kewaspadaan
print(f"2 ^ Tingkat Kewaspadaan    : 2 ** {tingkat_kewaspadaan} = {nilai_pangkat}")

# 4. Operator penugasan untuk simulasi akumulasi insiden
print("\n--- SIMULASI AKUMULASI INSIDEN (OPERATOR PENUGASAN) ---")
jumlah_insiden = 0
print(f"Nilai awal insiden         : {jumlah_insiden}")

jumlah_insiden += 5
print(f"Setelah += 5 (5 insiden baru terdeteksi)   : {jumlah_insiden}")

jumlah_insiden += 3
print(f"Setelah += 3 (3 insiden baru terdeteksi)   : {jumlah_insiden}")

jumlah_insiden -= 2
print(f"Setelah -= 2 (2 insiden telah diselesaikan): {jumlah_insiden}")

jumlah_insiden *= 2
print(f"Setelah *= 2 (eskalasi serangan 2x lipat)  : {jumlah_insiden}")

print("\n")
print("=" * 70)
print("BAGIAN 3: OPERATOR PERBANDINGAN DAN LOGIKA")
print("=" * 70)

threshold_log = 500
threshold_kewaspadaan = 7

print("\n--- OPERATOR PERBANDINGAN ---")
print(f"Threshold Log            : {threshold_log}")
print(f"Threshold Kewaspadaan    : {threshold_kewaspadaan}")
print(f"\njumlah_log > {threshold_log}             : {jumlah_log > threshold_log}")
print(f"jumlah_log <= {threshold_log}            : {jumlah_log <= threshold_log}")
print(f"jumlah_log == {threshold_log}            : {jumlah_log == threshold_log}")
print(f"kewaspadaan >= {threshold_kewaspadaan}            : {tingkat_kewaspadaan >= threshold_kewaspadaan}")
print(f"kewaspadaan < {threshold_kewaspadaan}             : {tingkat_kewaspadaan < threshold_kewaspadaan}")

log_wajar = jumlah_log <= threshold_log
log_tinggi = jumlah_log > threshold_log
kewaspadaan_tinggi = tingkat_kewaspadaan >= threshold_kewaspadaan
kewaspadaan_rendah = tingkat_kewaspadaan < threshold_kewaspadaan

print("\n--- OPERATOR LOGIKA ---")
print(f"Jumlah Log Wajar         : {log_wajar}")
print(f"Kewaspadaan Tinggi       : {kewaspadaan_tinggi}")

# AND: analis siap bertugas
siap_bertugas = log_wajar and kewaspadaan_tinggi
print(f"\nAnalis Siap Bertugas (AND)   : {siap_bertugas}")

# OR: perlu backup
perlu_backup = log_tinggi or kewaspadaan_rendah
print(f"Perlu Backup (OR)            : {perlu_backup}")

# NOT: kondisi sebaliknya
tidak_siap = not siap_bertugas
tidak_perlu_backup = not perlu_backup
print(f"Tidak Siap Bertugas (NOT)    : {tidak_siap}")
print(f"Tidak Perlu Backup (NOT)     : {tidak_perlu_backup}")

print("\n")
print("=" * 70)
print("BAGIAN 4: KLASIFIKASI ALAMAT IP")
print("=" * 70)

ip_input = input("\nMasukkan Alamat IP: ")

if ip_input in ["192.168.1.100", "10.0.0.1", "172.16.0.1"]:
    status_ip_input = "BERBAHAYA"
    rekomendasi_ip_input = "BLOKIR IP ini segera!"
elif ip_input.startswith("192.168") or ip_input.startswith("10.") or ip_input.startswith("172."):
    status_ip_input = "IP PRIVAT"
    rekomendasi_ip_input = "PANTAU aktivitas IP ini"
else:
    status_ip_input = "IP PUBLIK"
    rekomendasi_ip_input = "VERIFIKASI asal dan tujuan koneksi"

print(f"\nAlamat IP            : {ip_input}")
print(f"Status               : {status_ip_input}")
print(f"Rekomendasi          : {rekomendasi_ip_input}")

print("\n")
print("=" * 70)
print("BAGIAN 5: KLASIFIKASI PORT JARINGAN")
print("=" * 70)

nomor_port = int(input("\nMasukkan Nomor Port: "))

if 0 <= nomor_port <= 1023:
    klasifikasi_port = "Well-known Port"
elif 1024 <= nomor_port <= 49151:
    klasifikasi_port = "Registered Port"
elif 49152 <= nomor_port <= 65535:
    klasifikasi_port = "Dynamic/Private Port"
else:
    klasifikasi_port = "PORT TIDAK VALID"

print(f"\nNomor Port           : {nomor_port}")
print(f"Klasifikasi          : {klasifikasi_port}")

print("\n")
print("=" * 70)
print("BAGIAN 6: VALIDASI LOGIN (NESTED IF)")
print("=" * 70)

database_login = {
    "admin": {"password": "Admin123", "ip": "192.168.1.100"},
    "user1": {"password": "User123", "ip": "192.168.1.101"}
}

print("\n--- INPUT KREDENSIAL ---")
username_input = input("Masukkan Username   : ")
password_input = input("Masukkan Password   : ")
ip_login_input = input("Masukkan IP Address : ")

# Validasi berlapis: username -> password -> IP
if username_input in database_login:
    if password_input == database_login[username_input]["password"]:
        if ip_login_input == database_login[username_input]["ip"]:
            hasil_validasi = "LOGIN BERHASIL"
            alasan_validasi = f"Selamat datang, {username_input}!"
            if username_input == "admin":
                akses_level_login = "FULL ACCESS"
            else:
                akses_level_login = "LIMITED ACCESS"
        else:
            hasil_validasi = "LOGIN GAGAL"
            alasan_validasi = "IP Address tidak terdaftar untuk user ini"
            akses_level_login = "DITOLAK"
    else:
        hasil_validasi = "LOGIN GAGAL"
        alasan_validasi = "Password salah"
        akses_level_login = "DITOLAK"
else:
    hasil_validasi = "LOGIN GAGAL"
    alasan_validasi = "Username tidak ditemukan dalam database"
    akses_level_login = "DITOLAK"

print("\n--- HASIL VALIDASI ---")
print(f"Username             : {username_input}")
print(f"IP Address           : {ip_login_input}")
print(f"Hasil                : {hasil_validasi}")
print(f"Alasan               : {alasan_validasi}")
print(f"Akses Level          : {akses_level_login}")

print("\n")
print("=" * 70)
print("BAGIAN 7: STATUS PASSWORD (OPERATOR TERNARY)")
print("=" * 70)

password_cek = input("\nMasukkan Password yang akan dicek: ")
panjang_password = len(password_cek)

# Ternary sederhana
status_panjang = "PANJANG" if panjang_password >= 8 else "PENDEK"

# Ternary bertingkat (batas AMAN = 12 karakter)
kategori_password = "AMAN" if panjang_password >= 12 else "SEDANG" if panjang_password >= 8 else "LEMAH"

print(f"\nPassword             : {'*' * panjang_password}")
print(f"Panjang              : {panjang_password} karakter")
print(f"Status Panjang       : {status_panjang}")
print(f"Kategori             : {kategori_password}")

print("\n")
print("=" * 70)
print("BAGIAN 8: SIMULASI MONITORING 8 JAM KERJA (FOR + RANGE)")
print("=" * 70)

total_log_monitoring = 0

print()
for jam in range(1, 9):
    log_per_jam = jam * 10
    total_log_monitoring += log_per_jam
    print(f"Jam ke-{jam}: {log_per_jam:3} log diproses | Total sementara: {total_log_monitoring}")

print(f"\nTotal log diproses selama 8 jam: {total_log_monitoring}")

print("\n")
print("=" * 70)
print("BAGIAN 9: ANALISIS DAFTAR IP (FOR + LIST)")
print("=" * 70)

daftar_ip = [
    "192.168.1.100",
    "10.0.0.1",
    "8.8.8.8",
    "172.16.0.1",
    "1.1.1.1",
    "192.168.1.101"
]
ip_berbahaya = ["192.168.1.100", "10.0.0.1", "172.16.0.1"]

print("\nDaftar IP Berbahaya (referensi):", ip_berbahaya)
print("\nHasil Analisis:")
for ip in daftar_ip:
    if ip in ip_berbahaya:
        status_ip_list = "BERBAHAYA - BLOKIR!"
    else:
        status_ip_list = "AMAN"
    print(f"IP: {ip:18} | {status_ip_list}")

print("\n")
print("=" * 70)
print("BAGIAN 10: ANALISIS KARAKTER PASSWORD (FOR + STRING)")
print("=" * 70)

password_contoh = "Secure@2024!"
print(f"\nPassword contoh: {password_contoh}\n")

huruf_besar = 0
huruf_kecil = 0
angka = 0
spesial = 0

for karakter in password_contoh:
    if karakter.isupper():
        huruf_besar += 1
        tipe_karakter = "Huruf Besar"
    elif karakter.islower():
        huruf_kecil += 1
        tipe_karakter = "Huruf Kecil"
    elif karakter.isdigit():
        angka += 1
        tipe_karakter = "Angka"
    else:
        spesial += 1
        tipe_karakter = "Karakter Spesial"
    print(f"  '{karakter}' -> {tipe_karakter}")

print("\nRingkasan Analisis:")
print(f"  Huruf Besar      : {huruf_besar}")
print(f"  Huruf Kecil      : {huruf_kecil}")
print(f"  Angka            : {angka}")
print(f"  Karakter Spesial : {spesial}")
print(f"  Total Karakter   : {huruf_besar + huruf_kecil + angka + spesial}")

print("\n")
print("=" * 70)
print("BAGIAN 11: COUNTDOWN MAINTENANCE (WHILE)")
print("=" * 70)

counter_maintenance = 5
print()
while counter_maintenance > 0:
    print(f"  Maintenance selesai dalam {counter_maintenance} detik...")
    counter_maintenance -= 1

print("  Sistem siap digunakan!")

print("\n")
print("=" * 70)
print("BAGIAN 12: BREAK, CONTINUE, PASS (FILTER DATA)")
print("=" * 70)

daftar_port = [80, 443, -1, 22, 70000, 0, 3306, 3389, 8080]
port_berbahaya = [21, 23, 25, 445, 3389]

print(f"\nDaftar Port: {daftar_port}")

print("\n--- BREAK: Hentikan pencarian saat port berbahaya ditemukan ---")
for port in daftar_port:
    if port < 1 or port > 65535:
        continue  # port tidak valid tidak ikut diperiksa
    if port in port_berbahaya:
        print(f"  Port {port}: BERBAHAYA! Pencarian dihentikan.")
        break
    print(f"  Port {port}: aman")

print("\n--- CONTINUE: Lewati port yang tidak valid ---")
for port in daftar_port:
    if port < 1 or port > 65535:
        print(f"  Port {port}: TIDAK VALID (dilewati)")
        continue
    print(f"  Port {port}: valid")

print("\n--- PASS: Placeholder fitur yang belum diimplementasikan ---")
for port in daftar_port:
    if port < 1 or port > 65535:
        continue
    if port == 22:
        pass  
        print(f"  Port {port}: [Fitur analisis SSH belum tersedia]")
    else:
        print(f"  Port {port}: dianalisis")

print("\n")
print("=" * 70)
print("BAGIAN 13: MATRIKS ZONA KEAMANAN (NESTED LOOP)")
print("=" * 70)

zona_keamanan = [
    [2, 5, 1, 3],
    [4, 8, 6, 2],
    [7, 3, 9, 4],
    [1, 6, 5, 0]
]

print("\nMatriks Skor Ancaman (0-9):")
print("       ", end="")
for j in range(len(zona_keamanan[0])):
    print(f"Kol {j:<3}", end="")
print()
for i in range(len(zona_keamanan)):
    print(f"Baris {i}", end=" ")
    for j in range(len(zona_keamanan[i])):
        print(f"{zona_keamanan[i][j]:^6}", end="")
    print()

nilai_tertinggi = -1
baris_tertinggi = 0
kolom_tertinggi = 0

for i in range(len(zona_keamanan)):
    for j in range(len(zona_keamanan[i])):
        if zona_keamanan[i][j] > nilai_tertinggi:
            nilai_tertinggi = zona_keamanan[i][j]
            baris_tertinggi = i
            kolom_tertinggi = j

print(f"\nSkor Ancaman Tertinggi : {nilai_tertinggi}")
print(f"Posisi                 : Baris {baris_tertinggi}, Kolom {kolom_tertinggi}")

print("\n")
print("=" * 70)
print("BAGIAN 14: DETEKSI ANCAMAN LOGIN (STUDI KASUS TERINTEGRASI)")
print("=" * 70)

database_user = [
    {"username": "admin", "password": "Admin123", "role": "admin", "ip": "192.168.1.100"},
    {"username": "user1", "password": "User123", "role": "user", "ip": "192.168.1.101"},
    {"username": "security", "password": "Secure@2024", "role": "security", "ip": "192.168.1.102"}
]
ip_berbahaya = ["192.168.1.100", "10.0.0.1", "172.16.0.1"]
username_mencurigakan = ["admin", "root", "guest"]
karakter_spesial = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

print("\n--- INPUT DATA LOGIN ---")
username_login = input("Masukkan Username    : ")
ip_login = input("Masukkan Alamat IP  : ")
password_login = input("Masukkan Password    : ")

# Analisis IP
if ip_login in ip_berbahaya:
    status_ip = "BERBAHAYA"
    is_ip_berbahaya = True
else:
    status_ip = "AMAN"
    is_ip_berbahaya = False

# Analisis username
if username_login in username_mencurigakan:
    status_username = "MENCURIGAKAN"
    is_username_mencurigakan = True
else:
    status_username = "NORMAL"
    is_username_mencurigakan = False

# Analisis password (6 kriteria)
panjang = len(password_login)
jumlah_huruf_besar = 0
jumlah_huruf_kecil = 0
jumlah_angka = 0
ada_simbol = False

for c in password_login:
    if c.isupper():
        jumlah_huruf_besar += 1
    elif c.islower():
        jumlah_huruf_kecil += 1
    elif c.isdigit():
        jumlah_angka += 1
    if c in karakter_spesial:
        ada_simbol = True

kriteria1 = panjang >= 12
kriteria2 = jumlah_huruf_besar >= 2
kriteria3 = jumlah_huruf_kecil > 0
kriteria4 = jumlah_angka >= 3
kriteria5 = ada_simbol
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

if skor_password == 6:
    level_password = "SANGAT KUAT"
    is_password_lemah = False
elif skor_password == 5:
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

# Tingkat ancaman (nested if)
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
            rekomendasi = "Pantau aktivitas IP dan catat dalam log"
else:
    if is_username_mencurigakan:
        if is_password_lemah:
            tingkat_ancaman = "RENDAH"
            rekomendasi = "Pantau aktivitas user dan catat dalam log"
        else:
            tingkat_ancaman = "RENDAH"
            rekomendasi = "Pantau aktivitas user dan catat dalam log"
    else:
        if is_password_lemah:
            tingkat_ancaman = "RENDAH"
            rekomendasi = "Sarankan user untuk mengganti password"
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
print(f"- Minimal 2 huruf besar      : {'YA' if kriteria2 else 'TIDAK'} ({jumlah_huruf_besar})")
print(f"- Mengandung huruf kecil     : {'YA' if kriteria3 else 'TIDAK'} ({jumlah_huruf_kecil})")
print(f"- Minimal 3 angka            : {'YA' if kriteria4 else 'TIDAK'} ({jumlah_angka})")
print(f"- Mengandung simbol khusus   : {'YA' if kriteria5 else 'TIDAK'}")
print(f"- Tidak mengandung username  : {'YA' if kriteria6 else 'TIDAK'}")

print("\n--- REKOMENDASI PERBAIKAN PASSWORD ---")
if skor_password == 6:
    print("- Password sudah memenuhi semua kriteria")
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

print("\n" + "=" * 70)
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
print("BAGIAN 15: SIMULASI ANALISIS MULTI-LOG")
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
        tag = "[MENCURIGAKAN]"
    else:
        tag = ""

    print(f"Log #{total_log}: {username:10} | {ip:15} | {status_text:8} {tag}")

print("\n" + "=" * 70)
print("RINGKASAN ANALISIS LOG")
print("=" * 70)
print(f"Total Log            : {total_log}")
print(f"Login Sukses         : {login_sukses}")
print(f"Login Gagal          : {login_gagal}")
print(f"Log Mencurigakan     : {log_mencurigakan}")

print("\n--- REKOMENDASI ---")
if log_mencurigakan >= 5:
    print("PERINGATAN TINGGI: Banyak aktivitas mencurigakan terdeteksi!")
    print("Segera lakukan investigasi menyeluruh dan blokir IP terkait.")
elif log_mencurigakan >= 3:
    print("PERINGATAN SEDANG: Terdapat beberapa aktivitas mencurigakan.")
    print("Lakukan monitoring ketat pada IP dan username terkait.")
elif log_mencurigakan > 0:
    print("PERINGATAN RENDAH: Ada sedikit aktivitas mencurigakan.")
    print("Catat dan pantau perkembangannya.")
else:
    print("SISTEM AMAN: Tidak ada aktivitas mencurigakan.")

print("\n")
print("=" * 70)
print("BAGIAN 16: ANALISIS PASSWORD BANYAK USER")
print("=" * 70)

daftar_password = {
    "admin": "admin",
    "user1": "User123",
    "security": "Secure@2024",
    "root": "P@ssword!2024",
    "guest": "12345678"
}

print("\n--- ANALISIS KEKUATAN PASSWORD ---")
print(f"{'User':<10} | {'Password':<15} | {'K1':<3} {'K2':<3} {'K3':<3} {'K4':<3} {'K5':<3} {'K6':<3} | {'Skor':<5} | {'Level':<12}")
print("-" * 82)

for user, pwd in daftar_password.items():
    panjang_pwd = len(pwd)
    besar = 0
    kecil = 0
    digit = 0
    simbol = 0

    for c in pwd:
        if c.isupper():
            besar += 1
        elif c.islower():
            kecil += 1
        elif c.isdigit():
            digit += 1
        if c in karakter_spesial:
            simbol += 1

    k1 = panjang_pwd >= 12
    k2 = besar >= 2
    k3 = kecil > 0
    k4 = digit >= 3
    k5 = simbol > 0
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

    if skor == 6:
        level = "SANGAT KUAT"
    elif skor == 5:
        level = "KUAT"
    elif skor >= 3:
        level = "SEDANG"
    elif skor >= 1:
        level = "LEMAH"
    else:
        level = "SANGAT LEMAH"

    pwd_tampil = "*" * panjang_pwd
    print(f"{user:<10} | {pwd_tampil:<15} | "
          f"{'Y' if k1 else 'N':<3} {'Y' if k2 else 'N':<3} {'Y' if k3 else 'N':<3} "
          f"{'Y' if k4 else 'N':<3} {'Y' if k5 else 'N':<3} {'Y' if k6 else 'N':<3} | "
          f"{skor}/6   | {level:<12}")

print("\nKeterangan kriteria:")
print("K1 = Minimal 12 karakter     K2 = Minimal 2 huruf besar")
print("K3 = Ada huruf kecil         K4 = Minimal 3 angka")
print("K5 = Ada simbol khusus       K6 = Tidak mengandung username")

print("\n")
print("=" * 70)
print("PROGRAM SELESAI")
print("=" * 70)
print(f"Analis : {nama_analis} ({nim_analis})")
print(f"Shift  : {shift_kerja}")
print("=" * 70)