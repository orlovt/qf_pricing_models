import numpy as np

class difference():
    def f(x):
      return np.exp(x)

    def forward_difference(f, x, dx):
      return (f(x+dx) - f(x)) / dx

    def backward_difference(f, x, dx):
      return (f(x) - f(x-dx)) / dx

    def central_difference(f, x, dx):
     return (f(x+dx) - f(x-dx)) / (2*dx)


