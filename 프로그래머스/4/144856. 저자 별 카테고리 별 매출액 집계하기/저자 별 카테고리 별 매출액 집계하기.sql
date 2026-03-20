SELECT a.author_id, a.author_name, b.category, SUM(b.price * bs.sales) AS TOTAL_SALES
FROM BOOK b
JOIN AUTHOR a ON b.author_id = a.author_id
JOIN BOOK_SALES bs ON b.book_id = bs.book_id
WHERE DATE_FORMAT(bs.sales_date, '%Y-%m') = '2022-01'
GROUP BY a.author_id, a.author_name, b.category
ORDER BY a.author_id ASC, b.category DESC;