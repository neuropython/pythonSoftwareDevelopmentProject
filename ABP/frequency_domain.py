# -*- coding: utf-8 -*
from typing import Any
import biosppy
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
import pyhrv
from sympy.physics.quantum.identitysearch import scipy
import ABP._signal_preprocessing as SP


class FrequencyDomain:
    """
    @Author: Damian Pietroń,
    @Contact: 275277@student.pwr.edu.pl,
    @Licence: MIT,
    @Version: 0.0.1,
    @Last update: 06.01.2024r.
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
        """
        Parameters
        ----------
        self : FrequencyDomain

        signal : array
            The signal (filtered).
        sampling_frequency : int
            The sampling frequency of the signal.
        window_size : int
            The size of the window.
        overlap : int
            The overlap of the window.

        Returns
        -------
        None
        """
        self.signal = SP.SignalPreprocessing(signal).signal[0]
        self.r_peaks = biosppy.signals.abp.abp(signal=self.signal, sampling_rate=200, show = False)[2]
        self.sampling_frequency = sampling_frequency
        self.window_size = window_size
        self.overlap = overlap
        self._check_signal()
        self._calculate_power_in_band


    # def __str__(self):
    #     string = (f'{{"VLF": {self.VLF()}, "LF": {self.LF()}, "HF": {self.HF()}, "LFHF": {self.LFHF()}, '
    #           f'"pVLF": {self.pVLF()}, "pLF": {self.pLF()}, "pHF": {self.pHF()}, "prcVLF": {self.prcVLF()}, '
    #           f'"prcLF": {self.prcLF()}, "prcHF": {self.prcHF()}, "nLF": {self.nLF()}, "nHF": {self.nHF()}}}')
    #     return string

    def _check_signal(self):
        """
        Checks if the signal is correct.

        Parameters
        ----------
        self : FrequencyDomain

        Returns
        -------
        None

        Raises
        ------
        ValueError
            If the signal is not correct.

        """
        if self.signal is None:
            raise ValueError("Invalid signal.")
        
    def _calculate_power_in_band(self, band_index):
        """
        Calculates Absolute power of the specified frequency band.

        Parameters
        ----------
        self : FrequencyDomain
        band_index : int
            Index of the frequency band.

        Returns
        -------
        float
            The power of the specified frequency band.

        Raises
        ------
        ValueError
            If the band_index is invalid.
        """
        psd_result = pyhrv.frequency_domain.welch_psd(
            self.signal,
            rpeaks=self.r_peaks,
            show=False,
            legend=False,
            show_param=False,
        )
        self.VLF, self.LF, self.HF =  psd_result["fft_abs"]


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
        return self.LF / self.HF

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

        return self.VLF / self._total_power()

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

    # Generate a synthetic "heart rate" signal
    hr = 60 + 10 * np.sin(1 * np.pi * time) + 2 * np.random.randn(*time.shape)

    # Convert heart rate to intervals between beats
    rr_intervals = 60 / hr

    # Generate a signal with beats
    signal = scipy.signal.square(np.cumsum(rr_intervals) * 2 * np.pi)
    signal = (signal + 1) / 2  # Scale to [0, 1]

    # Now you can use this signal as input to your FrequencyDomain object
    frequency_domain = FrequencyDomain(signal, 200, 256, 128)

    print(f"{'':#^26}")
    print(f"{'FRQUENCY DOMAIN TEST':#^26}")
    print(f"{'':#^26}")

    print(f"VLF -> {frequency_domain.VLF()} [ms^2]")
    print(f"Lf -> {frequency_domain.LF()} [ms^2]")
    print(f"HF -> {frequency_domain.HF()} [ms^2]")

    print(f"LF/HF -> {frequency_domain.LFHF()}")

    print(f"pVLF -> {frequency_domain.pVLF()} [ms^2]")
    print(f"pLF -> {frequency_domain.pLF()} [ms^2]")
    print(f"pHF -> {frequency_domain.pHF()} [ms^2]")

    print(f"prcVLF -> {frequency_domain.prcVLF()} [%]")
    print(f"prcLF -> {frequency_domain.prcLF()} [%]")
    print(f"prcHF -> {frequency_domain.prcHF()} [%]")

    print(f"nLF -> {frequency_domain.nLF()}")
    print(f"nHF -> {frequency_domain.nHF()}")

    print(f"{'':#^26}")
    print(f"{'END OF TEST':#^26}")