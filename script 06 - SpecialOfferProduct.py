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

file = open('6 - SQL SPECIAL_OFFER_PRODUCT.sql', 'w+')

with open ('Sales.SpecialOfferProduct.csv', mode = 'r') as arq:
    leitor = csv.reader(arq, delimiter = ';')
    linhas = 0


    for coluna in leitor:
        if linhas == 0:

            file.write(f'CREATE TABLE SpecialOfferProduct(\n'+
                'SpecialOfferID	        int,\n'+
                'ProductID	            int,\n'+
                'rowguid	            varchar(50),\n'+
                'ModifiedDate           datetime,\n'+
                'PRIMARY KEY (SpecialOfferID,ProductID)\n'+
                ');\n\n\n\n\n')

            linhas += 1

        else:
            if linhas == 1:
                file.write(f'INSERT INTO SpecialOfferProduct (SpecialOfferID,	ProductID,	rowguid, ModifiedDate)\n'+
                f'VALUES ({coluna[0]},{coluna[1]},"{coluna[2]}","{coluna[3]}")')
                linhas +=1
            else:
                file.write(f',\n')
                file.write(f'({coluna[0]},{coluna[1]},"{coluna[2]}","{coluna[3]}")')
                linhas +=1
    file.close()
    print (f' {linhas}, linhas')


    
