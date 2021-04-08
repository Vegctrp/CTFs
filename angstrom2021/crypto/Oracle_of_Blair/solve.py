from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
from pwn import * # pip install pwntools
from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes

r = remote('crypto.2021.chall.actf.co', 21112)

r.recv()
def get(hexstr):
    r.sendline(hexstr)
    x = r.recv()
    x = str(x)[2:].split("\\")[0]
    return x

print(get("000000000000000000000000000000007B7D"))

base = get("7B7D")
for i in range(1,50):
    req = get("00"*i + "7B7D")
    print(req)
    if len(base) < len(req):
        print(i)
        print("flag length:", 32-i+1)
        flag_length = 32-i+1
        break

flag = "61637466"
for i in range(flag_length-4):
    header_length = (64-len(flag)//2-1)%16
    flag_f = "00"*16 + "00"*header_length + "7B7D" + "00"*(48-header_length-flag_length)
    #print(len(flag_f), flag_f)
    for i in range(41,128):
        flag_g = "00"*16 + "00"*header_length + flag + format(i, "02x") + "00"*(48-header_length-len(flag)//2-1)
        flag_h = flag_f + flag_g
        req = get(flag_h)
        if len(flag)<32:
            correct = req[32:64]
            if correct == req[32+128:64+128]:
                print(i, chr(i))
                flag += format(i, "02x")
                break
        else:
            correct = req[64:96]
            if correct == req[64+128:96+128]:
                print(i, chr(i))
                flag += format(i, "02x")
                break
    print(flag, long_to_bytes(int(flag, 16)))

"""
for k in range(1<<32):
    if k%(1<<16)==0:
        print("k:", k//(1<<16))
    key = long_to_bytes(k)
    key = b"\x00"*(32-len(key)) + key
    hoge = AES.new(key, AES.MODE_CBC, iv=b"\x00"*16).encrypt(c1+c2)
    if b"actf{" in hoge:
        print(hoge)
        break
"""