/*
select * from Person;
select * from Customer;
select * from Product;
select * from SalesOrderDetail order by (LineTotal) DESC ;
select * from SalesOrderHeader;
select * from SpecialOfferProduct where SpecialOfferID = 1 ;
*/

/*
drop table Person;
drop table Customer;
drop table Product;
drop table SalesOrderDetail;
drop table SalesOrderHeader;
drop table SpecialOfferProduct;
*/
/*
drop database BDTESTE;
create database BDTESTE;
use BDTESTE;
show tables;
*/

/*
1. Escreva uma query que retorna a quantidade de linhas na tabela
Sales.SalesOrderDetail pelo campo SalesOrderID, desde que tenham pelo menos
três linhas de detalhes.
*/

SELECT SalesOrderID, COUNT(*)  -- Retorna os dados agrupados pelo id, filtrando apenas 3 ou mais recorrências do mesmo id
FROM SalesOrderDetail
	GROUP BY SalesOrderID
	HAVING COUNT(*) >= 3;

/*
2. Escreva uma query que ligue as tabelas Sales.SalesOrderDetail,
Sales.SpecialOfferProduct e Production.Product e retorne os 3 produtos (Name)
mais vendidos (pela soma de OrderQty), agrupados pelo número de dias para
manufatura (DaysToManufacture).
*/

SELECT prod.NameProduct, SUM(detail.OrderQty), prod.DaysToManufacture
	FROM
		SpecialOfferProduct AS offer 
        INNER JOIN Product AS prod ON offer.ProductID = prod.ProductID -- intersecao da Product com a Offer
        INNER JOIN SalesOrderDetail AS detail ON offer.SpecialOfferID = detail.SalesOrderDetailID -- intersecao da Offer com a Detail
group by prod.DaysToManufacture
ORDER by SUM(detail.OrderQty) DESC LIMIT 3;

/*
3. Escreva uma query ligando as tabelas Person.Person, Sales.Customer e
Sales.SalesOrderHeader de forma a obter uma lista de nomes de clientes e uma
contagem de pedidos efetuados.
*/
SELECT 
		p.BusinessEntityID as IdPessoa, 
		CONCAT(p.FirstName,' ',p.LastName) as Nome, 
		COUNT(*) AS Num_Pedidos 
FROM 
        SalesOrderHeader AS header
        INNER JOIN	Customer AS c ON header.CustomerID = c.CustomerID -- intersecao da header com a customer
        INNER JOIN Person AS p ON c.PersonID = p.BusinessEntityID -- intersecao da person com a costumer
GROUP BY c.PersonID
ORDER BY Num_Pedidos DESC;

/*
4. Escreva uma query usando as tabelas Sales.SalesOrderHeader,
Sales.SalesOrderDetail e Production.Product, de forma a obter a soma total de
produtos (OrderQty) por ProductID e OrderDate.
*/
SELECT detail.ProductID as id, 
       prod.NameProduct as Nome_Produto,
       sum(OrderQty) OVER(PARTITION BY detail.ProductID) AS Soma_ProductID, -- Ordena por Product ID
       sum(OrderQty) OVER(PARTITION BY header.OrderDate) AS Soma_OrderDate -- Ordena pelo OrderDate
FROM 
    SalesOrderDetail AS detail
    INNER JOIN Product AS prod ON detail.ProductID = prod.ProductID -- intersecao da product com a detail
    INNER JOIN SalesOrderHeader as header ON detail.SalesOrderID  = header.SalesOrderID -- intersecao da detail com a header
GROUP BY detail.ProductID
ORDER BY id;
/*
5. Escreva uma query mostrando os campos SalesOrderID, OrderDate e TotalDue da
tabela Sales.SalesOrderHeader. Obtenha apenas as linhas onde a ordem tenha
sido feita durante o mês de setembro/2011 e o total devido esteja acima de 1.000.
Ordene pelo total devido decrescente.
*/

SELECT SalesOrderID, DATE(OrderDate), TotalDue 
FROM SalesOrderHeader
	WHERE DATE(OrderDate) 
		BETWEEN 
			DATE('2011-09-01') AND 
			DATE('2011-09-30') AND 
        TotalDue > 1.000
ORDER BY TotalDue DESC;
