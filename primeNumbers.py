#!/usr/bin/python3.5

######prime numbers
def prime(n):
	if n== 1:
		return 2
	i=2
	j=0
	b=0
	p=0
	while j < n-1:
		a=2
		b=0
		if i%2 != 0:
			while a != i-1:
				if i%a == 0:
					b+=1
				a+=1
			if b==0:
				j+=1
				p=i
			if j == n -1:
				return p
		i+=1


#This program found all the prime factors##########
m=600851475143 #number to find the prime factors
v=1 #increment
end=False
result=1
while end != True:
	w=prime(v)
	if w*w > m:
		result*=m
		print(m)
		print(result)
		end=True
	if w > m:
		print(result)
		end=True
	if m%w == 0:
		print(w)
		result*=w
		d=m/w
		m=d
	else:
		v+=1
 
