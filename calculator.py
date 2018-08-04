while True:
   
    operation = input("Choose a operation:")
    if operation == "+":
        a = int(input("First Varaible: "))
        b = int(input("Second Varaible: "))
        c=a+b
        print (c)
        continue
    if operation == "-":
        a = int(input("First Varaible: "))
        b = int(input("Second Varaible: "))
        c=a-b
        print (c)
        continue
    if operation == "*":
        a = int(input("First Varaible: "))
        b = int(input("Second Varaible: "))
        c=a*b
        print (c)
        continue
    if operation == "/":
        a = int(input("First Varaible: "))
        b = int(input("Second Varaible: "))
        c=a/b
        print (c) 
        continue
    else:
        print("bye..") 
        break
