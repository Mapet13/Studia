"""
Napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych wyrazów ciągu Fibonacciego. 
Wyznaczyć ten iloraz dla różnych wartości początkowych wyrazów ciągu.
"""

e = 1e-8    # dokładnośc 

# wczytuje wartości początkowe ciągów
a = int(input("Podaj pierwszą wartośc początkową: "))   
b = int(input("podaj drugą wartośc początkową: "))

current_quotient = b / a            # pierwszy iloraz
previous_quotient = 99999999999999  # losowa duuuza wartośc aby mnie wpuściło do pętli 

while (abs(current_quotient - previous_quotient) > e):     # dopóki różnica miedzy ilorazem aktualnych wyrazów a poprzednich jest wieksza niz zadana dokładnośc
    previous_quotient = current_quotient    # zachowuje iloraz do pozniejszego sprawdzenia
    sum = a + b                             # standargowy ciąg Fibonacciego
    a = b
    b = sum
    current_quotient = b / a                # wyliczam iloraz dla nowych wyrazów
    
print(current_quotient)