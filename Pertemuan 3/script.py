IP_BERBAHAYA = [
	"192.168.1.100",
	"192.186.1.100",
	"129.168.1.100",
	"10.0.0.1",
	"172.16.0.1",
]
USERNAME_MENCURIGAKAN = ["admin", "root", "guest"]
KARAKTER_KHUSUS = "!@#$%^&*()-_=+[]{}|;:,.<>?/\\~`"


def tampilkan_judul(judul):
	print(f"\n{'=' * 70}")
	print(f"{judul}")
	print(f"{'=' * 70}")


def input_ip(pesan):
	while True:
		alamat_ip = input(f"{pesan}").strip()
		bagian_ip = alamat_ip.split(".")
		format_valid = (
			len(bagian_ip) == 4
			and all(bagian.isdigit() and 0 <= int(bagian) <= 255 for bagian in bagian_ip)
		)
		if format_valid:
			return alamat_ip
		print(f"Format IP tidak valid. Gunakan format xxx.xxx.xxx.xxx.")


def registrasi_user(database_user):
	tampilkan_judul("1. REGISTRASI USER")
	username = input(f"Masukkan username baru: ").strip()
	while any(user["username"] == username for user in database_user):
		print(f"Username tersebut sudah terdaftar.")
		username = input(f"Masukkan username baru: ").strip()

	password = input(f"Masukkan password baru: ")
	alamat_ip = input_ip(f"Masukkan alamat IP (xxx.xxx.xxx.xxx): ")
	database_user.append(
		{"username": username, "password": password, "ip": alamat_ip}
	)
	print(f"Registrasi user berhasil.")
	print(f"Total user terdaftar: {len(database_user)}")
	return username, password, alamat_ip


def login_user(database_user):
	tampilkan_judul("2. LOGIN USER")
	username = input(f"Masukkan username: ").strip()
	password = input(f"Masukkan password: ")
	alamat_ip = input_ip(f"Masukkan alamat IP: ")

	user_ditemukan = next(
		(user for user in database_user if user["username"] == username), None
	)
	username_valid = user_ditemukan is not None
	password_valid = username_valid and password == user_ditemukan["password"]
	ip_valid = username_valid and alamat_ip == user_ditemukan["ip"]
	login_berhasil = username_valid and password_valid and ip_valid

	print(f"\nStatus login: {'BERHASIL' if login_berhasil else 'GAGAL'}")
	if login_berhasil:
		print(f"Selamat datang, {username}.")
	else:
		if not username_valid:
			print(f"Alasan: Username tidak ditemukan.")
		else:
			if not password_valid:
				print(f"Alasan: Password salah.")
			if not ip_valid:
				print(f"Alasan: IP tidak terdaftar.")
	return {
		"username": username,
		"password": password,
		"ip": alamat_ip,
		"berhasil": login_berhasil,
	}


def reset_password(database_user):
	tampilkan_judul("3. LUPA KATA SANDI")
	username = input(f"Masukkan username: ").strip()
	alamat_ip = input_ip(f"Masukkan alamat IP untuk verifikasi: ")
	user_ditemukan = next(
		(
			user
			for user in database_user
			if user["username"] == username and user["ip"] == alamat_ip
		),
		None,
	)

	if user_ditemukan is None:
		print(f"Reset password gagal. Username atau IP tidak sesuai.")
		return False

	password_baru = input(f"Masukkan password baru: ")
	user_ditemukan["password"] = password_baru
	print(f"Password berhasil direset.")
	return True


def analisis_ip(alamat_ip):
	status_ip = "BERBAHAYA" if alamat_ip in IP_BERBAHAYA else "AMAN"
	print(f"\n--- ANALISIS IP ---")
	print(f"Alamat IP : {alamat_ip}")
	print(f"Status IP : {status_ip}")
	return status_ip


def analisis_username(username):
	status_username = (
		"MENCURIGAKAN" if username.lower() in USERNAME_MENCURIGAKAN else "NORMAL"
	)
	print(f"\n--- ANALISIS USERNAME ---")
	print(f"Username : {username}")
	print(f"Status username : {status_username}")
	return status_username


def analisis_password(username, password):
	panjang = len(password)
	jumlah_huruf_besar = sum(1 for karakter in password if karakter.isupper())
	jumlah_huruf_kecil = sum(1 for karakter in password if karakter.islower())
	jumlah_angka = sum(1 for karakter in password if karakter.isdigit())
	jumlah_simbol = sum(1 for karakter in password if karakter in KARAKTER_KHUSUS)

	kriteria = {
		"Panjang minimal 12 karakter": panjang >= 12,
		"Huruf besar maksimal 2": jumlah_huruf_besar <= 2,
		"Mengandung huruf kecil": jumlah_huruf_kecil > 0,
		"Mengandung minimal 3 angka": jumlah_angka >= 3,
		"Mengandung simbol khusus": jumlah_simbol > 0,
		"Tidak mengandung username": username.lower() not in password.lower(),
	}
	skor = sum(kriteria.values())

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

	tampilkan_judul("5. ANALISIS PASSWORD")
	print(f"Password : {'*' * panjang}")
	print(f"Panjang password : {panjang} karakter")
	print(f"Skor password : {skor}/6")
	print(f"Level kekuatan : {level}")
	print(f"\nDetail kriteria:")
	for nama_kriteria, terpenuhi in kriteria.items():
		status = "YA" if terpenuhi else "TIDAK"
		print(f"- {nama_kriteria}: {status}")

	terpenuhi = [nama for nama, nilai in kriteria.items() if nilai]
	tidak_terpenuhi = [nama for nama, nilai in kriteria.items() if not nilai]
	print(f"\nKriteria terpenuhi: {', '.join(terpenuhi) if terpenuhi else 'Tidak ada'}")
	print(
		f"Kriteria tidak terpenuhi: "
		f"{', '.join(tidak_terpenuhi) if tidak_terpenuhi else 'Tidak ada'}"
	)
	print(f"\nRekomendasi perbaikan password:")
	if not tidak_terpenuhi:
		print(f"- Password sudah memenuhi semua kriteria.")
	else:
		for nama_kriteria in tidak_terpenuhi:
			print(f"- Penuhi kriteria: {nama_kriteria}.")

	return {"skor": skor, "level": level, "kriteria": kriteria}


def deteksi_ancaman(status_ip, status_username, hasil_password):
	poin_ip = 2 if status_ip == "BERBAHAYA" else 0
	poin_username = 1 if status_username == "MENCURIGAKAN" else 0
	poin_password = 1 if hasil_password["skor"] <= 2 else 0
	total_poin = poin_ip + poin_username + poin_password

	if total_poin >= 3:
		tingkat = "TINGGI"
		rekomendasi = "Segera blokir IP dan lakukan investigasi menyeluruh"
	elif total_poin == 2:
		tingkat = "SEDANG"
		rekomendasi = "Lakukan monitoring ketat dan verifikasi dengan user"
	elif total_poin == 1:
		tingkat = "RENDAH"
		rekomendasi = "Pantau aktivitas user dan catat dalam log"
	else:
		tingkat = "AMAN"
		rekomendasi = "Tidak ada tindakan yang diperlukan"

	tampilkan_judul("6. DETEKSI TINGKAT ANCAMAN")
	print(f"Poin analisis IP : {poin_ip}")
	print(f"Poin analisis username : {poin_username}")
	print(f"Poin analisis password : {poin_password}")
	print(f"Total poin ancaman : {total_poin}")
	print(f"Tingkat ancaman : {tingkat}")
	print(f"Rekomendasi SOC : {rekomendasi}")
	return tingkat, rekomendasi


def laporan_akhir(data_login, status_ip, status_username, hasil_password, tingkat, rekomendasi):
	tampilkan_judul("7. LAPORAN AKHIR")
	print(f"Username : {data_login['username']}")
	print(f"IP akses : {data_login['ip']}")
	print(f"Status login : {'BERHASIL' if data_login['berhasil'] else 'GAGAL'}")
	print(f"Status IP : {status_ip}")
	print(f"Status username : {status_username}")
	print(f"Kekuatan password : {hasil_password['level']} ({hasil_password['skor']}/6)")
	print(f"Tingkat ancaman : {tingkat}")
	print(f"Tindakan SOC : {rekomendasi}")


def main():
	database_user = []
	tampilkan_judul("SISTEM MANAJEMEN AKUN DAN DETEKSI ANCAMAN LOGIN")
	registrasi_user(database_user)
	data_login = login_user(database_user)
	reset_password(database_user)

	tampilkan_judul("4. ANALISIS LOGIN")
	username_analisis = input(f"Masukkan username untuk analisis: ").strip()
	alamat_ip_analisis = input_ip(f"Masukkan IP untuk analisis: ")
	password_analisis = input(f"Masukkan password untuk analisis: ")
	status_ip = analisis_ip(alamat_ip_analisis)
	status_username = analisis_username(username_analisis)
	hasil_password = analisis_password(username_analisis, password_analisis)
	tingkat, rekomendasi = deteksi_ancaman(
		status_ip, status_username, hasil_password
	)
	laporan_akhir(
		data_login,
		status_ip,
		status_username,
		hasil_password,
		tingkat,
		rekomendasi,
	)


if __name__ == "__main__":
	main()
