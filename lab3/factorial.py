def calculate_factorial(x):
	n=1
	for num in range(2,x+1):
		n*=num
	return n
n=int(input())
print(calculate_factorial(n))
