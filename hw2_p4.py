#The Root of The Number
digits_list=[]
def Digits_of_a_Number(n):
    while n>0:
        digit=n%10
        n=n//10
        digits_list.append(digit)
    return digits_list

num=int(input('input a natural number: n= '))

while num>=10:
    num=sum(Digits_of_a_Number(num))
    digits_list.clear()
    print(num)