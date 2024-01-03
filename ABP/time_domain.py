import numpy as np
import pyhrv


class TimeDomain:
    def __init__(self, time, signal):
        self.time = time
        self.signal = signal

    def RMSSD(self):
        """
        Calculates the Root Mean Square of Successive Differences (RMSSD) of the signal.

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
        int: The number of NN50 intervals of the signal.

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
        float: The percentage of NN50 intervals of the signal.

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
        int: The number of NN20 intervals of the signal.

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
        float: The percentage of NN20 intervals of the signal.

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
        float: The SDRR of the signal.

        Raises
        ------
        None

        """
        r_peaks = pyhrv.utils.find_peaks(self.signal, self.time)

        return np.std(np.diff(self.signal))


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
