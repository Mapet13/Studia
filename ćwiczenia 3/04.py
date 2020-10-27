'''
Napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg 
e = 1/0! + 1/1! + 1/2! + 1/3! + ... 
z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).
'''

n = int(input("n: "))

result = 0

#jest potrzebne do zaokraglenia
bonus_precision = 1

i = 2
current_factorial = 1
ten_to_n = 10**(n+bonus_precision) # kozystam że int w pythonie nie ma max
while current_factorial <= 10**n:
    current_factorial *= i
    result += ten_to_n // current_factorial
    i += 1
    
bonus_digits = result % (10 ** bonus_precision)
result //= (10 ** bonus_precision)

#zaokragalnie bo z round wywala float out of range xD
if bonus_digits >= ((10 ** bonus_precision) // 2):
    result += 1
    
print("2.", result, sep='')