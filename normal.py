import numpy as np

s=np.random.normal(loc=30.0,scale=1.0,size=1000)

import matplotlib.pyplot as plt

plt.hist(s,14,density=True)
plt.title("Normal Graph")
plt.grid(axis='x',alpha=0.75)
plt.grid(axis='y',alpha=0.75)
plt.show();