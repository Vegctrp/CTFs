from functools import reduce
from pwn import * # pip install pwntools
from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes
import binascii
import pickle

r = remote('crypto.2021.chall.actf.co', 21601, level = 'debug')

#key = [1,2,3]
#value = 2

#def substitute(value):
#    return (reduce(lambda x, y: x*value+y, key))%691
#print(substitute(value))

# 600 -> 418

pairs = []
print(r.recv())
for i in range(691):
    r.sendline(str(i))
    ret = int(str(r.recv())[5:-5])
    #print(ret)
    pairs.append((i, ret))

with open("pairs.bin", "wb") as out:
    pickle.dump(pairs, out)