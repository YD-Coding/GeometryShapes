
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMessageBox
from square import Square


class Ui_choose_Shape():
    def setupUi(self, choose_Shape):
        choose_Shape.setObjectName("choose_Shape")
        choose_Shape.resize(992, 701)
        choose_Shape.setWindowIcon(QtGui.QIcon('images/icon.ico'))
        self.centralwidget = QtWidgets.QWidget(choose_Shape)
        self.centralwidget.setObjectName("centralwidget")
        self.ClearButton = QtWidgets.QPushButton(self.centralwidget)
        self.ClearButton.setGeometry(QtCore.QRect(830, 580, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        self.ClearButton.setFont(font)
        self.ClearButton.setStyleSheet("QPushButton::hover\n"
"                             {\n"
"                             background-color : #C5EAEC;\n"
"                             }")
        self.ClearButton.setObjectName("ClearButton")
        self.square_Photo = QtWidgets.QLabel(self.centralwidget)
        self.square_Photo.setGeometry(QtCore.QRect(530, 240, 301, 271))
        self.square_Photo.setText("")
        self.square_Photo.setPixmap(QtGui.QPixmap("images/square.png"))
        self.square_Photo.setScaledContents(True)
        self.square_Photo.setObjectName("square_Photo")
        self.traingle_Button = QtWidgets.QPushButton(self.centralwidget)
        self.traingle_Button.setGeometry(QtCore.QRect(230, 510, 141, 41))
        self.traingle_Button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.traingle_Button.setFont(font)
        self.traingle_Button.setStyleSheet("background-color: #3498DB;\n"
" border: 3px solid black;\n"
"  border-radius: 6px;\n"
"\n"
"background-color: \n"
"white\n"
";\n"
"    min-width: 80px;\n"
"")
        self.traingle_Button.setObjectName("traingle_Button")
        self.square_Button = QtWidgets.QPushButton(self.centralwidget)
        self.square_Button.setGeometry(QtCore.QRect(610, 510, 141, 41))
        self.square_Button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.square_Button.setFont(font)
        self.square_Button.setStyleSheet("\n"
"\n"
"\n"
"background-color:#3498DB;\n"
"\n"
" border: 3px solid black;\n"
" border-radius: 6px;\n"
"\n"
"background-color: white;\n"
"    min-width: 80px;\n"
"\n"
"                             ")
    
        self.square_Button.setObjectName("square_Button")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 991, 691))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setStyleSheet("    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #00FFE4\n"
"\n"
", stop: 1 #dadbde);\n"
"    min-width:0px;\n"
"")
        self.background.setText("")
        self.background.setObjectName("background")
        self.traingle_Photo = QtWidgets.QLabel(self.centralwidget)
        self.traingle_Photo.setGeometry(QtCore.QRect(160, 240, 301, 251))
        self.traingle_Photo.setText("")
        self.traingle_Photo.setPixmap(QtGui.QPixmap("images/triangle.png"))
        self.traingle_Photo.setScaledContents(True)
        self.traingle_Photo.setObjectName("traingle_Photo")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(220, 80, 551, 121))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT Condensed Extra Bold")
        font.setPointSize(58)
        font.setBold(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setStyleSheet("\n"
"background-color: \n"
"white\n"
";\n"
"    min-width: 80px;\n"
"\n"
"border: 4px solid black\n"
";\n"
"    border-radius: 10px;")
        self.title.setAlignment(QtCore.Qt.AlignCenter)

        #* Square Screen Labels:
        #Photo:
        self.square_Photo2 = QtWidgets.QLabel(self.centralwidget)
        self.square_Photo2.setGeometry(QtCore.QRect(0, 70, 561, 501))
        self.square_Photo2.setPixmap(QtGui.QPixmap("images/square.png"))
        self.square_Photo2.setScaledContents(True)
        self.square_Photo2.setObjectName("square_Photo2")
        # Input:
        self.squareRib_input = QtWidgets.QLineEdit(self.centralwidget)
        self.squareRib_input.setGeometry(QtCore.QRect(230, 450, 91, 41))

        font2 = QtGui.QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.squareRib_input.setFont(font2)
        self.squareRib_input.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.squareRib_input.setAlignment(QtCore.Qt.AlignCenter)
        self.squareRib_input.setObjectName("squareRib_input")
        self.square_area_label = QtWidgets.QLabel(self.centralwidget)
        self.square_area_label.setGeometry(QtCore.QRect(540, 180, 391, 71))
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.square_area_label.setFont(font2)
        self.square_area_label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.square_area_label.setStyleSheet("background-color: white;\n"
" border: 4px solid black;")
        self.square_area_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.square_area_label.setObjectName("square_area_label")
        self.square_scope_label = QtWidgets.QLabel(self.centralwidget)
        self.square_scope_label.setGeometry(QtCore.QRect(540, 280, 391, 71))
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.square_scope_label.setFont(font2)
        self.square_scope_label.setStyleSheet("background-color: white;\n"
" border: 4px solid black;")
        self.square_scope_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.square_scope_label.setObjectName("square_scope_label")
        self.square_diagonals_label = QtWidgets.QLabel(self.centralwidget)
        self.square_diagonals_label.setGeometry(QtCore.QRect(540, 380, 391, 71))
        font2 = QtGui.QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.square_diagonals_label.setFont(font2 )
        self.square_diagonals_label.setStyleSheet("background-color: white;\n"
" border: 4px solid black;")
        self.square_diagonals_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.square_diagonals_label.setObjectName("square_diagonals_label")
        self.pushButton_submitSquare = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_submitSquare.setGeometry(QtCore.QRect(190, 540, 161, 61))
        font2 = QtGui.QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.pushButton_submitSquare.setFont(font2 )
        self.pushButton_submitSquare.setStyleSheet("QPushButton::hover\n"
"                             {\n"
"                             background-color : #62FFD4;\n"
"                             }")
        self.pushButton_submitSquare.setObjectName("pushButton_submitSquare")
        self.Back_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Back_Button.setGeometry(QtCore.QRect(20, 20, 81, 61))
        self.Back_Button.setAutoFillBackground(False)
        self.Back_Button.setStyleSheet("background-color: transparent;")
        self.Back_Button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/go_back.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Back_Button.setIcon(icon)
        self.Back_Button.setIconSize(QtCore.QSize(50, 50))
        self.Back_Button.setObjectName("Back_Button")
        self.square_title = QtWidgets.QLabel(self.centralwidget)
        self.square_title.setGeometry(QtCore.QRect(240, 40, 501, 71))
        font2  = QtGui.QFont()
        font2.setFamily("Tw Cen MT")
        font2.setPointSize(58)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setWeight(75)
        font2.setStrikeOut(False)
        self.square_title.setFont(font2 )
        self.square_title.setAlignment(QtCore.Qt.AlignCenter)
        self.square_title.setWordWrap(False)
        self.square_title.setObjectName("square_title")

# !

        self.title.setObjectName("title")
        self.background.raise_()
        self.square_Photo.raise_()
        self.ClearButton.raise_()
        self.traingle_Button.raise_()
        self.square_Button.raise_()
        self.traingle_Photo.raise_()
        self.title.raise_()
        self.square_Photo2.raise_()
        self.squareRib_input.raise_()
        self.square_area_label.raise_()
        self.square_scope_label.raise_()
        self.square_diagonals_label.raise_()
        self.pushButton_submitSquare.raise_()
        self.Back_Button.raise_()
        self.square_title.raise_()
        choose_Shape.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(choose_Shape)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 21))
        self.menubar.setObjectName("menubar")
        choose_Shape.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(choose_Shape)
        self.statusbar.setObjectName("statusbar")
        choose_Shape.setStatusBar(self.statusbar)

        self.retranslateUi(choose_Shape)
        QtCore.QMetaObject.connectSlotsByName(choose_Shape)
        
        

        self.win1_labels = [self.square_Photo, self.traingle_Photo, self.square_Button, self.traingle_Button, self.title]
        self.square_labels = [self.ClearButton, self.Back_Button,self.square_title ,self.square_Photo2,
         self.squareRib_input, self.square_area_label, self.square_diagonals_label, self.square_scope_label, self.pushButton_submitSquare]
        self.traingle_labels = [self.ClearButton, self.Back_Button]
        for label in self.square_labels:
            label.setHidden(True)
    def retranslateUi(self, choose_Shape):
        self.square_Button.clicked.connect(self.square_clicked)
        self.traingle_Button.clicked.connect(self.traingle_clicked)
        self.pushButton_submitSquare.clicked.connect(self.square_submit)
        self.Back_Button.clicked.connect(self.go_back_clicked)
        self.ClearButton.clicked.connect(self.clear_parameters)
        _translate = QtCore.QCoreApplication.translate
        
        choose_Shape.setWindowTitle(_translate("choose_Shape", "Geometry Shapes"))
        self.ClearButton.setText(_translate("choose_Shape", "Clear"))
        self.traingle_Button.setText(_translate("choose_Shape", "Triangle"))
        self.square_Button.setText(_translate("choose_Shape", "Square"))
        self.title.setText(_translate("choose_Shape", "Choose a Shape"))
        self.square_area_label.setText(_translate("choose_Shape", "Area(Square cm): "))
        self.square_scope_label.setText(_translate("choose_Shape", "Scope(cm): "))
        self.square_diagonals_label.setText(_translate("choose_Shape", "Diagonals Length: "))
        self.pushButton_submitSquare.setText(_translate("choose_Shape", "Submit"))
        self.square_title.setText(_translate("choose_Shape", "Square"))
    
    
    def go_back_clicked(self):
        for label in self.win1_labels:     
                label.setHidden(False)
        for label in self.square_labels:
                label.setHidden(True)
        for label in self.traingle_labels:
                label.setHidden(True)

    def square_clicked(self):
            for label in self.win1_labels:     
                label.setHidden(True)
            for label in self.square_labels:
                label.setHidden(False)


                       
    def traingle_clicked(self):
            for label in self.win1_labels:     
                label.setHidden(True)
            for label in self.traingle_labels:
                label.setHidden(False)
    @staticmethod
    def isFloat(number):
        if len(str(number).split('.')) > 1:
            return int(number) or True
        return("{:.2f}".format(number))
    
    def clear_parameters(self):
        self.square_area_label.setText(f"Area(Square cm): ")
        self.square_scope_label.setText(f"Scope(cm): ")
        self.square_diagonals_label.setText(f"Diagonals Length: ")
        self.squareRib_input.setText('')
    
    def toCommas(self, number):
        if self.isFloat(number):
            return "{:,}".format(number)
        else:
            splitted = str(number).split('.')
            intnumber = "{:,}".format(int(splitted[0]))
            return str(f"{intnumber}.{splitted[1]}")



    def square_submit(self):
        try:
            rib = float(self.squareRib_input.text())
            square = Square(rib)

            area = square.area()
            area = self.isFloat(area)
            area = self.toCommas(area)
            scope = square.scope()
            scope = self.isFloat(scope)
            scope = self.toCommas(scope)
            diagonal = square.diagonals()
            diagonal = self.isFloat(diagonal)
            diagonal = self.toCommas(diagonal)

            self.square_area_label.setText(f"Area(Square cm): {str(area)}")
            self.square_scope_label.setText(f"Scope(cm): {str(scope)}")
            self.square_diagonals_label.setText(f"Diagonals Length: {str(diagonal)}")
        except ValueError:
            error = QMessageBox()
            error.setWindowTitle("Error")
            error.setText("Please type a number!")
            error.setIcon(QMessageBox.Critical)

            x = error.exec_()

        
    

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    choose_Shape = QtWidgets.QMainWindow()
    ui = Ui_choose_Shape()
    ui.setupUi(choose_Shape)
    choose_Shape.show()
    sys.exit(app.exec_())
