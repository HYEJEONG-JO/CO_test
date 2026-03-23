-- 코드를 입력하세요
SELECT HOUR(datetime) AS hour, COUNT(*) AS count
FROM ANIMAL_OUTS
WHERE HOUR(datetime) BETWEEN 9 AND 19
GROUP BY HOUR(datetime)
ORDER BY hour;