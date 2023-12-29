import numpy as np
import matplotlib.pyplot as plt


def divided_difference(x_values, y_values):
    """
    Computes the divided differences table for Newton's divided difference interpolation.

    Parameters:
    - x_values: List of x coordinates of data points.
    - y_values: List of corresponding y coordinates of data points.

    Returns:
    - Two lists representing the divided differences for [xi, xi+1] and [xi-1, xi, xi+1].
    """
    n = len(x_values)
    table_xi_xi1 = []  # Divided differences for [xi, xi+1]
    table_xi1_xi_xi1 = []  # Divided differences for [xi-1, xi, xi+1]

    for i in range(n - 1):
        # Compute the divided difference for [xi, xi+1]
        diff_xi_xi1 = (y_values[i + 1] - y_values[i]) / (x_values[i + 1] - x_values[i])
        table_xi_xi1.append(round(diff_xi_xi1,4))

    for i in range(1, n - 1):
        # Compute the divided difference for [xi-1, xi, xi+1]
        diff_xi1_xi_xi1 = (table_xi_xi1[i] - table_xi_xi1[i - 1]) / (x_values[i + 1] - x_values[i - 1])
        table_xi1_xi_xi1.append(round(diff_xi1_xi_xi1,4))

    return table_xi_xi1, table_xi1_xi_xi1




def matrix(h ,x_values):
    dimension = len(x_values) - 2
    A = np.zeros((dimension,dimension))
    for i in range(dimension): #column
        for j in range(dimension):  #row
            print(i)
            if i == j:
                A[i][j] = round((h[j]+h[j+1]) / 3,4) # Diagonal element
            elif i - 1 == j :
                A[i][j] = round(h[j+1] / 6,4)  # Element before diagonal
            elif i + 1 == j:
                A[i][j] = round(h[j] / 6,4)  # Element after diagonal
    return A


def vector(h, table_xi1_xi_xi1, dimension):
    b = []
    for i in range(dimension-2):
        x = (h[i]+h[i+1]) * table_xi1_xi_xi1[i]
        b.append(round(x, 4))
    return b

def computeSpline(x_plot, w, h,x_values, y_values):
    def s(x, i):

        return(((w[i]/(6*h[i+1]))*((x_values[i+1]-x)**3))+((w[i+1]/(6*h[i+1]))*(x-x_values[i])**3)+((y_values[i]/h[i+1])-((h[i+1]*w[i])/6))*(x_values[i+1]-x)+((y_values[i+1]/h[i+1])-((h[i+1]*w[i+1])/6))*(x-x_values[i]))
    y_plot = []
    j = 0  # use to go through the x_plot values.

    for i in range(len(x_values)-1): #going through the x values finding the the y_plot value by evaluating the function s(x) where x is between x(i) and x(i+1).

        print("i: ",i)
        while(j<len(x_plot) and x_values[i]<=x_plot[j]<=x_values[i+1]):
            print(x_plot[j])
            y_plot.append(s(x_plot[j],i))
            j=j+1


    return y_plot

def f(x):
    return x**2



x_values = np.array([1,2,3,4,5])
y_values = np.array([1,4,9,16,25])

h = np.diff(x_values)
h=np.insert(h,0,0)

table_xi_xi1, table_xi1_xi_xi1 = divided_difference(x_values, y_values)

print(f"[xi, xi+1] divided differences: {table_xi_xi1}")
print(f"[xi-1, xi, xi+1] divided differences: {table_xi1_xi_xi1}")
A = matrix(h, x_values)
b = vector(h, table_xi1_xi_xi1,len(x_values))
print("matrix A is :    ",A)
print("b is: ",b)
x = np.linalg.solve(A,b)
x = np.insert(x,0,0)
w = np.append(x,0)
print("w is:",w)
print("h is:",h)

y_plot = []
z = []


x_plot = np.linspace(x_values[0], x_values[len(x_values)-1], 1000) # x_plot on all the point between x(0) and x(last)
print("x_plot is:",x_plot)
y_plot = computeSpline(x_plot, w, h, x_values, y_values)

print("y_plot is :----------------------\n",y_plot)

# errorValue = error(x_plot, f, x_values, y_plot)

trueValues=f(x_plot)
error=abs(trueValues-y_plot)


if y_plot:
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 2, 1)
    plt.plot(x_plot, y_plot, label='Cubic Spline', color='blue')
    plt.plot(x_plot, trueValues, label='true function', color='red', linestyle='dashdot')

    plt.plot(x_values, y_values, "o", label="points")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Cubic Spline Interpolation')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(x_plot, error, label="Absolute Error", color='red')
    plt.title("Interpolation Error")
    plt.xlabel("x")
    plt.ylabel("Error")
    plt.legend()

    plt.show()

