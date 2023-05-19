# Dicoding - Tugas Akhir 
## Bikes Sharing Data Analisis
Sistem Bike Sharing adalah generasi baru dari penyewaan sepeda tradisional di mana seluruh proses mulai dari keanggotaan, penyewaan, dan pengembalian 
kembali telah menjadi otomatis. Melalui sistem ini, pengguna dapat dengan mudah menyewa sepeda dari posisi tertentu dan mengembalikannya 
kembali ke posisi lain. Saat ini, terdapat lebih dari 500 program berbagi sepeda di seluruh dunia yang terdiri dari 
lebih dari 500 ribu sepeda. Saat ini, terdapat minat yang besar terhadap sistem ini karena peran pentingnya dalam lalu lintas, 
masalah lingkungan dan kesehatan.

## Struktur 
```
|dashboard  
|├───main_data.csv  
|└───dashboard.py  
|data  
|├───data_1.csv  
|└───data_2.csv  
|notebook.ipynb  
|README.md  
|requirements.txt  
```

## Setup environment
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit babel
```

## Run streamlit app
```
cd bikesharingdataanalisis-dicoding
streamlit run dashboard/dashboard.py
```
