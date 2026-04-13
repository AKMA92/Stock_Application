import pandas as pd
import matplotlib.pyplot as plt

class Plotter:
    data = None

    def init(self, data):
        self.data = data

    def plot(self):
        df = pd.DataFrame(self.data)
        df.plot()
        plt.show()