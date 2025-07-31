import requests
import csv

# URL endpoint API
url = "https://yudistira.turnbackhoax.id/api/antihoax/"

# Header yang dibutuhkan
headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

key = "request"
limit = 100  # Jumlah item per permintaan
offset = 0   # Mulai dari item pertama
total_news = 20000 # Total jumlah berita yang ingin diambil

all_news = []  # Menyimpan semua berita

while offset < total_news:
    # Parameter data untuk permintaan POST
    data = {
        "key": key,
        "limit": limit,
        "offset": offset
    }

    # Melakukan permintaan POST
    response = requests.post(url, headers=headers, data=data)

    # Mengecek status code dan memproses hasil jika berhasil
    if response.status_code == 200:
        try:
            result = response.json()
            if isinstance(result, list):
                all_news.extend(result)
                print(f"Data dari offset {offset} berhasil diambil, total {len(result)} item.")
            else:
                print(f"Struktur data tidak seperti yang diharapkan pada offset {offset}: {result}")
                break
        except ValueError:
            print(f"Gagal menguraikan JSON pada offset {offset}: {response.text}")
            break
    else:
        print(f"Gagal mengambil data pada offset {offset}: {response.status_code}, {response.text}")
        break

    # Tingkatkan offset untuk permintaan berikutnya
    offset += limit

print(f"Total berita yang berhasil diambil: {len(all_news)}")

# Menampilkan hasil tertentu dari setiap dictionary
csv_file = 'tbhoax_data.csv'
csv_columns = ['id', 'authors', 'status', 'classification', 'title', 'content', 'references','tanggal', 'conclusion']

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for news_item in all_news:
            if isinstance(news_item, dict):
                # Menyaring kunci yang diinginkan
                filtered_item = {key: news_item.get(key) for key in csv_columns}
                writer.writerow(filtered_item)
    print(f"Data berhasil disimpan dalam file {csv_file}")
except IOError:
    print("Gagal menyimpan data ke file CSV")