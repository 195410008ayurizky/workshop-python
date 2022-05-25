# Installing Jupyter

## JupyterLab
1. Instal JupyterLab dengan pip:
`pip install jupyterlab`

Catatan : Jika Anda menginstal JupyterLab dengan conda atau mamba, sebaiknya gunakan saluran conda-forge .

2. Setelah terinstal, luncurkan JupyterLab dengan:
`jupyter-lab`

## Jupyter Notebook
1. Instal Notebook Jupyter klasik dengan:
`pip install notebook`

2. Untuk menjalankan buku catatan:
`jupyter notebook`

## Voila
`pip install voila`



# BAB 5 struktur data 

## 5.1 lebih lanjut tentang daftar lists
Berikut metode dari objek daftar list:
1. list.append(x) --> Tambahkan item ke akhir daftar list. Setara dengan a[len(a):] = [x].
2. list.extend(iterable) --> Perpanjang daftar list dengan menambahkan semua item dari iterable. Setara dengan a[len(a):] = iterable
3. list.insert(i, x) --> Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen sebelum memasukkan, jadi a.insert(0, x) memasukkan di bagian depan daftar list, dan a.insert(len(a), x) sama dengan a.append(x).
4. list.remove(x) --> Hapus item pertama dari daftar list yang nilainya sama dengan x. Ini memunculkan ValueError jika tidak ada item seperti itu.
5. list.pop([i]) --> Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan, a.pop() menghapus dan mengembalikan item terakhir dalam daftar. (Tanda kurung siku di sekitar i dalam pengenal signature metode menunjukkan bahwa parameternya opsional, bukan Anda harus mengetik tanda kurung siku pada posisi itu. Anda akan sering melihat notasi ini di Referensi Pustaka Python.)
6. list.clear() --> Hapus semua item dari daftar list. Setara dengan del a[:].
7. list.index(x[, start[, end]]) --> Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x. Menimbulkan ValueError jika tidak ada item seperti itu.
8. list.count(x) --> Kembalikan berapa kali x muncul dalam daftar.
9. list.sort(*, key=None, reverse=False) --> Urutkan item daftar di tempat (argumen dapat digunakan untuk mengurutkan ubahsuaian customization, lihat sorted() untuk penjelasannya).
10. list.reverse() --> Balikkan elemen daftar list di tempatnya.
11. list.copy() --> Kembalikan salinan daftar list yang dangkal. Setara dengan a[:].

## 5.1.1 menggunakan daftar lists sebagai tumpukan stacks
Metode daftar memudahkan untuk menggunakan daftar list sebagai tumpukan stack, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("last-in, first-out"). Untuk menambahkan item ke bagian atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit.

## 5.1.2 Menggunakan Daftar Lists sebagai Antrian Queue
Metode daftar memudahkan untuk menggunakan daftar antrian, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("first-in, first-out "). Untuk menambahkan item ke bagian atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop() tanpa indeks eksplisit.

## 5.1.3 daftar list comprehensions
Pemahaman daftar list comprehensions menyediakan cara singkat untuk membuat daftar. Pemahaman daftar list comprehension terdiri dari tanda kurung yang berisi ekspresi diikuti oleh klausa for, lalu nol atau lebih klausa for atau if. Hasilnya akan menjadi daftar baru yang dihasilkan dari mengevaluasi ekspresi dalam konteks dari klausa for dan if yang mengikutinya. 

## 5.2 pernyataan del
Peryataan  ‘def’ adalah kata kunci yang digunakan untuk mendefinisikan sebuah fungsi. Fungsi sendiri adalah kelompok kode yang dapat digunakan kembali di bagian program yang lain. Sebab Python adalah bahasa pemrograman multi-paradigma, dalam paradigma OOP (pemrograman berorientasi objek), kata kunci ‘def’ digunakan juga untuk mendefinisikan ‘method’ alias fungsi dalam sebuah ‘class’. 

## 5.3 tuples and urutan sequences
Operasi indexing and slicing operations adalah dua contoh tipe data sequence (lihat Sequence Types --- list, tuple, range). Karena python adalah bahasa yang berkembang, tipe data urutan lainnya dapat ditambahkan. Ada juga tipe data urutan standar lain: tuple. tuple sering digunakan dalam situasi yang berbeda dan untuk tujuan yang berbeda. Tuples adalah immutable, dan biasanya berisi urutan elemen yang heterogen yang diakses melalui unpacking (lihat nanti di bagian ini) atau pengindeksan (atau bahkan berdasarkan atribut dalam kasus namedtuples <collections.namedtuple> `). Daftar adalah :term:`mutable(), dan elemen-elemennya biasanya homogen dan diakses dengan menyusuri iterating daftar list.

## 5.4 himpunan set
Himpunan atau Set adalah koleksi yang tidak terurut tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Kurung kurawal atau fungsi set() dapat digunakan untuk membuat himpunan.

## 5.5  dictionaries
Operasi utama pada dictionary adalah menyimpan nilai dengan beberapa kunci key dan mengekstraksi nilai yang diberikan kunci key. Dimungkinkan juga untuk menghapus pasangan kunci:nilai dengan del. Jika Anda menyimpan menggunakan kunci yang sudah digunakan, nilai lama yang terkait dengan kunci itu dilupakan. 

## 5.6  looping techniques
* Fungsi items() digunakan untuk mengakses pasangan dari setiap elemen dan nilai-nya yang terdapat di dalam dicionary.
* Fungsi enumerate() mengembalikan nilai berupa objek enumerate. Objek enumerate sendiri merupakan objek iterable yang tiap itemnya berpasangan dengan indeks atau angka yang mewakilinya. Dengan kata lain fungsi ini akan menambahkan penghitung (indeks) ke objek iterable dan mengembalikannya.
* Math merupakan nodul bawaan dari python untuk memperluas daftar fungsi matematika. Setelah mengimpor math modul, anda dapat mulai menggunakan metode dan konstanta.
