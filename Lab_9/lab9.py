from scipy import signal
import matplotlib.pyplot as plt
import numpy as np

def plotBode(denominator, numerator):
    sys = signal.TransferFunction(denominator, numerator)

    w, mag, phase = signal.bode(sys)

    plt.figure()
    plt.semilogx(w, mag)
    plt.grid(True)

    plt.figure()
    plt.semilogx(w, phase)
    plt.grid(True)

    plt.show()

def main():
    L = .994E-3
    C = 52.3E-6
    R = 7.15

    denom = [1/(L*C)]
    numer = [1, 1/(R*C), 1/(L*C)]

    plotBode(denom, numer)

    L = 1E-3
    C = 5E-6
    R = 8

    denom = [1, 0, 0]
    numer = [1, 1/(R*C), 1/(L*C)]
    plotBode(denom, numer)

if __name__ == "__main__":
    main()

    