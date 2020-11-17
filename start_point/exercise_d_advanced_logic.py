# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)

# 2. Print the difference between the largest and smallest value:
difference = max(numbers) - min(numbers)
print(difference)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
i = 0
while i < len(numbers):
    if numbers[i] and numbers[i+1] == 2:
        print(True)
        break
    i += 1

# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
i = 0
j = 0
sum = 0

while i < len(numbers):
    if numbers[i] == 6:
        j = 0
        while i + j < len(numbers):
            if numbers[i + j] == 7:
                i += j
                break
            else:
                j += 1
    else:
        sum += numbers[i]
    i += 1

print(sum)    

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5.
i = 0
sum = 0

while i < len(numbers):
    if numbers[i] != 13 and numbers[i -1] != 13:
        sum += numbers[i]
    i += 1
print(sum)
