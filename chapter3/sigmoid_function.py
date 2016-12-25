import numpy as np
import matplotlib.pylab as plt
import os, sys
sys.path.append(os.pardir)
from common.functions import sigmoid

if __name__ == "__main__":
    x = np.arange(-5.0, 5.0, 0.1)
    y = sigmoid(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1) # y axis
    plt.show()
