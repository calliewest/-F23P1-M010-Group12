# Task1
import pandas as pd 

wb = pd.read_excel("F23P1-M010-Group12.xlsx", dtype = str)

c = list(wb["characters"])
b = list(wb["binary"])

try:
    i = c.index("\\n")
    c[i] = "\n"
except:
    print("\\n was not found")
    
try:
    i = c.index("/space")
    c[i] = " "
except:
    print("/space was not found")

#Task 2
def getBin(s):
    if len(s) >= 4:
        s4 = s[0:4]
        for i in range(len(c)):
            if c[i] == s4:
                s = s[4:]
                binVal = b[i]
                return binVal, s
            
    if len(s) >= 3:      
        s3 = s[0:3]
        for i in range(len(c)):
            if c[i] == s3:
                s = s[3:]
                binVal = b[i]
                return binVal, s
            
    if len(s) >= 2: 
        s2 = s[0:2]
        for i in range(len(c)):
            if c[i] == s2:
                s = s[2:]
                binVal = b[i]
                return binVal, s
            
    if len(s) >= 1: 
        for i in range(len(c)):
            if c[i] == s[0]:
                if len(s) > 1:
                    s = s[1:]
                else:s = ''
                binVal = b[i]
                return binVal, s
    return '', ''

#Task 3
def getFirstBin(s):
    flag = s[0]
    if flag == "0":
        binVal = s[0:6]
        s = s[6:]
    else:
        binVal = s[0:7]
        s = s[7:]
    return binVal, s

def getChar(s):
    i = b.index(s)
    return c[i]


#Task 4
def task4(fn):
    f = open(fn,"r")
    s = f.read()
    f.close()

    binStr = ''
    while s != '':
        binVal, s = getBin(s)
        binStr = binStr + binVal

    print(binStr)
    numBits = len(binStr)
    binStr = str(numBits) + "." + binStr

    f = open("BinOutput.txt", "w+")
    f.write(binStr)
    f.close()
    

#Task 5
def task5(fn="BinOutput.txt"):
    f = open(fn,"r")
    s = f.read()
    f.close()

    i = s.index(".")
    s = s[i+1:]

    charStr = ''
    while (s!= ''):
        binVal, s = getFirstBin(s)
        charStr = charStr + getChar(binVal)

    f = open("TextOutput.txt","w+")
    f.write(charStr)
    f.close()
    
      
#Task 6
def task6(p1: str ,p2: str= "TextOutput.txt")->bool:
    f = open(p1, "r")
    s1 = f.read()
    f.close()

    f = open(p2, "r")
    s2 = f.read()
    f.close()

    for chars in s1:
        if chars in s2 and s1.index(chars) == s2.index(chars):
            #print(True)
            return True
    else:
        #print(False)
        return False

#task4('Test.txt')
#task5()
#task6('Test.txt',)

