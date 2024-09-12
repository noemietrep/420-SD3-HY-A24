from PySide6.QtWidgets import QApplication, QFrame, QLabel, QMainWindow, QWidget, QMenu, QVBoxLayout
from PySide6.QtGui import QAction, QFont, QPixmap

class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        widget = QWidget()
        disposition = QVBoxLayout(widget)
        widget.setLayout(disposition)

        self.barre_menu = self.menuBar()
        self.menu = QMenu("&Menu")
        self.action_menu1 = QAction("Item Menu1")
        self.menu.addAction(self.action_menu1)

        self.action_menu2 = QAction("Item Menu2")
        self.menu.addAction(self.action_menu2)

        texte_riche = QLabel("Woooooooooww!!!!!")
        police = QFont()
        police.setBold(False)
        police.setPointSize(20)
        police.setItalic(True)
        texte_riche.setFont(police)
        texte_riche.setFrameStyle(QFrame.Shape.WinPanel | QFrame.Shadow.Raised)
        disposition.addWidget(texte_riche)

        label = QLabel()
        image = QPixmap('ex1.png')
        label.setPixmap(image)
        disposition.addWidget(label)

        self.barre_menu.addMenu(self.menu)
        self.setCentralWidget(widget)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()