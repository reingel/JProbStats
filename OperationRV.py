import numpy as np
import matplotlib.pyplot as plt
from Bernoulli import Bernoulli



def sum_rvs(N):
    X1 = Bernoulli(p=0.5)
    X2 = Bernoulli(p=0.5)
    x1 = X1.generate(N)
    x2 = X2.generate(N)
    y = x1 + x2
    match = np.int32(np.vstack([y == 0, y == 1, y == 2]))
    num = np.arange(N) + 1
    nums = np.vstack([num, num, num])
    prob = np.cumsum(match, axis=1) / nums
    print(x1)
    print(x2)
    print(y)
    print(match)
    print(prob)

    n = np.arange(N)
    plt.figure(10)
    plt.plot(n, prob[0,:])
    plt.plot(n, prob[1,:])
    plt.plot(n, prob[2,:])
    plt.plot([0, N], [0.25, 0.25], 'k:')
    plt.plot([0, N], [0.5, 0.5], 'k:')
    plt.axis([0, N, 0, 1])
    plt.legend(['0','1','2'])
    plt.savefig('sum_rvs.jpg')
    plt.show()

def multiply_rvs(N):
    X1 = Bernoulli(p=0.5)
    X2 = Bernoulli(p=0.5)
    x1 = X1.generate(N)
    x2 = X2.generate(N)
    y = x1 * x2
    match = np.int32(np.vstack([y == 0, y == 1]))
    num = np.arange(N) + 1
    nums = np.vstack([num, num])
    prob = np.cumsum(match, axis=1) / nums
    print(x1)
    print(x2)
    print(y)
    print(match)
    print(prob)

    n = np.arange(N)
    plt.figure(10)
    plt.plot(n, prob[0,:])
    plt.plot(n, prob[1,:])
    plt.plot([0, N], [0.25, 0.25], 'k:')
    plt.plot([0, N], [0.75, 0.75], 'k:')
    plt.axis([0, N, 0, 1])
    plt.legend(['0','1'])
    plt.savefig('multiply_rvs.jpg')
    plt.show()


if __name__ == '__main__':
    sum_rvs(N=1000)
    multiply_rvs(N=1000)