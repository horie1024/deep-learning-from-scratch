import os, sys
sys.path.append(os.pardir)
from common.functions import softmax

if __name__ == '__main__':
    a = np.array([0.3, 2.9, 4.0])
    y = softmax(a)
    print(y)
    print(np.sum(y))
