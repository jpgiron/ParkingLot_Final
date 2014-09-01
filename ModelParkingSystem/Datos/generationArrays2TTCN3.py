# -*- coding: utf-8 -*-

from xlrd import open_workbook
from string import *

def main():

    nameWorkBook=input("Type the name of the workbook without ext.\n")
    nameOutputFileTTCN3=input("Type the name of the output ttcn3 without ext:\n")

    ArrayData=getData(nameWorkBook) #Store the info of the file *.xls in python's lists
    conversion2TTCN3(ArrayData,nameOutputFileTTCN3) # Store in a file *.ttcn3 the info of the lists.

def getData(nFile):

    #nFile is the name of the file *.xls that wil be read.

    filename = nFile+".xls"
    book = open_workbook(filename)

    ###constants definitions###

    zone0=0
    zone1=1
    ctrl0=0
    ctrl1=1
    CTRL0ZONE0=3
    CTRL0ZONE1=4
    CTRL1ZONE0=5
    CTRL1ZONE1=6
    SHEET_ENTRADA=1
    SHEET_CONSOLIDADO=3
    dataBook=[]
    total=[]

    sheet_index = 1 #begin from sheet called ENTRADA up the sheet called CONSOLIDADO

    for sheet_index in range(SHEET_ENTRADA,SHEET_CONSOLIDADO+1):
        sheet=book.sheet_by_index(sheet_index) #It select the sheet of the book *.xls
        row_index = 1 # Start reading the sheet from row 2
        value_Cars_WholeSheet = [] #Store the Cars Total than entered or out of whole the system.
        value_Ctrl_WholeSheet = [] #Store the Ctrl where a car Entered or Out...is beetwen 0 or 1.
        value_Zone_WholeSheet = [] #Store the Zone where a car Entered or Out...is beetwen 0 or 1.
        for row_index in range(sheet.nrows):
            col_index=0
            for col_index in range(sheet.ncols):
                if (row_index>0):
                    if ( col_index==CTRL0ZONE0 ):
                        value_Cars_WholeSheet.append(sheet.cell(row_index,col_index).value)
                        value_Ctrl_WholeSheet.append(ctrl0)
                        value_Zone_WholeSheet.append(zone0)
                    elif ( col_index==CTRL0ZONE1 ):
                        value_Cars_WholeSheet.append(sheet.cell(row_index,col_index).value)
                        value_Ctrl_WholeSheet.append(ctrl0)
                        value_Zone_WholeSheet.append(zone1)
                    elif ( col_index== CTRL1ZONE0):
                        value_Cars_WholeSheet.append(sheet.cell(row_index,col_index).value)
                        value_Ctrl_WholeSheet.append(ctrl1)
                        value_Zone_WholeSheet.append(zone0)
                    elif ( col_index== CTRL1ZONE1 ):
                        value_Cars_WholeSheet.append(sheet.cell(row_index,col_index).value)
                        value_Ctrl_WholeSheet.append(ctrl1)
                        value_Zone_WholeSheet.append(zone1)
        dataBook.append(value_Cars_WholeSheet)
        dataBook.append(value_Ctrl_WholeSheet)
        dataBook.append(value_Zone_WholeSheet)
    return dataBook

def conversion2TTCN3(dataWorkBook,nameTTCN3):

    #inputs: dataWorkBook represent the data of the file *.xls
    #but equivalent to lists in python and nameTTCN3 is the
    #name that will have the module in TTCN-3.

    ###CONSTANTS###

    nameArrays_TTCN3=['aEntryCar','aCtrlEntryCar','aZoneEntryCar','aOutCar','aCtrlOutCar','aZoneOutCar',
                      'aExpectedSpots','aCtrlExpected','aZoneExpected']
    Length_Vec_Datas=len(dataWorkBook)
    Length_Rows_Vec=len(dataWorkBook[0])
    i=0

    #Creation of file *.ttcn3#
    nameFileTTCN3=nameTTCN3+".ttcn3"
    fileTTCN3=open(nameFileTTCN3,'w')

    #Creation of type array in TTCN-3#
    fileTTCN3.write("module "+nameTTCN3+" {\n")
    fileTTCN3.write("/*These are the definitions of the array*/\n")
    fileTTCN3.write("type integer generic_array_data["+str(Length_Rows_Vec)+
                    "];\n")
    fileTTCN3.write("const integer length_array_data:="+str(Length_Rows_Vec)+";\n")

    for i in range(len(dataWorkBook)):
        data=dataWorkBook[i]

        # Change the syntaxis of the List in Python for a vector in TTCN-3

        dataStr=str(data).replace("[","{")
        dataStr=dataStr.replace("]","}")
        dataStr=dataStr.replace(".0","")

        #Write in the file *.ttcn3

        fileTTCN3.write("const generic_array_data "+nameArrays_TTCN3[i]+":="+dataStr+";\n")
    fileTTCN3.write("}")
    fileTTCN3.close()

#called to main function:
main()
