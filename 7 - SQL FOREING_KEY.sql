
ALTER TABLE SpecialOfferProduct
ADD CONSTRAINT fk_product FOREIGN KEY ( ProductID ) REFERENCES Product ( ProductID );

ALTER TABLE Customer
ADD CONSTRAINT fk_person FOREIGN KEY ( PersonID ) REFERENCES Person ( BusinessEntityID );

ALTER TABLE SalesOrderHeader
ADD CONSTRAINT fk_costumer FOREIGN KEY ( CustomerID ) REFERENCES Customer ( CustomerID );

ALTER TABLE SalesOrderDetail
ADD CONSTRAINT fk_order_header FOREIGN KEY ( SalesOrderID ) REFERENCES SalesOrderHeader ( SalesOrderID );

ALTER TABLE SalesOrderDetail
ADD CONSTRAINT fk_order_offer FOREIGN KEY ( SpecialOfferID ) REFERENCES SpecialOfferProduct ( SpecialOfferID );

ALTER TABLE SalesOrderDetail
ADD CONSTRAINT fk_order_detail FOREIGN KEY ( ProductID ) REFERENCES Product ( ProductID );






