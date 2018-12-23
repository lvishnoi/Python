import re

fileRead = open("code.txt", "r")
# error log will be stored in result.txt in the same directory 
fileWrite = open("result.txt", "w")

funFlag = 0

for line in fileRead:
    if(line.split(" ")[0] == "DEFSUB" and line.split(" ")[1][0] == "'"):
        funFlag = 1

        if(next(fileRead).split(" ")[0].strip() != "REM"):
            fileWrite.write(line)
            fileWrite.write("Function defination is not given." + "\n")
    
    if(funFlag == 1):
        if(line.split(" ")[0] == "LOCAL" and line.split(" ")[1] == "DIM"):
            length = len(line.split(" ")[2].strip()) - 1

            if(line.split(" ")[2][0] == "i" and re.findall("[a-z]",line.split(" ")[2][length]) == []):
                fileWrite.write(line)
                fileWrite.write("Interger is not declared properly." + "\n")
            elif(line.split(" ")[2][0] == "s" and line.split(" ")[2][length] != "$" and re.findall("[0-9]",line.split(" ")[2][length]) == []):
                fileWrite.write(line)
                fileWrite.write("String should end with $ and default size." + "\n")
            #elif(line.split(" ")[2][0] == "o"):
            #else:
             #   pass


