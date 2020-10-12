numbers = [1]
current_number = 1
current_index = 2
        
while current_number < 1000000:
    numbers.append(current_number)
    current_number = numbers[current_index-2] + numbers[current_index-1]
    current_index += 1
    
print(numbers)