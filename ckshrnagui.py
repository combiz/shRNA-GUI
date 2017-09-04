# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ckshrnagui.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ckshrnagui(object):
    def setupUi(self, ckshrnagui):
        ckshrnagui.setObjectName("ckshrnagui")
        ckshrnagui.resize(1583, 507)
        ckshrnagui.setStyleSheet("\n"
"#mainView, #calibration_tab, #mask_tab, #integration_tab {\n"
"     background: #3C3C3C;\n"
"    border: 5px solid #3C3C3C;\n"
" }\n"
"\n"
"QTabWidget::tab-bar{\n"
"    alignment: center;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"  border:  1px solid #2F2F2F;\n"
"  border-radius: 3px;\n"
"}\n"
"\n"
"QWidget{\n"
"    color: #F1F1F1;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab:left, QTabBar::tab:right {\n"
"     background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #3C3C3C, stop:1 #505050);\n"
"     border: 1px solid  #5B5B5B;\n"
"    font: normal 14px;\n"
"    color: #F1F1F1;\n"
"     border-radius:2px;\n"
"\n"
"    padding: 0px;\n"
"     width: 20px;\n"
"    min-height:140px;\n"
" }\n"
"\n"
"\n"
"QTabBar::tab::top, QTabBar::tab::bottom {\n"
"     background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3C3C3C, stop:1 #505050);\n"
"     border: 1px solid  #5B5B5B;\n"
"    border-right: 0px solid white;\n"
"      color: #F1F1F1;\n"
"    font: normal 11px;\n"
"     border-radius:2px;\n"
"     min-width: 65px;\n"
"    height: 19px;\n"
"    padding: 0px;\n"
"     margin-top: 1px ;\n"
"    margin-right: 1px;\n"
" }\n"
"QTabBar::tab::left:last, QTabBar::tab::right:last{\n"
"    border-bottom-left-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"QTabBar::tab:left:first, QTabBar::tab:right:first{\n"
"    border-top-left-radius: 10px;\n"
"    border-top-right-radius: 10px;\n"
"}\n"
"\n"
"QTabWidget, QTabWidget::tab-bar,  QTabWidget::panel, QWidget{\n"
"     background: #3C3C3C;\n"
" }\n"
"\n"
"QTabWidget::tab-bar {\n"
"    alignment: center;\n"
"}\n"
"\n"
" QTabBar::tab:hover {\n"
"     border: 1px solid #ADADAD;\n"
" }\n"
"\n"
" QTabBar:tab:selected{\n"
"\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #727272,\n"
"        stop: 1 #444444\n"
"    );\n"
"     border:1px solid  rgb(255, 120,00);/*#ADADAD; */\n"
"}\n"
"\n"
"QTabBar::tab:bottom:last, QTabBar::tab:top:last{\n"
"    border-top-right-radius: 10px;\n"
"    border-bottom-right-radius: 10px;\n"
"}\n"
"QTabBar::tab:bottom:first, QTabBar::tab:top:first{\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
" QTabBar::tab:top:!selected {\n"
"    margin-top: 1px;\n"
"    padding-top:1px;\n"
" }\n"
"QTabBar::tab:bottom:!selected{\n"
"    margin-bottom: 1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QGraphicsView {\n"
"    border-style: none;\n"
"}\n"
"\n"
" QLabel , QCheckBox, QGroupBox, QRadioButton, QListWidget::item, QPushButton, QToolBox::tab, QSpinBox, QDoubleSpinBox , QComboBox{\n"
"     color: #F1F1F1;\n"
"    font-size: 12px;\n"
" }\n"
" QCheckBox{\n"
"     border-radius: 5px;\n"
" }\n"
" QRadioButton, QCheckBox {\n"
"     font-weight: normal;\n"
"    height: 15px;\n"
" }\n"
"\n"
" QLineEdit  {\n"
"     border-radius: 2px;\n"
"     background: #F1F1F1;\n"
"     color: black;\n"
"    height: 18 px;\n"
" }\n"
"\n"
"QLineEdit::focus{\n"
"    border-style: none;\n"
"     border-radius: 2px;\n"
"     background: #F1F1F1;\n"
"     color: black;\n"
"}\n"
"\n"
"QLineEdit:disabled, QSpinBox:disabled, QDoubleSpinBox:disabled{\n"
"    color:rgb(148, 148, 148)\n"
"}\n"
"QSpinBox, QDoubleSpinBox {\n"
"    background-color:  #F1F1F1;\n"
"    color: black;\n"
"    /*margin-left: -15px;\n"
"    margin-right: -2px;*/\n"
"}\n"
"\n"
"QComboBox QAbstractItemView{\n"
"    background: #2D2D30;\n"
"    color: #F1F1F1;\n"
"    selection-background-color: rgba(221, 124, 40, 120);\n"
"    border-radius: 5px;\n"
"    min-height: 40px;\n"
"\n"
"}\n"
"\n"
"QComboBox QAbstractItemView:QScrollbar::vertical {\n"
"    width:100px;\n"
"}\n"
"\n"
"QComboBox:!editable {\n"
"    margin-left: 1px;\n"
"    padding: 0px 10px 0px 10px;\n"
"    height: 23px;\n"
"    background-color: #3C3C3C;\n"
"}\n"
"\n"
"QComboBox::item{\n"
"    background-color: #3C3C3C;\n"
"}\n"
"\n"
"QComboBox::item::selected {\n"
"    background-color: #505050;\n"
"}\n"
"QToolBox::tab:QToolButton{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3C3C3C, stop:1 #505050);\n"
"     border: 1px solid  #5B5B5B;\n"
"\n"
"     border-radius:2px;\n"
"     padding-right: 10px;\n"
"\n"
"      color: #F1F1F1;\n"
"    font-size: 12px;\n"
"    padding: 3px;\n"
"}\n"
"QToolBox::tab:QToolButton{\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3C3C3C, stop:1 #505050);\n"
"     border: 1px solid  #5B5B5B;\n"
"\n"
"     border-radius:2px;\n"
"     padding-right: 10px;\n"
"\n"
"      color: #F1F1F1;\n"
"    font-size: 12px;\n"
"    padding: 3px;\n"
"}\n"
"\n"
"QPushButton{\n"
"     color: #F1F1F1;\n"
"     background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop:1 #505050);\n"
"     border: 1px solid #5B5B5B;\n"
"     border-radius: 5px;\n"
"     padding-left: 8px;\n"
"height: 18px;\n"
"    padding-right: 8px;\n"
" }\n"
"QPushButton:pressed{\n"
"        margin-top: 2px;\n"
"        margin-left: 2px;\n"
"}\n"
"QPushButton::disabled{\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"     border:1px solid #ADADAD;\n"
" }\n"
"\n"
"\n"
"QPushButton::checked{\n"
"    background: qlineargradient(\n"
"        x1: 0, y1: 1,\n"
"        x2: 0, y2: 0,\n"
"        stop: 0 #727272,\n"
"        stop: 1 #444444\n"
"    );\n"
"     border:1px solid  rgb(255, 120,00);\n"
"}\n"
"\n"
"QPushButton::focus {\n"
"    outline: None;\n"
"}\n"
" QGroupBox {\n"
"     border: 1px solid #ADADAD;\n"
"     border-radius: 4px;\n"
"     margin-top: 7px;\n"
"     padding: 0px\n"
" }\n"
" QGroupBox::title {\n"
"      subcontrol-origin: margin;\n"
"      left: 20px\n"
"  }\n"
"\n"
"QSplitter::handle:hover {\n"
"    background: #3C3C3C;\n"
" }\n"
"\n"
"\n"
"QGraphicsView{\n"
"    border-style: none;\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"      border: 2px solid #3C3C3C;\n"
"      background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0 #323232, stop:1 #505050);\n"
"      width: 12px;\n"
"      margin: 0px 0px 0px 0px;\n"
"  }\n"
"  QScrollBar::handle:vertical {\n"
"      background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #969696, stop:1 #CACACA);\n"
"     border-radius: 3px;\n"
"      min-height: 20px;\n"
"    padding: 15px;\n"
"  }\n"
"  QScrollBar::add-line:vertical {\n"
"      border: 0px solid grey;\n"
"      height: 0px;\n"
"  }\n"
"\n"
"  QScrollBar::sub-line:vertical {\n"
"      border: 0px solid grey;\n"
"      height: 0px;\n"
"  }\n"
"  QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"      background: none;\n"
"  }\n"
"\n"
"QScrollBar:horizontal {\n"
"    border: 2px solid #3C3C3C;\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #323232, stop:1 #505050);\n"
"    height: 12 px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #969696, stop:1 #CACACA);\n"
"   border-radius: 3px;\n"
"    min-width: 20px;\n"
"  padding: 15px;\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: 0px solid grey;\n"
"    height: 0px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: 0px solid grey;\n"
"    height: 0px;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"\n"
"\n"
"QSplitterHandle:hover {}\n"
"\n"
"QSplitter::handle:vertical{\n"
"    image: url(Views/UiFiles/images/vertical_splitter.png);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.3 #3C3C3C,  stop:0.5 #505050,\n"
"stop: 0.7 #3C3C3C);\n"
"    height: 15px;\n"
"}\n"
"\n"
"QSplitter::handle:vertical:pressed, QSplitter::handle:vertical:hover{\n"
"    image: url(Views/UiFiles/images/vertical_splitter_pressed.png);\n"
"    background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0.3 #3C3C3C,  stop:0.5 #5C5C5C,\n"
"stop: 0.7 #3C3C3C);\n"
"}\n"
"\n"
"QSplitter::handle:horizontal{\n"
"    image: url(Views/UiFiles/images/horizontal_splitter.png);\n"
"    background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.3 #3C3C3C,  stop:0.5 #505050,\n"
"stop: 0.7 #3C3C3C);\n"
"    width: 15px;\n"
"}\n"
"\n"
"QSplitter::handle:horizontal:pressed, QSplitter::handle:horizontal:hover{\n"
"    image: url(Views/UiFiles/images/horizontal_splitter_pressed.png);\n"
"    background: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:0, stop:0.3 #3C3C3C,  stop:0.5 #5C5C5C,\n"
"stop: 0.7 #3C3C3C);\n"
"}\n"
"\n"
"QSplitter::handle:hover {\n"
"    background: #3C3C3C;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    spacing: 10px;\n"
"    color: #F1F1F1;\n"
"     background: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #323232, stop:1 #505050);\n"
"    border: None;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QTableWidget {\n"
"    font-size: 12px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"\n"
"QFrame#main_frame {\n"
"    color: #F1F1F1;\n"
"    border: 1px solid #5B5B5B;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#calibration_mode_btn, #mask_mode_btn, #integration_mode_btn {\n"
"    font: normal 12px;\n"
"    border-radius: 1px;\n"
"}\n"
"\n"
"#calibration_mode_btn {\n"
"   border-top-right-radius:8px;\n"
"   border-bottom-right-radius: 8px;\n"
"}\n"
"#integration_mode_btn {\n"
"   border-top-left-radius:8px;\n"
"   border-bottom-left-radius: 8px;\n"
"}\n"
"")
        self.buttonBox = QtWidgets.QDialogButtonBox(ckshrnagui)
        self.buttonBox.setGeometry(QtCore.QRect(200, 471, 151, 21))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.generateOligosBtn = QtWidgets.QPushButton(ckshrnagui)
        self.generateOligosBtn.setGeometry(QtCore.QRect(1380, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.generateOligosBtn.setFont(font)
        self.generateOligosBtn.setObjectName("generateOligosBtn")
        self.inputSequence = QtWidgets.QLineEdit(ckshrnagui)
        self.inputSequence.setGeometry(QtCore.QRect(50, 30, 611, 41))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(18)
        self.inputSequence.setFont(font)
        self.inputSequence.setMouseTracking(False)
        self.inputSequence.setInputMask("")
        self.inputSequence.setMaxLength(29)
        self.inputSequence.setObjectName("inputSequence")
        self.verticalLayoutWidget = QtWidgets.QWidget(ckshrnagui)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 100, 1421, 95))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.senseLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.senseLabel.setFont(font)
        self.senseLabel.setStyleSheet("font: 18pt \"Courier New\";")
        self.senseLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.senseLabel.setObjectName("senseLabel")
        self.verticalLayout.addWidget(self.senseLabel)
        self.bondsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bondsLabel.setFont(font)
        self.bondsLabel.setStyleSheet("font: 18pt \"Courier New\";")
        self.bondsLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.bondsLabel.setObjectName("bondsLabel")
        self.verticalLayout.addWidget(self.bondsLabel)
        self.antisenseLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.antisenseLabel.setFont(font)
        self.antisenseLabel.setStyleSheet("font: 18pt \"Courier New\";")
        self.antisenseLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.antisenseLabel.setObjectName("antisenseLabel")
        self.verticalLayout.addWidget(self.antisenseLabel)
        self.tableWidget = QtWidgets.QTableWidget(ckshrnagui)
        self.tableWidget.setGeometry(QtCore.QRect(50, 230, 1421, 192))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.undoBtn = QtWidgets.QPushButton(ckshrnagui)
        self.undoBtn.setGeometry(QtCore.QRect(1400, 430, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.undoBtn.setFont(font)
        self.undoBtn.setObjectName("undoBtn")

        self.retranslateUi(ckshrnagui)
        self.buttonBox.accepted.connect(ckshrnagui.accept)
        self.buttonBox.rejected.connect(ckshrnagui.reject)
        QtCore.QMetaObject.connectSlotsByName(ckshrnagui)

    def retranslateUi(self, ckshrnagui):
        _translate = QtCore.QCoreApplication.translate
        ckshrnagui.setWindowTitle(_translate("ckshrnagui", "shRNA Oligo Design Tool"))
        self.generateOligosBtn.setText(_translate("ckshrnagui", "Go!"))
        self.inputSequence.setText(_translate("ckshrnagui", "AGGTCAAGGTCAAGGTCAAGGTCA"))
        self.inputSequence.setPlaceholderText(_translate("ckshrnagui", "Enter stem sequence here..."))
        self.senseLabel.setText(_translate("ckshrnagui", "testttttttttttttttt"))
        self.bondsLabel.setText(_translate("ckshrnagui", "testttttttttttttttt"))
        self.antisenseLabel.setText(_translate("ckshrnagui", "testttttttttttttttt"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ckshrnagui", "Sense"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ckshrnagui", "Anti-sense"))
        self.undoBtn.setText(_translate("ckshrnagui", "Undo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ckshrnagui = QtWidgets.QDialog()
    ui = Ui_ckshrnagui()
    ui.setupUi(ckshrnagui)
    ckshrnagui.show()
    sys.exit(app.exec_())

