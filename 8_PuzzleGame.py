import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from View import MenuWindow

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
    GameStates = []
    gameState = 0

    app = QApplication(sys.argv)
    GameStates = [QMainWindow() for i in range(3)]   # 3個遊戲視窗 type = PyQt5.QtWidgets.QMainWindow
    menuWindow = MenuWindow.Menu()
    menuWindow.setupUi(GameStates[0])
    # Choose Begin Block Window
    GameStates[1] = Second()
    # Gaming Window
    GameStates[2] = Third()

    GameStates[0].show()
    menuWindow.buttonStart.clicked.connect(lambda: showAnotherWindow(1, 0))
    GameStates[1].btn.clicked.connect(lambda: showAnotherWindow(2, 1))
    GameStates[2].btn.clicked.connect(lambda: showAnotherWindow(0, 2))

    sys.exit(app.exec_())



