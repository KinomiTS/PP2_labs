def getMax(a,b,c):
	if a>b:
		if a>c:
			return a
		else: return c
	else: 
		if b>c:
			return b
		else: return c
a=int(input())
b=int(input())
c=int(input())
x=getMax(a,b,c)
print(x)
