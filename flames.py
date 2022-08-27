from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    fname=''
    sname=''
    p1_list=[]
    p2_list=[]
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 640)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.bg = QtWidgets.QLabel(self.centralwidget)
        self.bg.setGeometry(QtCore.QRect(-30, -30, 521, 711))
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("flames poster.png"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMidLineWidth(3)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(70, 250, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 220, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setMidLineWidth(3)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setObjectName("label_2")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(260, 250, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 350, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setMidLineWidth(3)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(230, 320, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setMidLineWidth(3)
        self.label_4.setTextFormat(QtCore.Qt.PlainText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 260, 16, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setMidLineWidth(3)
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(190, 380, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setMidLineWidth(3)
        self.label_6.setText("")
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setObjectName("label_6")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 400, 481, 221))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setMidLineWidth(3)
        self.label_7.setText("")
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setObjectName("label_7")
        
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 530, 111, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.calculate)
        self.label_7.mousePressEvent = self.delevry
        
        
    def delevry(self,event):
        self.textEdit.setText("")
        self.textEdit_2.setText("")
        self.label_6.setText("")
        
        
    def remove_match_char(self,list1, list2):
        for i in range(len(list1)) :
            for j in range(len(list2)) :
                if list1[i] == list2[j] :
                    c = list1[i]
                    list1.remove(c)
                    list2.remove(c)
                    list3 = list1 + ["*"] + list2
                    return [list3, True]
                
        list3 = list1 + ["*"] + list2
        return [list3, False]
        
    def calculate(self):
        self.fname = self.textEdit.toPlainText()
        self.sname = self.textEdit_2.toPlainText()
        self.fname = self.fname.lower()
        self.sname = self.sname.lower()
        self.fname.replace(" ","")
        self.sname.replace(" ","")
        self.p1_list = list(self.fname)
        self.p2_list = list(self.sname)
        proceed = True
        while proceed:
            ret_list = self.remove_match_char(self.p1_list, self.p2_list)
            con_list = ret_list[0]
            proceed = ret_list[1]
            star_index = con_list.index("*")
            p1_list = con_list[ : star_index]

            p2_list = con_list[star_index + 1 : ]

        count = len(p1_list) + len(p2_list)

        result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

        while len(result) > 1 :
            split_index = (count % len(result) - 1)

            if split_index >= 0 :

                right = result[split_index + 1 : ]
                left = result[ : split_index]

                result = right + left

            else :
                result = result[ : len(result) - 1]

        self.label_6.setText(result[0])
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "1st Name:"))
        self.label_2.setText(_translate("MainWindow", "2nd Name:"))
        self.label_3.setText(_translate("MainWindow", "Your Relation"))
        self.label_4.setText(_translate("MainWindow", "="))
        self.label_5.setText(_translate("MainWindow", "+"))
        self.pushButton.setText(_translate("MainWindow", "Find Relation"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
