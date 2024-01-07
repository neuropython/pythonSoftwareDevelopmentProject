# -*- coding: utf-8 -*

from typing import Any
import biosppy.signals.abp
import numpy as np
from matplotlib import pyplot as plt
from sympy.physics.quantum.identitysearch import scipy
from ABP._signal_preprocessing import SignalPreprocessing as SP


class TimeDomain:
    """
    @Author: Damian Pietroń,
    @Contact: 275277@student.pwr.edu.pl,
    @Licence: MIT,
    @Version: 0.0.1,
    @Last update: 06.01.2024r.
    """
    """
    This class is used to calculate time domain parameters.
    
    Attributes
    ----------
    time : array
        The time vector of the signal.
    signal : array
        The signal (filtered).
    
    Methods
    -------
    RMSSD()
        Calculates the Root Mean Square of Successive Differences (RMSSD) of the signal.
    SDNN()
        Calculates the Standard Deviation of NN intervals (SDNN) of the signal.
    NN50()
        Calculates the number of NN50 intervals of the signal.
    pNN50()
        Calculates the percentage of NN50 intervals of the signal.
    NN20()
        Calculates the number of NN20 intervals of the signal.
    pNN20()
        Calculates the percentage of NN20 intervals of the signal.
    SDRR()
        Calculates the Standard Deviation of RR intervals (SDRR) of the signal.
    mRR()
        Calculates the mean of RR intervals (mRR) of the signal.
    mHRV()
        Calculates the mean of HRV (mHRV) of the signal.
    SDHR()
        Calculates the Standard Deviation of HR (SDHR) of the signal.
    """

    def __init__(self, time, signal, sampling_frequency=200):
        """
        Parameters
        ----------
        time : array
            The time vector of the signal.
        signal : array
            The signal (filtered).
        sampling_frequency : int
            The sampling frequency of the signal.

        Returns
        -------
        None
        """
        self.time = time
        self.signal = SP(signal).signal[0]
        self.sampling_frequency = sampling_frequency
        self.r_peaks = biosppy.signals.abp.abp(signal=self.signal, sampling_rate=200)[2]

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        """
        This method is used to call the class.

        Parameters
        ----------
        args : Any
            Any arguments.
        kwds : Any
            Any keyword arguments.

        Returns
        -------
        dict
            Dictionary with time domain parameters.
        
        Keys and values:
        ----------------
        RMSSD -> float [ms] 
            The RMSSD of the signal.
        SDNN -> float [ms]
            The SDNN of the signal.
        NN50 -> int [n]
            The number of NN50 intervals of the signal.
        pNN50 -> float [%]
            The percentage of NN50 intervals of the signal.
        NN20 -> int [n]
            The number of NN20 intervals of the signal.
        pNN20 -> float [%]
            The percentage of NN20 intervals of the signal.
        SDRR -> float [ms]
            The SDRR of the signal.
        mRR -> float [ms]
            The mRR of the signal.
        mHRV -> float [1/min]
            The mHRV of the signal.
        SDHR -> float [1/min]
            The SDHR of the signal.
        """

        ReturnDict = {
            "RMSSD": self.RMSSD(),
            "SDNN": self.SDNN(),
            "NN50": self.NN50(),
            "pNN50": self.pNN50(),
            "NN20": self.NN20(),
            "pNN20": self.pNN20(),
            "SDRR": self.SDRR(),
            "mRR": self.mRR(),
            "mHRV": self.mHRV(),
            "SDHR": self.SDHR()
        }

        return ReturnDict


    def RMSSD(self):
        """
        Calculates the Root Mean Square of Successive Differences (RMSSD) of the signal [ms].

        Parameters
        ----------
        self : TimeDomain

        Returns
        -------
        float: The RMSSD of the signal.

        Raises
        ------
        None

        """
        return np.sqrt(np.mean(np.diff(self.signal) ** 2))

    def SDNN(self):
        """
        Calculates the Standard Deviation of NN intervals (SDNN) of the signal.

        Parameters
        ----------
        self : TimeDomain

        Returns
        -------
        float: The SDNN of the signal.

        Raises
        ------
        None

        """
        return np.std(self.signal)

    def NN50(self):
        """
        Calculates the number of NN50 intervals of the signal.

        Parameters
        ----------
        self : TimeDomain

        Returns
        -------
        int: The number of NN50 intervals of the signal [n].

        Raises
        ------
        None

        """
        return len(np.where(np.diff(self.signal) > 50)[0])

    def pNN50(self):
        """
        Calculates the percentage of NN50 intervals of the signal.

        Parameters
        ----------
        self : TimeDomain

        Returns
        -------
        float: The percentage of NN50 intervals of the signal [%].

        Raises
        ------
        None

        """
        return self.NN50() / len(self.signal)

    def NN20(self):
        """
        Calculates the number of NN20 intervals of the signal.

        Parameters
        ----------
        self : TimeDomain

        Returns
        -------
        int: The number of NN20 intervals of the signal [n].

        Raises
        ------
        None

        """
        return len(np.where(np.diff(self.signal) > 20)[0])

    def pNN20(self):
        """
        Calculates the percentage of NN20 intervals of the signal.

        Parameters
        ----------
        self : TimeDomain

        Returns
        -------
        float: The percentage of NN20 intervals of the signal [%].

        Raises
        ------
        None

        """
        return self.NN20() / len(self.signal)

    def SDRR(self):
        """
        Calculates the Standard Deviation of RR intervals (SDRR) of the signal.

        Parameters
        ----------
        self : TimeDomain

        Returns
        -------
        float: The SDRR of the signa [ms]l.

        Raises
        ------
        None

        """
        return np.std(np.diff(self.r_peaks))

    def mRR(self):
        """
        Calculates the mean of RR intervals (mRR) of the signal.

        Parameters
        ----------
        self : TimeDomain

        Returns
        -------
        float: The mRR of the signal [ms].

        Raises
        ------
        None

        """
        return np.mean(np.diff(self.r_peaks))

    def mHRV(self):
        """
        Calculates the mean of HRV (mHRV) of the signal.

        Parameters
        ----------
        self : TimeDomain

        Returns
        -------
        float: The mHRV of the signal [1/min].

        Raises
        ------
        None

        """
        return 60 / self.mRR()

    def SDHR(self):
        """
        Calculates the Standard Deviation of HR (SDHR) of the signal.

        Parameters
        ----------
        self : TimeDomain

        Returns
        -------
        float: The SDHR of the signal [1/min].

        Raises
        ------
        None

        """
        return 60 / np.std(self.signal)


if __name__ == "__main__":
    # Generate a time array
    time = np.arange(0, 10, 0.01)

    # Generate a synthetic "heart rate" signal
    hr = 60 + 10 * np.sin(1 * np.pi * time) + 2 * np.random.randn(*time.shape)

    # Convert heart rate to intervals between beats
    rr_intervals = 60 / hr

    # Generate a signal with beats
    signal = scipy.signal.square(np.cumsum(rr_intervals) * 2 * np.pi)
    signal = (signal + 1) / 2  # Scale to [0, 1]

    plt.plot(time, signal)
    plt.show()

    # Create an instance of the class
    time_domain = TimeDomain(time, signal)

    print(f"{'':_^26}")
    print(f"{'TIME DOMAIN TEST':_^26}")
    print(f"{'':_^26}")
    print("NN50 -> {}".format(time_domain.NN50()))
    print("pNN50 -> {}".format(time_domain.pNN50()))

    print("NN20 -> {}".format(time_domain.NN20()))
    print("pNN20 -> {}".format(time_domain.pNN20()))

    print("SDRR -> {}".format(time_domain.SDRR()))
    print("mRR -> {}".format(time_domain.mRR()))
    print("mHRV -> {}".format(time_domain.mHRV()))
    print("SDHR -> {}".format(time_domain.SDHR()))
    print("RMSSD -> {}".format(time_domain.RMSSD()))
    print("SDNN -> {}".format(time_domain.SDNN()))
    print(f"{'':_^26}")
    print(f"{'END OF TEST':_^26}")
