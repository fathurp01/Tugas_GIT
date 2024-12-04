# Tugas GIT
#
# Kode data panen
# Nama : Fathurrahman Pratama Putra
# NRP : 152023057
# Matkul : Pemrograman Dasar
# Kelas : BB

data_panen = {
    "lokasi1": {
        "nama_lokasi": "Kebun A",
        "hasil_panen": {"padi": 1200, "jagung": 800, "kedelai": 500},
    },
    "lokasi2": {
        "nama_lokasi": "Kebun B",
        "hasil_panen": {"padi": 1500, "jagung": 900, "kedelai": 450},
    },
    "lokasi3": {
        "nama_lokasi": "Kebun C",
        "hasil_panen": {"padi": 1100, "jagung": 750, "kedelai": 600},
    },
    "lokasi4": {
        "nama_lokasi": "Kebun D",
        "hasil_panen": {"padi": 1300, "jagung": 850, "kedelai": 550},
    },
    "lokasi5": {
        "nama_lokasi": "Kebun E",
        "hasil_panen": {"padi": 1400, "jagung": 950, "kedelai": 480},
    },
}

# Menampilkan seluruh data dari data_panen
print("Data Panen:")
for lokasi, data in data_panen.items():
    print(f"Nama Lokasi: {data['nama_lokasi']}, Hasil Panen: {data['hasil_panen']}")
print()

# Menampilkan jumlah hasil panen jagung dari lokasi2
print("Jumlah hasil panen jagung dari lokasi2:")
print(data_panen["lokasi2"]["hasil_panen"]["jagung"])
print()

# Menampilkan nama lokasi dari lokasi3
print("Nama lokasi dari lokasi3:")
print(data_panen["lokasi3"]["nama_lokasi"])
print()

# Memasukkan Jumlah Hasil Panen Padi dan Kedelai Setiap Lokasi ke Dalam Variabel yang Berbeda
jum_hasil_padi = []
jum_hasil_kedelai = []
for lokasi, data in data_panen.items():
    jum_hasil_padi.append(data["hasil_panen"]["padi"])
    jum_hasil_kedelai.append(data["hasil_panen"]["kedelai"])

# Percabangan untuk menentukan perhatian khusus
print("Status dari setiap lokasi:")
for i, lokasi in enumerate(data_panen.keys()):
    if jum_hasil_padi[i] > 1300 or data_panen[lokasi]["hasil_panen"]["jagung"] > 800:
        print(f"Lokasi {data_panen[lokasi]['nama_lokasi']} memerlukan perhatian khusus")
    else:
        print(f"Lokasi {data_panen[lokasi]['nama_lokasi']} dalam kondisi baik")



print("coba merge")








