import matplotlib.pyplot as plt
import numpy as np

# Default interval for the plot. Represents the default [-75, 75] interval
default_interval = 75
p2 = [-1/10000, 1/200000, 19/500, -8/125, -289/100, 43/100, 27.45] 

def plotfunc(func):
    print("Specify the upper and lower interval limits, leave blank if satisfied with current interval")

    lower_limit = -1*default_interval
    upper_limit = default_interval

    plt.title("Plot of f(x)")
    plt.xlabel("x")
    plt.ylabel("f(x)")

    while True:
        lower_input = input("Lower Limit: ")
        upper_input = input("Upper Limit: ")
        if lower_input and upper_input != "":
            lower_limit = float(lower_input)
            upper_limit = float(upper_input)
            x_list = np.arange(lower_limit, upper_limit, 0.01)
            zeros = np.zeros(len(x_list))
            y_list = func(x_list)
#            roots = np.roots(p2)
#            root_zeros = np.arange(len(roots))
            plt.plot(roots, root_zeros, label = "Roots", marker = 'o') 
            plt.plot(x_list, y_list, label = "Plot of f(x)")
            plt.plot(x_list, zeros)
            plt.legend()
            plt.show()

        else:
            x_list = np.arange(lower_limit, upper_limit, 0.01)
            y_list = func(x_list)
            zeros = np.zeros(len(x_list))
#            roots = np.roots(p2)
#            root_zeros = np.arange(len(roots))
            plt.plot(roots, root_zeros, label = "Roots", marker = 'o')          
            plt.plot(x_list, y_list, label = "Plot of f(x)")
            plt.plot(x_list, zeros)
            plt.legend()
            plt.show()
            break


def f1(x):
    return -0.425*x**3 + 0.18*x**2 + 2.316*x - 1.428

def f2(x):
    return (-1/10000)*x**6 + (1/200000)*x**5 + (19/500)*x**4 + - (8/125)*x**3 - (289/100)*x**2 + (43/100)*x + 27.45

def bisection(func, limits, target_err):
    a = limits[0]
    b = limits[1]
    f_a = func(a)
    f_b = func(b)

    i = 0
    while True:
        xi = (a + b)/2
        if f_a*f_b >= 0:
            return None
        elif (np.abs(func(xi)) - target_err) / (np.abs(func(xi))) <= target_err:
            return "Root Found!\nRoot Value : " + str(xi) + "\n Iteration Number: " + str(i) 
        elif func(xi)*f_a < 0:
            b = xi
        elif func(xi)*f_b < 0:
            a = xi
        i += 1

def falsepos(func, limits, target_err):
    a = limits[0]
    b = limits[1]
    f_a = func(a)
    f_b = func(b)

    i = 0
    while True:
        xi = (a*f_b-b*f_a)/(f_b-f_a)
        if f_a*f_b >= 0:
            return None
        elif np.abs(func(xi)) <= target_err:
            return "Root Found!\nRoot Value : " + str(xi) + "\n Iteration Number: " + str(i) 
        elif func(xi)*f_a < 0:
            b = xi
        elif func(xi)*f_b < 0:
            a = xi
        i += 1

if __name__ == '__main__':
    plotfunc(f1)
#    print(falsepos(f1, [0, 1], 0.01))
