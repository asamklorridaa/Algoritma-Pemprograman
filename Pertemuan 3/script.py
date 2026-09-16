# ==========================================
# 3.1. Utility Functions
# ==========================================

def tanya_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print(" [!] input harus berupa angka")

def tanya_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print(" [!] input harus berupa angka")

def tanya_ya(prompt):
    return input(prompt + " (y/n): ").strip().lower() == "y"

def garis(panjang=70, karakter="="):
    print(karakter * panjang)

def judul(teks):
    garis()
    print(f"  {teks}")
    garis()

def sub(teks):
    print(f"\n[ {teks} ]")
    garis(70, "-")

# ==========================================
# 3.2. Login Dasar
# ==========================================

def login_dasar():
    judul("BAGIAN 1 - LOGIN DASAR")
    USER_VALID = "admin"
    PWD_VALID = "Admin123!"
    
    sub("Input Kredensial")
    username = input(" Username: ").strip()
    password = input(" Password : ")
    
    if username == USER_VALID:
        if password == PWD_VALID:
            print(" LOGIN BERHASIL")
            print(f" Selamat datang, {username}!")
        else:
            print(" LOGIN GAGAL - password salah")
    else:
        print(" LOGIN GAGAL - username tidak terdaftar")
        
    sub("Analisis Panjang Password (IF-ELIF)")
    panjang = len(password)
    
    if panjang >= 12:
        kategori = "PANJANG"
    elif panjang >= 8:
        kategori = "CUKUP"
    elif panjang >= 4:
        kategori = "PENDEK"
    else:
        kategori = "SANGAT PENDEK"
        
    print(f" Panjang : {panjang} karakter")
    print(f" Kategori: {kategori}")

# ==========================================
# 3.3. Login Berlapis
# ==========================================

def login_berlapis():
    judul("BAGIAN 2 - LOGIN BERLAPIS")
    USERS = {
        "admin": {"pwd": "Admin!2024", "role": "admin", "mfa": True, "lock": False},
        "budi": {"pwd": "Budi1234", "role": "user", "mfa": False, "lock": False},
        "tamu": {"pwd": "guest", "role": "guest", "mfa": False, "lock": True},
    }
    
    sub("Input Kredensial")
    username = input(" Username: ").strip()
    password = input(" Password : ")
    
    sub("Proses Autentikasi")
    if username in USERS:
        user = USERS[username]
        if not user["lock"]:
            if user["pwd"] == password:
                if user["mfa"]:
                    mfa = input(" Kode MFA: ").strip()
                    if mfa == "123456":
                        print("\n LOGIN BERHASIL - akses penuh")
                        print(f" Role: {user['role']}")
                    else:
                        print("\n LOGIN GAGAL - kode MFA salah")
                else:
                    print("\n LOGIN BERHASIL - akses standar")
                    print(f" Role: {user['role']}")
            else:
                print("\n LOGIN GAGAL - password salah")
        else:
            print("\n LOGIN GAGAL - akun terkunci")
    else:
        print("\n LOGIN GAGAL - username tidak terdaftar")
        
    sub("Analisis Keamanan (Ternary)")
    akun_aman = username.isalnum() if username else False
    status_akun = "AMAN" if akun_aman else "MENCURIGAKAN"
    kekuatan = ("KUAT" if len(password) >= 12 else
                "SEDANG" if len(password) >= 8 else
                "LEMAH")
                
    print(f" Username: {username} -> {status_akun}")
    print(f" Password: {kekuatan}")

# ==========================================
# 3.4. Otorisasi Akses Berbasis Role
# ==========================================

def otorisasi_akses():
    judul("BAGIAN 3 - OTORISASI AKSES BERBASIS ROLE")
    
    sub("Input Permintaan Akses")
    role = input(" Role (admin/user/guest): ").strip().lower()
    resource = input(" Resource (file/database/settings): ").strip().lower()
    aksi = input(" Aksi (read/write/delete): ").strip().lower()
    
    sub("Evaluasi Hak Akses")
    if role == "admin":
        if resource in ["file", "database", "settings"]:
            if aksi in ["read", "write", "delete"]:
                keputusan = "DIBERIKAN"
                level = "FULL CONTROL"
            else:
                keputusan = "DITOLAK"
                level = "AKSI TIDAK DIKENAL"
        else:
            keputusan = "DITOLAK"
            level = "RESOURCE TIDAK DIKENAL"
    elif role == "user":
        if resource in ["file", "database"]:
            if aksi in ["read", "write"]:
                keputusan = "DIBERIKAN"
                level = "AKSES TERBATAS"
            else:
                keputusan = "DITOLAK"
                level = "USER TIDAK BOLEH DELETE"
        else:
            keputusan = "DITOLAK"
            level = "DI LUAR WEWENANG"
    elif role == "guest":
        if resource == "file" and aksi == "read":
            keputusan = "DIBERIKAN"
            level = "READ ONLY"
        else:
            keputusan = "DITOLAK"
            level = "AKSES SANGAT TERBATAS"
    else:
        keputusan = "DITOLAK"
        level = "ROLE TIDAK DIKENAL"
        
    print(f" Role     : {role}")
    print(f" Resource : {resource}")
    print(f" Aksi     : {aksi}")
    print(f" Keputusan: {keputusan}")
    print(f" Level    : {level}")
    
    sub("Severity (Nested Ternary)")
    severity = ("INFO" if keputusan == "DIBERIKAN" and level == "FULL CONTROL"
                else "LOW" if keputusan == "DIBERIKAN"
                else "MEDIUM" if keputusan == "DITOLAK" and role in ["user", "guest"]
                else "HIGH")
    print(f" Severity: {severity}")

# ==========================================
# 3.5. Analisis Kekuatan Password
# ==========================================

def analisis_password():
    judul("BAGIAN 4 - ANALISIS KEKUATAN PASSWORD")
    
    sub("Input Password")
    pwd = input(" Password : ")
    if len(pwd) == 0:
        print("\n [!] Password tidak boleh kosong")
        return
        
    sub("Analisis Panjang (IF-ELIF)")
    panjang = len(pwd)
    if panjang >= 16:
        level_p = "SANGAT PANJANG"
        skor_p = 3
    elif panjang >= 12:
        level_p = "PANJANG"
        skor_p = 2
    elif panjang >= 8:
        level_p = "CUKUP"
        skor_p = 1
    else:
        level_p = "PENDEK"
        skor_p = 0
    print(f" Panjang: {panjang} ({level_p}) - skor {skor_p}/3")
    
    sub("Analisis Karakter (Ternary + any())")
    ada_lower = any('a' <= c <= 'z' for c in pwd)
    ada_upper = any('A' <= c <= 'Z' for c in pwd)
    ada_digit = any('0' <= c <= '9' for c in pwd)
    ada_special = False
    for c in pwd:
        if not ('a' <= c <= 'z') and not ('A' <= c <= 'Z') and not ('0' <= c <= '9'):
            ada_special = True
            break
            
    print(f" Huruf kecil    : {'YA' if ada_lower else 'TIDAK'}")
    print(f" Huruf besar    : {'YA' if ada_upper else 'TIDAK'}")
    print(f" Angka          : {'YA' if ada_digit else 'TIDAK'}")
    print(f" Karakter khusus: {'YA' if ada_special else 'TIDAK'}")
    
    sub("Skor Total & Level")
    skor = skor_p + (1 if ada_lower else 0) + (1 if ada_upper else 0) \
           + (1 if ada_digit else 0) + (2 if ada_special else 0)
    print(f" Skor total: {skor}/8")
    
    if skor >= 8:
        level = "SANGAT KUAT"
    elif skor >= 6:
        level = "KUAT"
    elif skor >= 4:
        level = "SEDANG"
    elif skor >= 2:
        level = "LEMAH"
    else:
        level = "SANGAT LEMAH"
    print(f" Level: {level}")
    
    sub("Cek Password Umum")
    umum = ["password", "123456", "qwerty", "admin", "letmein",
            "welcome", "monkey", "dragon", "abc123", "password123"]
    if pwd.lower() in umum:
        print(" STATUS: DITEMUKAN di daftar umum - GANTI SEGERA!")
    else:
        print(" STATUS: Tidak ada di daftar umum")
        
    sub("Rekomendasi")
    if not ada_lower:
        print(" - Tambahkan huruf kecil")
    if not ada_upper:
        print(" - Tambahkan huruf besar")
    if not ada_digit:
        print(" - Tambahkan angka")
    if not ada_special:
        print(" - Tambahkan karakter spesial")
    if panjang < 12:
        print(" - Tambah panjang minimal 12 karakter")
    if level in ["SANGAT KUAT", "KUAT"]:
        print(" - Password sudah baik, pertahankan")

# ==========================================
# 3.6. Validasi Form Registrasi
# ==========================================

def validasi_registrasi():
    judul("BAGIAN 5 - VALIDASI FORM REGISTRASI")
    
    sub("Input Data Registrasi")
    username = input(" Username       : ").strip()
    password = input(" Password       : ")
    konfirmasi = input(" Konfirmasi pwd : ")
    usia = tanya_int(" Usia           : ")
    
    sub("Validasi Data")
    valid = True
    
    if len(username) < 3:
        print(" [X] Username minimal 3 karakter")
        valid = False
    elif len(username) > 20:
        print(" [X] Username maksimal 20 karakter")
        valid = False
    else:
        if not username.isalnum():
            print(" [X] Username hanya boleh huruf dan angka")
            valid = False
        else:
            print(" [OK] Username valid")
            
    if len(password) < 8:
        print(" [X] Password minimal 8 karakter")
        valid = False
    else:
        if password != konfirmasi:
            print(" [X] Konfirmasi password tidak cocok")
            valid = False
        else:
            print(" [OK] Password dan konfirmasi cocok")
            
    if usia < 13:
        print(" [X] Usia minimal 13 tahun")
        valid = False
    elif usia < 18:
        print(" [!] Usia di bawah 18 - akun terbatas")
    else:
        print(" [OK] Usia memenuhi syarat")
        
    sub("Hasil Akhir")
    if valid:
        print(" STATUS: REGISTRASI BERHASIL")
    else:
        print(" STATUS: REGISTRASI GAGAL - perbaiki data di atas")
        
    sub("Kategori Akun (Ternary)")
    kategori = ("DEWASA" if usia >= 18 else
                "REMAJA" if usia >= 13 else
                "ANAK")
    print(f" Kategori: {kategori}")

# ==========================================
# 3.7. Simulasi Login dengan Batas Percobaan
# ==========================================

def simulasi_login():
    judul("BAGIAN 6 - SIMULASI LOGIN DENGAN BATAS PERCOBAAN")
    USER_VALID = "admin"
    PWD_VALID = "Admin!2024"
    MAX_PERCOBAAN = 3
    percobaan = 0
    berhasil = False
    
    sub("Silakan Login")
    print(f" Maksimal {MAX_PERCOBAAN} percobaan\n")
    
    while percobaan < MAX_PERCOBAAN:
        percobaan += 1
        print(f" --- Percobaan ke-{percobaan} ---")
        username = input(" Username: ").strip()
        password = input(" Password : ")
        
        if username == USER_VALID:
            if password == PWD_VALID:
                print(" -> LOGIN BERHASIL\n")
                berhasil = True
                break
            else:
                print(" -> Password salah\n")
        else:
            print(" -> Username tidak dikenal\n")
            
    sub("Hasil Akhir")
    if berhasil:
        print(f" Login berhasil pada percobaan ke-{percobaan}")
        sisa = MAX_PERCOBAAN - percobaan
        print(f" Sisa percobaan: {sisa}")
    else:
        print(" AKUN DIKUNCI SEMENTARA")
        print(f" Sudah {MAX_PERCOBAAN} percobaan gagal")
        print(" Hubungi administrator")
        
    sub("Analisis Risiko (Ternary)")
    risiko = ("TINGGI" if not berhasil
              else "RENDAH" if percobaan == 1
              else "SEDANG")
    print(f" Tingkat risiko: {risiko}")

# ==========================================
# 3.8. Integrasi: Sistem Login Lengkap
# ==========================================

def sistem_login_lengkap():
    judul("BAGIAN 7 - SISTEM LOGIN LENGKAP")
    USERS = {
        "admin": {"pwd": "Admin!2024", "role": "admin", "mfa": True},
        "budi": {"pwd": "Budi1234", "role": "user", "mfa": False},
    }
    
    sub("Autentikasi")
    user = input(" Username: ").strip()
    pwd = input(" Password: ")
    berhasil = False
    role = "unknown"
    
    if user in USERS:
        data = USERS[user]
        if data["pwd"] == pwd:
            if data["mfa"]:
                mfa = input(" MFA      : ").strip()
                if mfa == "123456":
                    berhasil = True
                    role = data["role"]
                    print(" -> Autentikasi BERHASIL (MFA OK)")
                else:
                    print(" -> MFA SALAH")
            else:
                berhasil = True
                role = data["role"]
                print(" -> Autentikasi BERHASIL")
        else:
            print(" -> Password SALAH")
    else:
        print(" -> Username TIDAK DIKENAL")
        
    if not berhasil:
        sub("Status")
        print(" Akses DITOLAK - tidak bisa lanjut ke otorisasi")
        return
        
    sub("Otorisasi Akses")
    resource = input(" Resource (file/database/settings): ").strip().lower()
    aksi = input(" Aksi (read/write/delete): ").strip().lower()
    
    if role == "admin":
        if resource in ["file", "database", "settings"]:
            if aksi in ["read", "write", "delete"]:
                keputusan = "DIBERIKAN"
                level = "FULL CONTROL"
            else:
                keputusan = "DITOLAK"
                level = "AKSI TIDAK DIKENAL"
        else:
            keputusan = "DITOLAK"
            level = "RESOURCE TIDAK DIKENAL"
    elif role == "user":
        if resource in ["file", "database"]:
            if aksi in ["read", "write"]:
                keputusan = "DIBERIKAN"
                level = "AKSES TERBATAS"
            else:
                keputusan = "DITOLAK"
                level = "USER TIDAK BOLEH DELETE"
        else:
            keputusan = "DITOLAK"
            level = "DI LUAR WEWENANG"
    else:
        keputusan = "DITOLAK"
        level = "ROLE TIDAK DIKENAL"
        
    sub("Analisis Password (Ternary)")
    panjang = len(pwd)
    kekuatan = ("KUAT" if panjang >= 12 else
                "SEDANG" if panjang >= 8 else
                "LEMAH")
                
    sub("Laporan Akhir")
    garis()
    print(f" User     : {user}")
    print(f" Role     : {role}")
    print(f" Password : {kekuatan} ({panjang} karakter)")
    print(f" Resource : {resource}")
    print(f" Aksi     : {aksi}")
    garis(70, "-")
    print(f" KEPUTUSAN: {keputusan}")
    print(f" LEVEL    : {level}")
    
    severity = ("INFO" if keputusan == "DIBERIKAN" and level == "FULL CONTROL"
                else "LOW" if keputusan == "DIBERIKAN"
                else "HIGH")
    print(f" SEVERITY : {severity}")
    garis()

# ==========================================
# 3.9. Main Program
# ==========================================

def menu():
    print()
    garis()
    print("                LATIHAN PRAKTIKUM 3 - PERCABANGAN")
    print("                   D4 Rekayasa Keamanan Siber")
    garis()
    print(" [1] Login Dasar")
    print(" [2] Login Berlapis")
    print(" [3] Otorisasi Akses Berbasis Role")
    print(" [4] Analisis Kekuatan Password")
    print(" [5] Validasi Form Registrasi")
    print(" [6] Simulasi Login dengan Batas Percobaan")
    print(" [7] Sistem Login Lengkap")
    print(" [A] Jalankan SEMUA bagian")
    print(" [Q] Keluar")
    garis()

def jalankan_semua():
    for fungsi in [login_dasar, login_berlapis, otorisasi_akses,
                   analisis_password, validasi_registrasi,
                   simulasi_login, sistem_login_lengkap]:
        fungsi()
        input("\n[ENTER untuk lanjut]")
        print("\n")
    garis()
    print("                    PRAKTIKUM SELESAI")
    garis()

def main():
    aksi = {
        "1": login_dasar,
        "2": login_berlapis,
        "3": otorisasi_akses,
        "4": analisis_password,
        "5": validasi_registrasi,
        "6": simulasi_login,
        "7": sistem_login_lengkap,
        "A": jalankan_semua,
    }
    
    while True:
        menu()
        pilihan = input("Pilih [1-7/A/Q]: ").strip().upper()
        if pilihan == "Q":
            print("\nKeluar dari program.")
            break
        elif pilihan in aksi:
            aksi[pilihan]()
            input("\n[ENTER untuk kembali ke menu]")
        else:
            print("\nPilihan tidak valid.")

if __name__ == "__main__":
    main()