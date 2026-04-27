SELECT C.id, C.genotype, P.genotype
FROM ECOLI_DATA C
    JOIN ECOLI_DATA P
    ON C.parent_id = P.id
WHERE C.genotype & P.genotype = P.genotype
ORDER BY C.id ASC