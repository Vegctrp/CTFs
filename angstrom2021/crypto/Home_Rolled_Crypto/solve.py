from pwn import * # pip install pwntools
from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes
import binascii

r = remote('crypto.2021.chall.actf.co', 21602, level = 'debug')

print(r.recv())
r.sendline("1")
print(r.recv())
r.sendline("00"*16)
a = r.recv()
key1 = a[:32]

r.sendline("1")
print(r.recv())
r.sendline("ff"*16)
a = r.recv()
key2 = a[:32]
print(key1,key2)
key1 = binascii.unhexlify(str(key1)[2:-1].rjust(32, "0"))
key2 = binascii.unhexlify(str(key2)[2:-1].rjust(32, "0"))
print(key1,key2)
mask = bytes_to_long(key1) & bytes_to_long(key2)
bit = bytes_to_long(key1) ^ bytes_to_long(key2)
print(mask, hex(mask))
print(bit, hex(bit))

r.sendline("2")

for i in range(15):
    xxx = r.recv()
    plain = str(xxx)[16:-3]
    print(plain)
    ciphertext = ""
    for i in range(len(plain)//32):
        inp = int(plain[i*32:(i+1)*32], 16)
        ciph = ((inp & bit) ^ bit) + (mask)
        ciphertext += hex(ciph)[2:].rjust(32,"0")
    print("###", ciphertext)
    r.sendline(ciphertext)
    #print(r.recv())
print(r.recv())