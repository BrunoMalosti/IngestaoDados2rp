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

def EhNull(palavra):
    if palavra == "NULL" :
        return 'NULL'
    else: 
        return  '"'+palavra+'"'

file = open('1 - SQL PERSON.sql', 'w+')

with open ('Person.Person.csv', mode = 'r') as arq:
    leitor = csv.reader(arq, delimiter = ';')
    linhas = 0


    for coluna in leitor:
        if linhas == 0:
            file.write(f'CREATE TABLE Person(\n'+
                'BusinessEntityID       int primary key NOT NULL,\n'+
                'PersonType	            varchar(20),\n'+
                'NameStyle	            int,\n'+
                'Title	                varchar(50),\n'+
                'FirstName              varchar(50),\n'+
                'MiddleName	            varchar(20),\n'+
                'LastName	            varchar(50),\n'+
                'Suffix	                varchar(20),\n'+
                'EmailPromotion	        int,\n'+
                'AdditionalContactInfo	varchar(2000),\n'+
                'Demographics	        varchar(800),\n'+
                'rowguid	            varchar(80),\n'+
                'ModifiedDate           datetime\n'+
                ');\n\n\n\n\n')
            linhas += 1

        else:
            if linhas == 1:
                file.write(f'INSERT INTO Person (BusinessEntityID,PersonType,NameStyle,Title,FirstName,MiddleName,LastName,Suffix,EmailPromotion,AdditionalContactInfo,Demographics,rowguid,ModifiedDate)\n'+
                f'VALUES ({coluna[0]},"{coluna[1]}",{coluna[2]},{EhNull(coluna[3])},"{removerAcentosECaracteresEspeciais(coluna[4])}","{coluna[5]}","{removerAcentosECaracteresEspeciais(coluna[6])}",{EhNull(coluna[7])},{coluna[8]},{EhNull(removerAspasDuplas(coluna[9]))},"{removerAspasDuplas(coluna[10])}","{coluna[11]}","{coluna[12]}")')
                linhas +=1
            else:
                file.write(f',\n')
                file.write(f'({coluna[0]},"{coluna[1]}",{coluna[2]},{EhNull(coluna[3])},"{removerAcentosECaracteresEspeciais(coluna[4])}","{coluna[5]}","{removerAcentosECaracteresEspeciais(coluna[6])}",{EhNull(coluna[7])},{coluna[8]},{EhNull(removerAspasDuplas(coluna[9]))},"{removerAspasDuplas(coluna[10])}","{coluna[11]}","{coluna[12]}")')
                linhas +=1
    file.close()
    print (f' {linhas}, linhas')