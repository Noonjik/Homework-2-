#Largest power of 3
given_number = int(input('Please input a natural number: N= '))
power_value = 1
while power_value <= given_number/3:
    power_value *= 3
print(power_value)
