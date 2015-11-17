from scipy.misc import *


class Signature:
    def __init__(self):
        self.filename = None
    def signatureGeneration(self):
        # self.filename = askopenfilename(filetypes=(("All files", "*.*"),
        #                                    ("JPEG Files", "*.jpg")))
        # print(self.filename)
        image = imread("lena_color.png")
        print(image)

if __name__ == '__main__':
    sig = Signature()
    sig.signatureGeneration()