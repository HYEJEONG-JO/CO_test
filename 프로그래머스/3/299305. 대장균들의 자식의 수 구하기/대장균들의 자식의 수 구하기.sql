SELECT e1.id, count(e2.id) AS CHILD_COUNT
FROM ECOLI_DATA e1
    LEFT JOIN ECOLI_DATA e2
    ON e1.id = e2.parent_id
GROUP BY e1.id
ORDER BY e1.id ASC;