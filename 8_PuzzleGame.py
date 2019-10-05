import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QDialog
from View import MenuWindow, InitialWindow, GamingWindow, CompleteDialog
from View import MenuWindow2 as mw2
from Model import DataModel as DM

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

    GameStates[0].show()
    menuWindow.ui.buttonStart.clicked.connect(lambda: showAnotherWindow(1, 0))
    menuWindow.ui.buttonLoad.clicked.connect(lambda: showAnotherWindow(2, 0))
    preGamingWindow.ui.buttonBack.clicked.connect(lambda: showAnotherWindow(0, 1))
    preGamingWindow.ui.buttonDynamic.clicked.connect(lambda: showAnotherWindow(2, 1))
    gameWindow.ui.buttonMenu.clicked.connect(lambda: showAnotherWindow(0, 2))
    gameWindow.completeDialog.ui.buttonMenu.clicked.connect(lambda: showAnotherWindow(0, 2))
    sys.exit(app.exec_())




