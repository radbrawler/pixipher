import hashlib

import numpy as np
from PIL import Image
import bitstring

import imageHandler


class Encryption:
    def __init__(self, filename, window,outfile="out.png", key="image_encryption".encode('utf-8'), iteration=10):
        self.filename = filename
        self.key = hashlib.sha256(key).digest()
        # print("File opened for encryption is ", self.filename)
        if outfile == "out.png":
            self.outfile = self.filename + ".enc"
        else:
            self.outfile = self.filename
        self.iteration = iteration
        self.window = window

    def encrypt_file(self):
        try:
            print("outfile is ", self.outfile)
            image = Image.open(self.filename)
            image_out = Image.new(image.mode, image.size, None)

            if image.mode == 'L':
                im2 = image.crop((0, 0, image.size[0], image.size[1]))
                # pixels = im2.load()
                # print("Here ", pixels)
                # image.show()
                # print(type(pixels))  # pixel <class 'PixelAccess'>

                # for k in range(4, 5):
                #     for j in range(im2.size[1]):
                #         print('{0:3d}'.format(pixels[k, j]), end=' ')
                #     print(end='\n')

                for i in range(self.iteration):
                    print(i)
                    im2 = self.scrambler(im2, im2.size, im2.mode)
                    # print(pixels)

                    # image_out.paste(pixels)

                # print("############################################################")
                # time.sleep(4)
                # for k in range(4, 5):
                #     for j in range(im2.size[1]):
                #         print('{0:3d}'.format(pixels[k, j]), end=' ')
                #     print(end='\n')

                im2.save(self.outfile, 'png')
                # im2.show()
                print("After show")
                imageHandler.ImageHandler(self.window).showImage(self.outfile, 350, 10)

            elif image.mode == 'RGB':
                im_rgb = image.crop((0, 0, image.size[0], image.size[1]))
                hist = im_rgb.histogram()
                # print("Original image histogram ", hist)
                # im_rgb.show()
                for i in range(self.iteration):
                    print(i)
                    red, green, blue = self.scrambler(im_rgb, im_rgb.size, im_rgb.mode)
                    im_rgb = Image.merge(im_rgb.mode, [red, green, blue])

                im_rgb.save(self.outfile, 'png')
                # print(type(im_rgb))
                # im_rgb.show()
                hist = im_rgb.histogram()
                # print("Scrambled image histogram", hist)
                imageHandler.ImageHandler(self.window).showImage(self.outfile, 350, 10)

            else:
                print("Image is neither \'L\' or \'RGB\'")

        except IOError as e:
            print("File Name not Found", e)

    def scrambler(self, c_image, size, mode):  # c_image->cropped image

        # c_image_new = Image.new(c_image.mode, c_image.size, None)
        # list2 = c_image_new.load()
        # print("list is ", type(list2))

        if mode == 'L':
            try:
                list1 = c_image.load()
                c_image_new = Image.new(c_image.mode, c_image.size, None)
                list2 = c_image_new.load()
                for x in range(size[0]):
                    for y in range(size[1]):
                        xn = (x+y) % size[0]
                        yn = ((2*x)+(3*y)) % size[1]
                        list2[x, y] = list1[xn, yn]

                # print(list2[x, y], list1[x, y])
                # for k in range(4, 5):
                #     for j in range(c_image.size[1]):
                #         print('{0:3d}'.format(list2[k, j]), end=' ')
                #     print(end='\n')

                return c_image_new

            except TypeError:
                print("Caught TypeError !! Image may be 3-channel")

        elif mode == 'RGB':
            try:
                red, green, blue = c_image.split()
                r = red.load()
                g = green.load()
                b = blue.load()
                c_image_new = Image.new(c_image.mode, c_image.size, None)
                red1, green1, blue1 = c_image_new.split()
                r1 = red1.load()
                g1 = green1.load()
                b1 = blue1.load()

                for x in range(size[0]):
                    for y in range(size[1]):
                        xn = ((2*x)+y) % size[0]
                        yn = (x+y) % size[1]
                        r1[x, y] = r[xn, yn]
                        g1[x, y] = g[xn, yn]
                        b1[x, y] = b[xn, yn]

                return red1, green1, blue1

            except SystemError:
                print("Image is probably neither grey scale nor 3-channel")

    def key_encryption(self, image, key):
        w = 0.72
        g = lambda x: w*x*(1-x)
        p = 8
        x = np.zeros(1, p)
        y = np.zeros(1, p)


        x[0] = 0.35
        x[0] = 0.43

        for i in range(p):
            x[i+1] = g[x[i]]
            y[i+1] = g[y[i]]

        # for j in range(p*8):


if __name__ == '__main__':

    # for i in range(1):
    #     print(i)
    #     file = '/home/anmol/PycharmProjects/pixipher/output3/lena'+str(i)+'.png'
    #     file2 = '/home/anmol/PycharmProjects/pixipher/output3/lena'+str(i+1)+'.png'
    #     # print(file, file2)
    #     Encryption(file, outfile=file2, iteration=1).encrypt_file()

    a = bitstring.BitArray(bin='1010')
    print(a)
