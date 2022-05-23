# Installation

## Versi Python
disarankan menggunakan versi terbaru dari Python. Flask mendukung Python 3.7 dan yang lebih baru.

## Dependencies
Distribusi ini akan diinstal secara otomatis saat menginstal Flask.

* Werkzeug mengimplementasikan WSGI, antarmuka Python standar antara aplikasi dan server.

* Jinja adalah bahasa template yang merender halaman yang dilayani aplikasi Anda.

* MarkupSafe hadir dengan Jinja. Itu lolos dari input yang tidak tepercaya saat merender template untuk menghindari serangan injeksi.

* ItsDangerous menandatangani data dengan aman untuk memastikan integritasnya. Ini digunakan untuk melindungi cookie sesi Flask.

* Klik adalah kerangka kerja untuk menulis aplikasi baris perintah. Ini memberikan flaskperintah dan memungkinkan menambahkan perintah manajemen kustom.

## Dependensi opsional
Distribusi ini tidak akan diinstal secara otomatis. Flask akan mendeteksi dan menggunakannya jika Anda menginstalnya.

* Blinker menyediakan dukungan untuk Sinyal .

* python-dotenv mengaktifkan dukungan untuk Variabel Lingkungan Dari dotenv saat menjalankan flask perintah.

* Watchdog menyediakan reloader yang lebih cepat dan efisien untuk server pengembangan.

## greenlet
Anda dapat memilih untuk menggunakan gevent atau eventlet dengan aplikasi Anda. Dalam hal ini, diperlukan greenlet>=1.0. Saat menggunakan PyPy, PyPy>=7.3.7 diperlukan.

Ini bukan versi minimum yang didukung, mereka hanya menunjukkan versi pertama yang menambahkan fitur yang diperlukan. Anda harus menggunakan versi terbaru dari masing-masing.

## Virtual environments
Gunakan virtual environments untuk mengelola dependensi untuk proyek Anda, baik dalam pengembangan maupun produksi.

Masalah apa yang dipecahkan oleh virtual environments? Semakin banyak proyek Python yang Anda miliki, semakin besar kemungkinan Anda perlu bekerja dengan berbagai versi pustaka Python, atau bahkan Python itu sendiri. Versi pustaka yang lebih baru untuk satu proyek dapat merusak kompatibilitas di proyek lain.

Lingkungan virtual adalah grup independen dari pustaka Python, satu untuk setiap proyek. Paket yang diinstal untuk satu proyek tidak akan memengaruhi proyek lain atau paket sistem operasi.

Python dibundel dengan venvmodul untuk membuat virtual environments.
1. Buat folder proyek dan venvfolder di dalam:
- mkdir myproject
- cd myproject
- py -3 -m venv venv

2. Sebelum Anda mengerjakan proyek Anda, aktifkan lingkungan yang sesuai:
- venv\Scripts\activate

3. Dalam lingkungan yang diaktifkan, gunakan perintah berikut untuk menginstal Flask:
- pip install Flask

# Project Layout
Buat direktori proyek dan masukkan:
- mkdir flask-tutorial
- cd flask-tutorial

Tutorial akan menganggap Anda bekerja dari flask-tutorial direktori mulai sekarang. Nama file di bagian atas setiap blok kode relatif terhadap direktori ini.

A Flask application can be as simple as a single file.
```python
hello.py
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
```

Namun, ketika sebuah proyek semakin besar, menjadi sangat sulit untuk menyimpan semua kode dalam satu file. Proyek Python menggunakan paket untuk mengatur kode ke dalam beberapa modul yang dapat diimpor jika diperlukan, dan tutorial ini juga akan melakukannya.
Direktori proyek akan berisi:
* flaskr/, paket Python yang berisi kode aplikasi dan file Anda.

* tests/, direktori yang berisi modul pengujian.

* venv/, lingkungan virtual Python tempat Flask dan dependensi lainnya diinstal.

* File instalasi memberi tahu Python cara menginstal proyek Anda.

* Konfigurasi kontrol versi, seperti git . Anda harus membiasakan menggunakan beberapa jenis kontrol versi untuk semua proyek Anda, berapa pun ukurannya.

* File proyek lain yang mungkin Anda tambahkan di masa mendatang.

Pada akhirnya, tata letak proyek Anda akan terlihat seperti ini:
/home/user/Projects/flask-tutorial
├── flaskr/
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── auth.py
│   ├── blog.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   └── blog/
│   │       ├── create.html
│   │       ├── index.html
│   │       └── update.html
│   └── static/
│       └── style.css
├── tests/
│   ├── conftest.py
│   ├── data.sql
│   ├── test_factory.py
│   ├── test_db.py
│   ├── test_auth.py
│   └── test_blog.py
├── venv/
├── setup.py
└── MANIFEST.in

Jika Anda menggunakan kontrol versi, file berikut yang dihasilkan saat menjalankan proyek Anda harus diabaikan. Mungkin ada file lain berdasarkan editor yang Anda gunakan. Secara umum, abaikan file yang tidak Anda tulis. Misalnya, dengan git:
.gitignore
venv/

*.pyc
__pycache__/

instance/

.pytest_cache/
.coverage
htmlcov/

dist/
build/
*.egg-info/