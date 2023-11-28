'''
DOC
The program calculate the count of substring in string
'''
string = input("Enter the string: ")  # input string
substring = 'l'
count = 0
for i in string:
    if i == substring:
        count += 1

print(f"Count of {substring} substring -", count)
