from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import soundfile as sf

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

def audio(lowPass, highPass):
    sysLP = signal.TransferFunction(lowPass[0], lowPass[1])
    w, h_lp, phase = signal.bode(sysLP)
    sysHP = signal.TransferFunction(highPass[0], highPass[1])
    w, h_hp, phase = signal.bode(sysHP)

    print(type(sysLP))

    filename = 'handel.wav'
    data, fs = sf.read(filename, dtype='float32')
    data = data[:,0]
    data_lp = np.convolve(data, h_lp)
    data_lp /= max(abs(data_lp))
    data_hp = np.convolve(data, h_hp)
    data_hp /= max(abs(data_hp))

    sound_break = np.zeros(fs*2)

    data_play = np.hstack((sound_break, data,
                           sound_break, data_lp,
                           sound_break, data,
                           sound_break, data_hp))
    sd.play(data_play, fs)
    status = sd.wait()

def main():
    L = .994E-3
    C = 52.3E-6
    R = 7.15
    denomLP = [1/(L*C)]
    numerLP = [1, 1/(R*C), 1/(L*C)]
    # plotBode(denomLP, numerLP)

    L = 1E-3
    C = 5E-6
    R = 8
    denomHP = [1, 0, 0]
    numerHP = [1, 1/(R*C), 1/(L*C)]
    # plotBode(denomHP, numerHP)

    audio((denomLP, numerLP), (denomHP, numerHP))

if __name__ == "__main__":
    main()

    