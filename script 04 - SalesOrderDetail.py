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

def removerPonto(palavra):
    return palavra.replace('.','')

def EhNull(palavra):
    if palavra == "NULL" :
        return 'NULL'
    else: 
        return  '"'+palavra+'"'

file = open('4 - SQL SALES_ORDER_DETAIL.sql', 'w+')

with open ('Sales.SalesOrderDetail.csv', mode = 'r') as arq:
    leitor = csv.reader(arq, delimiter = ';')
    linhas = 0


    for coluna in leitor:
        if linhas == 0:

            file.write(f'CREATE TABLE SalesOrderDetail(\n'+
                
                'SalesOrderID	        int,\n'+
                'SalesOrderDetailID	    int,\n'+
                'CarrierTrackingNumber	varchar(20),\n'+
                'OrderQty	            int,\n'+
                'ProductID	            int,\n'+
                'SpecialOfferID	        int,\n'+
                'UnitPrice	            numeric (16,4),\n'+
                'UnitPriceDiscount	    numeric (16,4),\n'+
                'LineTotal	            bigint,\n'+
                'rowguid	            varchar(50),\n'+
                'ModifiedDate           datetime,\n'+
                'PRIMARY KEY (SalesOrderID,SalesOrderDetailID)\n'+
                ');\n\n\n\n\n')
            linhas += 1



        else:
            if linhas == 1:
                file.write(f'INSERT INTO SalesOrderDetail(SalesOrderID,SalesOrderDetailID,CarrierTrackingNumber,OrderQty,ProductID,SpecialOfferID,UnitPrice,UnitPriceDiscount,LineTotal,rowguid,ModifiedDate)\n'+
                f'VALUES ({coluna[0]},{coluna[1]},"{coluna[2]}",{coluna[3]},{coluna[4]},{coluna[5]},{removerVirgulaPorPonto(coluna[6])},{removerVirgulaPorPonto(coluna[7])},{removerPonto(coluna[8])},"{coluna[9]}","{coluna[10]}")')
                linhas +=1
            else:
                file.write(f',\n')
                file.write(f'({coluna[0]},{coluna[1]},"{coluna[2]}",{coluna[3]},{coluna[4]},{coluna[5]},{removerVirgulaPorPonto(coluna[6])},{removerVirgulaPorPonto(coluna[7])},{removerPonto(coluna[8])},"{coluna[9]}","{coluna[10]}")')
                linhas +=1
    file.close()
    print (f' {linhas}, linhas')
