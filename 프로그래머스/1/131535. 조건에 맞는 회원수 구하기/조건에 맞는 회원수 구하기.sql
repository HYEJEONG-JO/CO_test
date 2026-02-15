-- 코드를 입력하세요
SELECT count(user_id) AS users
FROM USER_INFO
WHERE YEAR(joined) = 2021 AND (age between 20 and 29);