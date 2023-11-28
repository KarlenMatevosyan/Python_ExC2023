'''
DOC
The program checks if the number is divisible by 5 or not
'''

input_values = input("Enter the elements seperated by space: ")  # Input values seperated by spaces
values = [int(x) for x in input_values.split()]  # all inputed numbers are splited by space and assigned to list

for i in values:
    if i % 5 == 0:
        print(f"{i} is divisible by 5")  
    else:
        print(f"{i} isn`t divisible by 5")
        
