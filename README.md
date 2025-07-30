# Project Skripsi

Dataset
```bash
curl -L -o ./chexpert.zip https://www.kaggle.com/api/v1/datasets/download/ashery/chexpert # Download dataset
unzip -q chexpert.zip -d CheXpert-v1.0-small  # Ekstrak ke folder baru
rm chexpert.zip  # Hapus file zip
```

Ubah bentuk pohon direktori datset yang sudah didownload ke bentuk yang simpel dengan menjalankan `dataset.ipynb`

Jalankan training:
- `train_v2.ipynb`, code backup 1 (ignore)
- `train_v3.ipynb`, code backup 2 (ignore)
- `train_v3.ipynb`, current code (use)

**Task:**

- [x] Tambahin `ratio` pada `transform`
- [x] Tambahin `ploting` akurasi dan loss real time saat training
- [x] Tanbahin `scheduler learning rate`
- [x] Run train di `50 epoch`
- [x] tangani uncertain = -1 jadi 1
- [x] hapus outlier gambar
- [x] hapus label yang memiliki sedikit data
- [ ] Tambahkan atgumrnted balancing
