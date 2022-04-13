import zlib
s = b'witch which has which witches wrist watch'
len(s)
#output
41
t = zlib.compress(s)
len(t)
37
zlib.decompress(t)
#output
b'witch which has which witches wrist watch'
zlib.crc32(s)
#output:
226805979