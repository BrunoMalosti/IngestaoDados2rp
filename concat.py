arq = open("SQL_DADOS.sql", "w")
arq1 = open("1 - SQL PERSON.sql", "r") 
arq2 = open("2 - SQL PRODUCT.sql", "r")
arq3 = open("3 - SQL CUSTOMER.sql", "r")
arq4 = open("4 - SQL SALES_ORDER_DETAIL.sql", "r")
arq5 = open("5 - SQL SALES_ORDER_HEADER.sql", "r")
arq6 = open("6 - SQL SPECIAL_OFFER_PRODUCT.sql", "r")
arq7 = open("7 - SQL FOREING_KEY.sql", "r")

arq.write(arq1.read()+";\n\n\n\n\n"+arq2.read()+";\n\n\n\n\n"+arq3.read()+";\n\n\n\n\n"+arq4.read()+";\n\n\n\n\n"+arq5.read()+";\n\n\n\n\n"+arq6.read()+";\n\n\n\n\n"+arq7.read())
arq.close()