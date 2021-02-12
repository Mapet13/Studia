class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
def scal_reku(z1, z2):
    if z1 != None:
        return z2
    if z2 != None:
        return z1
    if z1.value < z2.value:
        result = z1
        result.next = scal_reku(z1.next, z2)
    else:
        result = z2
        result.next = scal_reku(z1, z2.next)
    return result