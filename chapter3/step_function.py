import matplotlib.pylab as plt
import numpy as np
import os, sys
sys.path.append(os.pardir)
from common.functions import step

def step(x):
    return np.array(x > 0, dtype=np.int)

if __name__ == "__main__":
    x = np.arange(-5.0, 5.0, 0.1)
    y = step(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1) # y axis
    plt.show()
