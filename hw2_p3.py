#triangle
#Getting sides of a triangle
sides=[]
for i in range(0,3):
    print('Enter side ', end='')
    print(i+1,end=': ')
    side=int(input())
    sides.append(side)

#sort sides in ascending order
sides.sort()
a=sides[0]
b=sides[1]
c=sides[2]

#main problem
if c>=a+b:
    print('No triangle')
elif c**2 == a**2 + b**2:
    print('Right triangle')
elif c**2 < a**2+b**2:
    print('Acute triangle')
else:
    print ('Obtuse triangle')