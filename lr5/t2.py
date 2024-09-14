from integral import Simpson, Trapezoidal


def f(x):
    return x*x

simpson = Simpson(0, 2, 11) 
print(simpson.integrate(f)) 
trapez = Trapezoidal(0, 2, 11) 
print(trapez.integrate(f))