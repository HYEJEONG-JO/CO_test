SELECT o.product_id, p.product_name, SUM(p.price * o.amount) AS total_sales
FROM FOOD_PRODUCT p
    JOIN FOOD_ORDER o
    ON p.product_id = o.product_id
WHERE EXTRACT(MONTH FROM produce_date) = 5
GROUP BY o.product_id, p.product_name
ORDER BY total_sales DESC, o.product_id;