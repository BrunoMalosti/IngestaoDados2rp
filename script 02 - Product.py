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

file = open('2 - SQL PRODUCT.sql', 'w+')

with open ('Production.Product.csv', mode = 'r') as arq:
    leitor = csv.reader(arq, delimiter = ';')
    linhas = 0


    for coluna in leitor:
        if linhas == 0:
            file.write(f'CREATE TABLE Product(\n'+
                'ProductID	            int primary key NOT NULL,\n'+
                'NameProduct            varchar(100),\n'+
                'ProductNumber	        varchar(20),\n'+
                'MakeFlag	            int,\n'+
                'FinishedGoodsFlag	    int,\n'+
                'Color	                varchar(20),\n'+
                'SafetyStockLevel	    int,\n'+
                'ReorderPoint	        int,\n'+
                'StandardCost	        numeric (16,4),\n'+
                'ListPrice	            numeric (16,4),\n'+
                'Size	                varchar(20),\n'+
                'SizeUnitMeasureCode	varchar(20),\n'+
                'WeightUnitMeasureCode	varchar(20),\n'+
                'Weight	                numeric (16,4),\n'+
                'DaysToManufacture	    int,\n'+
                'ProductLine	        varchar(20),\n'+
                'Class	                varchar(20),\n'+
                'Style	                varchar(20),\n'+
                'ProductSubcategoryID	int,\n'+
                'ProductModelID	        int,\n'+
                'SellStartDate	        datetime,\n'+
                'SellEndDate	        datetime,\n'+
                'DiscontinuedDate	    datetime,\n'+
                'rowguid	            varchar(50),\n'+
                'ModifiedDate           datetime\n'+
                ');\n\n\n\n\n')


            linhas += 1

        else:
            if linhas == 1:
                file.write(f'INSERT INTO Product (ProductID,NameProduct,ProductNumber,MakeFlag,FinishedGoodsFlag,Color,SafetyStockLevel,ReorderPoint,StandardCost,ListPrice,Size,SizeUnitMeasureCode,WeightUnitMeasureCode,Weight,DaysToManufacture,ProductLine,Class,Style,ProductSubcategoryID,ProductModelID,SellStartDate,SellEndDate,DiscontinuedDate,rowguid,ModifiedDate)\n'+
                f'VALUES ({coluna[0]},"{coluna[1]}","{coluna[2]}",{coluna[3]},{coluna[4]},{EhNull(coluna[5])},{coluna[6]},{coluna[7]},{removerVirgulaPorPonto(coluna[8])},{removerVirgulaPorPonto(coluna[9])},{EhNull(coluna[10])},{EhNull(coluna[11])},{EhNull(coluna[12])},{EhNull(coluna[13])},{coluna[14]},{EhNull(coluna[15])},{EhNull(coluna[16])},{EhNull(coluna[17])},{EhNull(coluna[18])},{EhNull(coluna[19])},"{coluna[20]}",{EhNull(coluna[21])},{EhNull(coluna[22])},"{coluna[23]}","{coluna[24]}")')
                linhas +=1
            else:
                file.write(f',\n')
                file.write(f'({coluna[0]},"{coluna[1]}","{coluna[2]}",{coluna[3]},{coluna[4]},{EhNull(coluna[5])},{coluna[6]},{coluna[7]},{removerVirgulaPorPonto(coluna[8])},{removerVirgulaPorPonto(coluna[9])},{EhNull(coluna[10])},{EhNull(coluna[11])},{EhNull(coluna[12])},{EhNull(coluna[13])},{coluna[14]},{EhNull(coluna[15])},{EhNull(coluna[16])},{EhNull(coluna[17])},{EhNull(coluna[18])},{EhNull(coluna[19])},"{coluna[20]}",{EhNull(coluna[21])},{EhNull(coluna[22])},"{coluna[23]}","{coluna[24]}")')
                linhas +=1
    file.close()
    print (f' {linhas}, linhas')


    
