
# BAB 8 Errors and Exceptions

## 8.1.Syntax Errors (Kesalahan Sintaksis)
Kesalahan pada sintaksis dikenal juga dengan kesalahan pengguraian parsing. 
```python
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                   ^
SyntaxError: invalid syntax
Parser Pengurai mengulangi baris yang menyinggung dan mengembalikan "arrow" kecil yang menunjuk ke titik paling awal di baris di mana kesalahan terdeteksi. Kesalahan disebabkan oleh (atau setidaknya terdeteksi) penanda di depan panah: pada contoh, kesalahan terdeteksi di fungsi print() karena kurangnya titik dua (':')) di depan dia. Cetak nama file dan nomor baris sehingga Anda tahu di mana mencarinya jika input berasal dari skrip.

 ## 8.2.Exceptions (Pengecualian)
Meski pernyataan atau ekspresi dari Python sudah Anda tulis dengan benar, ada kemungkinan terjadi kesalahan ketika perintah tersebut dieksekusi. Kesalahan yang terjadi saat proses sedang berlangsung disebut pengecualian (exceptions) dan akan berakibat fatal jika tidak ditangani. Kebanyakan pengecualian di Python tidak ditangani oleh aplikasi, sehingga aplikasi terhenti kemudian muncul pesan kesalahan.
```python
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
 Tipe dalam contoh adalah ZeroDivisionError, NameError dan TypeError. String yang dicetak sebagai jenis pengecualian adalah nama pengecualian bawaan yang terjadi. Ini berlaku untuk semua pengecualian bawaan, tetapi tidak harus sama untuk pengecualian yang dibuat pengguna (meskipun ini adalah konvensi yang bermanfaat). Nama pengecualian standar adalah pengidentifikasi bawaan (bukan kata kunci yang dipesan reserved keyword).

## 8.3	Handling Exceptions (Menangani Pengecualian)
Pada aplikasi Python yang Anda buat bisa dilengkapi dengan penanganan terhadap pengecualian (exceptions handling) dari kelompok (tipe) kesalahan yang Anda tentukan. Proses penanganan pengecualian menggunakan pernyataan try yang berpasangan dengan except. 

Pernyataan `try` berfungsi sebagai berikut.
  * Pertama, try clause (pernyataan(-pernyataan) di antara kata kunci `try` dan `except`) dieksekusi.
  * Jika tidak ada pengecualian terjadi, except clause dilewati dan eksekusi pernyataan :keyword: `try` selesai.
  * Jika pengecualian terjadi selama eksekusi klausa `try`, sisa klausa akan dilewati. Kemudian, jika tipenya cocok dengan pengecualian yang dinamai kata kunci `kecuali`, klausa kecuali dijalankan, dan kemudian eksekusi dilanjutkan setelah blok coba/kecuali.
  * Jika terjadi pengecualian yang tidak cocok dengan pengecualian yang disebutkan dalam klausa kecuali, hal tersebut diteruskan ke pernyataan percobaan luar; jika tidak ada penangan yang ditemukan, hal itu adalah pengecualian yang tidak tertangani dan eksekusi berhenti dengan pesan seperti yang ditunjukkan di atas.

Pernyataan `try` mungkin memiliki lebih dari satu klausa `kecuali`, untuk menentukan penanganan untuk pengecualian yang berbeda. Satu handler akan dieksekusi. Handler hanya menangani pengecualian yang terjadi di klausa try yang sesuai, bukan di handler lain dari pernyataan try yang sama. Klausa pengecualian dapat menyebutkan beberapa pengecualian sebagai tupel dalam kurung, misalnya:

```python
... except (RuntimeError, TypeError, NameError):
...     pass

Kelas dalam exceptklausa pengecualian kompatibel dengan pengecualian jika mereka adalah kelas yang sama atau kelas dasarnya (dan sebaliknya --- klausa pengecualian yang mencantumkan kelas turunan tidak kompatibel dengan kelas dasar). Misalnya, kode berikut akan mencetak B, C, D dalam urutan itu:
```python
class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
```

## 8.4.	Raising Exceptions (Memunculkan Pengecualian)
Dalam membuat aplikasi, ada kemungkinan Anda butuh untuk menghasilkan pengecualian (raise exceptions), salah satu caranya bisa dengan menggunakan pengecualian yang sudah ada, hanya ditambahkan informasi detailnya saja.
Pernyataan raise memungkinkan programmer untuk memaksa pengecualian yang ditentukan terjadi. Sebagai contoh:
```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: HiThere
```
Satu-satunya argumen untuk `raise` mewakili pengecualian yang dimunculkan. Itu harus berupa `instance` pengecualian (`Exception) atau kelas pengecualian (kelas yang diturunkan dari `Pengecualian`). Jika kelas pengecualian dilewatkan, itu akan secara implisit dipakai dengan memanggil konstruktornya `konstruktor` tanpa argumen:

```python
raise ValueError  # shorthand for 'raise ValueError()'
```
Jika perlu menentukan apakah pengecualian muncul tetapi tidak bermaksud menanganinya, bentuk yang lebih sederhana dari pernyataan raise memungkinkan kita untuk memunculkan kembali pengecualian:

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiThere
```

## 8.5. Rantai Pengecualian (Exception Chaining)
Pernyataan `raise` memungkinkan opsional yang memungkinkan pengecualian rantai. Sebagai contoh:

```python
# exc must be exception instance or None.
raise RuntimeError from exc
```

Hal ini dapat berguna saat kita mengubah pengecualian. Sebagai contoh:
```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
```

Rantai pengecualian terjadi secara otomatis ketika pengecualian dinaikkan di dalam bagian `except` atau `finally`. Ini dapat dinonaktifkan dengan menggunakan `dari None` idiom: from None

```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
... 
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError
```
## 8.6. Pengecualian yang Ditentukan Pengguna (User-defined Exceptions)
Program dapat memberi nama pengecualian mereka sendiri dengan membuat kelas pengecualian baru (lihat tut- class untuk informasi lebih lanjut tentang kelas Python). Pengecualian biasanya berasal dari kelas Exception, baik secara langsung atau tidak langsung.

Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk pengecualian.
Sebagian besar pengecualian didefinisikan dengan nama yang diakhiri dengan" Error", mirip dengan penamaan pengecualian standar.

Banyak modul standar menentukan pengecualian mereka sendiri untuk melaporkan kesalahan yang mungkin terjadi pada fungsi yang mereka tetapkan. Informasi lebih lanjut tentang kelas disajikan dalam bab tut- class.

## 8.7. Mendefinisikan Tindakan Pembersihan (Defining Clean-up Actions)
```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
```
Jika ada klausa `finally`, klausa untuk finally akan dijalankan sebagai tugas terakhir sebelum pernyataan untuk `try` selesai. Klausa untuk `finally` dapat berjalan baik atau tidak apabila pernyataan try menghasilkan suatu pengecualian. Poin-poin berikut membahas kasus yang lebih kompleks saat pengecualian terjadi:
   * Jika pengecualian terjadi selama eksekusi klausa untuk :keyword: `!try`, maka pengecualian tersebut dapat ditangani oleh klausa `except`. Jika pengecualian tidak ditangani oleh klausa :keyword: `!except`, maka pengecualian dimunculkan kembali setelah klausa `finally` dieksekusi.
   * Pengecualian dapat terjadi selama pelaksanaan klausa `except` atau `else`. Sekali lagi, pengecualian akan muncul kembali setelah klausa `finally` telah dieksekusi.
   * Jika klausa terakhir mengeksekusi pernyataan `break`, `continue`, atau `return`, eksepsi tidak dimunculkan kembali.
   * Jika pernyataan klausa untuk try mencapai klausa `break`, `continue` atau :keyword:` return` maka, pernyataan untuk klausa finally akan dieksekusi sebelum break, continue atau return dieksekusi.
   * Jika klausa untuk :keyword:`!finally` telah menyertakan pernyataan `return`, nilai yang dikembalikan akan menjadi salah satu dari pernyataan untuk finally dan dari klausa return, bukan nilai dari `try` pernayataan untuk return.

Contohnya:
```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in divide
TypeError: unsupported operand type(s) for /: 'str' and 'str'
```

Seperti yang kita lihat, klausa `finally` dieksekusi dalam peristiwa apa pun. `TypeError` yang ada dua string tidak ditangani oleh klausa `except` dan karenanya kembali muncul setelah klausa `finally` telah dieksekusi. Klausa `finally` berguna untuk melepaskan sumber daya `eksternal` (seperti berkas atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya tersebut berhasil. 
