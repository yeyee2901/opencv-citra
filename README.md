# Kuliah Citra
## GETTING STARTED
### Windows
1. Download & Install [Python 3.7](https://www.python.org/ftp/python/3.7.9/python-3.7.9.exe) (versi python yang sudah disepakati digunakan). Untuk langkah instalasi dapat melihat [contoh artikel di link Ini](https://programmingwithjim.wordpress.com/2020/09/08/installing-python-3-in-git-bash-on-windows-10/). **PERHATIKAN LANGKAH-LANGKAH NYA BAIK-BAIK**
2. Download [Git & Git Bash](https://github.com/git-for-windows/git/releases/download/v2.35.1.windows.2/Git-2.35.1.2-64-bit.exe) (Version control system untuk manage perubahan file & git bash untuk terminal command line utility). Pastikan arsitektur sesuai (64-bit atau 32-bit)
3. Download [Visual Studio Code](https://code.visualstudio.com/download) untuk Windows. Pastikan arsitektur sesuai juga (64-bit atau 32-bit)
4. Buka Git Bash (Start > search "Git Bash"), lalu jalankan command ini untuk memastikan semua terinstall dengan benar (setelah tanda # merupakan komentar, jadi diabaikan oleh sistem)
```bash
git --version       # cek git
python --version    # cek python
pip --version       # cek pip (package manager python)
python -m venv -h   # cek virtualenv manager
```
5. Jika `pip` tidak terinstall, maka bisa [lihat artikel ini](https://www.liquidweb.com/kb/install-pip-windows/)
6. Buat akun [github](https://github.com) agar bisa melakukan berkontribusi ke repositori-nya.
7. Buka Git Bash, lalu Atur `git` untuk sistem agar menyesuaikan akun github yang sudah dibuat
```bash
git config user.username <user github anda>
git config user.email <email anda>
git config user.name <Nama lengkap anda>
```
8. Buat Direktori Sembarang, misalnya di folder `D:\Kuliah-Citra`
```bash
cd /d                   # pergi ke Drive D
mkdir Kuliah-Citra      # buat folder Kuliah-Citra
cd Kuliah-Citra         # pergi ke folder yang baru saja dibuat
```
9. Clone repository ini di folder yang baru saja dibuat
```bash
git clone https://github.com/yeyee2901/opencv-citra
```
10. Pergi ke repository (folder) yang merupakan hasil clone
```bash
# untuk melihat daftar file di `current directory`
# atau direktori lokasi sekarang
ls

cd opencv-citra
```
11. Buat virtual environment
```bash
python -m venv devEnv
```
12. **PENTING** Aktifkan virtual environment
```bash
source devEnv/bin/activate
```
13. Upgrade pip yang ada di virtual environment dan install dependency project
```bash
pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
```
14. Sekarang, coba jalankan ini, kalau tidak ada error berarti sukses.
```bash
python -c "import cv2"
```
15. Sekarang buka Visual Studio Code (code editor), di direktori yang tadi
```bash
pwd         # untuk mengetahui sekarang ada di direktori apa
# output: /d/Kuliah-Citra/opencv-citra

# buka visual studio code di direktori ini ( . = direktori sekarang )
code .
```
16. Install extension `Python` agar coding di Python menjadi nyaman
17. Cara menjalankan program: Buka Git Bash yang tadi (dalam kondisi virtual environment sudah aktif), lalu jalankan
```
python <nama folder>

# misalnya:
python percobaan-pertama
```

## Notes
- Agar dapat menjalankan program Python cukup dengan memanggil nama folder-nya, pastikan setiap folder project mempunyai `__main__.py` & `app.py`
```
.
├── devEnv                          # untuk virtual environment jangan diutak atik
│   ├── bin
│   ├── lib
│   └── ...
├── percobaan-pertama               # contoh folder project
│   ├── app.py                      # setiap folder project harus ada ini
│   ├── __main__.py                 # setiap folder project harus ada ini
│   ├── module_satu.py              # misalkan ada modul lain
│   └── module_<dan seterusnya>.py  # dan seterusnya
├── README.md
└── requirements.txt                # list dependency (jangan diutak atik)
```
- Isi dari `__main__.py`:
```python
# file: __main__.py
from app import main

main()
```
- Nah, berarti setiap file `app.py`, juga harus ada fungsi `main()`
```python
# file: app.py

def main():
    """
    Ini komentar multi line. 

    Beri komentar untuk bagian coding an yang kompleks dan perlu penjelasan langsung!
    """
    # lakukan sesuatu .... (ini komentar single line)
```
- Fungsi-fungsi kecil bisa dipisah di file terpisah nanti bisa di import, tapi untuk program utama, tetap harus ada di `app.py`
