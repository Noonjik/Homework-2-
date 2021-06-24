#Quadratic equation
import math 

a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))
if a == 0:
    print ('Non quadratic equation')
    if b == 0:
        if c==0:
            print('infinite solutions')
        else:
            print('no solutions')
    else: 
        print('one solution x=', end= '')
        print(c/b) 
else: 
    D=b**2-4*a*c
    print("Discriminant: ", end= '')
    print(D)
    if D<0:
        print('No solutions')
    elif D != 0:
        x1=(-b+math.sqrt(D))/2*a
        x2=(-b-math.sqrt(D))/2*a
        print('two solutions: ', end= '')
        print(x1, end= '\t')
        print(x2)
    else:
        print('one solution', end ='')
        print(-b/(2*a))
