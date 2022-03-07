# Bab 6

**6. Modules**
Fungsi dan variabel akan hilang jika kamu berhenti dari interpreter python dan memasukkannya lagi. Oleh karna itu jika program yang ditulis agak panjang, sebaiknya menggunakan editor teks untuk menyiapkan input bagi penerjemah yang lebih panjang. Python memiliki cara untuk meletakkan definisi dalam file dan menggunakannya dalam skrip atau dalam contoh interaktif dari interpreter. File seperti itu disebut module; definisi dari modul dapat imported ke modul lain atau ke modul main (kumpulan variabel yang Anda memiliki akses ke dalam skrip yang dieksekusi di tingkat atas dan dalam mode kalkulator). Modul adalah file yang berisi definisi dan pernyataan Python. Nama berkas adalah nama modul dengan akhiran .py diakhirnya. Dalam sebuah modul, nama modul (sebagai string) tersedia sebagai nilai variabel global "__name__". Misalnya, gunakan editor teks favorit Anda untuk membuat bernama bernama fibo.

**6.1 more on modules**
Untuk menginisialisasi modul dapat berisi pernytaan yang dapat dieksekusi serta definisi fungsi. Setiap modul memiliki tabel symbol sendiri yang digunakan sebagai tabel symbol global yang berfungsi untuk didefinisikan dalam modul. Variabel global modul dengan notasi yang sama yang digunakan untuk merujuk ke fungsinya, modname.itemname. Modul dapat mengimpor modul lain. Biasanya, tetapi tidak diperlukan untuk menempatkan semua pernyataan import di awal modul (atau skrip, dalam hal ini). Nama-nama modul yang diimpor ditempatkan di tabel simbol global modul impor.

**6.1.1. Executing modules as scripts**
kode dalam modul akan dieksekusi jika mengimpornya, tetapi dengan __name__ diatur ke "__main__". Kita dapat membuat berkas yang digunakan sebagai skrip dan juga modul yang dapat diimpor, karena kode yang mengurai parsing baris perintah hanya beroperasi jika modul dieksekusi sebagai berkas "main":

**6.1.2. The module search path**
modul bernama spam diimpor, interpreter pertama-tama mencari modul bawaan dengan nama itu. Jika tidak ditemukan, ia kemudian mencari berkas bernama spam.py dalam daftar direktori yang diberikan oleh variabel sys.path. sys.path diinisialisasi dari lokasi ini:
•	Direktori yang berisi skrip masukan (atau direktori saat ini ketika tidak ada file ditentukan).
•	PYTHONPATH (daftar nama direktori, dengan sintaksis yang sama dengan variabel shell PATH).
•	The installation-dependent default (by convention including a site-packages directory, handled by the site module).

**6.1.3. “Compiled” Python files**
Dalam program Python untuk menyimpan cache versi terkompilasi dari setiap modul di direktori __pycache__ dengan nama module. version.pyc. Python tidak memeriksa cache dalam dua keadaan. Pertama, selalu mengkompilasi ulang dan tidak menyimpan hasil untuk modul yang dimuat langsung dari baris perintah. Kedua, itu tidak memeriksa cache jika tidak ada modul sumber. 

**6.2. standard modules**
Satu modul tertentu patut mendapat perhatian: sys, yang dibangun ke dalam setiap interpreter Python. Variabel sys.ps1 dan sys.ps2 menentukan string yang digunakan sebagai prompt primer dan sekunder

**6.3. The dir() function**
Fungsi bawaan dir() digunakan untuk mencari tahu nama-nama yang ditentukan oleh modul.


**6.4. Packages**
Packages adalah cara untuk penataan namespace modul Python dengan menggunakan "dotted module names". Sebagai contoh, nama modul A.B menetapkan submodule bernama B dalam sebuah paket bernama A. 

**6.4.1. Importing * From a Package**
Yang terjadi jika pengguna manulis from sound.effects import *, menemukan submodul mana yang ada dalam paket, dan mengimpor semuanya. Ini bisa memakan waktu lama dan mengimpor submodul mungkin memiliki efek samping yang tidak diinginkan yang seharusnya hanya terjadi ketika submodul diimpor secara eksplisit. Pernyataan import menggunakan konvensi berikut: jika suatu paket punya kode __init __.py yang mendefinisikan daftar bernama __all__, itu diambil sebagai daftar nama modul yang harus diimpor ketika from package import * ditemukan. 

**6.4.2. Inter-package Reference**
impor absolut untuk merujuk pada submodul paket saudara kandung. Misalnya, jika modul sound.filters.vocoder perlu menggunakan modul echo dalam paket sound.effects. 

**6.4.3. Packages in Multiple Directories**
Packages mendukung satu atribut khusus  yaitu  __path__. ni diinisialisasi menjadi daftar yang berisi nama direktori yang menyimpan file paket: __init__.py sebelum kode dalam file tersebut dieksekusi. Variabel ini dapat dimodifikasi; hal itu memengaruhi pencarian modul dan subpackage di masa depan yang terkandung dalam paket.
