from Downloader import Downloader
from Plotter import Plotter

class StockApplication:
    downloader = Downloader()
    data = downloader.get_data()
    plotter = Plotter(data)
    plotter.plot()

