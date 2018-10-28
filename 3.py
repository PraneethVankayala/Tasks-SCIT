from poisson import ar
from normal import s
import random
import csv
import numpy as np
import matplotlib.pyplot as plt

lp = []
ln = []
totallist = []
for i in range(100):
	sp=random.choice(ar)
	lp.append(sp)
for i in range(100):
	n=random.choice(s)
	ln.append(n)
totallist=lp+ln
print totallist
totallist=np.array([lp,ln])
totallist=np.average(totallist,axis=0)
bins = plt.hist(totallist,14,density=True)
plt.grid(axis='x',alpha=0.75)
plt.grid(axis='y',alpha=0.75)
plt.show();

with open('average.csv','w') as csvfile:
	fieldnames=['points']
	writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
	writer.writeheader()
	for i in totallist:
		writer.writerow({'points': i})
