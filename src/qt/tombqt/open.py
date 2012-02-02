import sys

from PyQt4 import QtCore, QtGui

from ui_open_tombfile import Ui_tombfile
from ui_open_keymethod import Ui_keymethod
from ui_open_success import Ui_success
from ui_open_opening import Ui_opening

from tomblib.tomb import Tomb
from tomblib.undertaker import Undertaker

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class TombfilePage(QtGui.QWizardPage):
    def __init__(self, *args, **kwargs):
        QtGui.QWizardPage.__init__(self, *args)
        self.ui = Ui_tombfile()
        self.ui.setupUi(self)
        if 'tombfile' in kwargs and kwargs['tombfile'] is not None:
            self.ui.tomb_line.setText(kwargs['tombfile'])
        self.ui.tomb_browse.clicked.connect(self.on_tomb_location_clicked)
    def on_tomb_location_clicked(self, *args, **kwargs):
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Select Tomb',
                filter="Tomb (*.tomb)")
        self.ui.tomb_line.setText(filename)

class MethodPage(QtGui.QWizardPage):
    def __init__(self, *args, **kwargs):
        QtGui.QWizardPage.__init__(self, *args, **kwargs)
        self.ui = Ui_keymethod()
        self.ui.setupUi(self)
        self.group = group = QtGui.QButtonGroup()
        for radio in self.children():
            if type(radio) == QtGui.QRadioButton:
                group.addButton(radio)

    def initializePage(self):
        self.found = Undertaker.check( str('near://' + self.wizard().get_tombfile()) ) or []
        box = self.ui.radio_layout

        for key in self.found:
            radio = QtGui.QRadioButton('Automatically found: ' + key, parent=self)
            radio.setChecked(True)
            radio.setProperty('path', key)
            box.insertWidget(0, radio)
            self.group.addButton(radio)


    def nextId(self):
        '''Virtual method reimplemented to decide next page'''
#FIXME: detect if this is called on _incoming_ or _outgoing_
#FIXME: this seem to be called multiple times
        if self.ui.usb.isChecked():
            return TombOpenWizard.USB_PAGE
#if no standard method, it is the "automatically detected" path
        return TombOpenWizard.OPENING_PAGE


class SuccessPage(QtGui.QWizardPage):
    def __init__(self, *args, **kwargs):
        QtGui.QWizardPage.__init__(self, *args, **kwargs)
        self.ui = Ui_success()
        self.ui.setupUi(self)

class OpeningPage(QtGui.QWizardPage):
    def __init__(self, *args, **kwargs):
        QtGui.QWizardPage.__init__(self, *args, **kwargs)
        self.ui = Ui_opening()
        self.ui.setupUi(self)
        self.parent().currentIdChanged.connect(self.on_change)

    def on_change(self, id):
        '''Called when the user arrives to this page'''
#FIXME: this should be done in a "opening..." page, not success!
        if id != TombOpenWizard.OPENING_PAGE:
            return
        path = self.wizard().get_tombkeyfile()
        print 'path is', path
        if Tomb.open(self.wizard().get_tombfile(), Undertaker.pipe(path)):
            self.wizard().next()
        else:
            QtCore.qCritical( 'Cannot open the tomb' )
            sys.exit(1)

class TombOpenWizard(QtGui.QWizard):
    TOMBFILE_PAGE=1
    METHOD_PAGE=2
    OPENING_PAGE=30
    SUCCESS_PAGE=99
    USB_PAGE=20
    def __init__(self, *args, **kwargs):
        QtGui.QWizard.__init__(self, *args)
        self.setPage(TombOpenWizard.TOMBFILE_PAGE,
                TombfilePage(self, tombfile = kwargs['tombfile']
                    if 'tombfile' in kwargs else None))
        self.setPage(TombOpenWizard.METHOD_PAGE, MethodPage(self))
        self.setPage(TombOpenWizard.OPENING_PAGE, OpeningPage(self))
        self.setPage(TombOpenWizard.SUCCESS_PAGE, SuccessPage(self))
        if 'tombfile' in kwargs and kwargs['tombfile'] is not None:
            self.setStartId(TombOpenWizard.METHOD_PAGE)

    def get_tombfile(self):
        page = self.page(TombOpenWizard.TOMBFILE_PAGE)
        return page.ui.tomb_line.text()

    def get_tombkeyfile(self):
        page = self.page(TombOpenWizard.METHOD_PAGE)
        button = page.group.checkedButton()
        path = button.property('path').toPyObject()
        if path is not None:
            return path
        #TODO: this should depend on selected method
        path = QtGui.QFileDialog.getOpenFileName(self, 'Key file',
                filter="Tomb keys (*.tomb.key);;Buried keys (*.jpeg)")
        path = 'file://' + path
        button.setProperty('path', path)
        return path


        

def run_open_wizard():
    app = QtGui.QApplication(sys.argv)
    window = TombOpenWizard(tombfile=sys.argv[1] if len(sys.argv) > 1 else None)
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    Undertaker.undertakerexec = '/home/davide/coding/projects/tomb/src/undertaker'
    Tomb.tombexec = '/home/davide/coding/projects/tomb/src/tomb'
    run_open_wizard()






