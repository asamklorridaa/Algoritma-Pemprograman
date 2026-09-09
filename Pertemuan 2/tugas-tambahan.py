import ipaddress
import socket


DATABASE_USER = {
    "admin": {
        "password": "Admin123",
        "role": "admin",
        "ip": "192.168.1.100",
    },
    "user1": {
        "password": "User123",
        "role": "user",
        "ip": "192.168.1.101",
    },
    "security": {
        "password": "Secure@2024",
        "role": "security",
        "ip": "192.168.1.102",
    },
}

PORT_BERBAHAYA = {21, 23, 135, 139, 445, 3389}


def login():
    print("\n" + "=" * 60)
    print("SISTEM KEAMANAN TERINTEGRASI")
    print("=" * 60)

    for percobaan in range(1, 4):
        print(f"\nPercobaan ke-{percobaan} dari 3")
        username = input("Username: ").strip()
        password = input("Password: ")
        ip_akses = input("IP terdaftar: ").strip()

        data_user = DATABASE_USER.get(username)
        login_valid = (
            data_user is not None
            and data_user["password"] == password
            and data_user["ip"] == ip_akses
        )

        if login_valid:
            print(f"Login berhasil. Selamat datang, {username}.")
            print(f"Role: {data_user['role']}")
            return username, data_user["role"]

        print("Login gagal.")
        if data_user is None:
            print("Username tidak terdaftar.")
        elif data_user["password"] != password:
            print("Password salah.")
        elif data_user["ip"] != ip_akses:
            print("IP tidak sesuai dengan database.")
        print(f"Sisa percobaan: {3 - percobaan}")

    print("Akses ditolak karena batas 3 percobaan tercapai.")
    return None, None


def analisis_password(username):
    password = input("\nPassword yang akan dianalisis: ")
    jumlah_besar = sum(karakter.isupper() for karakter in password)
    jumlah_kecil = sum(karakter.islower() for karakter in password)
    jumlah_angka = sum(karakter.isdigit() for karakter in password)
    jumlah_spesial = sum(not karakter.isalnum() for karakter in password)

    kriteria = [
        ("Minimal 10 karakter", len(password) >= 10, 2),
        ("Minimal 2 huruf besar", jumlah_besar >= 2, 1),
        ("Minimal 2 huruf kecil", jumlah_kecil >= 2, 1),
        ("Minimal 2 angka", jumlah_angka >= 2, 1),
        ("Minimal 2 karakter spesial", jumlah_spesial >= 2, 1),
        (
            "Tidak mengandung username",
            username.lower() not in password.lower(),
            1,
        ),
    ]
    skor = sum(nilai for _, terpenuhi, nilai in kriteria if terpenuhi)

    if skor == 7:
        level = "SANGAT KUAT"
    elif skor >= 5:
        level = "KUAT"
    elif skor >= 3:
        level = "SEDANG"
    elif skor >= 1:
        level = "LEMAH"
    else:
        level = "SANGAT LEMAH"

    print("\n--- HASIL ANALISIS PASSWORD ---")
    print(f"Password: {'*' * len(password)}")
    print(f"Skor: {skor}/7")
    print(f"Level: {level}")
    for nama, terpenuhi, _ in kriteria:
        status = "YA" if terpenuhi else "TIDAK"
        print(f"- {nama}: {status}")


def tentukan_kelas_ip(oktet_pertama):
    if 1 <= oktet_pertama <= 126:
        return "A"
    if 128 <= oktet_pertama <= 191:
        return "B"
    if 192 <= oktet_pertama <= 223:
        return "C"
    if 224 <= oktet_pertama <= 239:
        return "D"
    if 240 <= oktet_pertama <= 255:
        return "E"
    return "Khusus (0 atau 127)"


def analisis_ip():
    alamat = input("\nAlamat IPv4: ").strip()
    try:
        ip = ipaddress.ip_address(alamat)
        if ip.version != 4:
            raise ValueError
    except ValueError:
        print("Format IPv4 tidak valid.")
        return

    oktet_pertama = int(str(ip).split(".")[0])
    tipe = "PRIVAT" if ip.is_private else "PUBLIK"
    print("\n--- HASIL ANALISIS IP ---")
    print(f"IP: {ip}")
    print("Format: VALID")
    print(f"Kelas: {tentukan_kelas_ip(oktet_pertama)}")
    print(f"Tipe: {tipe}")


def klasifikasi_port(port):
    if port <= 1023:
        return "Well-known"
    if port <= 49151:
        return "Registered"
    return "Dynamic"


def baca_port():
    try:
        port = int(input("\nNomor port (0-65535): "))
    except ValueError:
        print("Port harus berupa angka.")
        return None
    if not 0 <= port <= 65535:
        print("Port harus berada di antara 0 dan 65535.")
        return None
    return port


def analisis_port():
    port = baca_port()
    if port is None:
        return

    status = "BERBAHAYA" if port in PORT_BERBAHAYA else "AMAN"
    print("\n--- HASIL ANALISIS PORT ---")
    print(f"Port: {port}")
    print(f"Klasifikasi: {klasifikasi_port(port)}")
    print(f"Status: {status}")


def scan_port_range():
    teks_range = input("\nRange port (contoh 1-100): ").strip()
    try:
        awal_teks, akhir_teks = teks_range.split("-", maxsplit=1)
        awal = int(awal_teks)
        akhir = int(akhir_teks)
    except ValueError:
        print("Format range tidak valid. Gunakan contoh: 1-100")
        return

    if not 0 <= awal <= akhir <= 65535:
        print("Range harus berada di antara 0 dan 65535.")
        return

    target = input("Host target (Enter untuk localhost): ").strip() or "127.0.0.1"
    try:
        socket.gethostbyname(target)
    except socket.gaierror:
        print("Host target tidak ditemukan.")
        return

    port_terbuka = []
    print(f"Memindai {target} pada port {awal}-{akhir}...")
    for port in range(awal, akhir + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as koneksi:
            koneksi.settimeout(0.05)
            if koneksi.connect_ex((target, port)) == 0:
                port_terbuka.append(port)

    hasil = ", ".join(map(str, port_terbuka)) or "tidak ada"
    print(f"Port terbuka: {hasil}")


def tampilkan_database():
    print("\n--- DATABASE USER ---")
    for username, data_user in DATABASE_USER.items():
        print(
            f"Username: {username} | Role: {data_user['role']} "
            f"| IP: {data_user['ip']}"
        )


def tampilkan_menu(role):
    print("\n" + "=" * 60)
    print(f"MENU ROLE: {role.upper()}")
    print("1. Analisis kekuatan password")
    print("2. Analisis alamat IP")
    print("3. Analisis port")
    print("4. Scan port range")
    if role in ("admin", "security"):
        print("5. Tampilkan database user")
    print("6. Jalankan semua")
    print("0. Logout")


def jalankan_semua(username, role):
    print("\nMenjalankan semua fitur...")
    analisis_password(username)
    analisis_ip()
    analisis_port()
    scan_port_range()
    if role in ("admin", "security"):
        tampilkan_database()


def menu_utama(username, role):
    while True:
        tampilkan_menu(role)
        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            analisis_password(username)
        elif pilihan == "2":
            analisis_ip()
        elif pilihan == "3":
            analisis_port()
        elif pilihan == "4":
            scan_port_range()
        elif pilihan == "5" and role in ("admin", "security"):
            tampilkan_database()
        elif pilihan == "6":
            jalankan_semua(username, role)
        elif pilihan == "0":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan menu tidak tersedia untuk role Anda.")


def main():
    username, role = login()
    if username is not None:
        menu_utama(username, role)


if __name__ == "__main__":
    main()
