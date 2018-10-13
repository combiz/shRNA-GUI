# Combiz Khozoie, Ph.D. 
# September 2017
# PyQt5 GUI based design of oligonucleotide pairs suitable for
# cloning into pLKO1-stuffer for shRNA mediated gene knockdown
# note: for internal laboratory use only

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem
from ckshrnagui import Ui_ckshrnagui

import sys

class OligoConstruct:

    """
    Generate two complementary oligos from a target sequence for shRNA cloning.

    This class receives a shRNA sense sequence input and generates two
    oligos ready for ordering in the 5'->3' direction.  These oligos are ready
    for annealing and ligation into the AgeI / EcoRI fragment of pLKO1-stuffer.

    The strings sense_label, antisense_label, and bond_label can be printed in a
    monospace font to illustrate base pairing in dsDNA in the pLKO1 construct.

    The two ready to order complementary oligos are: -
    sense_oligo
    antisense_oligo
    """
 
    # define a class attribute tuple for base pairing
    my_dictionary = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    def __init__(self, senseInput):
        self.shRNA_sense = senseInput
        self.loop_sequence = "CTCGAG" # the 6bp loop CTCGAG or the 9bp loop TTCAAGAGA are good choices
        self.sense_3 = "TTTTTG"  # 3' of the sense strand includes the ttttt pol iii termination sequence
        self.sense_5 = "CCGG"  # 5' of the sense strand includes the AgeI overhang
        self.antisense_5 = "AATTCAAAAA"  # includes the EcoRI underhang and reverse complement of the term seq
        
    @staticmethod
    def reverse_complement(my_sequence):
        return "".join([OligoConstruct.my_dictionary[base] for base in reversed(my_sequence)])
    
    @staticmethod
    def complement(my_sequence):
        return "".join([OligoConstruct.my_dictionary[base] for base in my_sequence])
    
    @staticmethod
    def reverse(my_sequence):
        return my_sequence[::-1]
    
    def shRNA_antisense(self):
        return self.reverse_complement(self.shRNA_sense)
    
    def antisense_oligo(self):
        return ''.join([self.antisense_5.lower(), 
                        self.shRNA_sense, 
                        self.loop_sequence.lower(), 
                        self.shRNA_antisense()])

    def sense_oligo(self):
        return ''.join([self.sense_5.lower(), 
                        self.shRNA_sense, 
                        self.loop_sequence.lower(), 
                        self.shRNA_antisense(), 
                        self.sense_3.lower()])
    
    def sense_label(self):
        return "shRNA     sense 5'- " + self.sense_oligo() + ' ' * 4 + " -3'"

    def antisense_label(self):
        return "shRNA antisense 3'- " + ' ' * 4 + self.reverse(self.antisense_oligo()) + " -5'"
    
    def bonds_label(self):
        return "                    " + ' ' * 4 + '|' * (len(self.antisense_oligo()) - 4)    


class ckshrnagui(Ui_ckshrnagui):

    def __init__(self, dialog):
        Ui_ckshrnagui.__init__(self)
        self.setupUi(dialog)

        # Connect "add" button with a custom function (addInputTextToListbox)
        self.generateOligosBtn.clicked.connect(self.beginOligoDesign)

        # restrict user input to nucleotides only
        reg_ex = QRegExp("[agtcAGTC_]+")
        input_validator = QRegExpValidator(reg_ex, self.inputSequence)
        self.inputSequence.setValidator(input_validator)

        # Connect 'undo' button with a custom function (undoLastOligo)
        self.undoBtn.clicked.connect(self.undoLastOligo)

        # initialize text labels with instructions
        self.senseLabel.setText("Instructions: (1) Enter your 19-29bp shRNA target sequence above.")
        self.bondsLabel.setText("              (2) Press 'Go' to generate oligonucleotides for cloning.")
        self.antisenseLabel.setText("")


    def undoLastOligo(self):
        # Remove the last added oligo pair from the table
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.removeRow(currentRowCount - 1)

    def beginOligoDesign(self):       
        # retrieve the target shRNA sequence from user input
        shRNA_sense = self.inputSequence.text().upper()
        if len(shRNA_sense) < 19:
            self.inputSequence.setText("Error: too short.")
            return

        # generate the oligos for the given target
        myConstruct = OligoConstruct(shRNA_sense)

        # update the dsDNA bonding illustration
        self.senseLabel.setText(myConstruct.sense_label())
        self.antisenseLabel.setText(myConstruct.antisense_label())
        self.bondsLabel.setText(myConstruct.bonds_label())

        # append these oligos to the table
        currentRowCount = self.tableWidget.rowCount()  # necessary even when there are no rows in the table
        self.tableWidget.insertRow(currentRowCount)
        self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(myConstruct.sense_oligo()))
        self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(myConstruct.antisense_oligo()))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = ckshrnagui(dialog)

    dialog.show()
    sys.exit(app.exec_())
