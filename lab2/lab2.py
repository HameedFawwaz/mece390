import matplotlib.pyplot as plt
import numpy as np

# Default interval for the plot. Represents the default [-75, 75] interval
default_interval = 75
p2 = [-1/10000, 1/200000, 19/500, -8/125, -289/100, 43/100, 27.45] 

def plotfunc(func):
    """
    Plots the function and prompts the user to enter in the interval limits to assist in determining roots graphically
    """
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
#            plt.plot(roots, root_zeros, label = "Roots", marker = 'o') 
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
#            plt.plot(roots, root_zeros, label = "Roots", marker = 'o')          
            plt.plot(x_list, y_list, label = "Plot of f(x)")
            plt.plot(x_list, zeros)
            plt.legend()
            plt.show()
            break


def f1(x):
    """
    Definition of f1(x) used in the graphic method root finding section of Question 1
    """
    return -0.425*x**3 + 0.18*x**2 + 2.316*x - 1.428

def f2(x):
    
    """
    Definition of f2(x) used in the root finding part of Question 2
    """
    return (-1/10000)*x**6 + (1/200000)*x**5 + (19/500)*x**4 + - (8/125)*x**3 - (289/100)*x**2 + (43/100)*x + 27.45

def brackroot(method, func, limits, target_err):
    """
    Finds the root of a function either using the Bisection Method or the False Position Method
    """
    a = limits[0]
    b = limits[1]
    f_a = func(a)
    f_b = func(b)
    
 

    i = 0
    while True:
        if method == "0":
            xi = (a + b)/2
        elif method == "1":
            xi = (a*f_b-b*f_a)/(f_b-f_a)
        
        if f_a*f_b >= 0:
            return None
        elif (np.abs(func(xi)) - target_err) / (np.abs(func(xi))) <= target_err:
            return "Root Found!\nRoot Value : " + str(xi) + "\n Iteration Number: " + str(i) 
        elif func(xi)*f_a < 0:
            b = xi
        elif func(xi)*f_b < 0:
            a = xi
        i += 1



if __name__ == '__main__':
    err = 0.0001
    #plotfunc(f2)
    #method = input("Enter 0 for Bisection Method and 1 for False Position Method: ")
    print("Root 1 Using Bisection Method: ") 
    print(brackroot("0", f2, [-2115/100, -163/10], err))
    print("Root 1 Using False Position Method: ")
    print(brackroot("1", f2, [-2115/100, -163/10], err))
    print("Root 2 Using Bisection Method: ")
    print(brackroot("0", f2, [-917/100, -693/100], err))
    print("Root 2 Using False Position Method: ")
    print(brackroot("1", f2, [-917/100, -693/100], err))
    print("Root 3 Using Bisection Method: ")
    print(brackroot("0", f2, [-5, 0], err))
    print("Root 3 Using False Position Method: ")
    print(brackroot("1", f2, [-5, 0], err))
    print("Root 4 Using Bisection Method: ")
    print(brackroot("0", f2, [0, 5], err))
    print("Root 4 Using False Position Method: ")
    print(brackroot("1", f2, [0, 5], err))
    print("Root 5 Using Bisection Method: ")
    print(brackroot("0", f2, [10, 13], err))
    print("Root 5 Using False Position Method: ")
    print(brackroot("1", f2, [10, 13], err))
    print("Root 6 Using Bisection Method: ")
    print(brackroot("0", f2, [13, 15], err))
    print("Root 6 Using False Position Method: ")
    print(brackroot("1", f2, [13, 15], err))

