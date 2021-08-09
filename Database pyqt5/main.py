
from PyQt5.QtWidgets import *
import sys
import MySQLdb
from PyQt5.uic import loadUiType
ui,_ = loadUiType('UI Design.ui')


class MainApp(QMainWindow,ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()

    def open_database(self):
        self.statusBar().showMessage('')
        self.tabWidget.setCurrentIndex(0)

    def attribute(self):
        self.statusBar().showMessage('')
        self.tabWidget.setCurrentIndex(1)

    def values(self):
        self.statusBar().showMessage('')
        self.db_attribute()
        self.tabWidget.setCurrentIndex(2)



    def Handel_UI_Changes(self):
        self.tabWidget.tabBar().setVisible(False)



    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.db_database)
        self.pushButton_2.clicked.connect(self.values)
        self.pushButton_3.clicked.connect(self.db_add)
        self.pushButton_4.clicked.connect(self.attribute)



    def db_database(self):
        try:
            db_name=self.lineEdit.text()
            global dbs
            dbs=db_name
            self.db = MySQLdb.connect(host='localhost', user='root', password='root')
            print("done1")
            self.cur = self.db.cursor()
            print("done2")
            self.cur.execute("CREATE DATABASE {} ".format(db_name))
            print("done")
            self.attribute()
            self.statusBar().showMessage('Done')
            self.lineEdit.setText('')
        except:
            self.statusBar().showMessage('ERROR')

    def db_attribute(self):
        try:
            table_name = self.lineEdit_2.text()
            global tablename
            tablename=table_name
            self.lineEdit_2.setText('')
            self.statusBar().showMessage('Done')
        except:
            self.statusBar().showMessage('Table Already present')

    def db_add(self):
        try:
            attri1 = self.lineEdit_3.text()
            type1 = self.comboBox.currentText()
            num1 = self.lineEdit_5.text()
            attri2 = self.lineEdit_6.text()
            type2 = self.comboBox_2.currentText()
            num2 = self.lineEdit_8.text()
            attri3 = self.lineEdit_9.text()
            type3 = self.comboBox_3.currentText()
            num3 = self.lineEdit_11.text()
            attri4 = self.lineEdit_12.text()
            type4 = self.comboBox_4.currentText()
            num4 = self.lineEdit_14.text()

            print(dbs)
            print(tablename)
            self.db = MySQLdb.connect(host='localhost', user='root', password='root', db=dbs)
            print(dbs)
            print(tablename)
            self.cur = self.db.cursor()
            self.cur.execute('''CREATE TABLE {0}(
                                {1} {2}({3}),
                                {4} {5}({6}),
                                {7} {8}({9}),
                                {10} {11}({12}));'''.format(tablename,attri1,type1,num1,attri2,type2,num2,attri3,type3,num3,attri4,type4,num4))
            print("done")
            self.statusBar().showMessage('Done')
            self.lineEdit_3.setText('')
            self.lineEdit_5.setText('')
            self.lineEdit_6.setText('')
            self.lineEdit_8.setText('')
            self.lineEdit_9.setText('')
            self.lineEdit_11.setText('')
            self.lineEdit_12.setText('')
            self.lineEdit_14.setText('')

        except:
            self.statusBar().showMessage('ERROR')





def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
