'''
Authors: Hunter Van Horn, Dexter Ward
Date: 01/30/2025
This program will solve a complex system of equations
'''

import numpy as np

def solveSystem():
    twoPi = np.pi*2
    f = 1000
    Vs = 7.07
    r1 = 680
    r2 = 2200
    r4 = 4700
    r5 = 1000
    r6 = 1000
    c1 = .22E-6
    l1 = 100E-3
    xc = -1j*(1/(twoPi*f*c1))
    xl = 1j*(twoPi*f*l1)
    
    a = np.array([[(1/r1+1/r4+1/r6+1/xc),(-1/r6),(-1/r4)],
                  [(-1/r6),(1/r6+1/xl+1/r2),(-1/xl)],
                  [(-1/r4),(-1/xl),(1/r4+1/xl+1/r5)]])
    b = np.array([[(Vs/r1)],[0],[0]])

    c = np.linalg.solve(a,b)

    print(f'V1: {float(np.absolute(c[0]))}\u2220{str(np.rad2deg(np.angle(c[0])))[1:-1]}')
    print(f'V2: {str(np.absolute(c[1]))[1:-1]}\u2220{str(np.rad2deg(np.angle(c[1])))[1:-1]}')
    print(f'V3: {str(np.absolute(c[2]))[1:-1]}\u2220{str(np.rad2deg(np.angle(c[2])))[1:-1]}')

if __name__ == "__main__":
    solveSystem()