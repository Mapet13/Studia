# n = int(input("n: "))
# k = 0
# l = 0
# m = 0
# number = 2**k * 3**l * 5**m
# counter = 0
# while number <= n:
#     counter += 1
#     number  =  2**k * 3**l * 5**m
#     if number * 2 <= n:
#         k += 1
#     else:
#         k = 0
#         if 2**k * 3**l * 5**m * 3 <= n:
#             l += 1
#         else:
#             k = 0
#             l = 0
#             if 2**k * 3**l * 5**m *5 <= n:
#                 m += 1
#             else:
#                 break

# print(counter)
                    
# alternatywa

n = int(input("n: "))

counter = 0

m2 = 1
while m2 <= n:
    m3 = m2
    while m3 <= n:
        m5 = m3
        while m5 <= n:
            counter += 1
            m5  *= 5    
        m3 *= 3
    m2 *= 2

print(counter)