SELECT name AS Customers
FROM Customers
WHERE id IN (SELECT customerId FROM Orders);