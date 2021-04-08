from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes
from random import getrandbits
from math import gcd

c = 0xae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c
c = long_to_bytes(c)

for i in range(len(c)-5):
    flaghead = c[i:i+5]
    #print(flaghead, type(flaghead), len(flaghead))
    #print(b"actf{", type(b"actf{"), len(b"actf{"))
    #key = [bytes(a^b) for a,b in zip(flaghead, b"actf{")]
    key = [a^b for a,b in zip(flaghead, b"actf{")]
    #print(key)
    #print(bytes(key))
    key = key*27
    key = key[5-i%5:]
    d = [a^b for a,b in zip(c, key[:len(c)])]
    print(bytes(d))