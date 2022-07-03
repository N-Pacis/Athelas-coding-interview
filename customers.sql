#Question 1
SELECT * FROM Customers WHERE City='Berlin';

#Question 2
SELECT * FROM Customers WHERE City='Mexico City';

#Question 3
SELECT avg(Price) FROM Products;

#Question 4
SELECT count(ProductID) FROM Products where Price=18;

#Question 5
SELECT * FROM Orders WHERE OrderDate BETWEEN '1996-08-01' AND '1996-09-06';

#Question 6
SELECT c.CustomerID,c.CustomerName,ContactName, Address, Country, count(o.CustomerID) as  Orders FROM Orders o INNER JOIN Customers c ON c.customerId = o.CustomerID GROUP BY o.CustomerID  HAVING count(o.CustomerID) > 3;

#Question 7
SELECT Country,City,count(CustomerID) as "Number_Of_Customers" FROM Customers GROUP BY City HAVING count(CustomerID) > 1 ORDER BY City;        

