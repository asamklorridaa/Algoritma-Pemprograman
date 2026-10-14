print("="*70)
print("SISTEM MANAJEMEN LOG KEAMANAN SECURELOG")
print("="*70)

# BAGIAN 1: MEMBUAT DAN MENGAKSES LIST
print("\n")
print("="*70)
print("BAGIAN 1: MEMBUAT DAN MENGAKSES LIST")
print("="*70)

# Membuat list berisi IP berbahaya
ip_berbahaya = ["192.168.1.100", "10.0.0.1", "172.16.0.1"]

# Membuat list berisi port berbahaya
port_berbahaya = [21, 23, 25, 135, 445, 3389]

# Membuat list kosong untuk menampung log
log_akses = []

# Membuat list campuran (heterogen)
data_insiden = ["INC-001", 9, 3.14, True]

# Membuat list bersarang (nested)
matriks_zona = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Mengakses elemen list
print(f"\nIP berbahaya           : {ip_berbahaya}")
print(f"Elemen pertama         : {ip_berbahaya[0]}")
print(f"Elemen kedua           : {ip_berbahaya[1]}")
print(f"Elemen terakhir        : {ip_berbahaya[-1]}")
print(f"Port berbahaya         : {port_berbahaya}")
print(f"Data insiden           : {data_insiden}")
print(f"Matriks zona [1][2]    : {matriks_zona[1][2]}")


# BAGIAN 2: OPERASI DASAR LIST MENAMBAH DATA
print("\n")
print("=" * 70)
print("BAGIAN 2: OPERASI DASAR LIST MENAMBAH DATA")
print("=" * 70)

# Data awal
ip_blacklist = ["192.168.1.100"]
print(f"\nData awal              : {ip_blacklist}")

# append: menambah di akhir
ip_blacklist.append("10.0.0.1")
print(f"Setelah append         : {ip_blacklist}")

# insert: menyisipkan di posisi tertentu
ip_blacklist.insert(1, "172.16.0.1")
print(f"Setelah insert         : {ip_blacklist}")

# extend: menggabungkan dengan list lain
ip_blacklist.extend(["203.0.113.5", "198.51.100.7"])
print(f"Setelah extend         : {ip_blacklist}")

# Menambaah denga operator +
ip_lain = ip_blacklist + ["185.220.101.1"]
print(f"Setelah operator +     : {ip_lain}")


# BAGIAN 3: OPERASI DASAR LIST MENGHAPUS DATA
print("\n")
print("=" * 70)
print("BAGIAN 3: OPERASI DASAR LIST MENGHAPUS DATA")
print("=" * 70)

# Data awal
ip_blacklist = ["192.168.1.100", "10.0.0.1", "172.16.0.1", "203.0.113.5", "198.51.100.7"]
print(f"\nData awal              : {ip_blacklist}")

# remove: menghapus berdasarkan nilai
ip_blacklist.remove("10.0.0.1")
print(f"Setelah remove         : {ip_blacklist}")

# pop: menghapus dan mengembalikan elemen terakhir
ip_terakhir = ip_blacklist.pop()
print(f"Setelah pop            : {ip_blacklist}")
print(f"Elemen yang di-pop     : {ip_terakhir}")

# pop dengan index
ip_index1 = ip_blacklist.pop(1)
print(f"Setelah pop(1)         : {ip_blacklist}")
print(f"Elemen yang di-pop     : {ip_index1}")

# del: menghapus berdasarkan index
del ip_blacklist[0]
print(f"Setelah del [0]        : {ip_blacklist}")

# clear: menghapus semua elemen
ip_temp = ["8.8.8.8", "1.1.1.1"]
ip_temp.clear()
print(f"Setelah clear          : {ip_temp}")


# BAGIAN 4: SLICING LIST
print("\n")
print("=" * 70)
print("BAGIAN 4: SLICING LIST")
print("=" * 70)

# Data log IP
log_ip = [
    "10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4",
    "10.0.0.5", "10.0.0.6", "10.0.0.7", "10.0.0.8"
]

print(f"\nData lengkap           : {log_ip}")
print(f"[2:5]                  : {log_ip[2:5]}")
print(f"[:3]                   : {log_ip[:3]}")
print(f"[5:]                   : {log_ip[5:]}")
print(f"[::2]                  : {log_ip[::2]}")
print(f"[::-1]                 : {log_ip[::-1]}")
print(f"5 IP pertama           : {log_ip[:5]}")
print(f"3 IP terakhir          : {log_ip[-3:]}")

# Copy list dengan slicing
log_copy = log_ip[:]
print(f"\nCopy list dengan [:]   : {log_copy}")


# BAGIAN 5: METHOD LIST
print("\n")
print("=" * 70)
print("BAGIAN 5: METHOD LIST")
print("=" * 70)

# Data skor ancaman
skor = [85, 60, 90, 75, 88, 60, 95, 70]
print(f"\nData skor              : {skor}")

# count: menghitung kemunculan
print(f"Jumlah skor 60         : {skor.count(60)}")

# index: mencari index nilai
print(f"Index skor 90          : {skor.index(90)}")

# sort ascending
skor.sort()
print(f"Setelah sort asc       : {skor}")

# sort desccending
skor.sort(reverse=True)
print(f"Setelah sort desc      : {skor}")

# reverse
skor.reverse()
print(f"Setelah reverse        : {skor}")

# copy
skor_copy = skor.copy()
print(f"Copy skor              : {skor_copy}")

# Panjang list
print(f"Panjang list           : {len(skor)}")

# Cek keanggotaan
print(f"90 ada di list?        : {90 in skor}")
print(f"100 ada di list?       : {100 in skor}")


# BAGIAN 6: ITERASI LIST
print("\n")
print("=" * 70)
print("BAGIAN 6: ITERASI LIST")
print("=" * 70)

ip_berbahaya = ["192.168.1.100", "10.0.0.1", "172.16.0.1"]

# Iterasi sederhana
print("\n--- ITERASI SEDERHANA ---")
for ip in ip_berbahaya:
    print(f" IP: {ip}")

# Iterasi dengan index
print("\n--- ITERASI DENGAN ENUMERATE ---")
for i, ip in enumerate(ip_berbahaya):
    print(f" IP ke-{i+1}: {ip}")

# Interasi dengan kondisi
print("\n--- ITERASI DENGAN KONDISI ---")
for ip in ip_berbahaya:
    if ip.startswith("10."):
        print(f" IP privat: {ip}")
    else:
        print(f" IP publik: {ip}")


# BAGIAN 7: TUPLE
print("\n")
print("=" * 70)
print("BAGIAN 7: TUPLE")
print("=" * 70)

# Membuat tuple
PROTOKOL_AMAN = ("HTTPS", "SSH", "SFTP", "TLS")
KATEGORI_ANCAMAN = ("MALWARE", "PHISHING", "DDOS", "RANSOMWARE")
KOORDINAT_SERVER = (10, 20)


print(f"\nProtokol aman          : {PROTOKOL_AMAN}")
print(f"Kategori ancaman       : {KATEGORI_ANCAMAN}")
print(f"Koordinat server       : {KOORDINAT_SERVER}")

# Mengakses elemen tuple
print(f"\nProtokol pertama       : {PROTOKOL_AMAN[0]}")
print(f"Protokol terakhir      : {PROTOKOL_AMAN[-1]}")
print(f"Slicing [1:3]          : {PROTOKOL_AMAN[1:3]}")

# Panjang tuple
print(f"Jumlah protokol        : {len(PROTOKOL_AMAN)}")

# Cek keanggotaan
print(f"HTTPS ada?             : {'HTTPS' in PROTOKOL_AMAN}")
print(f"HTTP ada?              : {'HTTP' in PROTOKOL_AMAN}")

# index dan count
print(f"Index 'SSH'            : {PROTOKOL_AMAN.index('SSH')}")
print(f"Count 'HTTPS'          : {PROTOKOL_AMAN.count('HTTPS')}")

# Menggabungkan tuple
protokol_baru = PROTOKOL_AMAN + ("IPSEC", "WPA3")
print(f"\nProtokol baru          : {protokol_baru}")

# Mengulang tuple
ulang = ("A",) * 3
print(f"Tuple diulang          : {ulang}")


# BAGIAN 8: TUPLE UNPACKING
print("\n")
print("=" * 70)
print("BAGIAN 8: TUPLE UNPACKING")
print("=" * 70)

# Unpacking sederhana
koordinat = (10, 20)
x, y = koordinat
print(f"\nKoordinat: x={x}, y={y}")

# unpacking data insiden
insiden = ("INC-001", "192.168.1.100", 9, "blocked")
id_insiden, ip_insiden, skor_insiden, status = insiden
print(f"\nData insiden:")
print(f" ID                    : {id_insiden}")
print(f" IP                    : {ip_insiden}")
print(f" Skor                  : {skor_insiden}")
print(f" Status                : {status}")

# Unpacking dengan bintang
angka = (1, 2, 3, 4, 5)
pertama, *tengah, terakhir = angka
print(f"\nPertama                : {pertama}")
print(f"Tengah                 : {tengah}")
print(f"Terakhir               : {terakhir}")

# Konversi lis ke tuple dan sebaliknyaa
list_ip = ["10.0.0.1", "10.0.0.2"]
tuple_ip = tuple(list_ip)
print(f"\nList ke Tuple          : {tuple_ip}")
print(f"Tipe data              : {type(tuple_ip)}")

tuple_port = (21, 22, 80)
list_port = list(tuple_port)
print(f"Tuple ke List          : {list_port}")
print(f"Tipe data              : {type(list_port)}")


# BAGIAN 9: LIST COMPREHENSION DASAR
print("\n")
print("=" * 70)
print("BAGIAN 9: LIST COMPREHENSION DASAR")
print("=" * 70)

angka = [1, 2, 3, 4, 5]

# Cara biasa dengan perulangan
kuadrat_biasa = []
for x in angka:
    kuadrat_biasa.append(x**2)
print(f"\nDengan perulangan      : {kuadrat_biasa}")

# Dengan list comprehension
kuadrat_lc = [x**2 for x in angka]
print(f"Dengan comprehension   : {kuadrat_lc}")

# Konversi string ke integer
port_str = ["21", "22", "80", "443", "8080"]
port_int = [int(p) for p in port_str]
print(f"\nPort string            : {port_str}")
print(f"Port integer           : {port_int}")

# Membuat list berisi nol
nol = [0] * 5
print(f"\nList nol               : {nol}")

# List dari range
range_list = [i for i in range(1, 11)]
print(f"List dari range        : {range_list}")


# BAGIAN 10: LIST COMPREHENSION DENGAN KONDISI
print("\n")
print("=" * 70)
print("BAGIAN 10: LIST COMPREHENSION DENGAN KONDISI")
print("=" * 70)

angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter angka genap
genap = [x for x in angka if x % 2 == 0]
print(f"\nAngka genap            : {genap}")

# Filter angka ganjil
ganjil = [x for x in angka if x % 2 != 0]
print(f"Angka ganjil           : {ganjil}")

# Filter angka > 5
besar = [x for x in angka if x > 5]
print(f"Angka > 5              : {besar}")

# Filter IP lokal
ip_list = [
    "192.168.1.100", "8.8.8.8",
    "10.0.0.1", "1.1.1.1",
    "192.168.1.101", "172.16.0.1"
]
ip_lokal = [ip for ip in ip_list if ip.startswith("192.168.")]
print(f"\nIP list                : {ip_list}")
print(f"IP lokal (192.168.)    : {ip_lokal}")

ip_privat = [ip for ip in ip_list if ip.startswith("10.") or ip.startswith("192.168.") or ip.startswith("172.")]
print(f"IP privat              : {ip_privat}")


# BAGIAN 11: LIST COMPREHENSION DENGAN IF-ELSE
print("\n")
print("=" * 70)
print("BAGIAN 11: LIST COMPREHENSION DENGAN IF-ELSE")
print("=" * 70)

angka = [1, 2, 3, 4, 5, 6, 7, 8]

# Label genap/ganjil
label = ["GENAP" if x % 2 == 0 else "GANJIL" for x in angka]
print(f"\nAngka                  : {angka}")
print(f"Label                  : {label}")

# Klasifikasi skor ancaman
skor = [3, 8, 5, 9, 2, 7, 6, 4]
kategori = [
    "CRITICAL" if s >= 8 else
    "HIGH" if s >= 6 else
    "MEDIUM" if s >= 4 else
    "LOW"
    for s in skor
]
print(f"\nSkor                   : {skor}")
print(f"Kategori               : {kategori}")

# Menambah prefix pada IP
ip_list = ["192.168.1.100", "10.0.0.1", "8.8.8.8"]
ip_prefixed = [f"IP-{ip}" for ip in ip_list]
print(f"\nIP asli                : {ip_list}")
print(f"IP prefix              : {ip_prefixed}")


# BAGIAN 12: LIST COMPREHENSION BERSARANG
print("\n")
print("=" * 70)
print("BAGIAN 12: LIST COMPREHENSION BERSARANG")
print("=" * 70)

# Matriks 3x3 dengan list comprehension
matriks = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"\nMatriks 3x3:")
for baris in matriks:
    print(f" {baris}")

# Flatten matriks menjadi list
flatten = [angka for baris in matriks for angka in baris]
print(f"\nFlatten matriks        : {flatten}")

# Matriks identitas
identitas = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
print(f"\nMatriks identitas 4x4:")
for baris in identitas:
    print(f" {baris}")


# BAGIAN 13: STUDI KASUS MANAJEMEN IP BLACKLIST
print("\n")
print("=" * 70)
print("BAGIAN 13: STUDI KASUS MANAJEMEN IP BLACKLIST")
print("=" * 70)

# Database IP blacklist
ip_blacklist = [
    "192.168.1.100", "10.0.0.1", "172.16.0.1",
    "203.0.113.5", "198.51.100.7", "185.220.101.1"
]

# Log akses dari firewall
log_akses = [
    "192.168.1.100", "8.8.8.8", "10.0.0.1",
    "1.1.1.1", "203.0.113.5", "172.16.0.1",
    "192.168.1.50", "185.220.101.1", "8.8.4.4"
]


print(f"\nTotal IP blacklist     : {len(ip_blacklist)}")
print(f"Total log akses        : {len(log_akses)}")

# Filter IP berbahaya
ip_terdeteksi = [ip for ip in log_akses if ip in ip_blacklist]
print(f"\nIP berbahaya terdeteksi: {ip_terdeteksi}")
print(f"Total                  : {len(ip_terdeteksi)}")

# Filter IP aman
ip_aman = [ip for ip in log_akses if ip not in ip_blacklist]
print(f"\nIP aman                : {ip_aman}")
print(f"Total                  : {len(ip_aman)}")

# Statistik
total_akses = len(log_akses)
total_bahaya = len(ip_terdeteksi)
persentase = (total_bahaya / total_akses) * 100

print(f"\n--- STATISTIK ---")
print(f"Total akses            : {total_akses}")
print(f"Akses berbahaya        : {total_bahaya}")
print(f"Akses aman             : {len(ip_aman)}")
print(f"Persentase bahaya      : {persentase:.2f}%")


# BAGIAN 14: STUDI KASUS ANALISIS SKOR ANCAMAN
print("\n")
print("=" * 70)
print("BAGIAN 14: STUDI KASUS ANALISIS SKOR ANCAMAN")
print("=" * 70)

# Data skor ancaman dari berbagai insiden
skor_ancaman = [3, 8, 5, 9, 2, 7, 6, 4, 9, 5, 7, 8, 6, 3, 9]

print(f"\nData skor              : {skor_ancaman}")
print(f"Total insiden          : {len(skor_ancaman)}")

# Statistik dasar
total_skor = sum(skor_ancaman)
rata_rata = total_skor / len(skor_ancaman)
skor_maks = max(skor_ancaman)
skor_min = min(skor_ancaman)

print(f"\nTotal skor             : {total_skor}")
print(f"Rata-rata skor         : {rata_rata:.2f}")
print(f"Skor maksimum          : {skor_maks}")
print(f"Skor minimum           : {skor_min}")

# Klasifikasi dengan list comprehension
kritis = [s for s in skor_ancaman if s >= 8]
tinggi = [s for s in skor_ancaman if 6 <= s < 8]
sedang = [s for s in skor_ancaman if 4 <= s < 6]
rendah = [s for s in skor_ancaman if s < 4]

print(f"\n--- KLASIFIKASI ---")
print(f"Kritis (>=8)           : {kritis} ({len(kritis)} insiden)")
print(f"Tinggi (6-7)           : {tinggi} ({len(tinggi)} insiden)")
print(f"Sedang (4-5)           : {sedang} ({len(sedang)} insiden)")
print(f"Rendah (<4)            : {rendah} ({len(rendah)} insiden)")

# Klasifikasi label
label = [
    "CRITICAL" if s >= 8 else
    "HIGH" if s >= 6 else
    "MEDIUM" if s >= 4 else
    "LOW"
    for s in skor_ancaman
]
print(f"\nLabel                  : {label}")


# BAGIAN 15: STUDI KASUS TUPLE UNTUK DATA KONSTAN
print("\n")
print("=" * 70)
print("BAGIAN 15: STUDI KASUS TUPLE UNTUK DATA KONSTAN")
print("=" * 70)

# Data konstan dalam tuple
PROTOKOL_AMAN = ("HTTPS", "SSH", "SFTP", "TLS")
PROTOKOL_BERBAHAYA = ("FTP", "TELNET", "HTTP", "SMTP")
KATEGORI_ANCAMAN = ("MALWARE", "PHISHING", "DDOS", "RANSOMWARE", "SQL_INJECTION")
LEVEL_ANCAMAN = ("LOW", "MEDIUM", "HIGH", "CRITICAL")

print(f"\nProtokol aman          : {PROTOKOL_AMAN}")
print(f"Protokol berbahaya     : {PROTOKOL_BERBAHAYA}")
print(f"Kategori ancaman       : {KATEGORI_ANCAMAN}")
print(f"Level ancaman          : {LEVEL_ANCAMAN}")

# Data log dengan protokol
log_koneksi = [
    ("192.168.1.100", "HTTPS"),
    ("10.0.0.1", "FTP"),
    ("172.16.0.1", "TELNET"),
    ("8.8.8.8", "HTTPS"),
    ("203.0.113.5", "SSH"),
    ("1.1.1.1", "HTTP")
]

print("\n--- ANALISIS KONEKSI ---")
for ip, protokol in log_koneksi:
    if protokol in PROTOKOL_AMAN:
        status = "AMAN"
    elif protokol in PROTOKOL_BERBAHAYA:
        status = "BERBAHAYA"
    else:
        status = "TIDAK DIKETAHUI"
    print(f" {ip:18} | {protokol:10} | {status}")


# BAGIAN 16: STUDI KASUS SISTEM MANAJEMEN LOG TERPADU
print("\n")
print("=" * 70)
print("BAGIAN 16: SISTEM MANAJEMEN LOG TERPADU")
print("=" * 70)

# Database utama
IP_BLACKLIST = (
    "192.168.1.100", "10.0.0.1", "172.16.0.1",
    "203.0.113.5", "198.51.100.7", "185.220.101.1"
)

# Log akses
log_akses = [
    {"ip": "192.168.1.100", "skor": 9, "status": "blocked", "port": 22},
    {"ip": "8.8.8.8", "skor": 2, "status": "allowed", "port": 443},
    {"ip": "10.0.0.1", "skor": 8, "status": "blocked", "port": 445},
    {"ip": "1.1.1.1", "skor": 3, "status": "allowed", "port": 80},
    {"ip": "203.0.113.5", "skor": 9, "status": "blocked", "port": 21},
    {"ip": "172.16.0.1", "skor": 7, "status": "blocked", "port": 3389},
    {"ip": "192.168.1.50", "skor": 4, "status": "allowed", "port": 8080},
    {"ip": "185.220.101.1", "skor": 9, "status": "blocked", "port": 23}
]

print(f"\nTotal log              : {len(log_akses)}")

# 1. Filter log kritis
log_kritis = [log for log in log_akses if log["skor"] >= 7]
print(f"\n--- LOG KRITIS (skor >= 7) ---")
for log in log_kritis:
    print(f" IP: {log['ip']:18} | Skor: {log['skor']} | Status: {log['status']}")

# 2. Filter log dengan IP blacklist
log_blacklist = [log for log in log_akses if log["ip"] in IP_BLACKLIST]
print(f"\n--- LOG DENGAN IP BLACKLIST ---")
for log in log_blacklist:
    print(f" IP: {log['ip']:18} | Skor: {log['skor']}")

# 3. Filter log dengan port berbahaya
PORT_BERBAHAYA = [21, 22, 23, 25, 135, 445, 3389]
log_port_bahaya = [log for log in log_akses if log["port"] in PORT_BERBAHAYA]
print(f"\n--- LOG DENGAN PORT BERBAHAYA ---")
for log in log_port_bahaya:
    print(f" IP: {log['ip']:18} | Port: {log['port']}")

# 4. Ekstrak semua IP
semua_ip = [log["ip"] for log in log_akses]
print(f"\nSemua IP               : {semua_ip}")

# 5. Ekstrak semua skor
semua_skor = [log["skor"] for log in log_akses]
print(f"Semua skor             : {semua_skor}")

# Statistik
total_skor = sum(semua_skor)
rata_skor = total_skor / len(semua_skor)
persentase_kritis = (len(log_kritis) / len(log_akses)) * 100

print(f"\n--- STATISTIK ---")
print(f"Total skor             : {total_skor}")
print(f"Rata-rata skor         : {rata_skor:.2f}")
print(f"Log kritis             : {len(log_kritis)}")
print(f"Persentase kritis      : {persentase_kritis:.2f}%")

# 7. Klasifikasi log
for log in log_akses:
    if log["skor"] >= 8:
        log["kategori"] = "CRITICAL"
    elif log["skor"] >= 6:
        log["kategori"] = "HIGH"
    elif log["skor"] >= 4:
        log["kategori"] = "MEDIUM"
    else:
        log["kategori"] = "LOW"

print("\n--- LAPORAN LENGKAP ---")
print(f"{'IP':<18} | {'Skor':<5} | {'Status':<10} | {'Kategori':<10}")
print("-" * 60)
for log in log_akses:
    print(f"{log['ip']:<18} | {log['skor']:<5} | {log['status']:<10} | {log['kategori']:<10}")

# Rekomendasi
print(f"\n--- REKOMENDASI ---")
if persentase_kritis >= 50:
    print("PERINGATAN TINGGI: Lebih dari 50% log kritis!")
    print("Segera lakukan investigasi menyeluruh.")
elif persentase_kritis >= 25:
    print("PERINGATAN SEDANG: Terdapat beberapa log kritis.")
    print("Lakukan monitoring ketat.")
else:
    print("SISTEM AMAN: Sebagian besar log dalam kondisi normal.")

# Penutup
print("\n")
print("=" * 70)
print("PRAKTIKUM STRUKTUR DATA LIST & TUPLE SELESAI")
print("=" * 70)
print("\nMateri yang telah dipraktikkan:")
print(" 1. Membuat dan mengakses list")
print(" 2. Operasi dasar list: append, insert, extend")
print(" 3. Operasi dasar list: remove, pop, del, clear")
print(" 4. Slicing list")
print(" 5. Method list: count, index, sort, reverse, copy")
print(" 6. Iterasi list dengan for dan enumerate")
print(" 7. Membuat dan mengakses tuple")
print(" 8. Tuple unpacking")
print(" 9. List comprehension dasar")
print(" 10. List comprehension dengan kondisi")
print(" 11. List comprehension dengan if-else")
print(" 12. List comprehension bersarang")
print(" 13. Studi kasus manajemen IP blacklist")
print(" 14. Studi kasus analisis skor ancaman")
print(" 15. Studi kasus tuple untuk data konstan")
print(" 16. Sistem manajemen log terpadu")
print("=" * 70)