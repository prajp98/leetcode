SELECT name as Customers
FROM Customers c
WHERE c.id NOT IN (
    SELECT customerId FROM Orders
);

SELECT c.name
FROM Customers c
LEFT JOIN Orders o
  ON c.id = o.customerId
WHERE o.id IS NULL;