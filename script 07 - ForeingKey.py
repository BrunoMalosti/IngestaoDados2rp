file = open('7 - SQL FOREING_KEY.sql', 'w+')

file.write(f"\n"+
    "ALTER TABLE SpecialOfferProduct\n"+ 
        "ADD CONSTRAINT fk_product FOREIGN KEY ( ProductID ) REFERENCES Product ( ProductID );\n\n"+
    
    "ALTER TABLE Customer\n"+ 
        "ADD CONSTRAINT fk_person FOREIGN KEY ( PersonID ) REFERENCES Person ( BusinessEntityID );\n\n"+

    "ALTER TABLE SalesOrderHeader\n"+ 
        "ADD CONSTRAINT fk_costumer FOREIGN KEY ( CustomerID ) REFERENCES Customer ( CustomerID );\n\n"+

    "ALTER TABLE SalesOrderDetail\n"+ 
        "ADD CONSTRAINT fk_order_header FOREIGN KEY ( SalesOrderID ) REFERENCES SalesOrderHeader ( SalesOrderID );\n\n"+

    "ALTER TABLE SalesOrderDetail\n"+ 
        "ADD CONSTRAINT fk_order_offer FOREIGN KEY ( SpecialOfferID ) REFERENCES SpecialOfferProduct ( SpecialOfferID );\n\n"+
    
    "ALTER TABLE SalesOrderDetail\n"+ 
        "ADD CONSTRAINT fk_order_detail FOREIGN KEY ( ProductID ) REFERENCES Product ( ProductID );\n\n"+
    
    "\n\n\n\n\n")



file.close()
print (f'FEITO')


    
