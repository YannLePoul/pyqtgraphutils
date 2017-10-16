import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtQml import QQmlApplicationEngine,QQmlEngine, QQmlComponent

from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.Qt import PYQT_VERSION_STR
from sip import SIP_VERSION_STR

print("Qt version:", QT_VERSION_STR)
print("SIP version:", SIP_VERSION_STR)
print("PyQt version:", PYQT_VERSION_STR)

from PyQt5.QtWidgets import QApplication
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph as pg
import pyqtgraphutils.pyqtgraphutils as pgutils

import numpy as np

from scipy import ndimage
from scipy import misc


app = QApplication([])

## Create window with GraphicsView widget
w = pg.GraphicsView()
w.show()
w.resize(800,800)
w.setWindowTitle('pyqtgraph example: Draw')

view = pg.ViewBox()
w.setCentralItem(view)

## lock the aspect ratio
view.setAspectLocked(True)

## Create image item
I =  misc.imread('/media/badboy/DATA_SSD/postdoc/SpotDisectionNew/imagingData/raw/909/brightfield/2016-12-21_909-old_370_9.tif')
Mask =  misc.imread('/media/badboy/DATA_SSD/postdoc/SpotDisectionNew/imagingData/aligned/909/BrMasks/2016-12-21_909-old_370_9.tif')
Mask = Mask.astype(float)/ 25
I = I.astype(float)
print(Mask.max())
print(Mask.min())

#Mask
# 10*np.ones((200,200))
imageItem = pg.ImageItem(I)
maskItem = pg.ImageItem(Mask)

view.addItem(imageItem)
view.addItem(maskItem)
maskItem.setZValue(10)  # make sure this image is on top
maskItem.setOpacity(0.5)
## Set initial view bounds
view.setRange(QtCore.QRectF(0, 0, Mask.shape[0], Mask.shape[1]))




proxy = pg.SignalProxy(view.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)
## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QApplication.instance().exec_()



