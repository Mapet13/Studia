'''
Wyrazy budowane są z liter a..z. 
Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą liczbę samogłosek 
oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład 
"ula" → 117, 108, 97 oraz "exe" → 101, 120, 101. 
Proszę napisać funkcję wyraz(s1,s2), która sprawdza 
czy jest możliwe zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. 
Dodatkowo funkcja powinna wypisać znaleziony wyraz.
'''

vowels = ['A', 'Ą', 'E', 'Ę', 'I', 'O', 'U', 'Y']

def count_vowels(s):
    counter = 0
    for c in s:
        if c.upper() in vowels:
            counter += 1
    return counter

def get_weight(s):
    w = 0
    for c in s:
        w += ord(c)
    return w

def wyraz(s1, s2):
    
    def rec(vc, weight, i, s = ''):
        if vc == 0 and weight == 0:
            print(s1, s)
            return True
        if i >= 0 and vc >= 0 and weight >= 0:
            return rec(vc - int(s2[i].upper() in vowels), weight - ord(s2[i]), i - 1, s + s2[i]) or rec(vc, weight, i - 1, s)
        return False
    
    
    vc = count_vowels(s1)
    weight = get_weight(s1)
    
    return rec(vc, weight, len(s2) - 1)

print(wyraz("exe", "ula"))
print(wyraz("exe", "hdsfsldhsdbjhasbudacgiasjdkajytuatca"))
print(wyraz("aghvda", "hdsfsldhsdbjhkjasbkatuatca"))
print(wyraz("aghjshabjasbdhshkasbvda", "hdsfstuatca"))

