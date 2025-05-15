-- order_verification_query.sql

-- Verify order with ID 1023 exists and was placed by valid user
SELECT 
    o.order_id, o.date_added, o.total, c.firstname, c.lastname, c.email
FROM 
    orders o
JOIN 
    customers c ON o.customer_id = c.customer_id
WHERE 
    o.order_id = 1023;
