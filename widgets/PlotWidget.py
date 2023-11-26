from matplotlib.backends.backend_qt import NavigationToolbar2QT
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class PlotWidget(FigureCanvasQTAgg):
    def __init__(self, parent=None, dpi=100, data=None, *args, **kwargs):
        fig = Figure(dpi=dpi)
        self.figure = fig
        self.axes = fig.add_subplot()
        self.axes.bar(data.get("x"), data.get("y"))
        self.axes.set_title('Частоты повторений букв')

        self.axes.set_ylabel('Частота')
        self.axes.set_xlabel('Буква')
        super(PlotWidget, self).__init__(fig)

        self.toolbar = NavigationToolbar2QT(self, self)
