import csv
import unicodedata
import re


def removerAcentosECaracteresEspeciais(palavra):

    # Unicode normalize transforma um caracter em seu equivalente em latin.
    nfkd = unicodedata.normalize('NFKD', palavra)
    palavraSemAcento = u"".join([c for c in nfkd if not unicodedata.combining(c)])
    # Usa expressão regular para retornar a palavra apenas com números, letras e espaço
    return re.sub('[^a-zA-Z0-9 \\\]', '', palavraSemAcento)

def removerAspasDuplas(palavra):
    return palavra.replace('"','')

def removerVirgulaPorPonto(palavra):
    return palavra.replace(',','.')

def EhNull(palavra):
    if palavra == "NULL" :
        return 'NULL'
    else: 
        return  '"'+palavra+'"'

file = open('5 - SQL SALES_ORDER_HEADER.sql', 'w+')

with open ('Sales.SalesOrderHeader.csv', mode = 'r') as arq:
    leitor = csv.reader(arq, delimiter = ';')
    linhas = 0


    for coluna in leitor:
        if linhas == 0:
            file.write(f'CREATE TABLE SalesOrderHeader(\n'+
                'SalesOrderID	        int primary key NOT NULL,\n'+
                'RevisionNumber	        int,\n'+
                'OrderDate	            datetime,\n'+
                'DueDate	            datetime,\n'+
                'ShipDate	            datetime,\n'+
                'Status	                int,\n'+
                'OnlineOrderFlag	    int,\n'+
                'SalesOrderNumber	    varchar(20),\n'+
                'PurchaseOrderNumber	varchar(30),\n'+
                'AccountNumber	        varchar(40),\n'+
                'CustomerID	            int,\n'+
                'SalesPersonID	        int,\n'+
                'TerritoryID	        int,\n'+
                'BillToAddressID	    int,\n'+
                'ShipToAddressID	    int,\n'+
                'ShipMethodID	        int,\n'+
                'CreditCardID	        int,\n'+
                'CreditCardApprovalCode	varchar(40),\n'+
                'CurrencyRateID	        int,\n'+
                'SubTotal	            numeric (16,4),\n'+
                'TaxAmt	                numeric (16,4),\n'+
                'Freight	            numeric (16,4),\n'+
                'TotalDue	            numeric (16,4),\n'+
                'Comment	            varchar(100),\n'+
                'rowguid	            varchar(50),\n'+
                'ModifiedDate           datetime\n'+

                ');\n\n\n\n\n')


            linhas += 1

        else:
            if linhas == 1:
                file.write(f'INSERT INTO SalesOrderHeader (SalesOrderID, RevisionNumber, OrderDate, DueDate, ShipDate, Status, OnlineOrderFlag, SalesOrderNumber, PurchaseOrderNumber, AccountNumber, CustomerID, SalesPersonID, TerritoryID, BillToAddressID, ShipToAddressID, ShipMethodID, CreditCardID, CreditCardApprovalCode, CurrencyRateID, SubTotal, TaxAmt, Freight, TotalDue, Comment, rowguid, ModifiedDate)\n'+
                f'VALUES ({coluna[0]},{coluna[1]},"{coluna[2]}","{coluna[3]}","{coluna[4]}",{coluna[5]},{coluna[6]},"{coluna[7]}","{coluna[8]}","{coluna[9]}",{coluna[10]},{coluna[11]},{coluna[12]},{coluna[13]},{coluna[14]},{coluna[15]},{coluna[16]},"{coluna[17]}",{coluna[18]},{removerVirgulaPorPonto(coluna[19])},{removerVirgulaPorPonto(coluna[20])},{removerVirgulaPorPonto(coluna[21])},{removerVirgulaPorPonto(coluna[22])},{EhNull(coluna[23])},"{coluna[24]}","{coluna[25]}")')
                linhas +=1
            else:
                file.write(f',\n')
                file.write(f'({coluna[0]},{coluna[1]},"{coluna[2]}","{coluna[3]}","{coluna[4]}",{coluna[5]},{coluna[6]},"{coluna[7]}","{coluna[8]}","{coluna[9]}",{coluna[10]},{coluna[11]},{coluna[12]},{coluna[13]},{coluna[14]},{coluna[15]},{coluna[16]},"{coluna[17]}",{coluna[18]},{removerVirgulaPorPonto(coluna[19])},{removerVirgulaPorPonto(coluna[20])},{removerVirgulaPorPonto(coluna[21])},{removerVirgulaPorPonto(coluna[22])},{EhNull(coluna[23])},"{coluna[24]}","{coluna[25]}")')
                linhas +=1
    file.close()
    print (f' {linhas}, linhas')


    
