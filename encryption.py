import hashlib

from PIL import Image


class Encryption:
    def __init__(self, filename, key="image_encryption".encode('utf-8')):
        self.filename = filename
        self.key = hashlib.sha256(key).digest()
        print("File opened for encryption is ", self.filename)
        self.outfile = self.filename

    def encryption(self):
        try:
            image = Image.open(self.filename)
            image_out = Image.new(image.mode, image.size, None)
            pixels = image.load()
            image.show()
            print(type(pixels))

            for i in range(image.size[0]):
                for j in range(image.size[1]):
                    # print(i, j, end='')
                    pixels[i, j] = (256-pixels[i, j]) % 256
                    # print(pixels)
                # print(i)

            image_out.paste(pixels)
            image.save(self.outfile, 'png')
            image.show()
        except FileNotFoundError:
            print("File Name not Found")
