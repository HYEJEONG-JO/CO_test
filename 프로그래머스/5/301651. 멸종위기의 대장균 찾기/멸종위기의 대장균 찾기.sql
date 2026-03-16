WITH RECURSIVE GEN AS (
    SELECT id, parent_id, 1 AS generation
    FROM ECOLI_DATA
    WHERE parent_id IS NULL
    
    UNION ALL
    
    SELECT e.id, e.parent_id, g.generation + 1
    FROM ECOLI_DATA e
    JOIN GEN g
    ON e.parent_id = g.id
)

SELECT COUNT(*) AS COUNT, generation
FROM GEN g
LEFT JOIN ECOLI_DATA e
ON g.id = e.parent_id
WHERE e.id IS NULL
GROUP BY generation
ORDER BY generation