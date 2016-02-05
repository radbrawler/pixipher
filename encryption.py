import hashlib

from PIL import Image
import numpy as np


class Encryption:
    def __init__(self, filename, key="image_encryption".encode('utf-8')):
        self.filename = filename
        self.key = hashlib.sha256(key).digest()
        print("File opened for encryption is ", self.filename)
        self.outfile = self.filename + '.enc'

    def encrypt_file(self):
        try:
            image = Image.open(self.filename)
            image_out = Image.new(image.mode, image.size, None)
            print(image.mode)

            if image.mode == 'L':
                im2 = image.crop((0, 0, 200, 200))
                im2.show()
                pixels = self.encrypter(im2, im2.size, image.mode)
                image_out.paste(pixels)
                im2.save(self.outfile, 'png')
                im2.show()

            elif image.mode == 'RGB':
                im_rgb = image.crop((0, 0, 100, 100))
                im_rgb.show()
                red, green, blue = self.encrypter(im_rgb, im_rgb.size, im_rgb.mode)
                print(type(im_rgb))
                im_rgb = Image.merge(im_rgb.mode, [red, green, blue])
                im_rgb.save(self.outfile, 'png')
                im_rgb.show()

            else:
                print("Image is neither \'L\' or \'RGB\'")

        except IOError as e:
            print("File Name not Found", e)

    def encrypter(self, c_image, size, mode):  # c_image->cropped image
        list1 = c_image.load()
        p, q = 1, 1
        arnold = ([1, p], [q, p*q+1])

        if mode == 'L':
            try:
                for x in range(size[0]):
                    for y in range(size[1]):
                        x2 = np.dot([x, y], arnold) % size[0]
                        list1[x, y] += 100

                return list1

            except TypeError:
                print("Caught TypeError !! Image may be 3-channel")

        elif mode == 'RGB':
            try:
                red1, green1, blue1 = red, green, blue = c_image.split()
                r = red.load()
                g = green.load()
                b = blue.load()
                r1 = red1.load()
                g1 = green1.load()
                b1 = blue1.load()

                for x in range(size[0]):
                    for y in range(size[1]):
                        x2 = np.dot([x+1, y+1], arnold) % size[0]
                        r1[x, y] = r[0, 0]
                        r1[x, y] = r[int(x2[0]), int(x2[1])]
                        g1[x, y] = g[int(x2[0]), int(x2[1])]
                        b1[x, y] = b[int(x2[0]), int(x2[1])]
                return red, green, blue

            except SystemError:
                print("Image is probably neither grey scale nor 3-channel")
            return list1


if __name__ == '__main__':
    file = '/home/anmol/PycharmProjects/pixipher/lena_color.png'
    Encryption(file).encrypt_file()
