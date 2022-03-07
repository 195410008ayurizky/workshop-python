#kode dalam modul akan dieksekusi, sama seperti if Anda mengimpornya, tetapi dengan __name__ diatur ke "__main__"
if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))

#jika modul dieksekusi sebagai berkas "main":
python fibo.py 50

