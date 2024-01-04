import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pyhrv as hrv


class FrequencyDomain:
    """
    @Author: Damian Pietroń,
    @Contact: 275277@student.pwr.edu.pl,
    @Licence: MIT,
    @Version: 0.0.1,
    @Last update: 03.01.2020r.
    """
    """
    This class is used to calculate frequency domain parameters.
    
    Attributes
    ----------
    signal : array
        The signal (filtered).
    sampling_frequency : int
        The sampling frequency of the signal.
    window_size : int
        The size of the window.
    overlap : int
        The overlap of the window.
        
    Methods
    -------
    VLF()
        Calculates peak in a Very Low Frequency (VLF) band [Hz].
    LF()
        Calculates peak in a Low Frequency (VLF) band [Hz].
    HF()
        Calculates peak in a High Frequency (VLF) band [Hz].
    LFHF()
        Calculates the LF/HF ratio of the signal.
    pVLF()
        Calculates absolute power of the Very Low Frequency (VLF) band [ms^2].
    _total_power()
        Calculates the total power of the signal [ms^2].
    pLF()
        Calculates absolute power of the Low Frequency (LF) band [ms^2].
    pHF()
        Calculates absolute power of the High Frequency (HF) band [ms^2].
    prcVLF()
        Calculates relative power of the Very Low Frequency (VLF) band [%].
    _relative_power()
        Calculates the relative power of the signal [%].
    prcLF()
        Calculates relative power of the Low Frequency (LF) band [%].
    prcHF()
        Calculates relative power of the High Frequency (HF) band [%].
    nLF()
        Calculates normalized power of the Low Frequency (LF) band.
    nHF()
        Calculates normalized power of the High Frequency (HF) band.
    """
    def __init__(self, signal, sampling_frequency, window_size, overlap):
        self.signal = signal
        self.sampling_frequency = sampling_frequency
        self.window_size = window_size
        self.overlap = overlap

    def VLF(self):
        """
       Calculates peak in a Very Low Frequency (VLF) band [Hz].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The VLF power of the signal.

        Raises
        ------
        None

        """
        return hrv.frequency_domain.welch_psd(
            self.signal, self.sampling_frequency,
            method='welch',
            interp_freq=4,
            window='hann',
            nperseg=256,
            noverlap=128,
            nfft=None,
            detrend='constant',
            normalize=True,
            skewness=True,
            kurtosis=True,
            show=False,
            legend=False,
            saveas=None,
            show_param=False, )[0]

    def LF(self):
        """
        Calculates peak in a Low Frequency (VLF) band [Hz].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The LF power of the signal.

        Raises
        ------
        None

        """
        return hrv.frequency_domain.welch_psd(
            self.signal, self.sampling_frequency,
            method='welch',
            interp_freq=4,
            window='hann',
            nperseg=256,
            noverlap=128,
            nfft=None,
            detrend='constant',
            normalize=True,
            skewness=True,
            kurtosis=True,
            show=False,
            legend=False,
            saveas=None,
            show_param=False, )[1]

    def HF(self):
        """
        Calculates peak in a High Frequency (VLF) band [Hz].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The HF power of the signal.

        Raises
        ------
        None

        """
        return hrv.frequency_domain.welch_psd(
            self.signal, self.sampling_frequency,
            method='welch',
            interp_freq=4,
            window='hann',
            nperseg=256,
            noverlap=128,
            nfft=None,
            detrend='constant',
            normalize=True,
            skewness=True,
            kurtosis=True,
            show=False,
            legend=False,
            saveas=None,
            show_param=False, )[2]

    def LFHF(self):
        """
        Calculates the LF/HF ratio of the signal.

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The LF/HF ratio of the signal.

        Raises
        ------
        None

        """
        return self.LF() / self.HF()

    def pVLF(self):
        """
        Calculates absolute power of the Very Low Frequency (VLF) band [ms^2].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The absolute power of the VLF band.

        Raises
        ------
        None

        """

        return self.VLF() / self._total_power()

    def _total_power(self):
        """
        Calculates the total power of the signal [ms^2].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The total power of the signal.

        Raises
        ------
        None

        """
        return self.VLF() + self.LF() + self.HF()

    def pLF(self):
        """
        Calculates absolute power of the Low Frequency (LF) band [ms^2].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The absolute power of the LF band.

        Raises
        ------
        None

        """
        return self.LF() / self._total_power()

    def pHF(self):
        """
        Calculates absolute power of the High Frequency (HF) band [ms^2].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The absolute power of the HF band.

        Raises
        ------
        None

        """
        return self.HF() / self._total_power()

    def prcVLF(self):
        """
        Calculates relative power of the Very Low Frequency (VLF) band [%].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The relative power of the VLF band.

        Raises
        ------
        None

        """
        return self.pVLF() / self._relative_power("VLF")

    def _relative_power(self, caller: str):
        """
        Calculates the relative power of the signal [%].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The relative power of the signal.

        Raises
        ------
        None

        """
        if caller == "VLF":
            return self._total_power() * 100
        elif caller == "LF":
            return self._total_power() * 100
        elif caller == "HF":
            return self._total_power() * 100
        else:
            raise ValueError("Invalid caller.")

    def prcLF(self):
        """
        Calculates relative power of the Low Frequency (LF) band [%].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The relative power of the LF band.

        Raises
        ------
        None

        """
        return self.pLF() / self._relative_power("LF")

    def prcHF(self):
        """
        Calculates relative power of the High Frequency (HF) band [%].

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The relative power of the HF band.

        Raises
        ------
        None

        """
        return self.pHF() / self._relative_power("HF")

    def nLF(self):
        """
        Calculates normalized power of the Low Frequency (LF) band.

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The normalized power of the LF band.

        Raises
        ------
        None

        """
        return self.LF() / (self.LF() + self.HF())

    def nHF(self):
        """
        Calculates normalized power of the High Frequency (HF) band.

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        float: The normalized power of the HF band.

        Raises
        ------
        None

        """
        return self.HF() / (self.LF() + self.HF())


if __name__ == '__main__':
    time = np.arange(0, 10, 0.01)
    signal = np.sin(time)
    frequency_domain = FrequencyDomain(signal, 100, 256, 128)
    print(frequency_domain.VLF())
    print(frequency_domain.LF())
    print(frequency_domain.HF())
    print(frequency_domain.LFHF())
    print(frequency_domain.pVLF())
    print(frequency_domain.pLF())
    print(frequency_domain.pHF())
    print(frequency_domain.prcVLF())
    print(frequency_domain.prcLF())
    print(frequency_domain.prcHF())
    print(frequency_domain.nLF())
    print(frequency_domain.nHF())





