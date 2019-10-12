# print all even numbers between two numbers

onenumber = int(input("Enter a number: "))
x = onenumber
twonumber = int(input("Enter a number greater than the first: "))
while onenumber < twonumber:
    if onenumber % 2 == 1:
        print(onenumber)
    onenumber = onenumber + 1

print()
for i in range(x, twonumber):
    if i % 2 == 1:
        print(i)
