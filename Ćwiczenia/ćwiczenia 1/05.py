'''
Proszę zaimplementować funkcję odwracającą listę jednokierunkową
'''

def reverse(first):
    reverse_first = None
    while first is not None:
        temp = first.next
        first.next = reverse_first
        reverse_first = first
        first = temp
        
    return reverse_first