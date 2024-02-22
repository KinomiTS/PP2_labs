#generator  of squares of numbers up to N
def son(n):
	for i in range (n):
		yield i**2
num = int(input())
for j in son(num):
	print (j)

#2 even number generator
def evg(n):
	for i in range(1,n):
		if i%2==0:
			yield i
swag = int(input())
for j in evg(swag):
	print(j)

#3 3 and 4  divisible
def twelwe(n):
        for i in range (n):
                if (i%12 == 0) & (i>0):
                        yield i
lol= int(input())
for j in twelwe(lol):
        print(j)

#squares from a to b generator
def sab(n, m):
        for i in range (n, m+1):
                yield i**2
lol  = int(input())
dota = int(input())
for j in sab(lol, dota):
        print(j)

#from n to zero generator
def nzz(n):
	for i in range(n, 0, -1):
		yield i
stonks = int(input())
for j in nzz(stonks):
	print (j)
