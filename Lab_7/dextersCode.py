'''
Author(s): Dexter Ward, Hunter Van Horn
Date: 02/27/2025
This program will graph a Series and Parallel impedance as functions of 
frequency
'''

import numpy as np
import matplotlib.pyplot as plt
import cmath

"""
Parameters
----------
Z: array_like
Array of impedance values
omega : array_like
Array of frequency values in radians / second
circuit_type : string
This can either be ’series ’ or ’parallel ’
"""

def find_omega_0 (z , omega, circuit_type) :
    if (circuit_type == "series"):
        omega_0 = omega[np.argmin(z)]
        f_0 = omega_0 / (2 * np.pi)
    else:
        omega_0 = omega[np.argmax(z)]
        f_0 = omega_0 / (2 * np.pi)
    return omega_0 , f_0

"""
Parameters
----------
r: float, value of the resistor (Ohms)
l: float, value of the inductor (H)
c: float, value of the capacitor (F)
omega: float, value of the freq (rad)
"""
def imped_s(r, l, c, omega):
    zs = r + ((omega * l * 1j) + 1 / (omega * c * 1j))
    return zs

"""
Parameters
----------
r: float, value of the resistor (Ohms)
l: float, value of the inductor (H)
c: float, value of the capacitor (F)
omega: float, value of the freq (rad)
"""
def imped_p(r, l, c, omega):
    zp = 1 / ((1 / r) + (1 / (omega * l * 1j)) + (omega * c * 1j))
    return zp



if __name__ == "__main__":
    r = 1000
    l = 0.0047
    c = 0.000000033
    freq = np.arange(1000, 100001, 100)
    omega = 2 * np.pi * freq
    
    zsm = []
    zsa = []
    zpm = []
    zpa = []
        
    for i in omega:
        zs = imped_s(r, l, c, i)
        zp = imped_p(r, l, c, i)
        
        zsm.append(abs(zs))
        zsa.append(np.degrees(cmath.phase(zs)))
        
        zpm.append(abs(zp))
        zpa.append(np.degrees(cmath.phase(zp)))
        
    fig, axs = plt.subplots(2, 2)
    
    
    axs[0, 0].plot(freq, zsm, 'b')
    axs[0, 0].axvline(find_omega_0(zsm, omega, "series")[1], color = 'r')
    axs[0, 0].set_title('Zs Magnitude', fontsize=8)
    axs[0, 0].semilogx()
    axs[0, 0].set_xticklabels([])
    axs[0, 1].plot(freq, zpm, 'r')
    axs[0, 1].axvline(find_omega_0(zpm, omega, "parallel")[1], color = 'b')
    axs[0, 1].set_title('Zp Magnitude', fontsize=8)
    axs[0, 1].semilogx()
    axs[0, 1].set_xticklabels([])
    axs[1, 0].plot(freq, zsa, 'k')
    axs[1, 0].set_title('Zs Angle', fontsize=8)
    axs[1, 0].semilogx()
    axs[1, 1].plot(freq, zpa, 'g')
    axs[1, 1].set_title('Zp Angle', fontsize=8)
    axs[1, 1].semilogx()
    plt.show()
    
    for ax in fig.get_axes():
        ax.label_outer()