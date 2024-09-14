import numpy as np

class Integrator:
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError(f'no rule in class self.__class__.__name__')


    def integrate(self, f): 
        s = 0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i]) 
                
        return s


    def vectorized_integrate(self, f):
        # f must be vectorized for this to work return np.dot(self.weights, f(self.points))
        pass

class Trapezoidal(Integrator): 
    def construct_method(self):
        h = (self.b - self.a)/float(self.n - 1) 
        x = np.linspace(self.a, self.b, self.n) 
        w = np.zeros(len(x))
        w[1:-1] += h
        w[0] = h/2; w[-1] = h/2 
        
        return x, w
    


class Midpoint(Integrator): 
    def construct_method(self):
        a, b, n = self.a, self.b, self.n # quick forms 
        h = (b-a)/float(n)
        x = np.linspace(a + 0.5*h, b - 0.5*h, n) 
        w = np.zeros(len(x)) + h
        
        return x, w
    

class Simpson(Integrator):
    def construct_method(self): 
        if self.n % 2 != 1:
            print ('n=%d must be odd, 1 is added' % self.n) 
            self.n += 1
        x = np.linspace(self.a, self.b, self.n)
        h = (self.b - self.a)/float(self.n - 1)*2 
        w = np.zeros(len(x))
        w[0:self.n:2] = h*1.0/3 
        w[1:self.n-1:2] = h*2.0/3 
        w[0] /= 2
        w[-1] /= 2

        return x, w