previous_number = 1
current_number = 1

print(previous_number)
        
while current_number < 1000000:
    print(current_number)
    a = previous_number + current_number
    previous_number = current_number
    current_number = a