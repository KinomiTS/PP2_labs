import math 

def plgon(P, phem):
    area=0.5* P* phem
    return area

def P(nos, los):
    P=nos*los
    return P

def phem(nos, los):
    phem= los/(2*math.tan(math.pi/nos))
    return phem


nos=int(input())
los=int(input())

P = P(nos, los)
phem = phem(nos, los)
area=plgon(P, phem)

print("The area of regular polygon: " , area)
