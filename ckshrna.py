import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from ckshrnagui import Ui_ckshrnagui

#working version 03 09 2017 -- works

class ckshrnagui(Ui_ckshrnagui):
    def __init__(self, dialog):
        Ui_ckshrnagui.__init__(self)
        self.setupUi(dialog)

        # Connect "add" button with a custom function (addInputTextToListbox)
        self.generateOligosBtn.clicked.connect(self.beginOligoDesign)

        self.undoBtn.clicked.connect(self.undoLastOligo)

    def undoLastOligo(self):
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.removeRow(currentRowCount - 1)

    def beginOligoDesign(self):
        def reverse_complement(my_sequence):
            my_dictionary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            return "".join([my_dictionary[base] for base in reversed(my_sequence)])

        def complement(my_sequence):
            my_dictionary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
            return "".join([my_dictionary[base] for base in my_sequence])

        def reverse(my_sequence):
            return my_sequence[::-1]

        shRNA_sense = self.inputSequence.text().upper()

        # generate the 5' oligo
        shRNA_antisense = reverse_complement(shRNA_sense)
        loop_sequence = "CTCGAG"  # the 6bp loop CTCGAG or the 9bp loop TTCAAGAGA are good choices
        sense_3 = "TTTTTG"  # 3' of the sense strand includes the ttttt pol iii termination sequence
        sense_5 = "CCGG"  # 5' of the sense strand includes the AgeI overhang

        sense_oligo = ''.join([sense_5.lower(), shRNA_sense, loop_sequence.lower(), shRNA_antisense, sense_3.lower()])

        sense_label = "shRNA     sense 5'- " + sense_oligo + ' ' * 4 + " -3'"
        self.senseLabel.setText(sense_label)

        # and the complementary oligo
        antisense_5 = "AATTCAAAAA"  # includes the EcoRI underhang and reverse complement of the term seq
        antisense_oligo = ''.join([antisense_5.lower(), shRNA_sense, loop_sequence.lower(), shRNA_antisense])

        antisense_label = "shRNA antisense 3'- " + ' ' * 4 + reverse(antisense_oligo) + " -5'"
        self.antisenseLabel.setText(antisense_label)

        # print the bonds
        bonds_label = "                    " + ' ' * 4 + '|' * (len(antisense_oligo) - 4)
        self.bondsLabel.setText(bonds_label)

        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table

        self.tableWidget.insertRow(currentRowCount)
        self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(sense_oligo))
        self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(antisense_oligo))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = ckshrnagui(dialog)

    dialog.show()
    sys.exit(app.exec_())
