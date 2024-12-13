import pandas as pd

# Load dataset
file_path = 'disperkim-od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_data.csv'
user_dataset = pd.read_csv(file_path)

# Filter kolom yang relevan
filtered_data = user_dataset[['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun']].copy()

# Isi nilai kosong dengan 0 pada kolom jumlah_produksi_sampah
filtered_data['jumlah_produksi_sampah'].fillna(0, inplace=True)

# Membulatkan angka ke dua desimal
filtered_data['jumlah_produksi_sampah'] = filtered_data['jumlah_produksi_sampah'].round(2)

# Cetak hasil di terminal
print("\nJumlah sampah per Kabupaten/Kota:")
for _, row in filtered_data.iterrows():
    print(f"{row['nama_kabupaten_kota']}: {row['jumlah_produksi_sampah']:.2f} ton")

# Ekspor hasil ke CSV dan Excel
filtered_data.to_csv('produksi_sampah.csv', index=False)
filtered_data.to_excel('produksi_sampah.xlsx', index=False)

print("\nData telah diekspor ke produksi_sampah.csv dan produksi_sampah.xlsx")
