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
                if(line.split(" ")[2][0] == "i" and re.findall("[a-z,A-Z,0-9,_]", line.split(" ")[2][length]) == []):
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
                #elif(line.split(" ")[2][0] == "o"):
                #elif(line.split(" ")[2][0] == "h"):
                #else:
                #   pass
            else:
                fileWrite.write(line)
                fileWrite.write("Error: Multiple declarations or initialization of variable with declaration." + "\n")


fileRead.close()
fileWrite.close()