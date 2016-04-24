import hashlib
import json
import tkinter as tk

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

                # plaintext = list()
                # plaintextstr = ""
                #
                # pix = im_rgb.load()
                #
                # width = im_rgb.size[0]
                # height = im_rgb.size[1]
                #
                # for y in range(0, height):
                #     for x in range(0, width):
                #         plaintext.append(pix[x, y])
                #
                # for i in range(len(plaintext)):
                #     for j in range(0, 3):
                #         plaintextstr += "%d" % (int(plaintext[i][j]) + 100)
                #
                # relength = len(plaintext)
                # # print("real length is " + str(relength))
                #
                # plaintextstr += "h"+str(height)+"h"+"w"+str(width)+"w"
                #
                # while len(plaintextstr) % 16 != 0:
                #     plaintextstr += "k"
                #
                # h = open("plain.txt", "w")
                # h.write(plaintextstr)
                #
                # password = str("anmol").encode('utf-8')
                # key = hashlib.sha256(password).digest()
                # obj = AES.new(key, AES.MODE_CBC, "This is an IV456")
                # ciphertext = obj.encrypt(plaintextstr)
                #
                # print(type(ciphertext))
                #
                # cipher_name = self.filename + ".crypt"
                # g = open(cipher_name, "wb")
                # g.write(ciphertext)
                # # print(ciphertext)
                #
                # # hexlify the ciphertext
                # asciicipher = str(binascii.hexlify(ciphertext))
                # # print(asciicipher)
                #
                # # replace function
                # def replace_all(text, dic):
                #     for i, j in dic.items():
                #         text = text.replace(i, j)
                #     return text
                #
                # # use replace function to replace ascii cipher characters with numbers
                # reps = {'a':'1', 'b':'2', 'c':'3', 'd':'4', 'e':'5', 'f':'6', 'g':'7', 'h':'8', 'i':'9', 'j':'10', 'k':'11', 'l':'12', 'm':'13', 'n':'14', 'o':'15', 'p':'16', 'q':'17', 'r':'18', 's':'19', 't':'20', 'u':'21', 'v':'22', 'w':'23', 'x':'24', 'y':'25', 'z':'26'}
                # asciiciphertxt = replace_all(asciicipher, reps)
                # # print(asciiciphertxt)
                #
                # # construct encrypted image
                # step = 3
                # encimageone=[asciiciphertxt[i:i+step] for i in range(0, len(asciiciphertxt), step)]
                # # if the last pixel RGB value is less than 3-digits, add a digit a 1
                # print(encimageone[len(encimageone)-1], len(encimageone)-1)
                # if int(encimageone[len(encimageone)-1]) < 100:
                #     encimageone[len(encimageone)-1] += "1"
                # # check to see if we can divide the string into partitions of 3 digits.  if not, fill in with some garbage RGB values
                # if len(encimageone) % 3 != 0:
                #     while (len(encimageone) % 3 != 0):
                #         encimageone.append("101")
                #
                # encimagetwo=[(int(encimageone[int(i)]),int(encimageone[int(i+1)]),int(encimageone[int(i+2)])) for i in range(0, len(encimageone), step)]
                #
                # # make sizes of images equal
                # while (int(relength) != len(encimagetwo)):
                #     encimagetwo.pop()
                #
                # # encrypted image
                # encim = Image.new("RGB", (int(width),int(height)))
                # encim.putdata(encimagetwo)
                # encim.show()


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

                q = 3.75  # One of the parameter

                def h(l): return q*l*(1-l)
                temp_ki = [None]*(size[0]*size[1]+1)
                print(size[0]*size[1] + 1)
                ki = [None]*size[0]*size[1]

                # Encryption parameter
                temp_ki[0] = 0.46
                a = 1
                b = 2

                for m in range(self.iteration):
                    # print(m)
                    for x in range(size[0]):
                        for y in range(size[1]):
                            xn = (x+(a*y)) % size[0]
                            yn = ((b*x)+(((a*b) + 1)*y)) % size[1]

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

                # Asking encryption Parameters before Encryption
                read_file = open("config.json", "r", encoding='utf-8')
                parameters = json.load(read_file)  # parameters is a dict variable
                read_file.close()

                pop_up = tk.Toplevel()
                pop_up.title("Encryption Parameters")
                border = 3
                label1 = tk.Label(pop_up, text="Parameter (q)")
                p_arnold = tk.Entry(pop_up, bd=border)
                p_arnold.insert(0, str(parameters["parameter_arnold"]))

                label2 = tk.Label(pop_up, text="System Initial Value (w)")
                p_temp_ki = tk.Entry(pop_up, bd=border)
                p_temp_ki.insert(0, parameters["parameter_temp_ki"])

                label3 = tk.Label(pop_up, text="Arnold Map Value (a)")
                p_u = tk.Entry(pop_up, bd=border)
                p_u.insert(0, parameters["parameter_u"])

                label4 = tk.Label(pop_up, text="Arnold Map Value (b)")
                p_v = tk.Entry(pop_up, bd=border)
                p_v.insert(0, parameters["parameter_v"])

                def get_parameters():

                    print(" In get param ")

                    param_dict = {"parameter_v": p_v.get(), "parameter_u": p_u.get(),
                                  "parameter_arnold": p_arnold.get(), "parameter_temp_ki": p_temp_ki.get()}

                    parameters.update(param_dict)
                    write_file = open("config.json", "w", encoding='utf-8')
                    write_file.write(json.dumps(parameters, indent=4))

                    print(p_arnold.get())
                    print(p_temp_ki.get())
                    print(p_u.get())
                    print(p_v.get())
                    pop_up.destroy()

                def get_default():
                    print(" In get def")
                    pop_up.destroy()

                submit = tk.Button(pop_up, text="Submit", command=get_parameters)
                default = tk.Button(pop_up, text="Use Default Values", command=get_default)

                label1.pack()
                p_arnold.pack()
                label2.pack()
                p_temp_ki.pack()
                label3.pack()
                p_u.pack()
                label4.pack()
                p_v.pack()
                submit.pack(side=tk.BOTTOM)
                default.pack(side=tk.BOTTOM)

                self.window.wait_window(window=pop_up)

                read_file = open("config.json", encoding='utf-8')
                parameters = json.load(read_file)
                q = float((parameters["parameter_arnold"]))

                def h(l): return q*l*(1-l)
                temp_ki = [None]*(size[0]*size[1]+1)
                print(size[0]*size[1] + 1)
                ki = [None]*size[0]*size[1]

                # Encryption parameter
                temp_ki[0] = float((parameters["parameter_temp_ki"]))
                u = int((parameters["parameter_u"]))
                v = int((parameters["parameter_v"]))

                read_file.close()

                for m in range(self.iteration):
                    # print(m)
                    for x in range(size[0]):
                        for y in range(size[1]):
                            xn = ((((u*v)+1)*x)+(v*y)) % size[0]
                            yn = ((u*x)+y) % size[1]
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

                # for t in range(100):
                #     print(ki[t])

                top_level = tk.Toplevel()
                display_text = "Parameter (q)            = "+str(q) + \
                               "\nSystem Initial Value (w) = "+str(temp_ki[0]) + \
                               "\nArnold Map Value (a)     = "+str(u) + \
                               "\nArnold Map Value (b)     = "+str(v)
                label1 = tk.Label(top_level, text=display_text, width=40, justify=tk.LEFT)
                label1.pack()
                button = tk.Button(top_level, text="OK", command=top_level.destroy)
                button.pack()

                return red1, green1, blue1

            except SystemError:
                print("Image is probably neither grey scale nor 3-channel")


if __name__ == '__main__':

    for i in range(1):
        print(i)
        file = '/home/anmol/PycharmProjects/pixipher/lena1.png'
        file2 = '/home/anmol/PycharmProjects/pixipher/output2.png'
        # print(file, file2)
        Encryption(file, outfile=file2, iteration=1).encrypt_file()

    # a = bitstring.BitArray(bin='00000100')
    #
    # print(9^5)