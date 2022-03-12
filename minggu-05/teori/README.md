# BAB 7 Input and Output

** 7.1. Fancier Output Formatting **
Ada dua cara penulisan output yang lebih menarik yaitu expression statements dan fungsi print(). Adapun cara ke tiga dengan write metode objek bekas  standar keluaran dapat dirujuk sebagai sys.stdout. 

Format output:
-> Formatted string literals
Untuk memulai string dengan f atau F sebelum tanda kutip pembuka atau tandakutip tiga. Menulis ekspresi Python karakter { dan } yang dapat merujuk ke variabel atau nilai literal.
Contoh : f’Results of the {year} {event}

-> Metode str.format() 
Masih menggunakan { dan } untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi Anda juga harus memberikan informasi yang akan diformat.
Contoh : ‘{:-9} YES votes {:2.2%}’.format(yes_votes, percentage)

-> Manual String Formatting
Metode str.rjust() dari objek string merata-kanan-kan sebuah string dalam bidang dengan lebar tertentu dengan menambahkannya dengan spasi di sebelah kiri. Ada metode serupa str.ljust() dan str.center(). Metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Ada metode lain, str.zfill(), yang melapisi string numerik di sebelah kiri dengan nol. Itu mengerti tentang tanda plus dan minus
Contoh : ‘12’.zfill(5)

-> Old string formatting
Operator % (modulo) juga dapat digunakan untuk pemformatan string. Diberikan 'string' % values, instansiasi dari % in string diganti dengan nol atau elemen yang lebih dari values. Operasi ini umumnya dikenal sebagai interpolasi string.

**7.2. Reading and Writing Files**
open() mengembalikan sebuah file object, dan paling umum digunakan dengan dua argumen: open(filename, mode). 

-> Methods of File Objects
Untuk membaca konten file, panggil f.read(size), yang membaca sejumlah kuantitas data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). size adalah argumen numerik opsional. f.readline() membaca satu baris dari file; karakter baris baru (\n) dibiarkan di akhir string, dan hanya dihapus pada baris terakhir file jika file tidak berakhir pada baris baru. Fungsi f.write(string) menulis konten string ke berkas, mengembalikan jumlah karakter yang ditulis. f.tell() mengembalikan integer yang memberikan posisi objek file saat ini dalam berkas yang direpresentasikan sebagai jumlah byte dari awal berkas ketika dalam mode biner dan angka buram opaque ketika dalam mode teks.

-> Saving structured data with json
Format JSON umumnya digunakan oleh aplikasi modern untuk memungkinkan pertukaran data. Banyak programmer sudah terbiasa dengannya, yang membuatnya menjadi pilihan yang baik untuk interoperabilitas.
Contoh : import json
