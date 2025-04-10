from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(612, 479)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vertical_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vertical_layout.setObjectName("vertical_layout")

        self.input_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.input_label.setFont(font)
        self.input_label.setObjectName("input_label")
        self.vertical_layout.addWidget(self.input_label)

        self.input_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.input_text_edit.setFont(font)
        self.input_text_edit.setObjectName("input_text_edit")
        self.vertical_layout.addWidget(self.input_text_edit)

        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.setObjectName("button_layout")

        self.translate_button = QtWidgets.QPushButton(self.centralwidget)
        self.translate_button.setObjectName("translate_button")
        self.button_layout.addWidget(self.translate_button)

        self.attach_file_button = QtWidgets.QPushButton(self.centralwidget)
        self.attach_file_button.setObjectName("attach_file_button")
        self.button_layout.addWidget(self.attach_file_button)

        self.vertical_layout.addLayout(self.button_layout)

        self.output_label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.output_label.setFont(font)
        self.output_label.setObjectName("output_label")
        self.vertical_layout.addWidget(self.output_label)

        self.output_text_edit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.output_text_edit.setFont(font)
        self.output_text_edit.setReadOnly(True)
        self.output_text_edit.setObjectName("output_text_edit")
        self.vertical_layout.addWidget(self.output_text_edit)

        self.language_combo_box = QtWidgets.QComboBox(self.centralwidget)
        self.language_combo_box.setObjectName("language_combo_box")
        self.vertical_layout.addWidget(self.language_combo_box)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 612, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Translator App"))
        self.input_label.setText(_translate("MainWindow", "Enter Text"))
        self.translate_button.setText(_translate("MainWindow", "Translate"))
        self.attach_file_button.setText(_translate("MainWindow", "Attach File"))
        self.output_label.setText(_translate("MainWindow", "Translation"))
