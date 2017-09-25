# importing libraries
import os
import csv
import sys

#INPUT FILE PATH DEFINITION
Input_file_Path = "I0809_SI_WMS_Input_File.csv"

#OUT PUT FILE PATH DEFINITION
Output_file_Path = 'I0809_SI_Issues_SAP_Upload.CSV'
Error_file_Path = 'I0809_SI_Issues_SAP_Upload_Error_Records.CSV'


#OPEN INPUT FILE AND CHECK FOR EXCEPTION
try:
   fh = open(Input_file_Path, "r")
except IOError:
   print "Error: can\'t find file or read data - Input File name Should be I0809_SI_WMS_Input_File.csv"
   sys.exit(1)
else:
   print "Input File Opened Successfully"
   fh.close()

#OPEN OUTPUT FILE
OutputFile = open(Output_file_Path, 'wb')
WriteRecord = csv.writer(OutputFile, quoting=csv.QUOTE_ALL)

Errorfile = open(Error_file_Path, 'wb')
ErrorRecord = csv.writer(Errorfile, quoting=csv.QUOTE_ALL)

with open(Input_file_Path) as csvfile:
    next(csvfile, None)
    readCSV = csv.reader(csvfile, delimiter=',')
    LS_WMS_Data = list(readCSV)

#FORM THE SAP SCENARIOS FOR WHICH WMS DATA SHOULD BE COMPARED AND VALIDATED
DC_SAP_Secenarios = {}
DC_SAP_Secenarios['S1']='ADJUSTMENT,AD,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S2']='ADJUSTMENT,AD,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S3']='ADJUSTMENT,AD,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S4']='ADJUSTMENT,AD,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S5']='ADJUSTMENT,BK,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S6']='ADJUSTMENT,BK,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S7']='ADJUSTMENT,BK,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S8']='ADJUSTMENT,BK,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S9']='ADJUSTMENT,DI,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S10']='ADJUSTMENT,DI,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S11']='ADJUSTMENT,DW,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S12']='ADJUSTMENT,DW,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S13']='ADJUSTMENT,DW,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S14']='ADJUSTMENT,DW,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S15']='ADJUSTMENT,EX,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S16']='ADJUSTMENT,EX,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S17']='ADJUSTMENT,EX,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S18']='ADJUSTMENT,EX,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S19']='ADJUSTMENT,GAINSSTORE,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S20']='ADJUSTMENT,GAINSSTORE,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S21']='ADJUSTMENT,HO,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S22']='ADJUSTMENT,HO,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S23']='ADJUSTMENT,HO,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S24']='ADJUSTMENT,HO,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S25']='ADJUSTMENT,HS,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S26']='ADJUSTMENT,HS,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S27']='ADJUSTMENT,HS,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S28']='ADJUSTMENT,HS,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S29']='ADJUSTMENT,IE,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S30']='ADJUSTMENT,IE,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S31']='ADJUSTMENT,IE,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S32']='ADJUSTMENT,IE,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S33']='ADJUSTMENT,IF,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S34']='ADJUSTMENT,IF,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S35']='ADJUSTMENT,IF,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S36']='ADJUSTMENT,IF,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S37']='ADJUSTMENT,LOSSSTORE,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S38']='ADJUSTMENT,LOSSSTORE,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S39']='ADJUSTMENT,OS,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S40']='ADJUSTMENT,OS,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S41']='ADJUSTMENT,OS,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S42']='ADJUSTMENT,OS,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S43']='ADJUSTMENT,RT,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S44']='ADJUSTMENT,RT,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S45']='ADJUSTMENT,RT,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S46']='ADJUSTMENT,RT,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S47']='ADJUSTMENT,SC,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S48']='ADJUSTMENT,SC,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S49']='ADJUSTMENT,SC,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S50']='ADJUSTMENT,SC,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S51']='ADJUSTMENT,ST,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S52']='ADJUSTMENT,ST,LOCKED,LOCKED,-'
DC_SAP_Secenarios['S53']='ADJUSTMENT,ST,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S54']='ADJUSTMENT,ST,UNLOCKED,UNLOCKED,-'
DC_SAP_Secenarios['S55']='INV LOCK,CODEAPP,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S56']='INV LOCK,CS,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S57']='INV LOCK,DMGD,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S58']='INV LOCK,EVENT,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S59']='INV LOCK,EXCEPT,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S60']='INV LOCK,EXPD,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S61']='INV LOCK,HOREQ,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S62']='INV LOCK,HS,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S63']='INV LOCK,INCUB,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S64']='INV LOCK,LOCK,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S65']='INV LOCK,NV,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S66']='INV LOCK,OS,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S67']='INV LOCK,PRODRECALL,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S68']='INV LOCK,RDCRETURNS,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S69']='INV LOCK,SUDMG,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S70']='INV LOCK,SUPPRETURN,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S71']='INV LOCK,WHDMG,UNLOCKED,LOCKED,+'
DC_SAP_Secenarios['S72']='INV UNLOCK,UNLOCK,LOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S73']='KIT BUILD,BUFFER,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S74']='KIT BUILD,BUFFER,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S75']='PUTAWAY,PUTAWAY,UNLOCKED,UNLOCKED,+'
DC_SAP_Secenarios['S76']='UNKIT,BUFFER,LOCKED,LOCKED,+'
DC_SAP_Secenarios['S77']='UNKIT,BUFFER,UNLOCKED,UNLOCKED,+'

#WRITE THE HEADER RECORD FOR OUTPUT FILE
LS_Output_Record = []
LS_Output_Record.insert(0,'TransactionCode')
LS_Output_Record.insert(1,'ReasonCode')
LS_Output_Record.insert(2,'FromStatus')
LS_Output_Record.insert(3,'ToStatus')
LS_Output_Record.insert(4,'MovementSign')
LS_Output_Record.insert(5,'ArticleNumber')
LS_Output_Record.insert(6,'Qty')
LS_Output_Record.insert(7,'UOM')

WriteRecord.writerow(LS_Output_Record)

#WRITE THE HEADER RECORD FOR ERROR OUTPUT FILE
ErrorRecord.writerow(LS_Output_Record)

for eachrecord in LS_WMS_Data:
    #print eachrecord
    LS_Output_Record = []
    #DIRECT MAP THE CODE
    CODE = eachrecord[0].upper()

        
    # LOGIC TO DERIVE REASON CODE
    REASON_CODE = ''
    Bol_Write_Record = False
    if CODE == 'ADJUSTMENT':
        REASON_CODE = eachrecord[1].upper()
        Bol_Write_Record = True
    elif CODE == 'PUTAWAY':
        REASON_CODE = 'PUTAWAY'
        Bol_Write_Record = True
    elif CODE == 'INV LOCK' and eachrecord[7]:
        REASON_CODE = eachrecord[7].upper()
        Bol_Write_Record = True
    elif CODE == 'INV LOCK' and not eachrecord[7]:
        REASON_CODE = 'EXCEPT'
        Bol_Write_Record = True
    elif CODE == 'INV UNLOCK':
        REASON_CODE = 'UNLOCK'
        Bol_Write_Record = True
    else:
        Bol_Write_Record = False


    #print "REASON CODE " + str(Bol_Write_Record) + str(eachrecord)
    # LOGIC TO DERIVE FROM STATUS
    FROM_STATUS_CODE = ''
    if CODE == 'ADJUSTMENT' or CODE == 'PUTAWAY':
        FROM_STATUS_CODE = eachrecord[2].upper()
        Bol_Write_Record = True
    elif CODE == 'INV UNLOCK':
        FROM_STATUS_CODE = 'LOCKED'
        Bol_Write_Record = True
    elif CODE == 'INV LOCK':
        FROM_STATUS_CODE = 'UNLOCKED'
        Bol_Write_Record = True
    else:
        Bol_Write_Record = False

    #print "FROM STATUS " + str(Bol_Write_Record) + str(eachrecord)
    # LOGIC TO DERIVE TO STATUS
    TO_STATUS_CODE = ''
    if Bol_Write_Record:
        
        if CODE == 'ADJUSTMENT' or CODE == 'PUTAWAY':
            TO_STATUS_CODE = eachrecord[2].upper()
            Bol_Write_Record = True
        elif CODE == 'INV UNLOCK':
            TO_STATUS_CODE = 'UNLOCKED'
            Bol_Write_Record = True
        elif CODE == 'INV LOCK':
            TO_STATUS_CODE = 'LOCKED'
            Bol_Write_Record = True
        else:
            Bol_Write_Record = False
            
    #print "TO STATUS " + str(Bol_Write_Record) + str(eachrecord)   
    # LOGIC TO DERIVE THE SIGN OF THE QTY
    SIGN = ''
    if Bol_Write_Record:
        
        if int(eachrecord[5]) < 0:
            SIGN='-'
        elif int(eachrecord[5]) > 0:
            SIGN='+'
        else:
            Bol_Write_Record = False
            
    #print "SIGN " + str(Bol_Write_Record) + str(eachrecord)
    # SIGN
    ARTICLE = ''
    if Bol_Write_Record:
        
        if eachrecord[4]:
            ARTICLE = eachrecord[4]
        else:
           Bol_Write_Record = False
    #print "ARTICLE " + str(Bol_Write_Record) + str(eachrecord)
    # QTY
    QTY = ''
    if Bol_Write_Record:
        
        if eachrecord[5]:
            QTY = abs(int(eachrecord[5]))
        else:
            Bol_Write_Record = False
    #print "QTY " + str(Bol_Write_Record) + str(eachrecord)
    
    # UOM
    UOM = ''
    if Bol_Write_Record:
        
        if eachrecord[6]:
            UOM = eachrecord[6]
        else:
            Bol_Write_Record = False 
        
    #print "UOM " + str(Bol_Write_Record) + str(eachrecord)
    
    LS_Output_Record.insert(0,CODE)
    LS_Output_Record.insert(1,REASON_CODE)
    LS_Output_Record.insert(2,FROM_STATUS_CODE)
    LS_Output_Record.insert(3,TO_STATUS_CODE)
    LS_Output_Record.insert(4,SIGN)
    LS_Output_Record.insert(5,ARTICLE)
    LS_Output_Record.insert(6,QTY)
    LS_Output_Record.insert(7,UOM)

    iteration = 0
    WMS_Scenario_Key = ''
    #print LS_Output_Record
    if Bol_Write_Record:

        #DERIVE THE WMS SCENARIO KEY FROM THE OUTPUT RECORD
        WMS_Scenario_Key = ",".join([str(item) for index, item in enumerate(LS_Output_Record) if index < 5])
        
        # CHECK WHETHER THE WMS SCENARIO KEY MATCHES SAP SCENARIO KEY, IF NOT - ERROR THE RECORD
        if WMS_Scenario_Key in DC_SAP_Secenarios.values():
            WriteRecord.writerow(LS_Output_Record)
        else:
            ErrorRecord.writerow(LS_Output_Record)
    elif CODE == "RECEIPT":
        print "SKIPPING RECEIPT RECORD " + str(eachrecord)
    else:
        #write the record to error file
        ErrorRecord.writerow(LS_Output_Record)
        print 'WMS OUTPUT HAS GOT ERRORS - PLEASE CHECK'
        sys.exit(1)

# scanning through sub folders
OutputFile.close()
Errorfile.close()
print "Script Completed Successfully "
