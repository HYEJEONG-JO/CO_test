SELECT DATE_FORMAT(onli.sales_date, '%Y-%m-%d') AS sales_date, onli.product_id, onli.user_id, onli.sales_amount
FROM ONLINE_SALE onli
WHERE DATE_FORMAT(onli.sales_date, '%Y-%m') = '2022-03'

UNION ALL

SELECT DATE_FORMAT(offli.sales_date, '%Y-%m-%d') AS sales_date, offli.product_id, NULL AS user_id, offli.sales_amount
FROM OFFLINE_SALE offli
WHERE DATE_FORMAT(offli.sales_date, '%Y-%m') = '2022-03'
ORDER BY sales_date ASC, product_id ASC, user_id ASC;