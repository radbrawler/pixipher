import hashlib

from PIL import Image

import imageHandler


class Encryption:
    def __init__(self, filename, window=None, outfile="out.png", key="image_encryption".encode('utf-8'), iteration=1):
        self.filename = filename
        self.key = hashlib.sha256(key).digest()
        # print("File opened for encryption is ", self.filename)
        if outfile != "out.png":
            self.outfile = outfile
        else:
            self.outfile = self.filename
        self.iteration = iteration
        self.window = window

    def encrypt_file(self):
        try:
            if self.window:
                self.window.update_status_bar("Encrypting Image")
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

                for i in range(1):
                    # print(i)
                    lambda: self.scrambler(im2, im2.size, im2.mode)
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

                if self.window:
                    imageHandler.ImageHandler(self.window).showImage(self.outfile, 390, 40)

            elif image.mode == 'RGB':
                im_rgb = image.crop((0, 0, image.size[0], image.size[1]))
                hist = im_rgb.histogram()
                # print("Original image histogram ", hist)
                # im_rgb.show()
                for i in range(1):
                    # print(i)
                    red, green, blue = self.scrambler(im_rgb, im_rgb.size, im_rgb.mode)
                    im_rgb = Image.merge(im_rgb.mode, [red, green, blue])

                im_rgb.save(self.outfile, 'png')
                # print(type(im_rgb))
                # im_rgb.show()
                hist = im_rgb.histogram()
                # print("Scrambled image histogram", hist)

                # img = cv2.imread(self.outfile, 0)
                # plt.hist(img.ravel(), 256, [0, 256])
                # plt.show()

                if self.window:
                    imageHandler.ImageHandler(self.window).showImage(self.outfile, 390, 40)

            else:
                print("Image is neither \'L\' or \'RGB\'")

            if self.window:
                self.window.update_status_bar("Encryption Done")

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

                q = 3.75

                def h(l): return q*l*(1-l)
                temp_ki = [None]*(size[0]*size[1]+1)
                print(size[0]*size[1] + 1)
                ki = [None]*size[0]*size[1]
                temp_ki[0] = 0.46

                for m in range(self.iteration):
                    # print(m)
                    for x in range(size[0]):
                        for y in range(size[1]):
                            xn = (x+y) % size[0]
                            yn = ((2*x)+(3*y)) % size[1]

                            temp_ki[x*size[0] + y + 1] = h(temp_ki[x*size[0] + y])
                            ki[x*size[0] + y] = int(((10 ** 14)*temp_ki[x*size[0] + y]) % 256)

                            list2[x, y] = (list1[xn, yn] ^ ki[x*size[0] + y]) % 256

                    list1 = list2

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

                q = 3.75

                def h(l): return q*l*(1-l)
                temp_ki = [None]*(size[0]*size[1]+1)
                print(size[0]*size[1] + 1)
                ki = [None]*size[0]*size[1]
                temp_ki[0] = 0.46

                for m in range(self.iteration):
                    # print(m)
                    for x in range(size[0]):
                        for y in range(size[1]):
                            xn = ((2*x)+y) % size[0]
                            yn = (x+y) % size[1]
                            # print(x*size[0] + y + 1)
                            temp_ki[x*size[0] + y + 1] = h(temp_ki[x*size[0] + y])
                            ki[x*size[0] + y] = int(((10 ** 14)*temp_ki[x*size[0] + y]) % 256)
                            # ki[x*size[0] + y] = int(os.urandom(1))

                            r1[x, y] = (r[xn, yn] ^ ki[x*size[0]+y]) % 256
                            g1[x, y] = (g[xn, yn] ^ ki[x*size[0]+y]) % 256
                            b1[x, y] = (b[xn, yn] ^ ki[x*size[0]+y]) % 256

                    # for x in range(size[0]):
                    #     for y in range(size[1]):
                    #         xn = (x-y) % size[0]
                    #         yn = ((2*y) - x) % size[1]
                    #         r1[x, y] = r[xn, yn]
                    #         g1[x, y] = g[xn, yn]
                    #         b1[x, y] = b[xn, yn]

                    r = r1
                    g = g1
                    b = b1
                    # print("Scrambling Done")
                    # print(r1[10, 10], r[10, 10])

                for t in range(100):
                    print(ki[t])

                return red1, green1, blue1

            except SystemError:
                print("Image is probably neither grey scale nor 3-channel")


if __name__ == '__main__':

    for i in range(1):
        print(i)
        file = '/home/anmol/PycharmProjects/pixipher/output4/lena_color.png'
        file2 = '/home/anmol/PycharmProjects/pixipher/output4/output2.png'
        # print(file, file2)
        Encryption(file, outfile=file2, iteration=1).encrypt_file()

    # a = bitstring.BitArray(bin='00000100')
    #
    # print(9^5)