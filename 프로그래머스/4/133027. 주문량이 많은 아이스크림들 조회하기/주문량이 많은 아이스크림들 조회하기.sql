SELECT flavor
FROM (SELECT f.flavor, (SUM(f.total_order) + sum(j.total_order)) AS total_order
      FROM FIRST_HALF f
        JOIN JULY j
        ON f.flavor = j.flavor
      GROUP BY f.flavor
      ORDER BY total_order DESC) t
limit 3;