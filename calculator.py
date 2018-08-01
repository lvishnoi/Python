operation = input("Choose a operation:")
operator = ["+", "-", "*", "/"]
a = int(input("First Varaible: "))
b = int(input("Second Varaible: "))
for x in operator:
    if x == "+":
        c=a+b
        print (c)
        break
    if x == "-":
        c = a-b
        print (c)
        break
    