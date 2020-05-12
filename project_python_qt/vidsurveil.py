# This Python file uses the following encoding: utf-8
import subprocess
import sys
import PyQt5
import functools
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

def clickable(widget):

    class Filter(QObject):

        clicked = pyqtSignal()
         
        def eventFilter(self, obj, event):
            
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        # The developer can opt for .emit(obj) to get the object within the slot.
                        return True
           
            return False
    
    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

click = '/Users/iseongmin/Downloads/qt_projects/project_python_qt/file_dialog.ui'
#click = '/Users/iseongmin/Downloads/gui/application.ui'
class vidsurveil(QDialog):
    def __init__(self):
        #super().__init__()
        QDialog.__init__(self, None)
        #QDialog.__init__(self, None)
        uic.loadUi(click, self)

        #self.pushButton.clicked.connect(self.select_Files)
        #self.pushButton_2.clicked.connect(self.prepare_videos)
        #self.label_3.mousePressEvent = functools.partial(self.select_Files, self.label_3)
        #self.label_4.mousePressEvent = functools.partial(self.prepare_videos, self.label_4)
        #self.label_5.mousePressEvent = functools.partial(self.extract_features, self.label_5)
        #self.label_2.clicked.connect(self.select_Files)
        #self.label_3.clicked.connect(self.prepare_videos)
        #self.label_5.clicked.connect(self.extract_features)
        #pass  # call __init__(self) of the custom base class here

        clickable(self.label_3).connect(self.select_Files)
        clickable(self.label_4).connect(self.prepare_videos)
        clickable(self.label_5).connect(self.extract_features)

        #layout = QGridLayout(self)
        #layout.addWidget(self.label_2) 
        layout3 = self.verticalLayout_3
        layout4 = self.verticalLayout_4
        layout5 = self.verticalLayout_5

        layout3.addWidget(self.label_3)
        layout4.addWidget(self.label_4)
        layout5.addWidget(self.label_5)
        
        

    def select_Files(self):
        fname = QFileDialog.getOpenFileName(self)

        #label.setText(fname[0])
        result = subprocess.Popen(['cp', fname[0], '/home/callbarian/C3D/videos'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #result = subprocess.Popen(['cp', fname[0], '/Users/iseongmin/Downloads/qt_projects/project_python_qt'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out = result.communicate()
        result_message = out[0].decode()

        #if no error message is returned, then the string should be empty
        if not result_message.strip():
            msg = QMessageBox()
            msg.setWindowTitle("Move Success")
            msg.setText("Files has been successfully moved!")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

    def prepare_videos(self):
        #print("hi")
        result = subprocess.Popen(['python', '/home/callbarian/C3D/C3D-v1.0/examples/c3d_feature_extraction/run_feature_extraction.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        #result = subprocess.Popen(['python', '/Users/iseongmin/Downloads/qt_projects/application/application.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out= result.communicate()

    def extract_features(self):
        #print("hi")
        result = subprocess.Popen(['source', '/home/callbarian/C3D/C3D-v1.0/examples/switch_environment.sh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out = result.communicate()
        result_message = out[0].decode()
        if(result_message.split('::')[1]) is 'Anaconda, Inc.':
            msg = QMessageBox()
            msg.setWindowTitle("C3D to Anomaly")
            msg.setText("switch environment successfully")
            msg.setStandardButtons(QMessageBox.Ok)
            x = msg.exec_()

        result = subprocess.Popen(['python', '/home/callbarian/AnomalyDetectionCVPR2018-master/Demo_GUI.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out = result.communicate()

if __name__ == "__main__":
    app = QApplication([])
    window = vidsurveil()
    window.show()
    sys.exit(app.exec_())