import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def f1(x):
    return x ** 2 + 3 * x + 8

def f3(x, y):
    return x**4 - 16*x**3 + 96*x**2 - 256*x + y**2 - 4*y + 262

def df3_dx(x, y):
    return 4*x**3 - 48*x**2 + 192*x - 256

def df3_dy(x, y):
    return 2*y - 4

def f4(x,y):
    return np.exp(-(x - y)**2) * np.sin(y)

def df4_dx(x, y):
    return -2 * np.exp(-(x - y)**2) * np.sin(y) * (x - y)

def df4_dy(x, y):
    return np.exp(-(x - y)**2) * np.cos(y) + 2 * np.exp(-(x - y)**2) * np.sin(y)*(x - y)

def f5(x):
    return np.cos(x)**4 - np.sin(x)**3 - 4*np.sin(x)**2 + np.cos(x) + 1

def graddesc_1d(f, x_range, derivative=None):
    x_range = list(x_range)
    xbase = np.linspace(x_range[0], x_range[1], 100)
    ybase = f(xbase)

    bestx = np.random.uniform(x_range[0], x_range[1])
    fig, ax = plt.subplots()
    ax.plot(xbase, ybase)
    ax.set_xlabel('X')
    ax.set_ylabel('f(X)')
    xall, yall = [], []
    lnall,  = ax.plot([], [], 'ro-')
    lngood, = ax.plot([], [], 'go', markersize=10)

    lr = 0.1

    def numeric_derivative(x, f, epsilon=1e-5):
        # Approximate the derivative using the finite difference method
        df = (f(x + epsilon) - f(x)) / epsilon
        return df

    def onestepderiv(frame):
        nonlocal bestx, lr

        if derivative is not None:
            gradient = derivative(bestx)  # Use the provided derivative function
        else:
            gradient = numeric_derivative(bestx, f)  # Compute the gradient numerically

        x = bestx - gradient * lr
        bestx = x
        y = f(x)
        lngood.set_data(x, y)
        xall.append(x)
        yall.append(y)
        lnall.set_data(xall, yall)

    ani = FuncAnimation(fig, onestepderiv, frames=range(200), interval=0.1, repeat=False)
    ani.save('animation.gif', writer='pillow', fps=5)
    print("bestx = ",bestx)
    print("Minimum value = ",f(bestx))
    return ani

def graddesc_2d(f, x_range, y_range, lr, iterations, fx=None, fy= None):
    x_range = list(x_range)
    y_range = list(y_range)
    xbase = np.linspace(x_range[0], x_range[1], 100)
    ybase = np.linspace(y_range[0], y_range[1], 100)

    def numeric_derivative_x(x, y, f, epsilon=1e-5):
        df = (f(x + epsilon, y) - f(x, y)) / epsilon
        return df

    def numeric_derivative_y(x, y, f, epsilon=1e-5):
        df = (f(x, y + epsilon) - f(x, y)) / epsilon
        return df

    X, Y = np.meshgrid(xbase, ybase)
    Z = f(X, Y)

    bestx = np.random.uniform(x_range[0], x_range[1])
    besty = np.random.uniform(y_range[0], y_range[1])


    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.plot_surface(X, Y, Z, cmap = "viridis", alpha = 0.8)
    ax.set_xlabel('X')  # Add x-label
    ax.set_ylabel('Y')
    ax.set_zlabel('f(X,Y)')

    xall, yall, zall = [], [], []
    lnall = ax.scatter([], [], [], c='r', marker="o")
    lngood = ax.scatter([], [], [], c='g', marker='o', s=50)

    for frame in range(iterations):
        if fx is not None:
            gradient_x = fx(bestx, besty)  # Use the provided derivative function
        else:
            gradient_x = numeric_derivative_x(bestx, besty, f)

        if fy is not None:
            gradient_y = fy(bestx, besty)  # Use the provided derivative function
        else:
            gradient_y = numeric_derivative_y(bestx, besty, f)

        x = bestx - gradient_x * lr
        y = besty - gradient_y * lr
        bestx = x
        besty = y
        z = f(x, y)
        xall.append(x)
        yall.append(y)
        zall.append(z)

        lnall._offsets3d = (xall, yall, zall)
        lngood._offsets3d = ([x], [y], [z])
    plt.savefig('2dplot.png')
    return bestx, besty
