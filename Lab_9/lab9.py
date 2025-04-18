from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import soundfile as sf

def subwoofer(t):
    return (200000000/np.sqrt(43750000))*np.exp(-12500*t)*np.sin(np.sqrt(43750000)*t)
def tweeter(t):
    return 1-2500*np.exp(-1250*t)*np.cos(np.sqrt(198437500)*t)-(196875000/np.sqrt(198437500))*np.exp(-1250*t)*np.sin(np.sqrt(198437500)*t)


def plotBode(denominator, numerator, cutoff=None):
    sys = signal.TransferFunction(denominator, numerator)
    w, mag, phase = signal.bode(sys)

    plt.figure()
    plt.semilogx(w, mag)
    match cutoff:
        case 'LP':
            cutoffPoint = np.argmax(mag < -3)
            plt.scatter(w[cutoffPoint], mag[cutoffPoint], color='k', label=f'{w[cutoffPoint]:.3f},{mag[cutoffPoint]:.3f}')
        case 'HP':
            cutoffPoint = np.argmax(mag > -3)
            plt.scatter(w[cutoffPoint], mag[cutoffPoint], color='k', label=f'{w[cutoffPoint]:.3f},{mag[cutoffPoint]:.3f}')
    plt.legend(title='Cutoff Point')
    plt.grid(True)

    plt.figure()
    plt.semilogx(w, phase)
    plt.grid(True)

    # plt.show()

def audio():
    time = np.arange(0, .004, .00001)
    h_lp = subwoofer(time)
    h_hp = tweeter(time)

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
    plotBode(denomLP, numerLP, cutoff='LP')

    L = 1E-3
    C = 5E-6
    R = 8
    denomHP = [1, 0, 0]
    numerHP = [1, 1/(R*C), 1/(L*C)]
    plotBode(denomHP, numerHP, cutoff='HP')

    Freq = np.array([100,136.11259631,185.26638875,252.17089183,
                     343.23634802,467.18790478,635.90158686,865.54215987,
                     1178.11190599,1603.55870273,2182.6453837,2970.85530008,
                     4043.70828166,5503.99632953,7491.63230514,10197.05523682,
                     13879.47663039,18891.7159964,25714.00513094,35000])*2*np.pi
    swVo = np.array([.362,.332,.310,.261,.229,.197,.165,.157,.129,.109,.092,.08,
                     .0713,.066,.0625,.061,.0595,.0577,.0578,.057])
    twVo = np.array([.0273,.0362,.0466,.0611,.0780,.0980,.119,.141,.161,.177,
                     .205,.217,.233,.257,.265,.273,.281,.297,.314,.338])
    
    swVo = 20*np.log10(swVo)
    twVo = 20*np.log10(twVo)

    plt.figure()
    plt.semilogx(Freq,swVo)
    plt.grid(True)

    plt.figure()
    plt.semilogx(Freq,twVo)
    plt.grid(True)

    plt.show()
    

    # audio((denomLP, numerLP), (denomHP, numerHP))

if __name__ == "__main__":
    main()

    