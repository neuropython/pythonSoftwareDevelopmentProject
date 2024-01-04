import biosppy.signals.abp
import numpy as np
import pyhrv


class TimeDomain:
    """
    @Author: Damian Pietroń,
    @Contact: 275277@student.pwr.edu.pl,
    @Licence: MIT,
    @Version: 0.0.1,
    @Last update: 03.01.2020r.
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
    def __init__(self, time, signal):
        self.time = time
        self.signal = signal

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
        r_peaks = biosppy.signals.abp.abp(signal=self.signal, sampling_rate=200)[2]
        return np.std(np.diff(r_peaks))

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
        r_peaks = biosppy.signals.abp.abp(signal=self.signal, sampling_rate=200)[2]
        return np.mean(np.diff(r_peaks))

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
    time = np.arange(0, 10, 0.01)
    signal = np.sin(time)
    time_domain = TimeDomain(time, signal)
    print(time_domain.RMSSD())
    print(time_domain.SDNN())
    print(time_domain.NN50())
    print(time_domain.pNN50())
    print(time_domain.NN20())
    print(time_domain.pNN20())
    print(time_domain.SDRR())
    print(time_domain.mRR())
    print(time_domain.mHRV())
    print(time_domain.SDHR())

