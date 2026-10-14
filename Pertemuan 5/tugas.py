GARIS = "=" * 70
HARI_BERJALAN = 276  # 3 Oktober 2026 = hari ke-276 (ubah sesuai tanggal saat dijalankan)
DIGIT = "0123456789"
ALFANUM = DIGIT + "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
algoritma_diizinkan = ["AES", "RSA", "ECC", "ChaCha20"]


# BAGIAN 1: FUNGSI TANPA PARAMETER
def tampilkan_header():
    print(f"\n{GARIS}\nSISTEM MANAJEMEN KUNCI ENKRIPSI CRYPTOVAULT\nD4 Rekayasa Keamanan Siber\n{GARIS}")


tampilkan_header()


# BAGIAN 2: POSITIONAL ARGUMENT
def cek(teks, himpunan, panjang=None):
    return teks != "" and all(c in himpunan for c in teks) and (panjang is None or len(teks) == panjang)


def urai_key_id(key_id):
    if key_id[:3] != "KEY":
        return None
    sisa = key_id[3:]
    bagian = (sisa[1:] if sisa[:1] == "-" else sisa).split("-")
    if len(bagian) == 3 and cek(bagian[0], DIGIT, 4) and cek(bagian[1], ALFANUM) and cek(bagian[2], DIGIT, 3):
        return bagian
    return None


def validasi_key_id(key_id):
    return urai_key_id(key_id) is not None


def klasifikasi_key(key_id, daftar_algoritma):
    bagian = urai_key_id(key_id)
    if bagian and bagian[1] in daftar_algoritma:
        return "ALGORITMA VALID"
    return "ALGORITMA TIDAK DIIZINKAN"


print("\n--- PENGUJIAN FUNGSI POSITIONAL ---")
for key_uji in ["KEY-2024-AES-001", "KEY2024-AES-001", "KEY-2024-DES-002", "KUNCI-24-AES-1"]:
    print(f"Key {key_uji:<18} valid? {validasi_key_id(key_uji)} | {klasifikasi_key(key_uji, algoritma_diizinkan)}")


# BAGIAN 3: KEYWORD ARGUMENT
def validasi_akses_kms(engineer_id, passphrase, kms_endpoint):
    database = {
        "ENG-001": {"passphrase": "Crypto@2024", "endpoint": "kms.cryptovault.id:8443"},
        "ENG-002": {"passphrase": "Secure#Vault", "endpoint": "kms2.cryptovault.id:8443"},
    }
    if engineer_id not in database:
        return "GAGAL Engineer ID tidak terdaftar"
    if passphrase != database[engineer_id]["passphrase"]:
        return "GAGAL Passphrase salah"
    if kms_endpoint != database[engineer_id]["endpoint"]:
        return "GAGAL KMS endpoint tidak sesuai"
    return f"BERHASIL Akses KMS diberikan untuk {engineer_id}!"


print("\n--- PENGUJIAN FUNGSI KEYWORD ---")
print("Akses 1:", validasi_akses_kms(engineer_id="ENG-001", passphrase="Crypto@2024", kms_endpoint="kms.cryptovault.id:8443"))
print("Akses 2:", validasi_akses_kms(kms_endpoint="kms2.cryptovault.id:8443", engineer_id="ENG-002", passphrase="Secure#Vault"))
print("Akses 3:", validasi_akses_kms(passphrase="salah", kms_endpoint="kms.cryptovault.id:8443", engineer_id="ENG-001"))
print("Akses 4:", validasi_akses_kms(engineer_id="ENG-002", kms_endpoint="kms.cryptovault.id:8443", passphrase="Secure#Vault"))
print("Akses 5:", validasi_akses_kms(passphrase="Crypto@2024", engineer_id="ENG-999", kms_endpoint="kms.cryptovault.id:8443"))


# BAGIAN 4: DEFAULT ARGUMENT
def scan_port_kms(host, port=8443, protokol="HTTPS", timeout=30):
    if port == 8443:
        status = "KMS STANDAR"
    elif port == 9443:
        status = "KMS ALTERNATIF"
    elif port < 1024:
        status = "PORT SISTEM"
    else:
        status = "PORT TIDAK DIKENAL"
    return f"{host}:{port}/{protokol} (timeout {timeout} detik) -> {status}"


print("\n--- PENGUJIAN FUNGSI DEFAULT ---")
print(scan_port_kms("kms.cryptovault.id"))
print(scan_port_kms("kms.cryptovault.id", 9443))
print(scan_port_kms("kms.cryptovault.id", 22, "SSH", 10))
print(scan_port_kms("kms.cryptovault.id", 5000))


# BAGIAN 5: *ARGS
def pindai_banyak_port(host, *ports):
    port_berbahaya = [22, 23, 3389, 5900, 6379]
    jumlah = 0
    print(f"\nMemindai host: {host} ({len(ports)} port)")
    for port in ports:
        berbahaya = port in port_berbahaya
        jumlah += berbahaya
        print(f" - Port {port}: {'BERBAHAYA' if berbahaya else 'AMAN'}")
    return jumlah


print("\n--- PENGUJIAN FUNGSI ARGS ---")
print("Total port berbahaya:", pindai_banyak_port("kms.cryptovault.id", 8443, 22, 443))
print("Total port berbahaya:", pindai_banyak_port("kms.cryptovault.id", 8443, 9443, 23, 80, 3389))
print("Total port berbahaya:", pindai_banyak_port("kms.cryptovault.id", 22, 23, 443, 5900, 6379, 8443, 9443))


# BAGIAN 6: **KWARGS
def profil_engineer(**data):
    print("\n--- PROFIL ENGINEER ---")
    for key, value in data.items():
        print(f"{key.replace('_', ' ').title():<20} : {value}")
    return data.get("nama", "Unknown")


print("\n--- PENGUJIAN FUNGSI **KWARGS ---")
nama1 = profil_engineer(nama="Rina Wijaya", jabatan="Lead Cryptographic Engineer", shift="Pagi", tahun_bergabung=2019)
nama2 = profil_engineer(nama="Dimas Pratama", jabatan="Key Custodian")
nama3 = profil_engineer(jabatan="Auditor", lokasi_kantor="Jakarta")
print(f"\nEngineer yang bertugas: {nama1}, {nama2}, dan {nama3}")


# BAGIAN 7: MULTIPLE RETURN VALUES
def analisis_passphrase(passphrase, engineer_id=""):
    spesial = "!@#$%^&*()_+-=[]{}|;:,.<>?/~"
    detail = [
        len(passphrase) >= 16,
        sum(c.isupper() for c in passphrase) >= 2,
        any(c.islower() for c in passphrase),
        sum(c.isdigit() for c in passphrase) >= 4,
        any(c in spesial for c in passphrase),
        engineer_id.lower() not in passphrase.lower() if engineer_id else True,
    ]
    skor = sum(detail)
    if skor == 6:
        level = "SANGAT KUAT"
    elif skor == 5:
        level = "KUAT"
    elif skor >= 3:
        level = "CUKUP"
    elif skor >= 1:
        level = "LEMAH"
    else:
        level = "SANGAT LEMAH"
    return skor, level, detail


print("\n--- PENGUJIAN MULTIPLE RETURN ---")
pass_test = "Vault@2024#Key!99"
skor, level, detail = analisis_passphrase(pass_test, "ENG-001")
print(f"Passphrase : {'*' * len(pass_test)} | Skor: {skor}/6 | Level: {level}")
kriteria = ["Minimal 16 karakter", "Minimal 2 huruf besar", "Mengandung huruf kecil",
            "Minimal 4 angka", "Mengandung simbol khusus", "Tidak mengandung eng. ID"]
for nama_k, lolos in zip(kriteria, detail):
    print(f" - {nama_k:<26}: {'YA' if lolos else 'TIDAK'}")


# BAGIAN 8: LOCAL VS GLOBAL
total_audit_global = 0
log_audit_kripto = []


def catat_audit_kripto(engineer_id, skor, level):
    global total_audit_global  # perlu global karena int diubah nilainya
    status_aman = skor >= 5  # variabel lokal
    total_audit_global += 1
    log_audit_kripto.append({"no": total_audit_global, "engineer_id": engineer_id,
                             "skor": skor, "level": level, "aman": status_aman})
    return status_aman


def tampilkan_log_audit_kripto():
    print("\n--- LOG AUDIT KRIPTOGRAFI ---")
    print(f"{'No':<4} | {'Engineer':<10} | {'Skor':<6} | {'Level':<15} | Status")
    print("-" * 60)
    for e in log_audit_kripto:
        print(f"{e['no']:<4} | {e['engineer_id']:<10} | {e['skor']}/6    | {e['level']:<15} | "
              f"{'AMAN' if e['aman'] else 'PERLU PERBAIKAN'}")


print("\n--- PENGUJIAN SCOPE VARIABEL ---")
print(f"Total audit sebelum: {total_audit_global}")
for eng, pas in [("ENG-001", "Crypto@2024"), ("ENG-002", "Secure#Vault2024!Key"),
                 ("ENG-003", "Tr0ub4dor&3-Horse!Battery#2024"), ("ENG-004", "password")]:
    skor_u, level_u, _ = analisis_passphrase(pas, eng)
    print(f"Audit {eng}: skor {skor_u}/6, level {level_u}, aman={catat_audit_kripto(eng, skor_u, level_u)}")
print(f"Total audit setelah: {total_audit_global}")
tampilkan_log_audit_kripto()


# BAGIAN 9: FUNGSI ORKESTRATOR (dipanggil di akhir program)
def deteksi_anomali_kripto():
    print(f"\n\n{GARIS}\nDETEKSI ANOMALI KRIPTOGRAFI TERINTEGRASI\n{GARIS}")
    engineer_id = input("Masukkan Engineer ID (contoh ENG-001): ")
    key_id = input("Masukkan Key ID (contoh KEY-2024-AES-001): ")
    passphrase = input("Masukkan Passphrase: ")

    format_valid = validasi_key_id(key_id)
    status_algoritma = klasifikasi_key(key_id, algoritma_diizinkan)
    skor, level, _ = analisis_passphrase(passphrase, engineer_id)

    key_tidak_valid = (not format_valid) or (status_algoritma != "ALGORITMA VALID")
    passphrase_lemah = skor < 3

    if key_tidak_valid and passphrase_lemah:
        tingkat, rekomendasi = "ANOMALI TINGGI", "Blokir akses, cabut key, dan lakukan investigasi menyeluruh"
    elif key_tidak_valid:
        tingkat, rekomendasi = "ANOMALI SEDANG", "Periksa format dan algoritma key, lalu verifikasi ke engineer"
    elif passphrase_lemah:
        tingkat, rekomendasi = "ANOMALI SEDANG", "Wajibkan engineer mengganti passphrase dengan yang lebih kuat"
    else:
        tingkat, rekomendasi = "AKSES NORMAL", "Tidak ada tindakan yang diperlukan"

    print(f"\n{GARIS}\nLAPORAN DETEKSI ANOMALI KRIPTOGRAFI\n{GARIS}")
    print(f"Engineer ID      : {engineer_id}")
    print(f"Key ID           : {key_id}")
    print(f"Format Key       : {'VALID' if format_valid else 'TIDAK VALID'}")
    print(f"Status Algoritma : {status_algoritma}")
    print(f"Passphrase       : {'*' * len(passphrase)} (skor {skor}/6, {level})")
    print(f"Tingkat Anomali  : {tingkat}")
    print(f"Rekomendasi      : {rekomendasi}\n{GARIS}")
    catat_audit_kripto(engineer_id, skor, level)


# BAGIAN 10: BATCH PROCESSING
def audit_batch_engineer(daftar_engineer):
    statistik = {"total": 0, "SANGAT KUAT": 0, "KUAT": 0, "CUKUP": 0, "LEMAH": 0, "SANGAT LEMAH": 0}
    print("\n--- HASIL AUDIT BATCH ---")
    for eng in daftar_engineer:
        skor, level, _ = analisis_passphrase(eng["passphrase"], eng["engineer_id"])
        statistik["total"] += 1
        statistik[level] += 1
        print(f"{eng['engineer_id']:<10} | {'*' * len(eng['passphrase']):<32} | {skor}/6 | {level}")
    return statistik


daftar_engineer = [
    {"engineer_id": "ENG-001", "passphrase": "Crypto@2024"},
    {"engineer_id": "ENG-002", "passphrase": "Secure#Vault"},
    {"engineer_id": "ENG-003", "passphrase": "Tr0ub4dor&3-Horse!Battery#2024"},
    {"engineer_id": "ENG-004", "passphrase": "password"},
    {"engineer_id": "ENG-005", "passphrase": "Vault@2024Key!"},
    {"engineer_id": "ENG-006", "passphrase": "12345"},
]
print("\n--- STATISTIK AUDIT ---")
for k, v in audit_batch_engineer(daftar_engineer).items():
    print(f"{k.title():<14}: {v}")


# BAGIAN 11: KOMBINASI SEMUA PARAMETER
def laporan_engineer(nama, role, *sertifikasi, level=1, **info_tambahan):
    print(f"\n--- LAPORAN ENGINEER: {nama} ---")
    print(f"Role        : {role}\nLevel       : {level}")
    print(f"Sertifikasi : {', '.join(sertifikasi) if sertifikasi else '-'}")
    for key, value in info_tambahan.items():
        print(f" - {key.replace('_', ' ').title()} : {value}")
    return {"nama": nama, "role": role, "sertifikasi": list(sertifikasi), "level": level, "info": info_tambahan}


print("\n--- PENGUJIAN KOMBINASI PARAMETER LENGKAP ---")
laporan1 = laporan_engineer("Rina Wijaya", "Lead Cryptographic Engineer", "CISSP", "CISM", "CKMS",
                            level=5, pengalaman_tahun=8, tahun_bergabung=2018)
laporan2 = laporan_engineer("Dimas Pratama", "Key Custodian", level=2)


# BAGIAN 12: SIMULASI ROTASI KUNCI
def rotasi_kunci(key_lama, key_baru, interval_hari=90):
    def gagal(status, rekomendasi):
        return {"status": status, "sisa_hari": None, "rekomendasi": rekomendasi}

    if not validasi_key_id(key_lama):
        return gagal("GAGAL Format key lama tidak valid", "Perbaiki format key lama sebelum rotasi")
    if not validasi_key_id(key_baru):
        return gagal("GAGAL Format key baru tidak valid", "Perbaiki format key baru sebelum rotasi")
    if key_lama == key_baru:
        return gagal("GAGAL Key lama dan key baru sama", "Buat key baru dengan identifier yang berbeda")

    sisa_hari = interval_hari - (HARI_BERJALAN % interval_hari)
    rekomendasi = "Segera jadwalkan rotasi berikutnya" if sisa_hari <= 7 else "Rotasi berikutnya sesuai jadwal"
    return {"status": "BERHASIL Rotasi kunci disimulasikan", "sisa_hari": sisa_hari, "rekomendasi": rekomendasi}


print("\n--- SIMULASI ROTASI KUNCI ---")
for lama, baru, interval in [("KEY-2024-AES-001", "KEY-2025-AES-002", 90), ("KEY-2024-AES-001", "KEY-2024-AES-001", 90),
                             ("KEY-2024-AES-001", "KUNCI-BARU", 90), ("KEY-2023-RSA-014", "KEY-2025-RSA-015", 30)]:
    hasil = rotasi_kunci(lama, baru, interval)
    print(f"\n{lama} -> {baru} (interval {interval} hari)")
    print(f" Status: {hasil['status']} | Sisa hari: {hasil['sisa_hari']} | {hasil['rekomendasi']}")
print("\nInterval default 90 hari -> sisa hari:", rotasi_kunci("KEY-2024-ECC-003", "KEY-2025-ECC-004")["sisa_hari"])


# BAGIAN 13: FILTER LOG (continue & break)
def filter_log_kripto(daftar_log, kata_kunci):
    hasil = []
    for log in daftar_log:
        if kata_kunci.lower() not in log["pesan"].lower():
            continue  # lewati log yang tidak cocok
        hasil.append(log)
        if log["status"] == "CRITICAL":
            print(f" [!] Log CRITICAL ditemukan pada {log['waktu']}, pencarian dihentikan")
            break  # berhenti saat menemukan CRITICAL
    return hasil


log_kripto = [
    {"waktu": "08:00", "status": "INFO", "pesan": "Rotasi kunci KEY-2024-AES-001 berhasil"},
    {"waktu": "08:15", "status": "INFO", "pesan": "Engineer ENG-001 login ke KMS"},
    {"waktu": "09:30", "status": "WARNING", "pesan": "Percobaan akses kunci dengan passphrase salah"},
    {"waktu": "10:05", "status": "ERROR", "pesan": "Gagal rotasi kunci KEY-2023-RSA-014 karena timeout"},
    {"waktu": "11:20", "status": "INFO", "pesan": "Backup kunci master selesai"},
    {"waktu": "12:45", "status": "CRITICAL", "pesan": "Kunci privat diakses dari IP tidak dikenal"},
    {"waktu": "13:10", "status": "WARNING", "pesan": "Rotasi kunci tertunda melewati batas 90 hari"},
    {"waktu": "14:00", "status": "ERROR", "pesan": "Port 6379 terbuka pada server KMS"},
    {"waktu": "15:30", "status": "INFO", "pesan": "Audit kunci bulanan dijadwalkan"},
]
print("\n--- FILTER LOG KRIPTOGRAFI ---")
for kata in ["kunci", "rotasi", "port"]:
    hasil_filter = filter_log_kripto(log_kripto, kata)
    print(f"\nKata kunci '{kata}': ditemukan {len(hasil_filter)} log")
    for log in hasil_filter:
        print(f" [{log['waktu']}] {log['status']:<9} {log['pesan']}")


# BAGIAN 14: MATRIKS SKOR RISIKO (nested loop)
def matriks_risiko_kunci():
    tipe_kunci = ["AES", "RSA", "ECC", "ChaCha20"]
    level_akses = ["Read", "Write", "Admin", "Root"]
    matriks = [[1, 3, 6, 8], [2, 4, 7, 9], [1, 2, 5, 7], [0, 3, 4, 6]]

    print(f"{'Tipe Kunci':<12}" + "".join(f"{a:>8}" for a in level_akses) + "\n" + "-" * 44)
    tertinggi, baris, kolom = matriks[0][0], 0, 0
    for i in range(len(matriks)):
        print(f"{tipe_kunci[i]:<12}", end="")
        for j in range(len(matriks[i])):
            print(f"{matriks[i][j]:>8}", end="")
            if matriks[i][j] > tertinggi:
                tertinggi, baris, kolom = matriks[i][j], i, j
        print()
    print(f"\nRisiko tertinggi: {tipe_kunci[baris]} dengan akses {level_akses[kolom]}")
    return tertinggi, baris, kolom


print("\n--- MATRIKS SKOR RISIKO KUNCI ---")
tertinggi, baris, kolom = matriks_risiko_kunci()
print(f"Nilai tertinggi: {tertinggi} | Posisi (indeks): baris {baris}, kolom {kolom}")


# BAGIAN 15: ANALISIS MULTI-KEY
def analisis_multi_key(daftar_key):
    statistik = {"total": 0, "aktif": 0, "tidak_aktif": 0, "per_algoritma": {}}
    print("\n--- HASIL ANALISIS MULTI-KEY ---")
    print(f"{'Key ID':<22} | {'Algoritma':<10} | {'Bit':<5} | Status\n" + "-" * 55)
    for key in daftar_key:
        statistik["total"] += 1
        statistik["per_algoritma"].setdefault(key["algoritma"], []).append(key["key_id"])
        statistik["aktif" if key["status"] == "AKTIF" else "tidak_aktif"] += 1
        print(f"{key['key_id']:<22} | {key['algoritma']:<10} | {key['panjang_bit']:<5} | {key['status']}")
    return statistik


daftar_key = [
    {"key_id": "KEY-2024-AES-001", "algoritma": "AES", "panjang_bit": 256, "status": "AKTIF"},
    {"key_id": "KEY-2024-AES-002", "algoritma": "AES", "panjang_bit": 128, "status": "TIDAK AKTIF"},
    {"key_id": "KEY-2023-RSA-014", "algoritma": "RSA", "panjang_bit": 4096, "status": "AKTIF"},
    {"key_id": "KEY-2022-RSA-007", "algoritma": "RSA", "panjang_bit": 1024, "status": "TIDAK AKTIF"},
    {"key_id": "KEY-2024-ECC-003", "algoritma": "ECC", "panjang_bit": 384, "status": "AKTIF"},
    {"key_id": "KEY-2025-ECC-004", "algoritma": "ECC", "panjang_bit": 256, "status": "AKTIF"},
    {"key_id": "KEY-2024-ChaCha20-001", "algoritma": "ChaCha20", "panjang_bit": 256, "status": "AKTIF"},
    {"key_id": "KEY-2021-3DES-009", "algoritma": "3DES", "panjang_bit": 168, "status": "TIDAK AKTIF"},
    {"key_id": "KEY-2025-AES-010", "algoritma": "AES", "panjang_bit": 256, "status": "AKTIF"},
]
stat_key = analisis_multi_key(daftar_key)
print(f"\nTotal: {stat_key['total']} | Aktif: {stat_key['aktif']} | Tidak aktif: {stat_key['tidak_aktif']}")
for algo, daftar_id in stat_key["per_algoritma"].items():
    print(f" - {algo:<9} ({len(daftar_id)} key): {', '.join(daftar_id)}")


# BAGIAN 16: ANALISIS PASSPHRASE BANYAK ENGINEER
def analisis_passphrase_batch(daftar_passphrase):
    statistik = {"SANGAT KUAT": 0, "KUAT": 0, "CUKUP": 0, "LEMAH": 0, "SANGAT LEMAH": 0}
    print("\n--- TABEL ANALISIS PASSPHRASE ---")
    print(f"{'Engineer':<10} | {'Nama':<14} | {'Panjang':<8} | {'Skor':<5} | {'Level':<12} | Lolos\n" + "-" * 75)
    for d in daftar_passphrase:
        skor, level, detail = analisis_passphrase(d["passphrase"], d["engineer_id"])
        statistik[level] += 1
        print(f"{d['engineer_id']:<10} | {d['nama']:<14} | {len(d['passphrase']):<8} | {skor}/6   | "
              f"{level:<12} | {sum(detail)} dari {len(detail)}")
    return statistik


daftar_passphrase = [
    {"engineer_id": "ENG-101", "nama": "Rina Wijaya", "passphrase": "Blue#Horse!Staple2024Z"},
    {"engineer_id": "ENG-102", "nama": "Dimas Pratama", "passphrase": "dimas12345"},
    {"engineer_id": "ENG-103", "nama": "Sari Lestari", "passphrase": "Sari@Vault#2025"},
    {"engineer_id": "ENG-104", "nama": "Budi Santoso", "passphrase": "Qwerty!Zx9087Mn#Lk"},
    {"engineer_id": "ENG-105", "nama": "Andi Nugroho", "passphrase": "abc"},
    {"engineer_id": "ENG-106", "nama": "Maya Putri", "passphrase": "KunciRahasia2024"},
]
stat_pass = analisis_passphrase_batch(daftar_passphrase)
print("\n--- STATISTIK DISTRIBUSI LEVEL PASSPHRASE ---")
for level_stat, jumlah in stat_pass.items():
    print(f"{level_stat:<14}: {jumlah}")
print(f"{'Total':<14}: {sum(stat_pass.values())}")


# PEMANGGILAN ORKESTRATOR (DI AKHIR PROGRAM)
deteksi_anomali_kripto()
tampilkan_log_audit_kripto()

print(f"\n\n{GARIS}\nPRAKTIKUM FUNGSI SELESAI\n{GARIS}")
print("Materi: 1 Tanpa parameter | 2 Positional | 3 Keyword | 4 Default | 5 *args | 6 **kwargs | "
      "7 Multiple return | 8 Local vs global | 9 Orkestrator | 10 Batch | 11 Kombinasi parameter | "
      "12 Rotasi kunci | 13 Filter log (continue & break) | 14 Matriks (nested loop) | "
      "15 Multi-key | 16 Passphrase batch")
print(GARIS)