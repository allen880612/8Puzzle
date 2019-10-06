from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PIL import Image
from PIL.ImageQt import ImageQt
import os

class ImageControl():
    def __init__(self, dataModel):
        self.sourceImage = None # PIL
        self.sourceQPixmap = None

        self.pixmapList = False
        self.data = dataModel

        self.isloaded = False

    def LoadImage(self, image):

        try:
            image = Image.open(image)
        except Exception as e:
            print("import image fail!!")
            print(str(e))
            return

        self.isloaded = True

        cropPIL = self.NormalizeImage(image)
        # cropPIL.show()
        self.sourceImage = cropPIL
        self.sourceQPixmap = self.ConvertPILtoPixmap(cropPIL)

        self.data.SetSourceImage(cropPIL)
        self.data.SetPixmap(self.sourceQPixmap)

    def NormalizeImage(self, orginImg):
        img = orginImg
        baseHeight = 480
        # 以寬為基準，resize為 480 * 480
        hpercent = (baseHeight / float(img.size[1]))
        wsize = int((float(img.size[0]) * float(hpercent)))
        img = img.resize((wsize, baseHeight), Image.ANTIALIAS)
        box = (0, 0, 480, 480)
        return img.crop(box)


    def ConvertPILtoQImage(self, imagePIL):
        imgRGB = imagePIL.convert("RGB")
        imgByte = imgRGB.tobytes("raw", "RGB")
        qImage = QImage(imgByte, imgRGB.size[0], imgRGB.size[1], QtGui.QImage.Format_RGB888)
        return qImage

    def ConvertPILtoPixmap(self, imagePIL):
        qImage = self.ConvertPILtoQImage(imagePIL)
        return QPixmap(qImage)

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
        self.save_img(image_list)
        pixmapList = [self.ConvertPILtoPixmap(img) for img in image_list]
        return pixmapList

    def save_img(self, imageList):
        index = 0
        basepath = os.path.join(os.getcwd(), "subImage")
        if not os.path.isdir(basepath):
            print("路徑不存在, 自動建立")
            os.mkdir(basepath)
        for im in imageList:
            im.save(os.path.join(basepath, str(index) + ".png"))
            index += 1

    def SetImageList(self, count):
        # 確認有匯入過
        if self.isloaded:
            self.pixmapList = self.cropImage(self.sourceImage, count)
            self.data.SetPixmapList(self.pixmapList)
