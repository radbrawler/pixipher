import hashlib
import random
import struct
import os

from Crypto.Cipher import AES


class Encryption:
    def __init__(self, filename, key="image_encryption".encode('utf-8')):
        self.filename = filename
        self.key = hashlib.sha256(key).digest()

    def encryption(self):

        try:
            out_file = self.filename
            iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
            print(len(iv))
            encryptor = AES.new(self.key, AES.MODE_CBC, '0000000000000001')
            filesize = os.path.getsize(self.filename)
            chunksize = 64*1024

            with open(self.filename, 'rb') as infile:
                with open(out_file, 'wb') as outfile:
                    outfile.write(struct.pack('<Q', filesize))
                    outfile.write(iv)

                    while True:
                        chunk = infile.read(chunksize)
                        if chunk is True:
                            break
                        elif len(chunk) % 16 != 0:
                            chunk += ' ' *(16 - len(chunk)%16)

                        outfile.write(encryptor.encrypt(chunk))
        except FileNotFoundError:
            print("File Name not Found")