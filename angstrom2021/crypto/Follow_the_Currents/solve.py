import os
import zlib
from Crypto.Util.number import long_to_bytes
def keystream(num):
	key = num
	index = 0
	while 1:
		index+=1
		if index >= len(key):
			key += zlib.crc32(key).to_bytes(4,'big')
		yield key[index]

with open("enc","rb") as f:
	enc = f.read()
print(enc)


for i in range(1<<16):
    k = keystream(long_to_bytes(i))
    plaintext = []
    for i in enc:
        plaintext.append(i ^ next(k))
    plaintext = "".join([chr(x) for x in plaintext])
    if "actf{" in plaintext:
        print(plaintext)
