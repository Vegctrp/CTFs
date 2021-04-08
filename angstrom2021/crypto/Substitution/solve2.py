from functools import reduce
from pwn import * # pip install pwntools
from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes
import binascii
import pickle

#with open("pairs.bin", 'rb') as p:
#    pairs = pickle.load(p)
r = remote('crypto.2021.chall.actf.co', 21601)
pairs = []
r.recv()
for i in range(2,100):
    r.sendline(str(i))
    ret = int(str(r.recv())[5:-5])
    pairs.append((i, ret))

for length in range(5,50,1):
    matrix = []
    y = []
    for p in pairs[2:2+length]:
        y.append(p[1]%691)
        matrix.append([p[0]**i%691 for i in range(length)])

    for i in range(length):
        y[i] = y[i] * inverse(matrix[i][i], 691) % 691
        inv = inverse(matrix[i][i], 691)
        for j in range(length):
            matrix[i][j] = matrix[i][j] * inv % 691
        for j in range(length):
            if j != i:
                tm = matrix[j][i]
                y[j] = (y[j] - y[i] * tm) % 691
                for k in range(length):
                    matrix[j][k] = (matrix[j][k] - matrix[i][k] * tm) % 691

    if all([0<i and i<128 for i in y]):
        print("".join([chr(i) for i in y][::-1]))
