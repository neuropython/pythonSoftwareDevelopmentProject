from frequency_domain import FrequencyDomain as FD
from _signal_preprocessing import SignalPreprocessing as SP
from time_domain import TimeDomain as TD
import matplotlib.pyplot as plt
class Plotting:

    def __init__(self, signal, time):
        self.signal = signal
        self.time = time
        self.Sp = SP(self.signal)
        self.Td = TD(self.time, self.Sp)
        self.Fd = FD(self.Sp, 200, 256, 128)


    def plot_signal(self):
        plt.plot(self.time, self.signal)
        plt.show()
