import biosppy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Qt4Agg')


class SignalPreprocessing:
    """
    This class is used to preprocess the signal.

    Attributes
    ----------
    signal : array
        The preprocessed signal.

    Methods
    -------
    filter()
        Removes noise from the signal.

    remove_offsets()
        Smooths the signal.

    """

    def __init__(self, signal):
        self.signal = signal
        self.filter()
        self.remove_offsets()

    def filter(self):
        """
        Removes noise from the signal.

        Parameters
        ----------
        self : SignalPreprocessing

        Returns
        -------
        tuple[array, array]: The filtered signal and the noise.

        Raises
        ------
        None

        """
        self.signal = biosppy.signals.tools.filter_signal(
            signal=self.signal,
            ftype='FIR',
            band='bandpass',
            order=int(0.3 * 100),
            frequency=[0.5, 40],
            sampling_rate=100,
        )

    def remove_offsets(self):
        """
        Removes offsets from the signal.

        Parameters
        ----------
        self : SignalPreprocessing

        Returns
        -------
        array: The signal without offsets.

        Raises
        ------
        None

        """
        self.signal = biosppy.signals.tools.smoother(
            signal=self.signal[0],
            kernel='boxzen',
            size=int(0.1 * 100),
            mirror=True,
        )


if __name__ == "__main__":
    signal = np.random.rand(100)
    unfiltered, = plt.plot(signal, color='red')
    plt.show()
    signal_preprocessing = SignalPreprocessing(signal)
    print(signal_preprocessing.signal)
    filtered, = plt.plot(signal_preprocessing.signal[0], color='blue')
    plt.show()
