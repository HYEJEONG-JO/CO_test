WITH FIRST_PAR AS (
    SELECT e1.id
    FROM ECOLI_DATA e1
    WHERE e1.parent_id IS NULL
),
SECOND_PAR AS(
    SELECT e2.id
    FROM ECOLI_DATA e2
        JOIN FIRST_PAR f
        ON e2.parent_id = f.id
)

SELECT e3.id
FROM ECOLI_DATA e3 
    JOIN SECOND_PAR s
    ON e3.PARENT_ID = s.ID