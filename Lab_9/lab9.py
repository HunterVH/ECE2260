from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import sounddevice as sd
import soundfile as sf

def subwoofer(t):
    return 4657.780078*np.exp(-1250*t)*np.cos(np.radians(4293.891009*t-90))
def tweeter(t):
    return 30237.15784*np.exp(-12500*t)*np.cos(np.radians(6614.378278*t-145.771))

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
    sysLP = signal.TransferFunction(denomLP, numerLP)
    wLP, magLP, phaseLP = signal.bode(sysLP)

    L = 1E-3
    C = 5E-6
    R = 8
    denomHP = [1, 0, 0]
    numerHP = [1, 1/(R*C), 1/(L*C)]
    sysHP = signal.TransferFunction(denomHP, numerHP)
    wHP, magHP, phaseHP = signal.bode(sysHP)

    Freq = np.array([100,136.11259631,185.26638875,252.17089183,
                     343.23634802,467.18790478,635.90158686,865.54215987,
                     1178.11190599,1603.55870273,2182.6453837,2970.85530008,
                     4043.70828166,5503.99632953,7491.63230514,10197.05523682,
                     13879.47663039,18891.7159964,25714.00513094,35000])*2*np.pi
    swVo = np.array([.362,.332,.310,.261,.229,.197,.165,.157,.129,.109,.092,.08,
                     .0713,.066,.0625,.061,.0595,.0577,.0578,.057])
    swPh = np.array([-1.5, -2.8, -5.6, -23.3, -31, -39, -50.2, -3, -4.3, -6.6,
                     -5.4, -4.7, -5, -3, -4, -4, -4, -6, -8, -6])
    twVo = np.array([.0273,.0362,.0466,.0611,.0780,.0980,.119,.141,.161,.177,
                     .205,.217,.233,.257,.265,.273,.281,.297,.314,.338])
    twPh = np.array([90.5, 91, 89, 91.7, 92.4, 93.3, 94.1, 94, 94.5, 89, 81.2,
                     71.9, 60.6, 44.2, 34.3, 26.1, 18.3, 13.1, 10.6, 7.5])
    
    swVo = 20*np.log10(swVo/.362)
    twVo = 20*np.log10(twVo)

    

    plt.figure()
    plt.semilogx(wLP, magLP)
    cutoffPoint = np.argmax(magLP < -3)
    plt.scatter(wLP[cutoffPoint], magLP[cutoffPoint], color='k', label=f'{wLP[cutoffPoint]:.3f},{magLP[cutoffPoint]:.3f}')
    plt.semilogx(Freq,swVo)
    plt.grid(True)

    plt.figure()
    plt.semilogx(wLP, phaseLP)
    plt.semilogx(Freq,swPh)
    plt.grid(True)


    plt.figure()
    plt.semilogx(wHP, magHP)
    cutoffPoint = np.argmax(magHP > -3)
    plt.scatter(wHP[cutoffPoint], magHP[cutoffPoint], color='k', label=f'{wHP[cutoffPoint]:.3f},{magHP[cutoffPoint]:.3f}')
    plt.semilogx(Freq,twVo)
    plt.grid(True)

    plt.figure()
    plt.semilogx(wHP, phaseHP)
    plt.semilogx(Freq,twPh)
    plt.grid(True)

    # plt.show()
    

    audio()

if __name__ == "__main__":
    main()

    