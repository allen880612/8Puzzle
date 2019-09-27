import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QDialog
from View import MenuWindow, InitialWindow, GamingWindow, CompleteDialog
from View import MenuWindow2 as mw2
from Model import DataModel as DM

class First(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton("to Second", self)
        self.btn.move(30, 50)

        self.setGeometry(300, 300, 500, 500)
        self.setWindowTitle('8 Puzzle! - Initialize')
        self.show()


class Second(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton("to third", self)
        self.btn.move(30, 50)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('8 puzzle - Beginning')


class Third(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.btn = QPushButton("to First", self)
        self.btn.move(30, 50)
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('8 puzzle - Gaming')


def showAnotherWindow(openIndex, closeIndex):
    GameStates[openIndex].show()
    GameStates[closeIndex].hide()



if __name__ == '__main__':

    data = DM.DataModel()

    GameStates = []
    gameState = 0

    app = QApplication(sys.argv)
    GameStates = [QMainWindow() for i in range(4)]   # 3個遊戲視窗 type = PyQt5.QtWidgets.QMainWindow

    # Menu Window
    menuWindow = MenuWindow.Menu(data)
    GameStates[0] = menuWindow
    # menuWindow.setupUi(GameStates[0])

    # Choose Begin Block Window
    preGamingWindow = InitialWindow.PreGaming(data)
    GameStates[1] = preGamingWindow

    # Gaming Window
    gameWindow = GamingWindow.GameWindow(data)
    GameStates[2] = gameWindow

    # Complete Dialog
    # cDialog = QDialog()
    # completeDialog = CompleteDialog.CompleteDialog()
    # completeDialog.setupUi(cDialog)

    GameStates[0].show()
    menuWindow.ui.buttonStart.clicked.connect(lambda: showAnotherWindow(1, 0))
    menuWindow.ui.buttonLoad.clicked.connect(lambda: showAnotherWindow(2, 0))
    preGamingWindow.ui.buttonBack.clicked.connect(lambda: showAnotherWindow(0, 1))
    preGamingWindow.ui.buttonDynamic.clicked.connect(lambda: showAnotherWindow(2, 1))
    gameWindow.ui.buttonMenu.clicked.connect(lambda: showAnotherWindow(0, 2))
    gameWindow.completeDialog.ui.buttonMenu.clicked.connect(lambda: showAnotherWindow(0, 2))

    sys.exit(app.exec_())




