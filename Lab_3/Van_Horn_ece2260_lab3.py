'''
Author: Main was provided by Professor Gibbons and all other functions were written by Hunter Van Horn
Date: 01/23/2025
Assignment: ECE 2260 Lab 3
'''

import math

# Calculates the roots of polynomial given the coefficients
def calculate_roots(coef):
    b = coef[1]**2-4*coef[0]*coef[2]
    if(b < 0):
        b = b*-1
        return (-coef[1]/(2*coef[0]) + math.sqrt(b)*1j/(2*coef[0]), -coef[1]/(2*coef[0]) - math.sqrt(b)*1j/(2*coef[0]))
    return (((-coef[1] + math.sqrt(b))/(2*coef[0])), ((-coef[1] - math.sqrt(b))/(2*coef[0])))
    
# Calculates the factorial of a given number
def compute_factorial(n):
    total = 1
    for i in range(n):
        total = total*(i+1)
    return total

# Calculates the sum of factorials up to a given number
def sum_factorial(n):
    total = 0
    for i in range(n):
        total = total + compute_factorial(i+1)
    return total

# Calculates the left riemann sum of e^(-3x)*cos(πx) sum given a step size and bounds
def left_riemann(delta_x, lb, ub):
    xValue = lb
    total = 0
    for i in range(int(ub/delta_x)):
        total = total+math.exp(-3*xValue)*math.cos(math.pi*xValue)*delta_x
        xValue = xValue+delta_x
    return total

# Calculates the right riemann sum of e^(-3x)*cos(πx) sum given a step size and bounds
def right_riemann(delta_x, lb, ub):
    xValue = lb+delta_x
    total = 0
    for i in range(int(ub/delta_x)):
        total = total+math.exp(-3*xValue)*math.cos(math.pi*xValue)*delta_x
        xValue = xValue+delta_x
    return total
    
# Calculates the midpoint riemann sum of e^(-3x)*cos(πx) sum given a step size and bounds
def midpoint_riemann(delta_x, lb, ub):
    xValue = lb+(delta_x/2)
    total = 0
    for i in range(int(ub/delta_x)):
        total = total+math.exp(-3*xValue)*math.cos(math.pi*xValue)*delta_x
        xValue = xValue+delta_x
    return total

# Calculates the trapezoid riemann sum of e^(-3x)*cos(πx) sum given a step size and bounds
def trap_riemann(delta_x, lb, ub):
    xValue = lb
    total = 0
    for i in range(int(ub/delta_x)):
        left = math.exp(-3*xValue)*math.cos(math.pi*xValue)
        right = math.exp(-3*(xValue+delta_x))*math.cos(math.pi*(xValue+delta_x))
        diff = (left+right)/2
        total = total+diff*delta_x
        xValue = xValue+delta_x
    return total
        

    
def main():

    ##############################################################
    # Part 1
    ##############################################################
    print("Part 1 Results")
    
    coef = [2, 4, 0]
    roots = calculate_roots(coef)
    print("roots 1:")
    print(roots)

    coef = [1, 4, 4]
    roots = calculate_roots(coef)
    print("roots 2:")
    print(roots)
    
    coef = [1, 0, 9]
    roots = calculate_roots(coef)
    print("roots 3:")
    print(roots)

    coef = [2, 8, 26]
    roots = calculate_roots(coef)
    print("roots 4:")
    print(roots)

    ##############################################################
    # Part 2
    ##############################################################
    print("\n")
    print("Part 2 Results")
    
    for n in [4, 10, 16]:
        output_factorial = compute_factorial(n)
        print("computed factorial for n=%i is: %i" %
              (n, output_factorial))

    ##############################################################
    # Part 3
    ##############################################################
    print("\n")
    print("Part 3 Results")
    
    for n in [3, 5, 6]:
        output_summation = sum_factorial(n)
        print("computed factorial summation for n=%i is: %i" %
              (n, output_summation))
        
    ##############################################################
    # Part 4
    ##############################################################
    print("\n")
    print("Part 4 Results")
    
    lb = 0
    ub = 10
    
    print("calculating left Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = left_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating right Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = right_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating midpoint Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = midpoint_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

    print("calculating trapezoid Riemann sum")
    for delta_x in [1, 0.1, 0.01, 0.0001]:
        summation = trap_riemann(delta_x, lb, ub)
        print("\tdelta_x=%f, summation=%f" % (delta_x, summation))

        
if __name__ == "__main__":
    main()
