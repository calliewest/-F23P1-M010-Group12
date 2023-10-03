import pandas as pd #import the "tool" pandas to read excel file from the computer
# it can also replace by import openpyxl, so we can use the libary in Python to helpo us work with excel films

wb = pd.read_excel("23P1-M010-Group12.xlsx", dtype = str)# read the excel file according to the excel name

c = list(wb["characters"])#create a list for all the characters
b = list(wb["binary"])#create a list for all the binarys

try:
    i = c.index("\\n")
    c[i] = "\n"
except:
    print("\\n was not found")# try to fix \\n into \n, if there is no \\n then skip
    
try:
    i = c.index("<space>")
    c[i] = " "
except:
    print("<space> was not found")# try to fix <space> into " ", if there is no <space> then skip
