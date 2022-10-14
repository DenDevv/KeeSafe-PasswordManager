from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def create_master_key_window(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: #2C3E50;")
        MainWindow.setFixedWidth(700)
        MainWindow.setFixedHeight(400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.masterkey_label = QtWidgets.QLabel(self.centralwidget)
        self.masterkey_label.setGeometry(QtCore.QRect(200, 60, 300, 30))
        self.masterkey_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.masterkey_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 30px;\n")
        self.masterkey_label.setObjectName("masterkey_label")
        self.masterkey_label.setText("Create a MasterKey")
        
        self.complete_masterkey = QtWidgets.QPushButton(self.centralwidget)
        self.complete_masterkey.setGeometry(QtCore.QRect(265, 280, 160, 60))
        self.complete_masterkey.setObjectName("complete_masterkey")
        self.complete_masterkey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.complete_masterkey.setStyleSheet("QPushButton {\n"
        "    font-family: \"Eras Bold ITC\";\n"
        "    border-radius: 10px;\n"
        "    background-color: #3db39e;\n"
        "    color: white;\n"
        "    font-size: 25px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3ca492;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3d9888;\n"
        "    color: white;\n"
        "}")
        self.complete_masterkey.setText("Complete")

        self.masterkey_line = QtWidgets.QLineEdit(self.centralwidget)
        self.masterkey_line.setGeometry(QtCore.QRect(140, 180, 421, 31))
        self.masterkey_line.setObjectName("masterkey_line")
        self.masterkey_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.masterkey_line.setStyleSheet(
            "color: white;\n"
            "font-family: \"Eras Bold ITC\";\n"
            "outline: none;\n"
            "background-color: #3C556E;\n"
            "border: 2px solid #5B81A6;\n"
            "border-radius: 5px;")

        MainWindow.setCentralWidget(self.centralwidget)

    
    def login_master_key_window(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: #2C3E50;")
        MainWindow.setFixedWidth(700)
        MainWindow.setFixedHeight(400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.masterkey_labell = QtWidgets.QLabel(self.centralwidget)
        self.masterkey_labell.setGeometry(QtCore.QRect(200, 60, 300, 30))
        self.masterkey_labell.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.masterkey_labell.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 30px;\n")
        self.masterkey_labell.setObjectName("masterkey_labell")
        self.masterkey_labell.setText("Enter a MasterKey")
        
        self.login_masterkey = QtWidgets.QPushButton(self.centralwidget)
        self.login_masterkey.setGeometry(QtCore.QRect(265, 280, 160, 60))
        self.login_masterkey.setObjectName("login_masterkey")
        self.login_masterkey.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.login_masterkey.setStyleSheet("QPushButton {\n"
        "    font-family: \"Eras Bold ITC\";\n"
        "    border-radius: 10px;\n"
        "    background-color: #3db39e;\n"
        "    color: white;\n"
        "    font-size: 25px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3ca492;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3d9888;\n"
        "    color: white;\n"
        "}")
        self.login_masterkey.setText("Sign in")

        self.login_masterkey_line = QtWidgets.QLineEdit(self.centralwidget)
        self.login_masterkey_line.setGeometry(QtCore.QRect(140, 180, 421, 31))
        self.login_masterkey_line.setObjectName("login_masterkey_line")
        self.login_masterkey_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.login_masterkey_line.setStyleSheet(
            "color: white;\n"
            "font-family: \"Eras Bold ITC\";\n"
            "outline: none;\n"
            "background-color: #3C556E;\n"
            "border: 2px solid #5B81A6;\n"
            "border-radius: 5px;")

        MainWindow.setCentralWidget(self.centralwidget)
        

    def setupUi(self, MainWindow, rows):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setStyleSheet("background-color: #2C3E50;")
        MainWindow.setFixedWidth(970)
        MainWindow.setFixedHeight(600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(320, 120, 627, 430)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(["id", "name", "login", "password", "url"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
        self.tableWidget.setStyleSheet("color: white;")
        
        for row in rows:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

            if rowPosition > row[0]:
                continue

            itemCount = 0
            self.tableWidget.setRowCount(rowPosition + 1)
            qtablewidgetitem = QtWidgets.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(rowPosition, qtablewidgetitem)
            self.tableWidget.verticalHeader().setVisible(False)

            for item in row:
                self.qtablewidgetitem = QtWidgets.QTableWidgetItem(self.tableWidget.item(rowPosition, itemCount))
                self.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem.setText(str(item))

                itemCount += 1

            rowPosition += 1

        self.logo_label = QtWidgets.QLabel(self.centralwidget)
        self.logo_label.setGeometry(QtCore.QRect(50, 310, 261, 21))
        self.logo_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logo_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.logo_label.setObjectName("logo_label")

        self.logo_label2 = QtWidgets.QLabel(self.centralwidget)
        self.logo_label2.setGeometry(QtCore.QRect(20, 350, 300, 31))
        self.logo_label2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logo_label2.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.logo_label2.setObjectName("logo_label2")

        pixmap = QtGui.QPixmap("images/logo.png")
        self.labelImage = QtWidgets.QLabel(self.centralwidget)
        self.labelImage.setGeometry(QtCore.QRect(60, 130, 150, 140))
        self.labelImage.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.labelImage.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "font-size: 20px;\n"
        "color: white;")
        self.labelImage.setObjectName("labelImage")
        self.labelImage.setPixmap(pixmap)
        self.labelImage.setScaledContents(True)

        style_btns = ("QPushButton {\n"
        "    font-family: \"Eras Bold ITC\";\n"
        "    border-radius: 5px;\n"
        "    background-color: #3db39e;\n"
        "    color: white;\n"
        "    font-size: 21px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    background-color: #3ca492;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    background-color: #3d9888;\n"
        "    color: white;\n"
        "}")

        self.new_data_btn = QtWidgets.QPushButton(self.centralwidget)
        self.new_data_btn.setGeometry(QtCore.QRect(320, 50, 100, 35))
        self.new_data_btn.setObjectName("new_data_btn")
        self.new_data_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.new_data_btn.setStyleSheet(style_btns)
        self.new_data_btn.setText("New")

        self.edit_data_btn = QtWidgets.QPushButton(self.centralwidget)
        self.edit_data_btn.setGeometry(QtCore.QRect(440, 50, 100, 35))
        self.edit_data_btn.setObjectName("edit_data_btn")
        self.edit_data_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_data_btn.setStyleSheet(style_btns)
        self.edit_data_btn.setText("Edit")

        self.delete_data_btn = QtWidgets.QPushButton(self.centralwidget)
        self.delete_data_btn.setGeometry(QtCore.QRect(560, 50, 100, 35))
        self.delete_data_btn.setObjectName("delete_data_btn")
        self.delete_data_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_data_btn.setStyleSheet(style_btns)
        self.delete_data_btn.setText("Delete")

        self.copy_data_btn = QtWidgets.QPushButton(self.centralwidget)
        self.copy_data_btn.setGeometry(QtCore.QRect(680, 50, 100, 35))
        self.copy_data_btn.setObjectName("copy_data_btn")
        self.copy_data_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copy_data_btn.setStyleSheet(style_btns)
        self.copy_data_btn.setText("Copy")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.logo_label.setText(_translate("MainWindow", "KeeSafe v 1.0"))
        self.logo_label2.setText(_translate("MainWindow", "Password Manager"))


class Ui_OperData(object):
    def new_data_window(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.setStyleSheet("background-color: #2C3E50;")
        MainWindow.setFixedWidth(600)
        MainWindow.setFixedHeight(400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        style1 = ("color: white;\n"
            "font-family: \"Eras Bold ITC\";\n"
            "outline: none;\n"
            "background-color: #3C556E;\n"
            "border: 2px solid #5B81A6;\n"
            "border-radius: 5px;")

        self.add_name_label = QtWidgets.QLabel(self.centralwidget)
        self.add_name_label.setGeometry(QtCore.QRect(50, 50, 90, 21))
        self.add_name_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_name_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.add_name_label.setObjectName("add_name_label")
        self.add_name_label.setText("Name:")

        self.add_name = QtWidgets.QLineEdit(self.centralwidget)
        self.add_name.setGeometry(QtCore.QRect(140, 50, 321, 31))
        self.add_name.setObjectName("add_name")
        self.add_name.setStyleSheet(style1)

        self.add_login_label = QtWidgets.QLabel(self.centralwidget)
        self.add_login_label.setGeometry(QtCore.QRect(50, 120, 261, 30))
        self.add_login_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_login_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.add_login_label.setObjectName("add_login_label")
        self.add_login_label.setText("Login:")

        self.add_login = QtWidgets.QLineEdit(self.centralwidget)
        self.add_login.setGeometry(QtCore.QRect(140, 120, 321, 31))
        self.add_login.setObjectName("add_login")
        self.add_login.setStyleSheet(style1)

        self.add_password_label = QtWidgets.QLabel(self.centralwidget)
        self.add_password_label.setGeometry(QtCore.QRect(50, 190, 261, 21))
        self.add_password_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_password_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.add_password_label.setObjectName("add_password_label")
        self.add_password_label.setText("Password:")

        self.add_password = QtWidgets.QLineEdit(self.centralwidget)
        self.add_password.setGeometry(QtCore.QRect(190, 185, 361, 31))
        self.add_password.setObjectName("add_password")
        self.add_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.add_password.setStyleSheet(style1)

        self.add_url_label = QtWidgets.QLabel(self.centralwidget)
        self.add_url_label.setGeometry(QtCore.QRect(50, 260, 261, 21))
        self.add_url_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.add_url_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.add_url_label.setObjectName("add_url_label")
        self.add_url_label.setText("URL:")

        self.add_url = QtWidgets.QLineEdit(self.centralwidget)
        self.add_url.setGeometry(QtCore.QRect(130, 258, 321, 31))
        self.add_url.setObjectName("add_url")
        self.add_url.setStyleSheet(style1)

        self.add_submit = QtWidgets.QPushButton(self.centralwidget)
        self.add_submit.setGeometry(QtCore.QRect(240, 330, 130, 40))
        self.add_submit.setObjectName("add_submit")
        self.add_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_submit.setStyleSheet("QPushButton {\n"
        "    font-family: \"Eras Bold ITC\";\n"
        "    border-radius: 10px;\n"
        "    background-color: #3db39e;\n"
        "    color: white;\n"
        "    font-size: 23px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3ca492;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3d9888;\n"
        "    color: white;\n"
        "}")
        self.add_submit.setText("Save")

    
    def delete_data_window(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.setStyleSheet("background-color: #2C3E50;")
        MainWindow.setFixedWidth(600)
        MainWindow.setFixedHeight(250)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        style1 = ("color: white;\n"
            "font-family: \"Eras Bold ITC\";\n"
            "outline: none;\n"
            "background-color: #3C556E;\n"
            "border: 2px solid #5B81A6;\n"
            "border-radius: 5px;")

        self.delete_label = QtWidgets.QLabel(self.centralwidget)
        self.delete_label.setGeometry(QtCore.QRect(140, 30, 400, 31))
        self.delete_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.delete_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.delete_label.setObjectName("delete_label")
        self.delete_label.setText("Enter a name for deleting")

        self.delet_name = QtWidgets.QLineEdit(self.centralwidget)
        self.delet_name.setGeometry(QtCore.QRect(140, 100, 321, 31))
        self.delet_name.setObjectName("delet_name")
        self.delet_name.setStyleSheet(style1)

        self.delete_submit = QtWidgets.QPushButton(self.centralwidget)
        self.delete_submit.setGeometry(QtCore.QRect(230, 170, 130, 40))
        self.delete_submit.setObjectName("delete_submit")
        self.delete_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.delete_submit.setStyleSheet("QPushButton {\n"
        "    font-family: \"Eras Bold ITC\";\n"
        "    border-radius: 10px;\n"
        "    background-color: #3db39e;\n"
        "    color: white;\n"
        "    font-size: 23px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3ca492;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3d9888;\n"
        "    color: white;\n"
        "}")
        self.delete_submit.setText("Delete")

    
    def edit_data_window(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.setStyleSheet("background-color: #2C3E50;")
        MainWindow.setFixedWidth(600)
        MainWindow.setFixedHeight(250)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        style1 = ("color: white;\n"
            "font-family: \"Eras Bold ITC\";\n"
            "outline: none;\n"
            "background-color: #3C556E;\n"
            "border: 2px solid #5B81A6;\n"
            "border-radius: 5px;")

        self.edit_label = QtWidgets.QLabel(self.centralwidget)
        self.edit_label.setGeometry(QtCore.QRect(140, 30, 400, 31))
        self.edit_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.edit_label.setObjectName("edit_label")
        self.edit_label.setText("Enter a name for editing")

        self.edit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_name.setGeometry(QtCore.QRect(140, 100, 321, 31))
        self.edit_name.setObjectName("edit_name")
        self.edit_name.setStyleSheet(style1)

        self.edit_submit = QtWidgets.QPushButton(self.centralwidget)
        self.edit_submit.setGeometry(QtCore.QRect(230, 170, 130, 40))
        self.edit_submit.setObjectName("edit_submit")
        self.edit_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_submit.setStyleSheet("QPushButton {\n"
        "    font-family: \"Eras Bold ITC\";\n"
        "    border-radius: 10px;\n"
        "    background-color: #3db39e;\n"
        "    color: white;\n"
        "    font-size: 23px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3ca492;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3d9888;\n"
        "    color: white;\n"
        "}")
        self.edit_submit.setText("Next")


    def edit_data_window2(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.setStyleSheet("background-color: #2C3E50;")
        MainWindow.setFixedWidth(600)
        MainWindow.setFixedHeight(400)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        style1 = ("color: white;\n"
            "font-family: \"Eras Bold ITC\";\n"
            "outline: none;\n"
            "background-color: #3C556E;\n"
            "border: 2px solid #5B81A6;\n"
            "border-radius: 5px;")

        self.edit_name_label = QtWidgets.QLabel(self.centralwidget)
        self.edit_name_label.setGeometry(QtCore.QRect(50, 50, 90, 21))
        self.edit_name_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_name_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.edit_name_label.setObjectName("edit_name_label")
        self.edit_name_label.setText("Name:")

        self.edit_name2 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_name2.setGeometry(QtCore.QRect(140, 50, 321, 31))
        self.edit_name2.setObjectName("edit_name2")
        self.edit_name2.setStyleSheet(style1)

        self.edit_login_label = QtWidgets.QLabel(self.centralwidget)
        self.edit_login_label.setGeometry(QtCore.QRect(50, 120, 261, 30))
        self.edit_login_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_login_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.edit_login_label.setObjectName("edit_login_label")
        self.edit_login_label.setText("Login:")

        self.edit_login = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_login.setGeometry(QtCore.QRect(140, 120, 321, 31))
        self.edit_login.setObjectName("edit_login")
        self.edit_login.setStyleSheet(style1)

        self.edit_password_label = QtWidgets.QLabel(self.centralwidget)
        self.edit_password_label.setGeometry(QtCore.QRect(50, 190, 261, 21))
        self.edit_password_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_password_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.edit_password_label.setObjectName("edit_password_label")
        self.edit_password_label.setText("Password:")

        self.edit_password = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_password.setGeometry(QtCore.QRect(190, 185, 361, 31))
        self.edit_password.setObjectName("edit_password")
        self.edit_password.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.edit_password.setStyleSheet(style1)

        self.edit_url_label = QtWidgets.QLabel(self.centralwidget)
        self.edit_url_label.setGeometry(QtCore.QRect(50, 260, 261, 21))
        self.edit_url_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.edit_url_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.edit_url_label.setObjectName("edit_url_label")
        self.edit_url_label.setText("URL:")

        self.edit_url = QtWidgets.QLineEdit(self.centralwidget)
        self.edit_url.setGeometry(QtCore.QRect(130, 258, 321, 31))
        self.edit_url.setObjectName("edit_url")
        self.edit_url.setStyleSheet(style1)

        self.edit_submit2 = QtWidgets.QPushButton(self.centralwidget)
        self.edit_submit2.setGeometry(QtCore.QRect(240, 330, 130, 40))
        self.edit_submit2.setObjectName("edit_submit2")
        self.edit_submit2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.edit_submit2.setStyleSheet("QPushButton {\n"
        "    font-family: \"Eras Bold ITC\";\n"
        "    border-radius: 10px;\n"
        "    background-color: #3db39e;\n"
        "    color: white;\n"
        "    font-size: 23px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3ca492;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3d9888;\n"
        "    color: white;\n"
        "}")
        self.edit_submit2.setText("Save")


    def copy_data_window(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.setStyleSheet("background-color: #2C3E50;")
        MainWindow.setFixedWidth(600)
        MainWindow.setFixedHeight(250)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        style1 = ("color: white;\n"
            "font-family: \"Eras Bold ITC\";\n"
            "outline: none;\n"
            "background-color: #3C556E;\n"
            "border: 2px solid #5B81A6;\n"
            "border-radius: 5px;")

        self.copy_label = QtWidgets.QLabel(self.centralwidget)
        self.copy_label.setGeometry(QtCore.QRect(160, 30, 400, 31))
        self.copy_label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.copy_label.setStyleSheet("font-family: \"Eras Bold ITC\";\n"
        "color: white;\n"
        "font-size: 25px;\n")
        self.copy_label.setObjectName("copy_label")
        self.copy_label.setText("Enter a name for copy")

        self.copy_passwd = QtWidgets.QLineEdit(self.centralwidget)
        self.copy_passwd.setGeometry(QtCore.QRect(140, 100, 321, 31))
        self.copy_passwd.setObjectName("copy_passwd")
        self.copy_passwd.setStyleSheet(style1)

        self.copy_submit = QtWidgets.QPushButton(self.centralwidget)
        self.copy_submit.setGeometry(QtCore.QRect(230, 170, 130, 40))
        self.copy_submit.setObjectName("copy_submit")
        self.copy_submit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copy_submit.setStyleSheet("QPushButton {\n"
        "    font-family: \"Eras Bold ITC\";\n"
        "    border-radius: 10px;\n"
        "    background-color: #3db39e;\n"
        "    color: white;\n"
        "    font-size: 23px\n"
        "}\n"
        "\n"
        "QPushButton:hover {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3ca492;\n"
        "    color: white;\n"
        "}\n"
        "\n"
        "QPushButton:pressed {\n"
        "    border-radius: 10px;\n"
        "    background-color: #3d9888;\n"
        "    color: white;\n"
        "}")
        self.copy_submit.setText("Copy")