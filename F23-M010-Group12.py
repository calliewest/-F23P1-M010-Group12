import pandas as pd
import math

eFileRaw = pd.ExcelFile("/workspaces/-F23P1-M010-Group12/excel.xlsx")
eNames = eFileRaw.sheet_names
eFileParsed = eFileRaw.parse(eNames[0])
eFileList = eFileParsed.values.tolist()

#print(eFileParsed)
#print(f'{eFileList}\n')