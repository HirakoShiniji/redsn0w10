import sys
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
import sys
import os

def jb():
    mbox = QMessageBox()
    mbox.setText("Sent pwned dfu mode.\nnot worked? make sure you are in dfu mode.\ncheck youtube for dfu instructions!")
    label.setText("Sent pwned dfu mode.\nnot worked? make sure you are in dfu mode.\ncheck youtube for dfu instructions!")
    btn.hide()
    ex.hide()
    extra.hide()
    stats.move(10,173)
    stats.setText("exploitation success.")
    
    os.system(os.path.dirname(os.path.abspath(__file__)) + "/ipwndfu -p")
    
    cancel.move(10,210)
    cancel.setText('Return')
    cancel.clicked.connect(cancels)
    cancel.show()
    mbox.exec_()
  
def cancels():
    mbox = QMessageBox()
    label.setText("Welcome to redsn0w 1.0.0b1\nCopyright 2007-2020 iPhone Dev-Team & Hirako. All rights reserved. Not\nfor commercial use.")
    creds.show()
    label.show()
    ex.show()
    stats.resize(600,20)
    stats.move(100,173)
    stats.setText("  begin jailbreak operation by clicking exploit.")
    btn.show()
    extra.show()
    cancel.hide()
    mbox.exec_()

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(476,529)
    w.setWindowTitle('redsn0w 1.0.0b1')
    app.setStyle('Fusion')
    cancel = QPushButton(w)
    label = QLabel(w)
    creds = QLabel(w)
    stats = QLabel(w)
    ex = QLabel(w)
    label.setText("Welcome to redsn0w 1.0.0b1\nCopyright 2007-2020 iPhone Dev-Team & Hirako. All rights reserved. Not\nfor commercial use.")
    label.move(10,6)
    creds.move(10,400)
    stats.move(100,173)
    stats.resize(600,20)
    ex.move(110,217)
    ex.setText("Everything else.")
    ex.show()
    creds.setText("\n\n\n\nSpecial Thanks to:\nargp,axi0mx,danyl931,jaywalker,kirb,littlelailo,nitoTV,nullpixel\npimskeks,qwertyoruip,sbingner,siguza")
    creds.resize(9999,110)
    creds.show()
    label.show()
    stats.setText("  begin jailbreak operation by clicking exploit.")
    stats.show()
   
   
    btn = QPushButton(w)
    extra = QPushButton(w)
    btn.setText('Exploit')
    extra.move(10,210)
    extra.setText("  Extras  ")
    
    extra.show()
    cancel.hide()
    btn.move(10,170)
    btn.show()
    btn.clicked.connect(jb)
  
   
    
    
    w.show()
    sys.exit(app.exec_())