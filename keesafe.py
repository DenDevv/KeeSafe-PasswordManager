import os
import sys
import base64
import hashlib

from PyQt5 import QtWidgets, QtCore, QtGui
from rsa import newkeys, PrivateKey, decrypt

from interfaces.system_dialogs import SystemDialog
from interfaces.table import TableData
from themes.dark_theme import Ui_MainWindow, Ui_OperData
from utils.keesafe_module import KeeSafe


class GUI(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        try:
            self.ui = Ui_MainWindow()

            self.icon_critical = QtWidgets.QMessageBox.Icon.Critical
            self.icon_warning = QtWidgets.QMessageBox.Icon.Warning
            self.icon_info = QtWidgets.QMessageBox.Icon.Information

            self.btn_ok = QtWidgets.QMessageBox.StandardButton.Ok
            self.btn_close = QtWidgets.QMessageBox.StandardButton.Close

            self.ks = KeeSafe()
            self.dialog = SystemDialog()
            self.t = TableData()

            self.ks.create_tables()
            
            if self.ks.get_master_key() is None:
                self.ui.create_master_key_window(self)
                self.ui.complete_masterkey.clicked.connect(self.create_masterkey)
            else:
                self.ui.login_master_key_window(self)
                self.ui.login_masterkey.clicked.connect(
                    lambda checked, method="mp": self.login(method)
                )
        except Exception as e:
            print("line 43: ", e)



    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                              ADDING A NEW DATA TO DATABASE                        ///
    # /////////////////////////////////////////////////////////////////////////////////////////
    def new_d(self):
        try:
            self.ui = Ui_MainWindow()
            self.new = Ui_OperData()
            self.newDialog = QtWidgets.QDialog()
            
            self.dialog = SystemDialog()
            self.t = TableData()
            
            self.new.new_data_window(self.newDialog)
            self.new.add_submit.clicked.connect(self.validate_new)

            self.newDialog.setWindowTitle("Add new data")
            self.newDialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
            self.newDialog.exec_()
        except Exception as e:
            print("line 66: ", e)


    def validate_new(self):
        try:
            name = self.new.add_name.text()
            login = self.new.add_login.text()
            password = self.new.add_password.text()
            url = self.new.add_url.text()

            if name != "" and login != "" and password != "" and url != "":
                if self.ks.show_all_data() != []:
                    db_name = self.ks.show_all_data()[0][1]

                    if db_name != name:
                        self.ks.add_new_data(name, login, password, url)
                        self.ui.setupUi(self, self.t.data_table())
                        self.connect_btns()
                        self.newDialog.close()
                    else:
                        self.dialog.dialog_handler("Same data error", "This name is already in base.", self.icon_warning, self.btn_close)
                else:
                    self.ks.add_new_data(name, login, password, url)
                    self.ui.setupUi(self, self.t.data_table())
                    self.connect_btns()
                    self.newDialog.close()
        except Exception as e:
            print("line 93: ", e)
    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                       EDNOF ADDING A NEW DATA TO DATABASE                         ///
    # /////////////////////////////////////////////////////////////////////////////////////////



    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                             EDITING A DATA OF DATABASE                            ///
    # /////////////////////////////////////////////////////////////////////////////////////////
    def edit_d(self):
        try:
            self.ui.login_master_key_window(self)
            self.ui.login_masterkey.clicked.connect(
                lambda checked, method="edit": self.login(method)
            )
        except Exception as e:
            print("line 110: ", e)

    
    def input_name(self):
        try:
            name_to_edit = self.edit.edit_name.text()

            if name_to_edit != "":
                db_name = self.ks.show_all_data()[0][1]

                if db_name == name_to_edit:
                    self.Dialog.close()
                    self.validate_edit(name_to_edit)
                else:
                    self.dialog.dialog_handler("Not same data error", "You entered encorrectly name.", self.icon_warning, self.btn_close)
        except Exception as e:
            print("line 126: ", e)


    def validate_edit(self, name):
        try:
            self.editDialog = QtWidgets.QDialog()

            db_login = self.ks.check_data(name)[0][0]
            db_url = self.ks.check_data(name)[0][2]
            db_encrypted_password = self.ks.check_data(name)[0][1]

            f2 = QtWidgets.QFileDialog.getOpenFileName()
            path = f2[0]

            with open(path, 'r') as f:
                privatekey = PrivateKey.load_pkcs1(f.read().encode())

            passw = base64.b64decode(db_encrypted_password)
            password = decrypt(passw, privatekey)

            self.edit2 = Ui_OperData()
            self.edit2.edit_data_window2(self.editDialog)
            self.edit2.edit_submit2.clicked.connect(self.validate_edited_data)

            self.edit2.edit_name2.setText(name)
            self.edit2.edit_login.setText(db_login)
            self.edit2.edit_password.setText(password.decode())
            self.edit2.edit_url.setText(db_url)
            self.row_id = self.ks.get_row_id(name)[0]

            self.editDialog.setWindowTitle("Edit data")
            self.editDialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
            self.editDialog.exec_()
        except Exception as e:
            print("line 160: ", e)


    def validate_edited_data(self):
        try:
            name = self.edit2.edit_name2.text()
            login = self.edit2.edit_login.text()
            password = self.edit2.edit_password.text()
            url = self.edit2.edit_url.text()
            
            self.ks.edit_data(name, login, password, url, self.row_id)
            self.ui.setupUi(self, self.t.data_table())
            self.connect_btns()
            self.editDialog.close()
        except Exception as e:
            print("line 175: ", e)
    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                      EDN OF EDITING A DATA OF DATABASE                            ///
    # /////////////////////////////////////////////////////////////////////////////////////////



    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                             DELETING A DATA OF DATABASE                           ///
    # /////////////////////////////////////////////////////////////////////////////////////////
    def delete_d(self):
        try:
            self.ui.login_master_key_window(self)
            self.ui.login_masterkey.clicked.connect(
                lambda checked, method="delete": self.login(method)
            )
        except Exception as e:
            print("line 192: ", e)


    def validate_delete(self):
        try:
            name = self.delete.delet_name.text()

            if name != "":
                if self.ks.check_data(name) != []:
                    self.ks.delete_data(name)
                    self.ui.setupUi(self, self.t.data_table())
                    self.connect_btns()
                    self.Dialog.close()
                else:
                    self.dialog.dialog_handler("Value None error", "No such name. Please check again.", self.icon_warning, self.btn_close)
        except Exception as e:
            print("line 208: ", e)
    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                       END OF DELETING A DATA OF DATABASE                           ///
    # /////////////////////////////////////////////////////////////////////////////////////////



    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                             COPY A DATA OF DATABASE                               ///
    # /////////////////////////////////////////////////////////////////////////////////////////
    def copy_d(self):
        try:
            self.ui.login_master_key_window(self)
            self.ui.login_masterkey.clicked.connect(
                lambda checked, method="copy": self.login(method)
            )
        except Exception as e:
            print("line 225: ", e)

    
    def validate_copy(self):
        try:
            name = self.copy.copy_passwd.text()
            db_name = self.ks.show_all_data()[0][1]

            if db_name == name:
                password = self.ks.check_data(name)[0][1]
            
                f2 = QtWidgets.QFileDialog.getOpenFileName()

                with open(f2[0], 'r') as f:
                    privatekey = PrivateKey.load_pkcs1(f.read().encode())

                passw = base64.b64decode(password)
                data = decrypt(passw, privatekey).decode()

                cb = QtWidgets.QApplication.clipboard()
                cb.clear(mode=cb.Clipboard)
                cb.setText(data, mode=cb.Clipboard)
                self.Dialog.close()

                self.dialog.dialog_handler("Successful", "Password copied!", self.icon_info, self.btn_ok)

            else:
                self.dialog.dialog_handler("Value None error", "No such name. Please check again.", self.icon_warning, self.btn_close)
        except Exception as e:
            print("line 254: ", e)
    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                       END OF COPY A DATA OF DATABASE                              ///
    # /////////////////////////////////////////////////////////////////////////////////////////



    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                                LOGIN BY MASTERKEY                                 ///
    # /////////////////////////////////////////////////////////////////////////////////////////
    def login(self, method):
        try:
            if os.path.exists("public.pem"):
                self.Dialog = QtWidgets.QDialog()
                salt_from_storage = self.ks.get_master_key()[0][:32]
                key_from_storage = self.ks.get_master_key()[0][32:]

                password = self.ui.login_masterkey_line.text()
                hashed_password = hashlib.pbkdf2_hmac(
                    'sha256',
                    password.encode(),
                    salt_from_storage, 
                    100000
                )
                
                if password != "":
                    if hashed_password == key_from_storage:
                        if method == "mp":                        
                            self.ui.setupUi(self, self.t.data_table())
                            self.connect_btns()

                        if method == "edit":
                            self.ui.setupUi(self, self.t.data_table())
                            self.edit = Ui_OperData()
                            self.connect_btns()
                            self.edit.edit_data_window(self.Dialog)
                            self.edit.edit_submit.clicked.connect(self.input_name)

                            self.Dialog.setWindowTitle("Edit data")
                            self.Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
                            self.Dialog.exec_()

                        if method == "delete":
                            self.ui.setupUi(self, self.t.data_table())
                            self.connect_btns()
                            self.delete = Ui_OperData()
                            self.delete.delete_data_window(self.Dialog)
                            self.delete.delete_submit.clicked.connect(self.validate_delete)

                            self.Dialog.setWindowTitle("Delete data")
                            self.Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
                            self.Dialog.exec_()

                        if method == "copy":
                            self.ui.setupUi(self, self.t.data_table())
                            self.connect_btns()
                            self.copy = Ui_OperData()
                            self.copy.copy_data_window(self.Dialog)
                            self.copy.copy_submit.clicked.connect(self.validate_copy)

                            self.Dialog.setWindowTitle("Copy password")
                            self.Dialog.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
                            self.Dialog.exec_()
                    else:
                        self.dialog.dialog_handler("Login Error", 'MasterKey is invalid!', self.icon_warning, self.btn_ok)
        except Exception as e:
            print("line 319: ", e)
    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                         END OF LOGIN BY MASTERKEY                                 ///
    # /////////////////////////////////////////////////////////////////////////////////////////

    

    def connect_btns(self):
        try:
            self.ui.new_data_btn.clicked.connect(self.new_d)

            if self.ks.show_all_data() != []:
                self.ui.edit_data_btn.clicked.connect(self.edit_d)
                self.ui.delete_data_btn.clicked.connect(self.delete_d)
                self.ui.copy_data_btn.clicked.connect(self.copy_d)
            else:
                style = ("QPushButton {\n"
                        "    font-family: \"Eras Bold ITC\";\n"
                        "    border-radius: 5px;\n"
                        "    background-color: #2C8171;\n"
                        "    color: #C9C9C9;\n"
                        "    font-size: 23px\n"
                        "}\n")

                self.ui.edit_data_btn.setDisabled(True)
                self.ui.delete_data_btn.setDisabled(True)
                self.ui.copy_data_btn.setDisabled(True)

                self.ui.edit_data_btn.setStyleSheet(style)
                self.ui.delete_data_btn.setStyleSheet(style)
                self.ui.copy_data_btn.setStyleSheet(style)
        except Exception as e:
            print("line 351: ", e)



    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                                   GENERATE KEYS                                   ///
    # /////////////////////////////////////////////////////////////////////////////////////////
    def create_key_files(self):
        try:
            publicKey, privateKey = newkeys(2048)
            save_privatekey, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save a private key", "private", "PEM files (*.pem)")
            
            if save_privatekey:
                with open(save_privatekey, "w+") as pr:
                    pr.write(privateKey.save_pkcs1().decode())

                with open('public.pem', 'w+') as pb:
                    pb.write(publicKey.save_pkcs1().decode())

                if not os.path.exists(save_privatekey) or not os.path.exists("public.pem"):
                    self.dialog.dialog_handler("Saving keys error", "Keys cannot be saved.", self.icon_critical, self.btn_close)
                    os.abort()

        except Exception as e:
            print("line 374: ", e)


    def create_masterkey(self):
        try:
            key = self.ui.masterkey_line.text()

            if key != "":
                self.create_key_files()
                
                self.ks.create_master_key(key)
                self.ui.setupUi(self, self.t.data_table())
                self.connect_btns()
        except Exception as e:
            print("line 391: ", e)
    # //////////////////////////////////////////////////////////////////////////////////////////
    # ///                             END OF GENERATE KEYS                                   ///
    # /////////////////////////////////////////////////////////////////////////////////////////


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # check if file with themes exists
    if not os.path.isdir("./images") or not os.path.isdir("./themes"):
        e = GUI()
        e.dialog.dialog_handler("Missing files error", 'Some important files are missing!', e.icon_warning, e.btn_close)
    else:
        win = GUI()
        win.setWindowTitle("KeeSafe - v 1.0")
        win.setWindowIcon(QtGui.QIcon("images/icon.jpg"))
        win.show()
        sys.exit(app.exec_())