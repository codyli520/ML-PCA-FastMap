from __future__ import division
import math
import matplotlib.pyplot as plt

def fast_map(k,D,d):
	if k <= 0:
		return

	O_a, O_b, d_ab = d[0][0],d[0][1],D

	for i in range(1,11):
		d_ai,d_bi = 0,0
		for x in d:
			if (x[0] == i and x[1]== O_a) or (x[1] == i and x[0]== O_a): 
				d_ai = x[2]
			if (x[0] == i and x[1]== O_b) or (x[1] == i and x[0]== O_b):
				d_bi = x[2]

		x_i = (d_ai**2+d_ab**2-d_bi**2)/ (2*d_ab)

		X[i-1].append(x_i)

	new_d = []

	for p in d:
		D_prime =p[2]**2 - (X[p[0]-1][0]-X[p[1]-1][0])**2

		if D_prime > 0.0:
			D_prime = math.sqrt(D_prime)

		new_d.append([p[0],p[1],D_prime])

	new_d.sort(key = lambda x: x[2], reverse = True)
	
	fast_map(k-1,new_d[0][2],new_d)
	



fp = open('fastmap-data.txt','r')
data = []
for line in fp.readlines() :
	line = line.split()
	data.append(map(int,line))

data.sort(key = lambda x: x[2], reverse = True)

dab = data[0]

X = [[] for i in range(10)]

fast_map(2,dab[2],data)


fp = open('fastmap-wordlist.txt','r')
words = []
for line in fp.readlines() :
	word = line.strip()
	words.append(word)
for i in xrange(10):
	plt.plot(X[i][0], X[i][1],'xk') 
	plt.annotate(words[i], xy = (X[i][0], X[i][1])) 
plt.show()

