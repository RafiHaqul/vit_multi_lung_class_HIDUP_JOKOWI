import kagglehub

# Download latest version
path = kagglehub.dataset_download("ashery/chexpert")

print("Path to dataset files:", path)

# d:\Documents\AMIKOM\skripsi\project_1\.venv\Lib\site-packages\tqdm\auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html
#   from .autonotebook import tqdm as notebook_tqdm
# Resuming download from 11025776640 bytes (470353869 bytes left)...
# Resuming download from https://www.kaggle.com/api/v1/datasets/download/ashery/chexpert?dataset_version_number=1 (11025776640/11496130509) bytes left.
# 100%|██████████| 10.7G/10.7G [01:24<00:00, 5.54MB/s]Extracting files...

# Path to dataset files: C:\Users\HP Victus\.cache\kagglehub\datasets\ashery\chexpert\versions\1