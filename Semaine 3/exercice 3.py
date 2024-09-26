from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel
import csv


class TimesCover(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Times Cover')


        self.disposition = QVBoxLayout()
        widget_central = QWidget()
        widget_central.setLayout(self.disposition)
        self.setCentralWidget(widget_central)

        self.annee = self.creer_libelle('Year')
        self.honor = self.creer_libelle('Honor')
        self.nom = self.creer_libelle('Name')
        self.pays = self.creer_libelle('Country')
        self.naissance = self.creer_libelle('Birth Year')
        self.mort = self.creer_libelle('Death Year')
        self.titre = self.creer_libelle('Title')
        self.categorie = self.creer_libelle('Category')
        self.contexte = self.creer_libelle('Context')

        disposition_boutons = QHBoxLayout()
        self.precedent = QPushButton('Precedent')
        self.suivant = QPushButton('suivant')
        disposition_boutons.addWidget(self.precedent)
        disposition_boutons.addWidget(self.suivant)
        self.disposition.addLayout(disposition_boutons)

        self.entrees = []
        self.index_entrees = 0

        with open('times.csv', 'r') as fichier_csv:
            self.lignes = csv.DictReader(fichier_csv)
            for ligne in lignes:
                self.entrees.append(ligne)


    def creer_libelle(self,nom_propriete:str):
        disposition_libelle = QHBoxLayout
        libelle_titre = QLabel(nom_propriete + ':')
        libelle_valeur = QLabel('')
        disposition_libelle.addWidget(libelle_valeur)
        disposition_libelle.addWidget(libelle_titre)
        self.disposition.addLayout(disposition_libelle)
        return libelle_valeur

    def afficher_entrees(self):
        entree


app = QApplication()
tc = TimesCover()
tc.show()
app.exec()
