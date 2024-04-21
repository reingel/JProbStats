import numpy as np
import numpy.random as rd


class Bernoulli():
    def __init__(self, p=0.5):
        self.p = p

    def __repr__(self):
        return 'Bernoulli distribution'
    
    def generate(self, n=1):
        return np.array(list(map(int, rd.rand(n) > self.p)))


if __name__ == '__main__':
    a = Bernoulli(0.5)
    print(a)
    print(a.generate(10))
