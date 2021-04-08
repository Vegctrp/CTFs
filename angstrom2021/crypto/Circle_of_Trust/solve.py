import random
import secrets
import math
from decimal import Decimal, getcontext
from Crypto.Cipher import AES
from Crypto.Util.number import getPrime, bytes_to_long, inverse, long_to_bytes
kb1, ic1 = 45702021340126875800050711292004769456.2582161398, 310206344424042763368205389299416142157.00357571144
kb2, ic2 = 55221733168602409780894163074078708423.359152279, 347884965613808962474866448418347671739.70270575362
kb3, ic3 = 14782966793385517905459300160069667177.5906950984, 340240003941651543345074540559426291101.69490484699
enc = 0x838371cd89ad72662eea41f79cb481c9bb5d6fa33a6808ce954441a2990261decadf3c62221d4df514841e18c0b47a76

getcontext().prec = 500

kb1, kb2, kb3 = Decimal(kb1),Decimal(kb2),Decimal(kb3)
ic1, ic2, ic3 = Decimal(ic1),Decimal(ic2),Decimal(ic3)
b13 = kb1-kb3
b21 = kb2-kb1
b32 = kb3-kb2
c13 = ic1-ic3
c21 = ic2-ic1
c32 = ic3-ic2

x1 = b13*c21 - b21*c13
#x2 = -c32*(c13*c21+b13*b21)
#print(x1, x2)
q = ((c13*c21+b13*b21)/x1)*(-c32)
#q = x2/x1
print(q)
b3 = int((q+b32)/2)
print(b3)

p = -q * b32 / c32
print(p)
c3 = int((p+c32)/2)
print(c3)

key, iv = int(kb3-b3), int(ic3-c3)

for p in range(-10000000,10000000,1):
    #for q in range(-1000,1000,1):
    #cipher = AES.new(long_to_bytes(key+p), AES.MODE_CBC, iv=long_to_bytes(iv+q))
    cipher = AES.new(long_to_bytes(key+p), AES.MODE_CBC, iv=long_to_bytes(iv))
    dec = cipher.decrypt(long_to_bytes(enc))
    if dec[-5:]==b"\x00"*5:
        print(dec)