import random

N=16
l = []
s=''
for i in range(33,95):
	l+= chr(i)
random.shuffle(l)   
for i in range(97,127):
    l+= chr(i)
random.shuffle(l)
l*=N
random.shuffle(l)
for i in range(N):
    s += l[i]
print(s)
