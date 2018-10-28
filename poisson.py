import numpy as np
import matplotlib.pyplot as plt
import csv
ar=np.random.poisson(30,1000)

bins=plt.hist(ar, 14, normed=True)

plt.xlabel("k")
plt.ylabel("P(X=k)")
plt.grid(axis='x',alpha=0.75)
plt.grid(axis='y',alpha=0.75)
plt.title("Poisson Distribution")
plt.text(41,0.06,r'$lamda=30$')
plt.show()

with open('poisson.csv','w') as csvfile:
	fieldnames=['points']
	writer = csv.DictWriter(csvfile,fieldnames=fieldnames)
	writer.writeheader()
	for i in ar:
		writer.writerow({'points': i})