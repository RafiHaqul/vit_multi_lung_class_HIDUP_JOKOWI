# Project Skripsi 💢

Dataset
```bash
curl -L -o ./chexpert.zip https://www.kaggle.com/api/v1/datasets/download/ashery/chexpert # Download dataset
unzip -q chexpert.zip -d CheXpert-v1.0-small  # Ekstrak ke folder baru
rm chexpert.zip  # Hapus file zip
```

Ubah bentuk pohon direktori datset yang sudah didownload ke bentuk yang simpel dengan menjalankan `dataset.ipynb`

Jalankan training:
- `1.ipynb`, code backup 1 (ignore)
- `2.ipynb`, code backup 2 (ignore)
- `2 copy.ipynb`, current code (use)

**Task:**

- [x] Tambahin `ratio` pada `transform`
- [x] Tambahin `ploting` akurasi dan loss real time saat training
- [x] Tanbahin `scheduler learning rate`
- [x] Potong jumlah baris dataset
    - apakah data 'uncertain' perlu dimasukan?
    - apakah `uncertain` cenderung ke positif atau negatif
    - apakah data imbalance?
    - apakah ada gambar rusak (outlayer)
- [ ] Run train di `50 epoch`

# HIDUP JOKOWI! ✊
