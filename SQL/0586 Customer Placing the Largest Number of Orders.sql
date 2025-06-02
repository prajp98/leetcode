SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;

SELECT customer_number
FROM orders
GROUP BY customer_number
HAVING COUNT(order_number) =
(
SELECT MAX(count) from
    (
     SELECT COUNT(order_number) as count, customer_number from orders group by customer_number
     ) sub1
);