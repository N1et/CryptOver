from Crypto.Protocol.KDF import PBKDF2
from Crypto.PublicKey import RSA
from getpass import getpass
from hashlib import sha256 as sha
import sys
stdout = sys.stdout
sys.stdout = sys.stderr
keych = 0
if len(sys.argv) != 1 and sys.argv[1] == "Private_key":
    keych = 1
password = getpass("Password: ")
salt = sha(password).hexdigest()
master_key = PBKDF2(password, salt, count=10000)
def my_rand(n):
    my_rand.counter += 1
    return PBKDF2(master_key, "my_rand:%d" % my_rand.counter, dkLen=n, count=1)

my_rand.counter = 0
print "Gerando chave..."
key = RSA.generate(2048, randfunc=my_rand)
if keych == 1:
    dkey = key.export_key()
    dkey_hash = sha(dkey).hexdigest()
else:
    dkey = key.publickey().exportKey()
    dkey_hash = sha(dkey).hexdigest()

print >> stdout, dkey
print "SHA256: "+dkey_hash
