import os
from Crypto.Util.number import inverse, long_to_bytes

def fgen(rand1, rand2, s, f):
    v3 = s
    for v6 in range(0x300):
        v5 = v6 % 0x100
        v1 = rand1[v6 % len(rand1)] + v3 + f[v5]
        s = f[v1 % 0x100]
        f[s], f[v5] = f[v5], f[s]
        #print(v6, s, v1%0x100)
    
    for v6 in range(0x300):
        v5 = v6 % 0x100
        v1 = rand2[v6 % len(rand2)] + v3 + f[v5]
        s = f[v1 % 0x100]
        f[s], f[v5] = f[v5], f[s]
        #print(v6, s, v1%0x100)
    return s, f

def enc(xxx, s, f):
    out = [0] * len(xxx)
    for v6 in range(len(xxx)):
        v3 = v6 % 0x100
        v2 = f[v3] + s
        s = f[v2 % 0x100]
        f[v3], f[s] = f[s], f[v3]

        out[v6] = f[ (f[f[s]] + 1) % 0x100 ] ^ xxx[v6]
    return out

f = list(range(256))
s = 0

inp = "AAA"
flag = "actf{...}"
#xxx = inp + flag
xxx = long_to_bytes(0x1797d199b986bd9c9f93ea4155ab4d4415c0036269f82a1ce08144724a9d607dd9970434c2a745d1fb6165479a4083b261973d29f51735f3273a)
xxx = list(xxx)
out = [0] * len(xxx)


for x in range(1):
    rand2 = list(os.urandom(1))
    rand1 = list(os.urandom(len(xxx)))
    #s,f  = fgen(rand1, rand2, 0, f)
    for i in range(256):
        f = list(range(256))
        ans = [set([])]*256
        for _ in range(100):
            rand2 = list(os.urandom(1))
            rand1 = list(os.urandom(len(xxx)))
            _, ff = fgen(rand1, rand2, 0, f)
            for y in range(256):
                ans[y].add(ff[y])
        print(i, [len(p) for p in ans])
    #print(f)
    #print(f)
    #out = enc(xxx, s, f)
    #print("".join([chr(i) for i in out]))