#
# Copyright 2018-2019 Manuel Barrette
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call
import platform

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1101, 438)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)

        # Pour empêcher de changer la taille de la fenêtre
        MainWindow.setFixedSize(MainWindow.size())

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(670, 20, 421, 331))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(5, 0))
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setDragDropMode(QtWidgets.QAbstractItemView.DragOnly)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(7, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(8, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(9, 1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(10, 20, 651, 251))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setMinimumSize(QtCore.QSize(11, 0))
        self.tableWidget_2.setAutoFillBackground(False)
        self.tableWidget_2.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.tableWidget_2.setDragEnabled(True)
        self.tableWidget_2.setDragDropOverwriteMode(False)
        self.tableWidget_2.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.tableWidget_2.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.tableWidget_2.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget_2.setShowGrid(True)
        self.tableWidget_2.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setHighlightSections(False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setHighlightSections(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 290, 161, 27))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 141, 19))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(670, 0, 171, 19))
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(500, 290, 161, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 360, 1081, 31)) # ICI
        self.textBrowser.setObjectName("textBrowser")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 290, 131, 19))
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(160, 290, 161, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 270, 375, 19))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setGeometry(QtCore.QRect(10, 320, 651, 31))

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(lambda: self.reinitialiser())
        self.pushButton_2.clicked.connect(lambda: self.ecrireSequence())
        self.pushButton_3.clicked.connect(lambda: self.supprimerLigne())
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        print("Initialisation...")
        self.textBrowser.setText("Initialisation...")
        processus = QtCore.QProcess()
        processus.start("arduino-cli core update-index")
        processus.waitForFinished()
        processus.start("arduino-cli core install arduino:avr")
        processus.waitForFinished()
        print("Prêt!")
        self.textBrowser.setText("Prêt!")


        self.dico_commandes = {}
        self.dico_commandes['Arrêter la tourelle'] = 'arreterTourelle'
        self.dico_commandes['Arrêter la baliste'] = 'arreterBaliste'
        self.dico_commandes['Tirer à volonté'] = 'tournerBaliste'
        self.dico_commandes['Arrêter'] = 'arreter'
        self.dico_commandes['Tirer deux volants'] = 'tirerBaliste'

        self.dico_commandes_puissance = {}
        self.dico_commandes_puissance['Avancer'] = 'avancer'
        self.dico_commandes_puissance['Reculer'] = 'reculer'
        self.dico_commandes_puissance['Tourner sens horaire'] = 'tourelleHoraire'
        self.dico_commandes_puissance['Tourner sens antihoraire'] = 'tourelleAntihoraire'

        self.dico_commandes_pendant = {}
        self.dico_commandes_pendant['Continuer pendant'] = 'attendrePendant'

        self.dico_commandes_puissance_pendant = {}
        self.dico_commandes_puissance_pendant['Avancer pendant'] = 'avancerPendant'
        self.dico_commandes_puissance_pendant['Tourner horaire pendant'] = 'tourelleHorairePendant'
        self.dico_commandes_puissance_pendant['Reculer pendant'] = 'reculerPendant'
        self.dico_commandes_puissance_pendant['Tourner antihoraire pendant'] = 'tourelleAntihorairePendant'


    def supprimerLigne(self):
        self.tableWidget_2.removeRow(self.tableWidget_2.currentRow())


    def reinitialiser(self):
        i = 0
        while(i < self.tableWidget_2.rowCount()):
            self.tableWidget_2.removeRow(i)


    def ecrireSequence(self):
        self.progressBar.setValue(0)
        print("")
        self.textBrowser.setText("")
        self.disableAll(True)
        print("En cours...")
        self.textBrowser.setText("En cours...")
        fichier = "instructions.h"
        with open(fichier, 'w') as file_object:
            file_object.write("void instructions(Baliste baliste)\n")
            file_object.write("{\n")
            i = 0
            while(i < self.tableWidget_2.rowCount()):
                item = self.tableWidget_2.item(i, 0)
                try:
                    commande = item.text()
                except AttributeError:
                    i += 1
                    continue
                if commande in self.dico_commandes:
                    file_object.write("baliste." + self.dico_commandes[commande] + "();\n")
                elif commande in self.dico_commandes_puissance:
                    try:
                        pourcent = self.tableWidget_2.item(i,1).text()
                        if pourcent == "":
                            raise AttributeError
                        pourcent = int(pourcent)
                    except AttributeError:
                        pourcent = 100
                    except ValueError:
                        print("Ligne " + str(i+1) + " : Veuillez entrer un pourcentage entre 0 et 100")
                        self.textBrowser.setText("Ligne " + str(i+1) + " : Veuillez entrer un pourcentage entre 0 et 100")
                        self.disableAll(False)
                        return
                    if 0 <= pourcent <= 100:
                        file_object.write("baliste." + self.dico_commandes_puissance[commande] + "(" + str(pourcent)  + ");\n")
                    else:
                        print("Ligne " + str(i+1) + " : Veuillez entrer un pourcentage entre 0 et 100")
                        self.textBrowser.setText("Ligne " + str(i+1) + " : Veuillez entrer un pourcentage entre 0 et 100")
                        self.disableAll(False)
                        return
                elif commande in self.dico_commandes_pendant:
                    try:
                        temps = self.tableWidget_2.item(i,2).text()
                        temps = int(temps)
                    except AttributeError:
                        print("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.textBrowser.setText("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.disableAll(False)
                        return
                    except ValueError:
                        print("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.textBrowser.setText("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.disableAll(False)
                        return
                    if 0 <= temps <= 4294967295:
                        file_object.write("baliste." + self.dico_commandes_pendant[commande] + "(" + str(temps)  + ");\n")
                    else:
                        print("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.textBrowser.setText("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.disableAll(False)
                        return
                elif commande in self.dico_commandes_puissance_pendant:
                    try:
                        pourcent = self.tableWidget_2.item(i,1).text()
                        pourcent = int(pourcent)
                    except AttributeError:
                        pourcent = 100
                    except ValueError:
                        print("Ligne " + str(i+1) + " : Veuillez entrer un pourcentage entre 0 et 100")
                        self.textBrowser.setText("Ligne " + str(i+1) + " : Veuillez entrer un pourcentage entre 0 et 100")
                        self.disableAll(False)
                        return
                    if 0 <= pourcent <= 100:
                        flag_pourcent = True
                    else:
                        print("Ligne " + str(i+1) + " : Veuillez entrer un pourcentage entre 0 et 100")
                        self.textBrowser.setText("Ligne " + str(i+1) + " : Veuillez entrer un pourcentage entre 0 et 100")
                        self.disableAll(False)
                        return
                    try:
                        temps = self.tableWidget_2.item(i,2).text()
                        temps = int(temps)
                    except AttributeError:
                        print("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.textBrowser.setText("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.disableAll(False)
                        return
                    except ValueError:
                        print("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.textBrowser.setText("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.disableAll(False)
                        return
                    if 0 <= temps <= 4294967295:
                        flag_temps = True
                    else:
                        print("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.textBrowser.setText("Ligne " + str(i+1) + " : Veuillez entrer un temps entre 0 et 4 294 967 295 ms")
                        self.disableAll(False)
                        return
                    if flag_temps == True and flag_pourcent == True:
                        file_object.write("baliste." + self.dico_commandes_puissance_pendant[commande] + "(" + str(temps)  + ", " + str(pourcent) + ");\n")
                else:
                    print("Ligne " + str(i+1) + " : Commande invalide")
                    self.textBrowser.setText("Ligne " + str(i+1) + " : Commande invalide")
                    self.disableAll(False)
                    return
                i += 1
            file_object.write("}\n")
        print("Envoi des instructions...")
        self.textBrowser.setText("Envoi des instructions...")
        self.progressBar.setValue(50)
#        call(["arduino", "--upload", "Baliste.ino"])
        processus = QtCore.QProcess()
#        processus.start("arduino --upload Baliste.ino")
        systeme_exploitation = platform.system()
        if systeme_exploitation == 'Windows':
            processus.start("arduino-cli compile -b arduino:avr:uno ..\Baliste")
            processus.waitForFinished()
            processus.start("arduino-cli upload -p COM3 -b arduino:avr:uno -v ..\Baliste")
            processus.waitForFinished()
            code = processus.exitCode()
        elif systeme_exploitation == 'Darwin' or 'Linux':
            processus.start("arduino-cli compile -b arduino:avr:uno ../Baliste")
            processus.waitForFinished()
            processus.start("arduino-cli upload -p /dev/ttyACM0 -b arduino:avr:uno -v ../Baliste")
            processus.waitForFinished()
            code = processus.exitCode()
        else:
            code = 5
#        print(code)
        if code == 0:
             print("Envoi terminé avec succès!")
             self.textBrowser.setText("Envoi terminé avec succès!")
        elif code == 1:
            print("Erreur lors du téléversement, vérifiez que la machine est bien branchée, appuyez sur Reset et réessayez.")
            self.textBrowser.setText("Erreur lors du téléversement, vérifiez que la machine est bien branchée, appuyez sur Reset et réessayez.")
        elif code == 2:
            print("Croquis non trouvé")
            self.textBrowser.setText("Croquis non trouvé")
        elif code == 3:
            print("Option invalide passée en argument")
            self.textBrowser.setText("Option invalide passée en argument")
        elif code == 4:
            print("La préférence utilisée n'existe pas")
            self.textBrowser.setText("La préférence utilisé n'existe pas")
        elif code == 5:
            print("Système d'exploitation non supporté")
            self.textBrowser.setText("Système d'exploitation non supporté")
        else:
            print("Erreur inconnue")
            self.textBrowser.setText("Erreur inconnue")
        self.disableAll(False)
        self.progressBar.setValue(100)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Baliste programmable"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Actions des roues"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Actions de la tourelle"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Arrêter"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "Arrêter la tourelle"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "Avancer"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "Tourner sens horaire"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "Reculer"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "Tourner sens antihoraire"))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "Avancer pendant"))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "Tourner horaire pendant"))
        item = self.tableWidget.item(5, 0)
        item.setText(_translate("MainWindow", "Reculer pendant"))
        item = self.tableWidget.item(5, 1)
        item.setText(_translate("MainWindow", "Tourner antihoraire pendant"))
        item = self.tableWidget.item(9, 0)
        item.setText(_translate("MainWindow", "Continuer pendant"))
        item = self.tableWidget.item(7, 1)
        item.setText(_translate("MainWindow", "Arrêter la baliste"))
        item = self.tableWidget.item(8, 1)
        item.setText(_translate("MainWindow", "Tirer à volonté"))
        item = self.tableWidget.item(9, 1)
        item.setText(_translate("MainWindow", "Tirer deux volants"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Instructions"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "% puissance (défaut = 100)*"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Temps [ms] (actions \"pendant\")"))
        self.pushButton.setText(_translate("MainWindow", "Réinitialiser"))
        self.label.setText(_translate("MainWindow", "Liste d\'instructions"))
        self.label_3.setText(_translate("MainWindow", "Banque de commandes"))
        self.pushButton_2.setText(_translate("MainWindow", "Soumettre"))
        self.label_4.setText(_translate("MainWindow", "Messages système"))
        self.pushButton_3.setText(_translate("MainWindow", "Supprimer instruction"))
        self.label_2.setText(_translate("MainWindow", "* Sauf les \"Arrêter\", \"Tirer\" et \"Continuer\""))

    def disableAll(self, boolean):
        self.tableWidget.setDisabled(boolean)
        self.tableWidget_2.setDisabled(boolean)
        self.pushButton.setDisabled(boolean)
        self.pushButton_2.setDisabled(boolean)
        self.pushButton_3.setDisabled(boolean)
