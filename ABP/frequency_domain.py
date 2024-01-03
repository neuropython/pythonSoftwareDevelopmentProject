import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pyhrv as hrv
class FrequencyDomain:
    def __init__(self, signal, sampling_frequency, window_size, overlap):
        self.signal = signal
        self.sampling_frequency = sampling_frequency
        self.window_size = window_size
        self.overlap = overlap

