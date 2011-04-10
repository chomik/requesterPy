#!/usr/bin/env python

import sys
from urllib import *
from httplib import *
from PyQt4 import QtCore, QtGui, uic

class Requester(QtGui.QMainWindow):
    def __init__(self, *args):
        super(Requester, self).__init__(*args)
        uic.loadUi('requester.ui', self)

    @QtCore.pyqtSlot()
    def on_send_clicked(self):
        self.request.clear()
        self.response.clear()

        params = urlencode(eval(str(self.params.displayText()).strip()))
        headers = eval(str(self.headers.displayText()).strip())
        conn = HTTPConnection("%s:%d" % (str(self.host.displayText()).strip(), self.port.value()))

        self.request.appendPlainText("params:")
        self.request.appendPlainText(self.params.displayText())
        self.request.appendPlainText("headers:")
        self.request.appendPlainText(self.headers.displayText())
        self.request.appendPlainText("host:")
        self.request.appendPlainText(self.host.displayText())
        self.request.appendPlainText("port:")
        self.request.appendPlainText(self.port.textFromValue(self.port.value()))
        self.request.appendPlainText("method:")
        self.request.appendPlainText(self.method.itemText(self.method.currentIndex()))
        self.request.appendPlainText("path:")
        self.request.appendPlainText(self.path.displayText())
        
        conn.request(str(self.method.itemText(self.method.currentIndex())),
            str(self.path.displayText()),
            params, headers)
        
        response = conn.getresponse()
        self.response.appendPlainText("%s %s" % (response.status, response.reason))
        for header in response.getheaders():
            self.response.appendPlainText("%s: %s" % header)
        self.response.appendPlainText(response.read())

app = QtGui.QApplication(sys.argv)
widget = Requester()
widget.show()
sys.exit(app.exec_())
