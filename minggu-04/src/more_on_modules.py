#pernyataan import yang mengimpor nama dari modul 
# langsung ke tabel simbol modul impor
from fibo import fib, fib2
fib(500)

#ada varian untuk mengimpor 
# semua nama yang didefinisikan oleh modul:
from fibo import *
fib(500)

#Jika nama modul diikuti oleh as, 
# maka nama setelah as terikat langsung ke modul yang diimpor.
import fibo as fib
fib.fib(500)

#menggunakan from
from fibo import fib as fibonacci
fibonacci(500)