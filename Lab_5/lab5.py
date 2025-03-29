'''
Author: Hunter Van Horn, Dexter Ward
Date: 02/06/2025
This program graphs the voltage across a capactior of an RC Circuit and finds
the time constant (tau) of said circuit.
'''
import numpy as np
import matplotlib.pyplot as plt

def calculateTau(r, c):
    return r*c

def capacitorResponse(vf, vo, t, tau):
    return vf+(vo-vf)*np.exp(-t/tau)

def positionAtTau(yVal, vf, vo):
    return np.argmax(yVal > capacitorResponse(vf,vo,1,1))

def graphResponse():
    r = 10000
    c = .0000001
    tau = calculateTau(r,c)
    vf = 5
    vo = 0
    stepSize = .000001
    xVal = np.array([0])
    yVal = np.array([capacitorResponse(vf, vo, xVal[-1], tau)])

    while(xVal[-1] < 5*tau):
        xVal = np.append(xVal, [xVal[-1]+stepSize])
        yVal = np.append(yVal, [capacitorResponse(vf, vo, xVal[-1], tau)])

    xVal = xVal*1000

    plt.plot(xVal,yVal)
    plt.scatter(xVal[positionAtTau(yVal, vf, vo)],yVal[positionAtTau(yVal, vf, vo)])
    plt.xlabel('Time (ms)')
    plt.ylabel('Voltage (V)')
    plt.title('Voltage Across the Capacitor')
    plt.grid()
    plt.show()

if __name__ == '__main__':
    graphResponse()