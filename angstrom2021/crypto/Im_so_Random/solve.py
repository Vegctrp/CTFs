from pwn import * # pip install pwntools
from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes
import binascii

r = remote('crypto.2021.chall.actf.co', 21600)

print(r.recv())
r.sendline("r")
num1 = int(str(r.recv())[2:].split("\\")[0])
print(num1)

r.sendline("r")
num2 = int(str(r.recv())[2:].split("\\")[0])
print(num2)

print(num1*num1)

for i in range(10000000, 100000000):
    if num1 % i == 0:
        a1 = i
        a2 = num1 // i
        if num2 == (((a1*a1%10**12)//10000) * ((a2*a2%10**12)//10000)):
            break
assert(a1<=a2)

a1 = (a1*a1%10**12)//10000
a2 = (a2*a2%10**12)//10000

a1 = (a1*a1%10**12)//10000
a2 = (a2*a2%10**12)//10000

r.sendline("g")
r.sendline(str(a1*a2))
r.recv()
a1 = (a1*a1%10**12)//10000
a2 = (a2*a2%10**12)//10000
r.sendline(str(a1*a2))

print(r.recv())
print(r.recv())