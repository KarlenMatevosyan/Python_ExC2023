'''
DOC
The program checks if the inputed value is palindrome or not
'''

number = input("Enter the number: ")  # input number we want to check
print("Your number -", number)  # print original number
if number == number[::-1]:  # checks with the reversed number
    print("Your number is palindrome ")
else:
    print("Your number isn`t palindrome ")
    
