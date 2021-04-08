with open("out") as o:
    out = o.readlines()

for i in "123456": # 1だった
    flag = [o[11:-1] for i,o in enumerate(out) if i%3==2][::-1]
    print(i)
    flag = "0" + flag[0] + i + "".join(flag[1:])
    print(flag, len(flag))
    flag = bytes.fromhex(flag) 
    print(flag[::-1])