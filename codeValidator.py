import re

fileRead = open("code.txt", "r")
# error log will be stored in result.txt in the same directory 
fileWrite = open("result.txt", "w")

funFlag = 0
strFlag = 0

for line in fileRead:
    if(line.split(" ")[0] == "DEFSUB" and line.split(" ")[1][0] == "'"):
        funFlag = 1

        if(next(fileRead).split(" ")[0].strip() != "REM"):
            fileWrite.write(line)
            fileWrite.write("Error: Function defination is not given." + "\n")
    
    if(funFlag == 1):
        if(line.split(" ")[0] == "LOCAL" and line.split(" ")[1] == "DIM"):
            splitLen = len(line.strip().split(" "))
            if(splitLen < 4):
                length = len(line.split(" ")[2].strip()) - 1
                if(line.split(" ")[2][0] == "i"):
                    if(re.findall("[a-z,A-Z,0-9,_]", line.split(" ")[2][length]) == []):
                        fileWrite.write(line)
                        fileWrite.write("Error: Interger variable is not declared properly." + "\n")
                elif(line.split(" ")[2][0] == "s"):
                    if(re.search("[$]", line.split(" ")[2])):
                        strFlag = 1
                    else:
                        strFlag = 2
                    if(strFlag == 2):                        
                        fileWrite.write(line)
                        fileWrite.write("String should contain $ symbol." + "\n")
                    else:
                        if(line.split(" ")[2][length] == "$"):
                            fileWrite.write(line)
                            fileWrite.write("String should contain default size." + "\n")
                elif(line.split(" ")[2][0] == "o"):
                    #need to check object declaration
                    if(re.findall("[a-z,A-Z,0-9,_]", line.split(" ")[2][length]) == []):
                        fileWrite.write(line)
                        fileWrite.write("Error: Object variable is not declared properly." + "\n")
                elif(line.split(" ")[2][0] == "h"):
                    if(re.findall("[a-z,A-Z,0-9,_]", line.split(" ")[2][length]) == []):
                        fileWrite.write(line)
                        fileWrite.write("Error: Handle variable is not declared properly." + "\n")
                else:
                    fileWrite.write(line)
                    fileWrite.write("Error: Invalid variable type." + "\n")
            else:
                fileWrite.write(line)
                fileWrite.write("Error: Multiple declarations or initialization of variable with declaration." + "\n")
    
    if(line.split(" ")[0] == "RETURN"):
        returnLen = len(line.strip().split(" "))
        if(returnLen != 2):
            fileWrite.write(line)
            fileWrite.write("Error: Return should have a variable." + "\n")
        while True:
            checkVar = next(fileRead)
            if(checkVar.split(" ")[0].strip() == "REM" or checkVar.split(" ")[0].strip() == ""):
                continue
            elif(checkVar.strip() == "END SUB"):
                break
            else:
                fileWrite.write(line)
                fileWrite.write("Error: No code should lie after return statement." + "\n")
                break

fileRead.close()
fileWrite.close()