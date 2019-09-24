from PyQt5 import QtCore, QtGui, QtWidgets
from PIL import Image
from PIL.ImageQt import ImageQt

class ImageControl():
    def __init__(self, dataModel):
        self.sourceImage = None # PIL
        self.sourceQImage = None  # default image
        self.sourceQPixmap = None

        self.imageList_PIL = []
        self.qImageList = []
        self.pixmapList = []
        self.iconList = []
        self.data = dataModel

    def LoadImage(self, image):
        image = Image.open(image)

        #  補圖片正規劃
        box = (0, 0, 480, 480)
        cropPIL = image.crop(box)

        # cropPIL.show()
        self.sourceImage = cropPIL
        self.sourceQImage = self.ConvertPILtoQImage(cropPIL)
        self.sourceQPixmap = QtGui.QPixmap(self.sourceQImage)
        self.data.SetSourceImage(self.sourceQImage)
        self.data.SetSourcePixmap(self.sourceQPixmap)


    def ConvertPILtoQImage(self, imagePIL):
        im = imagePIL.convert("RGB")
        data = im.tobytes("raw", "RGB")
        qim = QtCore.QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_RGB888)
        return qim



    def cropImage(self, image, cropNum):
        width, height = image.size
        item_width = int(width / cropNum)
        box_list = []

        for i in range(0, cropNum):
            for j in range(0, cropNum):
                # print((i*item_width,j*item_width,(i+1)*item_width,(j+1)*item_width))
                box = (j * item_width, i * item_width, (j + 1) * item_width, (i + 1) * item_width)
                box_list.append(box)

        image_list = [image.crop(box) for box in box_list]
        return image_list

    def save_img(self, imageList):
        index = 0
        for im in imageList:
            # cv2.imwrite(str(index) + ".png", im)
            # im.save(os.path.join(os.getcwd(), "subImg", str(index) + ".jpg"))
            index += 1

    def SetImageList(self, count):
        self.rowButtonCount = count
