def LHS(a,b):
    return (a+b)**2
def RHS(a,b):
    return a**2+2*a*b+b**2
L=LHS (2,3)
R=RHS (2,3)
print("{}={}".format(L,R))