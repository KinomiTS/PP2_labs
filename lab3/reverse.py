def reverse(x):
	if len(x) <=1:
		return x
	return x[-1]+ reverse(x[0:-1])
str=input()
print (str, " ", reverse(str))
