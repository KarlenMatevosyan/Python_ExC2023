'''
DOC
The program prints pattern by inputed rows
'''

n = int(input("Enter the number of rows: ")) # input the number of rows
for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()  # Move to the next line
