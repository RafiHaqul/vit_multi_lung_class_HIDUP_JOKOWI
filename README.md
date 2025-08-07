# Project Skripsi

## Download Dataset
```bash
curl -L -o ./chexpert.zip https://www.kaggle.com/api/v1/datasets/download/ashery/chexpert # Download dataset
unzip -q chexpert.zip -d CheXpert-v1.0-small  # Ekstrak ke folder baru
rm chexpert.zip  # Hapus file zip
```

## Training Project
Jalankan training:
- ~~`train_v1.ipynb`-`train_v3.ipynb`, code backup 1 (ignore)~~
- ~~`train_v3.ipynb`, code backup 1 (ignore)~~
- ~~`train_v4.ipynb`, code backup 2 (ignore)~~
- `train_v5_16.ipynb`, current code 1 (use)
- `train_v5_32.ipynb`, current code 2 (use)

## Tugas
**Task:**

- [x] Tambahin `ratio` pada `transform`
- [x] Tambahin `ploting` akurasi dan loss real time saat training
- [x] Tanbahin `scheduler learning rate`
- [x] ~~Run train di `50 epoch`~~
- [x] tangani uncertain = -1 jadi 1
- [x] ~~hapus outlier gambar~~
- [x] ~~hapus label yang memiliki sedikit data~~
- [x] Tambahkan atgumrnted balancing
- [x] Tambahkan Label Smoothing Regularization


