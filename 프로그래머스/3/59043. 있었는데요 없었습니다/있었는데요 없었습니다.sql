-- 코드를 입력하세요
SELECT o.animal_id, o.name
FROM ANIMAL_INS i
    JOIN ANIMAL_OUTS o
    ON i.animal_id = o.animal_id
WHERE i.datetime > o.datetime
ORDER BY i.datetime;