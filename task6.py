#pseudocode
#Function takes as input two strings
#Open each file and read in the files into two different string variables
#Close the files
#Check to see if the two strings are identical Same length and same characters in the same order
#Return True if they are the same and False if they are no
def checktextfile("Binoutput.txt","Textoutput.txt" ): #the function for checking whether s(for original strings) and b(for binary values) are the same relationship in the excel file.
    f1 = open (Binoutput.txt)
    f2 = open (Textoutput.txt)  #open the binary and the original string text
    s1 = f1.read()
    s2 = f2.read()  # read the two files
    f1.close()
    f2.close()   # close the two files

    i = s1.index(".")   #count binary values from the "." which means the end of the length number
    s1 = s1[i+1:]      # get the binary value from the Binary file without the total length of the binary value

    charstr = ""   # get the charstr from the binval file
    while s1!= "":
        binval, s = getFirstBinary(s)
        charstr = charstr + getchar(binval)#decode all the binary values into actual strings
        for chars in s2:
            if charstr(binval) == chars(binval):# check if chars from binary value is equal to original text files
                return True#All corresponding then return True
            else:
                return False# If one of them went wrong, then return False