#digit product
n=int(input('input a natural number: n= '))
product=1
while n>0:  
    digit=n%10 
    n=n//10
    if digit==0 : 
        continue 
    else: 
        product*=digit 
print (product)