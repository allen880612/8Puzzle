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
    # app = QApplication(sys.argv)
    # Gamestate.append(MenuForm.Menu())
    # Gamestate.append(Second())
    # Gamestate.append(Third())
    # Gamestate[0].show()
    # Gamestate[0].btn.clicked.connect(lambda: showAnotherWindow(1, 0))
    # Gamestate[1].btn.clicked.connect(lambda: showAnotherWindow(2, 1))
    # Gamestate[2].btn.clicked.connect(lambda: showAnotherWindow(0, 2))

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
    # while True:
    #     if gameState == 0 and (not menuWindow.IsStart()) and (not menuWindow.isOpen):
    #         GameState[0].show()
    #         menuWindow.isOpen = True;
    #         # GameState[2].hide()
    #         print("I am a joke og you?")
    #     elif gameState == 0 and menuWindow.isOpen:
    #         menuWindow.isOpen = False
    #         GameState[1].show()
    #         GameState[0].hide()
    #         gameState = 1
    #         print(menuWindow.isOpen)

    sys.exit(app.exec_())



