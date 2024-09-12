from PySide6.QtWidgets import QApplication, QFrame, QLabel, QMainWindow, QWidget, QPushButton, QVBoxLayout, QSpinBox
from PySide6.QtGui import QAction, QFont, QPixmap

class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        widget = QWidget()
        disposition = QVBoxLayout(widget)
        widget.setLayout(disposition)

        self.texte = QLabel("L'informatique, ça fait gagner beaucoup de temps... à condition d'en avoir beaucoup devant soi !")
        self.texte.setFrameStyle(QFrame.Shape.WinPanel | QFrame.Shadow.Raised)
        self.police = QFont()
        self.police.setItalic(True)
        self.police.setItalic(False)
        self.texte.setWordWrap(True)
        self.police.setPointSize(1)
        self.texte.setFont(self.police)
        disposition.addWidget(self.texte)

        self.italique = QPushButton('Italique')
        self.italique.clicked.connect(self.italique_clicked)
        disposition.addWidget(self.italique)

        self.gras = QPushButton('Gras')
        self.gras.clicked.connect(self.gras_clicked)
        disposition.addWidget(self.gras)

        self.ww = QPushButton('WordWrap')
        self.ww.clicked.connect(self.ww_clicked)
        disposition.addWidget(self.ww)

        self.grosseur = QPushButton('Augmenter la grosseur de police')
        self.grosseur.clicked.connect(self.grosseur_clicked)
        disposition.addWidget(self.grosseur)

        self.setCentralWidget(widget)

    def italique_clicked(self):
        self.police.setItalic(not self.police.italic())
        self.texte.setFont(self.police)

    def gras_clicked(self):
        self.police.setBold(not self.police.bold())
        self.texte.setFont(self.police)

    def ww_clicked(self):
        self.texte.setWordWrap(not self.texte.wordWrap())

    def grosseur_clicked(self):
        self.police.setPointSize( self.police.pointSize() + 1)
        self.texte.setFont(self.police)



app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()