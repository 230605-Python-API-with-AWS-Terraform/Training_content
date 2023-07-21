1.You have a table for customers and a table for orders. How would you return all orders for the customer with email 'Ibrahim@email.com'?

Join the orders and customers table on the customer_id foreign key and filter for the email:

```SQL

SELECT *
FROM orders
JOIN customers ON orders.customer_id = customers.id
WHERE customers.email = 'Ibrahim@email.com';
```
---

2. You want to calculate the total sales value for each customer from their orders. How would you do this?

Join orders and customers, group by customer_id, and SUM the order totals:

```sql

Copy code

SELECT c.id, c.name, SUM(o.total) TOTAL_SALES
FROM customers c
JOIN orders o ON c.id = o.customer_id
GROUP BY c.id;
```
---

3. How would you return a list of customers who have never placed an order?

Use an outer join and check for NULL orders:

```sql

SELECT c.* 
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
WHERE o.id IS NULL;
```

---

4. You want to delete all orders for a customer but not the customer themselves. How would you do this?

Delete orders with a subquery filter:

``` Sql

DELETE FROM orders 
WHERE customer_id IN (
  SELECT id FROM customers WHERE name = 'Vetrivel'
);

```
---

5. You have a table for products and a table for orders. How would you find the order with the highest total value?

Join the tables, group by order id, use MAX() to find highest total:

``` sql

SELECT o.id, MAX(o.total) AS highest 
FROM orders o
JOIN products p ON o.product_id = p.id
GROUP BY o.id
ORDER BY highest DESC
LIMIT 1;
```
---

6. How would you return all customers who have placed more than 2 orders?

Join tables, group by customer, use HAVING count(*) > 2:

```sql

SELECT c.id, c.name
FROM customers c
JOIN orders o ON c.id = o.customer_id  
GROUP BY c.id
HAVING count(*) > 2;

```
---

7. You want to sort products by price in descending order but NULLs should appear first. How would you write this query?

Use ORDER BY price DESC NULLS FIRST:

```sql

SELECT * FROM products
ORDER BY price DESC NULLS FIRST;

```

---


8. How would you select the first 5 rows in a table?

 Use LIMIT 5:

```sql

SELECT * FROM products
LIMIT 5;

```

---

9. How would you find the total sales for each product by month?

Use DATE_TRUNC() to truncate timestamp, GROUP BY product and truncated date:

```sql

SELECT p.name, DATE_TRUNC('month', o.ordered_at) AS month, SUM(o.total)  
FROM products p
JOIN orders o ON p.id = o.product_id
GROUP BY p.name, DATE_TRUNC('month', o.ordered_at)
ORDER BY p.name, month;
```
---

10. How can you select a random row from a table?

Use ORDER BY random() to shuffle then LIMIT 1:

```sql

SELECT *
FROM table
ORDER BY random()
LIMIT 1;

```

---

12. How would you find all customers who have spent more than the average order total?

Use a subquery to calculate the average order value first:

```sql

SELECT * FROM customers
WHERE customer_total > (
  SELECT avg(total) FROM orders
);
```
---

13. How would you return products that have never been ordered?

Use a subquery with EXISTS to check no orders exist:

```sql

SELECT * FROM products p
WHERE NOT EXISTS (
  SELECT * FROM orders o 
  WHERE o.product_id = p.id
);

```
---

14. How can you delete all users who have not placed an order?

Delete with a subquery join the users and orders table:

```sql

DELETE FROM users 
WHERE id NOT IN (
  SELECT DISTINCT user_id FROM orders
);
```

---

15. How would you update the stock level for a product by adding its sold count?

Increment using a subquery to calculate sold count:

```sql

UPDATE products
SET stock = stock + (
  SELECT sum(quantity) FROM orders
  WHERE product_id = products.id
)

```

---

16. How can you find customers who have placed more orders than the average orders per customer?

Nest an aggregate subquery inside the HAVING clause to get average orders per customer:

```sql

SELECT customer_id, count(*)
FROM orders
GROUP BY customer_id
HAVING count(*) > (SELECT avg(order_count) FROM
  (SELECT customer_id, count(*) AS order_count
   FROM orders 
   GROUP BY customer_id) subquery);
```
---

17. How would you use a subquery inside a JOIN clause to select all customers along with their total order amounts?

Join a subquery that calculates the totals per customer:

```sql


SELECT c.*, t.total
FROM customers c
JOIN (
  SELECT customer_id, SUM(amount) AS total
  FROM orders
  GROUP BY customer_id
) t ON c.id = t.customer_id

```

---

