'''
DOC
The program removes first n characters from string
'''

name = 'Heriqnaz'
n = int(input("Enter the n: "))
print("Your name -", name)  # at first print original name
print(f"Removed first {n} -", name[n:])  # print name from n to up
