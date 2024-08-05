# Write your MySQL query statement below

SELECT Sales.year, Sales.price, Product.product_name
FROM Sales, Product
WHERE Sales.product_id = Product.product_id;
