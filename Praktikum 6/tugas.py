from functools import reduce

print("=" * 70)
print("SISTEM ANALISIS LOG FORENSIK CYBERTRACE")
print("D4 Rekayasa Keamanan Siber")
print("=" * 70)

print("\n")
print("=" * 70)
print("BAGIAN 1: FUNGSI LAMBDA DASAR")
print("=" * 70)

# Lambda tanpa parameter
sapa = lambda: "Selamat datang di CyberTrace DFIR"
print(sapa())

# Lambda dengan satu parameter
kuadrat = lambda x: x ** 2
print(f"Kuadrat 8: {kuadrat(8)}")

# Lambda dengan dua parameter
kali = lambda a, b: a * b
print(f"5 x 6 = {kali(5, 6)}")

# Lambda dengan kondisi ternary
status_ancaman = lambda skor: "CRITICAL" if skor >= 8 else "WARNING" if skor >= 5 else "INFO"
print(f"Skor 9: {status_ancaman(9)}")
print(f"Skor 6: {status_ancaman(6)}")
print(f"Skor 3: {status_ancaman(3)}")

# Lambda untuk klasifikasi IP
klasifikasi_ip = lambda ip: "BERBAHAYA" if ip in ["10.0.0.1", "192.168.1.100"] else "AMAN"
print(f"IP 10.0.0.1: {klasifikasi_ip('10.0.0.1')}")
print(f"IP 8.8.8.8: {klasifikasi_ip('8.8.8.8')}")

print("\n")
print("=" * 70)
print("BAGIAN 2: FUNGSI REKURSIF - FAKTORIAL")
print("=" * 70)

def faktorial(n):
    """Menghitung faktorial n dengan rekursi."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

print(f"Faktorial 5 = {faktorial(5)}")
print(f"Faktorial 7 = {faktorial(7)}")

print("\n")
print("=" * 70)
print("BAGIAN 3: FUNGSI REKURSIF - FIBONACCI")
print("=" * 70)

def fibonacci(n):
    """Menghitung deret Fibonacci ke-n dengan rekursi."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Deret Fibonacci 0-9:")
for i in range(10):
    print(f"  F({i}) = {fibonacci(i)}")

print("\n")
print("=" * 70)
print("BAGIAN 4: FUNGSI REKURSIF - JUMLAH DIGIT")
print("=" * 70)

def jumlah_digit(n):
    """Menghitung jumlah digit angka dengan rekursi."""
    if n < 10:
        return n
    else:
        return (n % 10) + jumlah_digit(n // 10)

angka = 12345
print(f"Jumlah digit {angka} = {jumlah_digit(angka)}")

# Studi kasus: validasi PIN
pin = 9087
print(f"Jumlah digit PIN {pin} = {jumlah_digit(pin)}")

print("\n")
print("=" * 70)
print("BAGIAN 5: FUNGSI REKURSIF - PENCARIAN LOG DIREKTORI")
print("=" * 70)

def hitung_log(direktori, kedalaman=0):
    """
    Menghitung total log dalam struktur direktori secara rekursif.
    Simulasi struktur direktori forensik.
    """
    struktur = {
        "root_logs": {"file": 5, "sub": "firewall_logs"},
        "firewall_logs": {"file": 12, "sub": "ids_logs"},
        "ids_logs": {"file": 8, "sub": "endpoint_logs"},
        "endpoint_logs": {"file": 15, "sub": None}
    }

    if direntri_kosong := (direktori not in struktur):
        return 0

    data = struktur[direktori]
    total = data["file"]

    if kedalaman >= 5:
        return total

    if data["sub"]:
        total += hitung_log(data["sub"], kedalaman + 1)

    return total

print(f"Total log di root_logs: {hitung_log('root_logs')}")

print("\n")
print("=" * 70)
print("BAGIAN 6: FUNGSI map() - TRANSFORMASI DATA")
print("=" * 70)

# Contoh 1: Mengkuadratkan semua angka
angka = [1, 2, 3, 4, 5]
kuadrat_list = list(map(lambda x: x ** 2, angka))
print(f"Kuadrat: {kuadrat_list}")

# Contoh 2: Konversi string ke integer
string_angka = ["100", "200", "300", "400"]
angka_int = list(map(int, string_angka))
print(f"Konversi: {angka_int}")

# Contoh 3: Transformasi log menjadi format kritis
skor_ancaman = [3, 8, 5, 9, 2, 7]
kategori = list(map(lambda x: f"Skor {x} = {'CRITICAL' if x >= 8 else 'WARNING' if x >= 5 else 'INFO'}", skor_ancaman))
for k in kategori:
    print(f"  {k}")

print("\n")
print("=" * 70)
print("BAGIAN 7: FUNGSI filter() - PENYARINGAN DATA")
print("=" * 70)

# Contoh 1: Menyaring angka genap
angka = [1, 2, 3, 4, 5, 6, 7, 8]
genap = list(filter(lambda x: x % 2 == 0, angka))
print(f"Angka genap: {genap}")

# Contoh 2: Menyaring IP berbahaya
daftar_ip = ["192.168.1.100", "8.8.8.8", "10.0.0.1", "1.1.1.1", "172.16.0.1"]
ip_berbahaya = ["192.168.1.100", "10.0.0.1", "172.16.0.1"]

hasil = list(filter(lambda ip: ip in ip_berbahaya, daftar_ip))
print(f"IP berbahaya: {hasil}")

# Contoh 3: Menyaring log dengan skor tinggi
skor_log = [3, 8, 5, 9, 2, 7, 6, 4]
log_kritis = list(filter(lambda x: x >= 7, skor_log))
print(f"Log kritis (skor >= 7): {log_kritis}")

# Contoh 4: Menyaring port berbahaya
daftar_port = [21, 22, 80, 135, 443, 445, 3306, 3389]
port_berbahaya = [21, 23, 25, 135, 445, 3389]

port_bahaya = list(filter(lambda p: p in port_berbahaya, daftar_port))
print(f"Port berbahaya: {port_bahaya}")

print("\n")
print("=" * 70)
print("BAGIAN 8: FUNGSI reduce() - AGREGASI DATA")
print("=" * 70)

# Contoh 1: Penjumlahan total
angka = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, angka)
print(f"Total: {total}")

# Contoh 2: Mencari nilai maksimum
nilai = [45, 12, 78, 34, 89, 23]
maks = reduce(lambda a, b: a if a > b else b, nilai)
print(f"Nilai maksimum: {maks}")

# Contoh 3: Perkalian semua elemen
angka2 = [2, 3, 4, 5]
hasil_kali = reduce(lambda a, b: a * b, angka2)
print(f"Perkalian: {hasil_kali}")

# Contoh 4: Total skor ancaman
skor_ancaman = [3, 7, 2, 9, 4, 8]
total_ancaman = reduce(lambda a, b: a + b, skor_ancaman)
print(f"Total skor ancaman: {total_ancaman}")

# Contoh 5: Mencari skor tertinggi
skor_max = reduce(lambda a, b: a if a > b else b, skor_ancaman)
print(f"Skor ancaman tertinggi: {skor_max}")

print("\n")
print("=" * 70)
print("BAGIAN 9: KOMBINASI map(), filter(), reduce()")
print("=" * 70)

skor_log = [3, 8, 5, 9, 2, 7, 6, 4]

# 1. Filter skor tinggi
skor_tinggi = list(filter(lambda x: x >= 5, skor_log))
print(f"1. Skor tinggi (>= 5)   : {skor_tinggi}")

# 2. Map untuk mengalikan dengan 10
skor_kali = list(map(lambda x: x * 10, skor_tinggi))
print(f"2. Skor x10             : {skor_kali}")

# 3. Reduce untuk total
total = reduce(lambda a, b: a + b, skor_kali)
print(f"3. Total                : {total}")

# Analisis dalam satu rantai
hasil_pipeline = reduce(
    lambda a, b: a + b,
    map(lambda x: x * 10, filter(lambda x: x >= 5, skor_log))
)
print(f"\nHasil pipeline lengkap: {hasil_pipeline}")

print("\n")
print("=" * 70)
print("BAGIAN 10: STUDI KASUS TERINTEGRASI")
print("=" * 70)

log_data = [
    {"ip": "192.168.1.100", "skor": 9, "status": "failed"},
    {"ip": "8.8.8.8", "skor": 2, "status": "success"},
    {"ip": "10.0.0.1", "skor": 8, "status": "failed"},
    {"ip": "1.1.1.1", "skor": 3, "status": "success"},
    {"ip": "172.16.0.1", "skor": 7, "status": "failed"},
    {"ip": "203.0.113.5", "skor": 9, "status": "failed"},
    {"ip": "198.51.100.7", "skor": 4, "status": "success"}
]

# 1. Filter log dengan skor >= 7 (kritis)
log_kritis = list(filter(lambda x: x["skor"] >= 7, log_data))
print("\n1. LOG KRITIS (skor >= 7):")
for log in log_kritis:
    print(f"   IP: {log['ip']:15} | Skor: {log['skor']} | Status: {log['status']}")

# 2. Map untuk mengambil semua IP
semua_ip = list(map(lambda x: x["ip"], log_data))
print(f"\n2. Semua IP: {semua_ip}")

# 3. Map untuk transformasi menjadi string laporan
laporan = list(map(lambda x: f"[{x['status'].upper()}] {x['ip']} - Skor {x['skor']}", log_data))
print("\n3. Laporan:")
for l in laporan:
    print(f"   {l}")
# 4. Reduce untuk total skor
total_skor = reduce(lambda a, b: a + b["skor"], log_data, 0)
print(f"\n4. Total skor ancaman: {total_skor}")

# 5. Reduce untuk skor tertinggi
skor_max = reduce(lambda a, b: a if a > b["skor"] else b["skor"], log_data, 0)
print(f"5. Skor tertinggi: {skor_max}")

# 6. Kombinasi: total skor log kritis
total_kritis = reduce(lambda a, b: a + b["skor"], log_kritis, 0)
print(f"6. Total skor log kritis: {total_kritis}")

# 7. Filter + map: IP berbahaya dari log gagal
ip_blacklist = ["192.168.1.100", "10.0.0.1", "172.16.0.1", "203.0.113.5"]
ip_gagal_berbahaya = list(map(
    lambda x: x["ip"],
    filter(lambda x: x["status"] == "failed" and x["ip"] in ip_blacklist, log_data)
))
print(f"\n7. IP gagal & berbahaya: {ip_gagal_berbahaya}")

print("\n")
print("=" * 70)
print("BAGIAN 11: REKURSI - ANALISIS ANCAMAN BERJENJANG")
print("=" * 70)

def hitung_ancaman_berjenjang(level, kedalaman=0):
    """
    Menghitung total ancaman secara rekursif dengan tingkat kedalaman.
    Level 1 = log terbaru, level berikutnya = log lama.
    """
    if kedalaman >= 5:
        return 0

    if level == 1:
        return 10 + hitung_ancaman_berjenjang(2, kedalaman + 1)
    elif level == 2:
        return 8 + hitung_ancaman_berjenjang(3, kedalaman + 1)
    elif level == 3:
        return 6 + hitung_ancaman_berjenjang(4, kedalaman + 1)
    elif level == 4:
        return 4 + hitung_ancaman_berjenjang(5, kedalaman + 1)
    else:
        return 2

print(f"Total ancaman berjenjang: {hitung_ancaman_berjenjang(1)}")

print("\n")
print("=" * 70)
print("BAGIAN 12: REKURSI - VALIDASI NESTED DICTIONARY")
print("=" * 70)

def hitung_total_skor(data, kedalaman=0):
    """Menghitung total skor dari nested dictionary secara rekursif."""
    if kedalaman >= 4:
        return 0

    total = 0
    for key, value in data.items():
        if isinstance(value, dict):
            total += hitung_total_skor(value, kedalaman + 1)
        else:
            total += value
    return total

data_ancaman = {
    "insiden1": {"skor": 5, "detail": {"skor": 3}},
    "insiden2": {"skor": 8, "detail": {"skor": 4}},
    "insiden3": {"skor": 6}
}

print(f"Total skor seluruh insiden: {hitung_total_skor(data_ancaman)}")

print("\n")
print("=" * 70)
print("BAGIAN 13: ANALISIS PASSFRASE BANYAK USER")
print("=" * 70)

def analisis_passphrase(passphrase, username=""):
    """Menganalisis kekuatan passphrase dengan 6 kriteria."""
    karakter_spesial = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

    k1 = len(passphrase) >= 16
    k2 = sum(1 for c in passphrase if c.isupper()) >= 2
    k3 = any(c.islower() for c in passphrase)
    k4 = sum(1 for c in passphrase if c.isdigit()) >= 4
    k5 = any(c in karakter_spesial for c in passphrase)
    k6 = username.lower() not in passphrase.lower() if username else True

    skor = 0
    if k1: skor += 1
    if k2: skor += 1
    if k3: skor += 1
    if k4: skor += 1
    if k5: skor += 1
    if k6: skor += 1

    if skor >= 6:
        level = "SANGAT KUAT"
    elif skor >= 5:
        level = "KUAT"
    elif skor >= 3:
        level = "CUKUP"
    elif skor >= 1:
        level = "LEMAH"
    else:
        level = "SANGAT LEMAH"

    return skor, level

daftar_user = [
    {"user": "admin", "passphrase": "admin"},
    {"user": "engineer01", "passphrase": "Secure@Vault2024!"},
    {"user": "analyst", "passphrase": "Analyst123"},
    {"user": "operator", "passphrase": "Op3r@tor#V4ult2024"},
    {"user": "guest", "passphrase": "12345678"}
]

print(f"\n{'User':<14} | {'Passphrase':<25} | {'Skor':<6} | {'Level':<15}")
print("-" * 70)

for data in daftar_user:
    user = data["user"]
    pwd = data["passphrase"]
    skor, level = analisis_passphrase(pwd, user)
    pwd_tampil = "*" * len(pwd)
    print(f"{user:<14} | {pwd_tampil:<25} | {skor}/6    | {level:<15}")

print("\n")
print("=" * 70)
print("BAGIAN 14: STATISTIK DENGAN LAMBDA & BUILT-IN")
print("=" * 70)

skor_insiden = [3, 8, 5, 9, 2, 7, 6, 4, 9, 5, 7, 8]

total = reduce(lambda a, b: a + b, skor_insiden)
rata_rata = total / len(skor_insiden)
maks = reduce(lambda a, b: a if a > b else b, skor_insiden)
minim = reduce(lambda a, b: a if a < b else b, skor_insiden)
kritis = list(filter(lambda x: x >= 8, skor_insiden))
sedang = list(filter(lambda x: 5 <= x < 8, skor_insiden))
rendah = list(filter(lambda x: x < 5, skor_insiden))

print(f"Data skor            : {skor_insiden}")
print(f"Total skor           : {total}")
print(f"Rata-rata            : {rata_rata:.2f}")
print(f"Skor maksimum        : {maks}")
print(f"Skor minimum         : {minim}")
print(f"Insiden kritis (>=8) : {kritis} ({len(kritis)} insiden)")
print(f"Insiden sedang (5-7) : {sedang} ({len(sedang)} insiden)")
print(f"Insiden rendah (<5)  : {rendah} ({len(rendah)} insiden)")

print("\n")
print("=" * 70)
print("BAGIAN 15: LAMBDA PADA SORTING DAN MAX/MIN")
print("=" * 70)

# Data insiden untuk diurutkan
insiden = [
    {"id": "INC-001", "skor": 8, "ip": "192.168.1.100"},
    {"id": "INC-002", "skor": 3, "ip": "8.8.8.8"},
    {"id": "INC-003", "skor": 9, "ip": "10.0.0.1"},
    {"id": "INC-004", "skor": 5, "ip": "1.1.1.1"},
    {"id": "INC-005", "skor": 7, "ip": "172.16.0.1"}
]

# Sorting berdasarkan skor (ascending)
insiden_urut = sorted(insiden, key=lambda x: x["skor"])
print("\n1. Insiden diurutkan berdasarkan skor (naik):")
for inc in insiden_urut:
    print(f"   {inc['id']} | Skor: {inc['skor']} | IP: {inc['ip']}")

# Sorting berdasarkan skor (descending)
insiden_urut_desc = sorted(insiden, key=lambda x: x["skor"], reverse=True)
print("\n2. Insiden diurutkan berdasarkan skor (turun):")
for inc in insiden_urut_desc:
    print(f"   {inc['id']} | Skor: {inc['skor']} | IP: {inc['ip']}")

# Mencari insiden dengan skor tertinggi
insiden_max = max(insiden, key=lambda x: x["skor"])
print(f"\n3. Insiden skor tertinggi: {insiden_max['id']} (skor {insiden_max['skor']})")

# Mencari insiden dengan skor terendah
insiden_min = min(insiden, key=lambda x: x["skor"])
print(f"4. Insiden skor terendah: {insiden_min['id']} (skor {insiden_min['skor']})")

print("\n")
print("=" * 70)
print("BAGIAN 16: PIPELINE ANALISIS LOG FORENSIK LENGKAP")
print("=" * 70)

log_forensik = [
    {"ip": "192.168.1.100", "skor": 9, "status": "failed", "port": 22},
    {"ip": "8.8.8.8", "skor": 2, "status": "success", "port": 80},
    {"ip": "10.0.0.1", "skor": 8, "status": "failed", "port": 445},
    {"ip": "1.1.1.1", "skor": 3, "status": "success", "port": 443},
    {"ip": "172.16.0.1", "skor": 7, "status": "failed", "port": 3389},
    {"ip": "203.0.113.5", "skor": 9, "status": "failed", "port": 21},
    {"ip": "198.51.100.7", "skor": 4, "status": "success", "port": 80}
]

# 1. Filter log kritis (skor >= 7)
log_kritis = list(filter(lambda x: x["skor"] >= 7, log_forensik))

# 2. Map untuk mengambil IP dari log kritis
ip_kritis = list(map(lambda x: x["ip"], log_kritis))

# 3. Reduce untuk total skor log kritis
total_skor_kritis = reduce(lambda a, b: a + b["skor"], log_kritis, 0)

# 4. Filter log dengan port berbahaya
port_berbahaya = [21, 22, 23, 25, 135, 445, 3389]
log_port_bahaya = list(filter(lambda x: x["port"] in port_berbahaya, log_forensik))

# 5. Map untuk mengklasifikasikan status
laporan_kritis = list(map(
    lambda x: f"[KRITIS] {x['ip']}:{x['port']} - Skor {x['skor']} - {x['status'].upper()}",
    log_kritis
))

# 6. Total skor seluruh log
total_skor_semua = reduce(lambda a, b: a + b["skor"], log_forensik, 0)

# 7. Rata-rata skor
rata_skor = total_skor_semua / len(log_forensik)

# 8. Persentase log kritis
persen_kritis = (len(log_kritis) / len(log_forensik)) * 100

# Tampilkan hasil
print("\n--- LAPORAN ANALISIS LOG FORENSIK ---")
print(f"Total log              : {len(log_forensik)}")
print(f"Total skor             : {total_skor_semua}")
print(f"Rata-rata skor         : {rata_skor:.2f}")
print(f"Log kritis (>=7)       : {len(log_kritis)}")
print(f"Persentase kritis      : {persen_kritis:.2f}%")
print(f"Total skor kritis      : {total_skor_kritis}")

print(f"\nIP Kritis              : {ip_kritis}")
print(f"Log port berbahaya     : {len(log_port_bahaya)} entri")
print(f"\nLaporan Log Kritis:")
for laporan in laporan_kritis:
    print(f"  {laporan}")

# Rekomendasi berdasarkan analisis
print(f"\n--- REKOMENDASI ---")
if persen_kritis >= 50:
    print("PERINGATAN TINGGI: Lebih dari 50% log bersifat kritis!")
    print("Segera lakukan investigasi menyeluruh.")
elif persen_kritis >= 25:
    print("PERINGATAN SEDANG: Terdapat beberapa log kritis.")
    print("Lakukan monitoring ketat terhadap IP terkait.")
else:
    print("SISTEM AMAN: Sebagian besar log dalam kondisi normal.")

print("\n")
print("=" * 70)
print("BAGIAN 17: REKURSI VS ITERASI")
print("=" * 70)

# Rekursi: menghitung total skor berjenjang
def total_rekursif(data, index=0):
    if index >= len(data):
        return 0
    return data[index] + total_rekursif(data, index + 1)

# Iterasi: menghitung total skor
def total_iteratif(data):
    total = 0
    for skor in data:
        total += skor
    return total

# Reduce: menghitung total skor
def total_reduce(data):
    return reduce(lambda a, b: a + b, data)

skor_test = [3, 5, 7, 2, 8, 4, 6, 9]

print(f"Data skor: {skor_test}")
print(f"Rekursif : {total_rekursif(skor_test)}")
print(f"Iteratif : {total_iteratif(skor_test)}")
print(f"Reduce   : {total_reduce(skor_test)}")

print("\n")
print("=" * 70)
print("BAGIAN 18: KLASIFIKASI LOG OTOMATIS")
print("=" * 70)

# Fungsi lambda untuk klasifikasi
klasifikasi_log = lambda skor, status: (
    "CRITICAL" if skor >= 8 else
    "HIGH" if skor >= 6 else
    "MEDIUM" if skor >= 4 else
    "LOW" if skor >= 2 else
    "INFO"
)

log_untuk_klasifikasi = [
    {"ip": "192.168.1.100", "skor": 9, "status": "failed"},
    {"ip": "8.8.8.8", "skor": 2, "status": "success"},
    {"ip": "10.0.0.1", "skor": 8, "status": "failed"},
    {"ip": "1.1.1.1", "skor": 3, "status": "success"},
    {"ip": "172.16.0.1", "skor": 7, "status": "failed"},
    {"ip": "203.0.113.5", "skor": 5, "status": "failed"}
]

print(f"\n{'IP':<18} | {'Skor':<6} | {'Status':<10} | {'Klasifikasi':<12}")
print("-" * 65)

for log in log_untuk_klasifikasi:
    kategori = klasifikasi_log(log["skor"], log["status"])
    print(f"{log['ip']:<18} | {log['skor']:<6} | {log['status']:<10} | {kategori:<12}")

print("\n")
print("=" * 70)
print("PRAKTIKUM FUNGSI LANJUTAN & REKURSI SELESAI")
print("=" * 70)
print("\nMateri yang telah dipraktikkan:")
print("  1. Fungsi lambda dasar (tanpa parameter, 1 parameter, 2 parameter)")
print("  2. Lambda dengan kondisi ternary")
print("  3. Fungsi rekursif: faktorial")
print("  4. Fungsi rekursif: fibonacci")
print("  5. Fungsi rekursif: jumlah digit")
print("  6. Fungsi rekursif: struktur direktori log")
print("  7. map() untuk transformasi data")
print("  8. filter() untuk penyaringan data")
print("  9. reduce() untuk agregasi data")
print(" 10. Kombinasi map, filter, reduce")
print(" 11. Studi kasus terintegrasi analisis log forensik")
print(" 12. Rekursi untuk analisis berjenjang")
print(" 13. Lambda pada sorting dan max/min")
print(" 14. Pipeline analisis log lengkap")
print("=" * 70)