import random
import secrets
import math
from decimal import Decimal, getcontext
from Crypto.Cipher import AES
from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes


getcontext().prec = 500
#          340282366920938463463374607431768211456
kb1, ic1 = 45702021340126875800050711292004769456.2582161398, 310206344424042763368205389299416142157.00357571144
kb2, ic2 = 55221733168602409780894163074078708423.359152279, 347884965613808962474866448418347671739.70270575362
kb3, ic3 = 14782966793385517905459300160069667177.5906950984, 340240003941651543345074540559426291101.69490484699
enc = 0x838371cd89ad72662eea41f79cb481c9bb5d6fa33a6808ce954441a2990261decadf3c62221d4df514841e18c0b47a76

BOUND = 2 ** 128
MULT = 10 ** 10

kb1, kb2, kb3 = Decimal(kb1),Decimal(kb2),Decimal(kb3)
ic1, ic2, ic3 = Decimal(ic1),Decimal(ic2),Decimal(ic3)
p, q = int((kb1+kb2+kb3)/3), int((ic1+ic2+ic3)/3)
p, q = Decimal(p), Decimal(q)
xs = [kb1, kb2, kb3]
ys = [ic1, ic2, ic3]

"""
def update_bmax_x(p,q, digit):
    dist = [((x-p)*(x-p)+(y-q)*(y-q)).sqrt() for x,y in zip(xs,ys)]
    argmax = -1
    if max(dist) == dist[0]:
        argmax = 0
    elif max(dist) == dist[1]:
        argmax = 1
    elif max(dist) == dist[2]:
        argmax = 2

    mx, my = xs[argmax]-p, ys[argmax]-q
    ddx = int(mx) // abs(int(mx))
    ddy = int(my) // abs(int(my))
    dx, dy = (2**digit)*ddx, (2**digit)*ddy
    print(dx, dy)
    return p+dx, q+dy

def update_bmin(p,q, digit):
    dist = [((x-p)*(x-p)+(y-q)*(y-q)).sqrt() for x,y in zip(xs,ys)]
    argmin = -1
    if min(dist) == dist[0]:
        argmin = 0
    elif min(dist) == dist[1]:
        argmin = 1
    elif min(dist) == dist[2]:
        argmin = 2

    mx, my = xs[argmin]-p, ys[argmin]-q
    mx = int(mx) // abs(int(mx))
    my = int(my) // abs(int(my))
    dx, dy = -(2**digit)*mx, -(2**digit)*my
    print(dx, dy)
    return p+dx, q+dy
"""

def argmin(l):
    m = min(l)
    for i in range(len(l)):
        if l[i] == m:
            return i

def energy(p,q):
    dist = [Decimal((x-p)*(x-p)+(y-q)*(y-q)).sqrt() for x,y in zip(xs,ys)]
    dist = [int(i) for i in dist]
    return abs(dist[0]-dist[1]) + abs(dist[1]-dist[2]) + abs(dist[2]-dist[0])

def update(p,q,digit):
    dis = 2**digit
    dx, dy = [1,0,-1], [1,0,-1]
    energies = [int(energy(p+dis*x, q+dis*y)) for x in dx for y in dy]
    argm = argmin(energies)
    #print(energies, argm)
    return p+dis*dx[argm//3], q+dis*dy[argm%3]

def learn(p,q):
    for dig in range(126, -1, -1):
        #print(dig)
        for _ in range(2):
            p,q = update(p,q,dig)
        #print(p,q)
    return p,q

p,q = learn(p,q)
p,q = abs(int(p)), abs(int(q))
dist = [Decimal((x-p)*(x-p)+(y-q)*(y-q)).sqrt() for x,y in zip(xs,ys)]
#print(dist)
key, iv = int(p), int(q)
print(key, iv)

#print(BOUND)
#print(int((kb1+kb2+kb3)/3), int((ic1+ic2+ic3)/3))
#print(long_to_bytes(key), long_to_bytes(iv))

for p in range(-10000000,10000000,1):
    cipher = AES.new(long_to_bytes(key+p), AES.MODE_CBC, iv=long_to_bytes(iv))
    dec = cipher.decrypt(long_to_bytes(enc))
    if all([b==b"\x00" or b<0x80 for b in dec[16:]]):
        print(dec)