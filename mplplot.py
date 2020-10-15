# ------------------------------------------------------
# -------------------- mplplot.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import*
import datetime
from datetime import*
from datetime import timedelta
from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure
import matplotlib.dates as mdates



class MplPlot(FigureCanvas):
    def __init__(self, parent=None, title='Title', xlabel='x label', ylabel='y label', dpi=80, hold=False):
        super(FigureCanvas, self).__init__(Figure())

        self.setParent(parent)
        self.figure = Figure(dpi=dpi)
        self.canvas = FigureCanvas(self.figure)
        
        self.fig = self.figure.add_subplot(111)
