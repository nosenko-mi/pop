import matplotlib.pyplot as plt

from math import sin

def f(x) -> float:
    return 2**(x * sin(10*x))



def plot(values_range: tuple[float, float], steps: int, fun):
    step_size = (values_range[1] - values_range[0]) / steps
    y = []
    x = []
    i = values_range[0]
    while i <= values_range[1]:
        y.append(fun(i))
        x.append(i)
        i+=step_size

    plt.scatter(x, y)
    plt.show()


plot((-3, 3), 100, f)