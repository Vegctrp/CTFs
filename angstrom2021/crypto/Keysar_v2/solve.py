import string

with open("out", "r") as f:
    out = f.read()


stdalph = string.ascii_lowercase
rkey = "qsuvwxyzb+airmt++cdfg+k+o+"
########abcdefghijklmnopqrstuvwxyz

enc = ""
for a in out:
    if a in rkey:
        enc += stdalph[rkey.index(a)]
    elif a in stdalph:
        enc += "_"
    else:
        enc += a

print(enc)