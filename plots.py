import matplotlib.pyplot as plt
import numpy as np
from math import factorial

x = np.arange(1, 30)

# plt.plot(x, x)
# plt.plot(x, np.log2(x))
# plt.plot(x, np.square(x))
plt.plot(x, [factorial(n) for n in x])
plt.plot(x, [pow(2, n) for n in x])


plt.legend(['y = x!',
            'y = 2 ^ x',
            ], loc='upper left')
plt.savefig('fig.png')