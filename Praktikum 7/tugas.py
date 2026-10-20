def reduce(fungsi, data, *awal):
    iterator = iter(data)
    hasil = awal[0] if awal else next(iterator)
    for item in iterator:
        hasil = fungsi(hasil, item)
    return hasil

print(f"{'=' * 70}")
print(f"SISTEM ANALISIS FORENSIK LOG DIGITALTRACE")
print(f"{'=' * 70}")

garis = lambda: "-" * 62

# Fungsi bantu: mencetak daftar log dalam format tabel
def cetak_tabel(daftar_log):
    print(f"{'No':<3} | {'IP':<16} | {'Port':<5} | {'Protokol':<9} | {'Skor':<4} | {'Status':<8}")
    print(f"{garis()}")
    for no, log in enumerate(daftar_log, 1):
        print(f"{no:<3} | {log['ip']:<16} | {log['port']:<5} | {log['protokol']:<9} | {log['skor']:<4} | {log['status']:<8}")
    if not daftar_log:
        print(f"(tidak ada data)")


# BAGIAN 1: MANAJEMEN DATABASE IP BLACKLIST (LIST & TUPLE)
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 1: MANAJEMEN DATABASE IP BLACKLIST (LIST & TUPLE)")
print(f"{'=' * 70}")

# Tuple IP blacklist (data konstan, minimal 6 IP)
IP_BLACKLIST = (
    "192.168.1.100", "10.0.0.1", "172.16.0.1",
    "203.0.113.5", "198.51.100.7", "185.220.101.1"
)

# Tuple port berbahaya (data konstan, minimal 8 port)
PORT_BERBAHAYA = (21, 22, 23, 25, 135, 445, 3389, 5900)

# Tuple protokol aman (data konstan, minimal 4 protokol)
PROTOKOL_AMAN = ("HTTPS", "SSH", "SFTP", "TLS")

# List of dictionary untuk log akses (minimal 10 log)
log_akses = [
    {"ip": "192.168.1.100", "port": 22,   "protokol": "SSH",    "skor": 9, "status": "blocked"},
    {"ip": "8.8.8.8",       "port": 443,  "protokol": "HTTPS",  "skor": 2, "status": "allowed"},
    {"ip": "10.0.0.1",      "port": 445,  "protokol": "SMB",    "skor": 8, "status": "blocked"},
    {"ip": "1.1.1.1",       "port": 80,   "protokol": "HTTP",   "skor": 3, "status": "allowed"},
    {"ip": "203.0.113.5",   "port": 21,   "protokol": "FTP",    "skor": 9, "status": "blocked"},
    {"ip": "172.16.0.1",    "port": 3389, "protokol": "RDP",    "skor": 7, "status": "blocked"},
    {"ip": "192.168.1.50",  "port": 8080, "protokol": "HTTP",   "skor": 4, "status": "allowed"},
    {"ip": "185.220.101.1", "port": 23,   "protokol": "TELNET", "skor": 9, "status": "blocked"},
    {"ip": "198.51.100.7",  "port": 5900, "protokol": "VNC",    "skor": 6, "status": "blocked"},
    {"ip": "8.8.4.4",       "port": 443,  "protokol": "TLS",    "skor": 1, "status": "allowed"}
]

# Menampilkan seluruh data referensi dengan format rapi
print(f"\n--- DATA REFERENSI ---")
print(f"Total IP blacklist     : {len(IP_BLACKLIST)}")
for no, ip in enumerate(IP_BLACKLIST, 1):
    print(f" {no}. {ip}")
print(f"\nPort berbahaya         : {PORT_BERBAHAYA}")
print(f"Protokol aman          : {PROTOKOL_AMAN}")
print(f"\n--- DATA LOG AKSES ---")
print(f"Total log              : {len(log_akses)}")
cetak_tabel(log_akses)

# List comprehension: ekstrak semua IP, port, dan skor dari log
semua_ip = [log["ip"] for log in log_akses]
semua_port = [log["port"] for log in log_akses]
semua_skor = [log["skor"] for log in log_akses]

print(f"\nSemua IP               : {semua_ip}")
print(f"Semua port             : {semua_port}")
print(f"Semua skor             : {semua_skor}")


# BAGIAN 2: OPERASI LIST PADA LOG
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 2: OPERASI LIST PADA LOG")
print(f"{'=' * 70}")

# len(): jumlah total log
print(f"\nJumlah total log       : {len(log_akses)}")

# Slicing [:3]: 3 log pertama
print(f"\n--- 3 LOG PERTAMA [:3] ---")
cetak_tabel(log_akses[:3])

# Slicing [-3:]: 3 log terakhir
print(f"\n--- 3 LOG TERAKHIR [-3:] ---")
cetak_tabel(log_akses[-3:])

# Slicing [2:5]: log index 2 sampai 4
print(f"\n--- LOG INDEX 2 SAMPAI 5 [2:5] ---")
cetak_tabel(log_akses[2:5])

# Slicing [::-1]: urutan terbalik
print(f"\n--- LOG URUTAN TERBALIK [::-1] ---")
cetak_tabel(log_akses[::-1])

# append: menambah log baru di akhir
log_baru = {"ip": "45.33.32.156", "port": 8443, "protokol": "HTTPS", "skor": 5, "status": "allowed"}
log_akses.append(log_baru)
print(f"\nSetelah append         : {len(log_akses)} log (log terakhir: {log_akses[-1]['ip']})")

# insert: menyisipkan log di index 1
log_sisip = {"ip": "91.240.118.172", "port": 1433, "protokol": "TDS", "skor": 8, "status": "blocked"}
log_akses.insert(1, log_sisip)
print(f"Setelah insert         : {len(log_akses)} log (log index 1: {log_akses[1]['ip']})")

# remove: menghapus log berdasarkan nilai (log yang disisipkan tadi)
log_akses.remove(log_sisip)
print(f"Setelah remove         : {len(log_akses)} log (log index 1: {log_akses[1]['ip']})")

# pop: menghapus log terakhir dan menampilkan log yang dihapus
log_terhapus = log_akses.pop()
print(f"Setelah pop            : {len(log_akses)} log")
print(f"\n--- LOG YANG DI-POP ---")
cetak_tabel([log_terhapus])

# copy dan slicing [:]: membuat salinan list log
log_salinan = log_akses.copy()
log_salinan_slice = log_akses[:]
print(f"\nCopy dengan copy()     : {len(log_salinan)} log")
print(f"Copy dengan [:]        : {len(log_salinan_slice)} log")
print(f"Objek sama dengan asli?: {log_salinan is log_akses}")


# BAGIAN 3: ANALISIS LOG DENGAN FILTER() DAN LAMBDA
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 3: ANALISIS LOG DENGAN FILTER() DAN LAMBDA")
print(f"{'=' * 70}")

# Filter 1: log kritis (skor >= 7)
log_kritis = list(filter(lambda log: log["skor"] >= 7, log_akses))
print(f"\n--- FILTER 1: LOG KRITIS (skor >= 7) ---")
cetak_tabel(log_kritis)

# Filter 2: log dengan IP yang ada di IP_BLACKLIST
log_blacklist = list(filter(lambda log: log["ip"] in IP_BLACKLIST, log_akses))
print(f"\n--- FILTER 2: LOG DENGAN IP BLACKLIST ---")
cetak_tabel(log_blacklist)

# Filter 3: log dengan port yang ada di PORT_BERBAHAYA
log_port_bahaya = list(filter(lambda log: log["port"] in PORT_BERBAHAYA, log_akses))
print(f"\n--- FILTER 3: LOG DENGAN PORT BERBAHAYA ---")
cetak_tabel(log_port_bahaya)

# Filter 4: log dengan status "blocked"
log_blocked = list(filter(lambda log: log["status"] == "blocked", log_akses))
print(f"\n--- FILTER 4: LOG DENGAN STATUS BLOCKED ---")
cetak_tabel(log_blocked)

# Filter 5: log dengan protokol yang tidak ada di PROTOKOL_AMAN
log_tidak_aman = list(filter(lambda log: log["protokol"] not in PROTOKOL_AMAN, log_akses))
print(f"\n--- FILTER 5: LOG DENGAN PROTOKOL TIDAK AMAN ---")
cetak_tabel(log_tidak_aman)


# BAGIAN 4: TRANSFORMASI LOG DENGAN MAP() DAN LAMBDA
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 4: TRANSFORMASI LOG DENGAN MAP() DAN LAMBDA")
print(f"{'=' * 70}")

# Map 1: ekstrak semua IP
hasil_ip = list(map(lambda log: log["ip"], log_akses))
print(f"\nSemua IP               : {hasil_ip}")

# Map 2: ekstrak semua skor
hasil_skor = list(map(lambda log: log["skor"], log_akses))
print(f"Semua skor             : {hasil_skor}")

# Map 3: label status "[STATUS] IP:PORT - Skor X"
hasil_label = list(map(
    lambda log: f"[{log['status'].upper()}] {log['ip']}:{log['port']} - Skor {log['skor']}",
    log_akses
))
print(f"\n--- LABEL STATUS ---")
for label in hasil_label:
    print(f" {label}")

# Map 4: ubah semua IP menjadi uppercase
hasil_upper = list(map(lambda ip: ip.upper(), hasil_ip))
print(f"\nIP uppercase           : {hasil_upper}")

# Map 5: klasifikasi skor menjadi kategori (ternary bertingkat)
hasil_kategori = list(map(
    lambda s: "CRITICAL" if s >= 8 else "HIGH" if s >= 6 else "MEDIUM" if s >= 4 else "LOW",
    hasil_skor
))
print(f"Skor                   : {hasil_skor}")
print(f"Kategori               : {hasil_kategori}")


# BAGIAN 5: AGREGASI LOG DENGAN REDUCE()
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 5: AGREGASI LOG DENGAN REDUCE()")
print(f"{'=' * 70}")

# Reduce 1: total skor semua log
total_skor = reduce(lambda acc, log: acc + log["skor"], log_akses, 0)

# Reduce 2: skor maksimum
skor_maks = reduce(lambda a, b: a if a > b else b, hasil_skor)

# Reduce 3: skor minimum
skor_min = reduce(lambda a, b: a if a < b else b, hasil_skor)

# Reduce 4: total skor log kritis dengan initial value 0
total_skor_kritis = reduce(lambda acc, log: acc + (log["skor"] if log["skor"] >= 7 else 0), log_akses, 0)

# Reduce 5: jumlah log berstatus blocked
jumlah_blocked = reduce(lambda acc, log: acc + (1 if log["status"] == "blocked" else 0), log_akses, 0)

# Rata-rata skor: total dibagi len()
rata_skor = total_skor / len(log_akses)

print(f"\n--- STATISTIK LOG ---")
print(f"Total log              : {len(log_akses)}")
print(f"Total skor             : {total_skor}")
print(f"Skor maksimum          : {skor_maks}")
print(f"Skor minimum           : {skor_min}")
print(f"Total skor log kritis  : {total_skor_kritis}")
print(f"Jumlah log blocked     : {jumlah_blocked}")
print(f"Rata-rata skor         : {rata_skor:.2f}")


# BAGIAN 6: PIPELINE FILTER -> MAP -> REDUCE
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 6: PIPELINE FILTER -> MAP -> REDUCE")
print(f"{'=' * 70}")

# Pipeline 1: log kritis -> ambil IP -> total karakter IP
print(f"\nPipeline 1 (total karakter IP kritis) : {reduce(lambda acc, ip: acc + len(ip), map(lambda log: log['ip'], filter(lambda log: log['skor'] >= 7, log_akses)), 0)}")

# Pipeline 2: log blacklist -> ambil port -> total port unik
print(f"Pipeline 2 (total port unik blacklist): {len(reduce(lambda acc, p: acc if p in acc else acc + [p], map(lambda log: log['port'], filter(lambda log: log['ip'] in IP_BLACKLIST, log_akses)), []))}")

# Pipeline 3: log blocked -> skor x 10 -> total
print(f"Pipeline 3 (total skor blocked x 10)  : {reduce(lambda acc, s: acc + s, map(lambda log: log['skor'] * 10, filter(lambda log: log['status'] == 'blocked', log_akses)), 0)}")


# BAGIAN 7: ANALISIS RANTAI SERANGAN DENGAN REKURSI
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 7: ANALISIS RANTAI SERANGAN DENGAN REKURSI")
print(f"{'=' * 70}")

# Nested dictionary rantai serangan (attack chain)
attack_chain = {
    "initial_access":       {"skor": 5,  "next": "execution"},
    "execution":            {"skor": 8,  "next": "persistence"},
    "persistence":          {"skor": 6,  "next": "privilege_escalation"},
    "privilege_escalation": {"skor": 9,  "next": "lateral_movement"},
    "lateral_movement":     {"skor": 7,  "next": "exfiltration"},
    "exfiltration":         {"skor": 10, "next": None}
}


# Fungsi rekursif: menghitung total dampak serangan
def hitung_dampak_serangan(chain, tahap="initial_access", kedalaman=0):
    # Base case: tahap tidak ada di chain ATAU kedalaman >= 6
    if tahap not in chain or kedalaman >= 6:
        return 0
    # Skor tahap saat ini + rekursi ke tahap berikutnya
    return chain[tahap]["skor"] + hitung_dampak_serangan(chain, chain[tahap]["next"], kedalaman + 1)


# Fungsi rekursif: menghitung kedalaman maksimum rantai serangan
def hitung_kedalaman_rantai(chain, tahap="initial_access", kedalaman=0):
    # Base case: tahap tidak ada di chain ATAU kedalaman >= 6
    if tahap not in chain or kedalaman >= 6:
        return kedalaman
    return hitung_kedalaman_rantai(chain, chain[tahap]["next"], kedalaman + 1)


# Fungsi rekursif: mengumpulkan tahapan rantai yang terdeteksi
def daftar_tahap_serangan(chain, tahap="initial_access", kedalaman=0):
    # Base case: tahap tidak ada di chain ATAU kedalaman >= 6
    if tahap not in chain or kedalaman >= 6:
        return []
    return [tahap] + daftar_tahap_serangan(chain, chain[tahap]["next"], kedalaman + 1)


print(f"\n--- RANTAI SERANGAN ---")
for tahap, info in attack_chain.items():
    print(f" {tahap:22} | Skor: {info['skor']:<3} | Next: {info['next']}")

total_dampak = hitung_dampak_serangan(attack_chain)
kedalaman_maks = hitung_kedalaman_rantai(attack_chain)
print(f"\nTotal dampak serangan  : {total_dampak}")
print(f"Kedalaman maksimum     : {kedalaman_maks} tahap")


# BAGIAN 8: ANALISIS BERJENJANG DENGAN REKURSI
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 8: ANALISIS BERJENJANG DENGAN REKURSI")
print(f"{'=' * 70}")


# Fungsi rekursif: menghitung ancaman berjenjang level 1 sampai 5
def hitung_ancaman_berjenjang(level, kedalaman=0):
    # Base case: kedalaman >= 5
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
    elif level == 5:
        return 2
    return 0


total_berjenjang = hitung_ancaman_berjenjang(1)
print(f"\nLevel 1 -> 2 -> 3 -> 4 -> 5 : 10 + 8 + 6 + 4 + 2")
print(f"Total ancaman berjenjang    : {total_berjenjang}")


# BAGIAN 9: SORTING DAN MAX/MIN DENGAN LAMBDA
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 9: SORTING DAN MAX/MIN DENGAN LAMBDA")
print(f"{'=' * 70}")

# sorted() ascending berdasarkan skor
log_asc = sorted(log_akses, key=lambda log: log["skor"])
print(f"\n--- SORT SKOR ASCENDING ---")
cetak_tabel(log_asc)

# sorted() descending dengan reverse=True
log_desc = sorted(log_akses, key=lambda log: log["skor"], reverse=True)
print(f"\n--- SORT SKOR DESCENDING ---")
cetak_tabel(log_desc)

# max() dengan key=lambda: log skor tertinggi
log_tertinggi = max(log_akses, key=lambda log: log["skor"])
print(f"\n--- LOG SKOR TERTINGGI ---")
cetak_tabel([log_tertinggi])

# min() dengan key=lambda: log skor terendah
log_terendah = min(log_akses, key=lambda log: log["skor"])
print(f"\n--- LOG SKOR TERENDAH ---")
cetak_tabel([log_terendah])


# BAGIAN 10: LAMBDA DENGAN KONDISI TERNARY
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 10: LAMBDA DENGAN KONDISI TERNARY")
print(f"{'=' * 70}")

# Lambda klasifikasi skor (rantai ternary)
klasifikasi_skor = lambda skor: "CRITICAL" if skor >= 8 else "HIGH" if skor >= 6 else "MEDIUM" if skor >= 4 else "LOW"

# Lambda klasifikasi IP (ternary)
klasifikasi_ip = lambda ip: "MALICIOUS" if ip in IP_BLACKLIST else "CLEAN"

# Lambda status protokol (ternary)
status_protokol = lambda protokol: "AMAN" if protokol in PROTOKOL_AMAN else "BERBAHAYA"

# Menerapkan ketiga lambda pada setiap log
print(f"\n{'IP':<16} | {'Skor':<4} | {'Kategori':<9} | {'Status IP':<10} | {'Protokol':<9} | {'Status Protokol':<10}")
print(f"{'-' * 72}")
for log in log_akses:
    print(f"{log['ip']:<16} | {log['skor']:<4} | {klasifikasi_skor(log['skor']):<9} | {klasifikasi_ip(log['ip']):<10} | {log['protokol']:<9} | {status_protokol(log['protokol']):<10}")


# BAGIAN 11: STATISTIK LOG DENGAN LIST COMPREHENSION
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 11: STATISTIK LOG DENGAN LIST COMPREHENSION")
print(f"{'=' * 70}")

# List skor per kategori
skor_kritis = [s for s in semua_skor if s >= 8]
skor_tinggi = [s for s in semua_skor if 6 <= s < 8]
skor_sedang = [s for s in semua_skor if 4 <= s < 6]
skor_rendah = [s for s in semua_skor if s < 4]

# List IP dari log kritis dan list port dari log blacklist
ip_kritis = [log["ip"] for log in log_kritis]
port_blacklist = [log["port"] for log in log_blacklist]

print(f"\nSkor kritis (>=8)      : {skor_kritis}")
print(f"Skor tinggi (6-7)      : {skor_tinggi}")
print(f"Skor sedang (4-5)      : {skor_sedang}")
print(f"Skor rendah (<4)       : {skor_rendah}")
print(f"\nIP dari log kritis     : {ip_kritis}")
print(f"Port dari log blacklist: {port_blacklist}")

# Persentase masing-masing kategori
total_log = len(semua_skor)
print(f"\n--- PERSENTASE KATEGORI ---")
print(f"Kritis                 : {len(skor_kritis) / total_log * 100:.2f}%")
print(f"Tinggi                 : {len(skor_tinggi) / total_log * 100:.2f}%")
print(f"Sedang                 : {len(skor_sedang) / total_log * 100:.2f}%")
print(f"Rendah                 : {len(skor_rendah) / total_log * 100:.2f}%")


# BAGIAN 12: LAPORAN FORENSIK TERINTEGRASI
print(f"\n")
print(f"{'=' * 70}")
print(f"BAGIAN 12: LAPORAN FORENSIK TERINTEGRASI")
print(f"{'=' * 70}")

# 1. Ringkasan eksekutif
persentase_kritis = (len(log_kritis) / len(log_akses)) * 100

print(f"\n--- 1. RINGKASAN EKSEKUTIF ---")
print(f"Total log dianalisis   : {len(log_akses)}")
print(f"Total skor keseluruhan : {total_skor}")
print(f"Rata-rata skor         : {rata_skor:.2f}")
print(f"Jumlah log kritis      : {len(log_kritis)}")
print(f"Persentase log kritis  : {persentase_kritis:.2f}%")

# 2. Analisis IP
ip_kritis_fm = list(map(lambda log: log["ip"], filter(lambda log: log["skor"] >= 7, log_akses)))
ip_di_blacklist = [ip for ip in semua_ip if ip in IP_BLACKLIST]
total_ip_unik = len(set(semua_ip))

print(f"\n--- 2. ANALISIS IP ---")
print(f"IP dari log kritis     : {ip_kritis_fm}")
print(f"IP di blacklist        : {ip_di_blacklist}")
print(f"Total IP unik          : {total_ip_unik}")

# 3. Analisis port
port_bahaya_muncul = sorted(set(filter(lambda p: p in PORT_BERBAHAYA, semua_port)))
frekuensi_port = {p: semua_port.count(p) for p in sorted(set(semua_port))}

print(f"\n--- 3. ANALISIS PORT ---")
print(f"Port berbahaya muncul  : {port_bahaya_muncul}")
print(f"Frekuensi tiap port:")
for port, jumlah in frekuensi_port.items():
    keterangan = "BERBAHAYA" if port in PORT_BERBAHAYA else "normal"
    print(f" Port {port:<6} : {jumlah}x ({keterangan})")

# 4. Analisis rantai serangan
tahap_terdeteksi = daftar_tahap_serangan(attack_chain)

print(f"\n--- 4. ANALISIS RANTAI SERANGAN ---")
print(f"Total dampak serangan  : {hitung_dampak_serangan(attack_chain)}")
print(f"Tahapan terdeteksi     : {' -> '.join(tahap_terdeteksi)}")

# 5. Rekomendasi bersyarat
print(f"\n--- 5. REKOMENDASI ---")
if persentase_kritis >= 50:
    print(f"PERINGATAN TINGGI: Lebih dari 50% log kritis!")
    print(f"Segera lakukan investigasi menyeluruh.")
elif persentase_kritis >= 25:
    print(f"PERINGATAN SEDANG: Terdapat beberapa log kritis.")
    print(f"Lakukan monitoring ketat.")
else:
    print(f"SISTEM AMAN: Sebagian besar log dalam kondisi normal.")


# PENUTUP
print(f"\n")
print(f"{'=' * 70}")
print(f"PRAKTIKUM SISTEM ANALISIS FORENSIK LOG DIGITALTRACE SELESAI")
print(f"{'=' * 70}")
print(f"\nMateri yang telah dipraktikkan:")
print(f" 1. Manajemen database IP blacklist (list & tuple)")
print(f" 2. Operasi list pada log: slicing, append, insert, remove, pop, copy")
print(f" 3. Analisis log dengan filter() dan lambda")
print(f" 4. Transformasi log dengan map() dan lambda")
print(f" 5. Agregasi log dengan reduce()")
print(f" 6. Pipeline filter -> map -> reduce")
print(f" 7. Analisis rantai serangan dengan rekursi")
print(f" 8. Analisis berjenjang dengan rekursi")
print(f" 9. Sorting dan max/min dengan lambda")
print(f" 10. Lambda dengan kondisi ternary")
print(f" 11. Statistik log dengan list comprehension")
print(f" 12. Laporan forensik terintegrasi")
print(f"{'=' * 70}")

