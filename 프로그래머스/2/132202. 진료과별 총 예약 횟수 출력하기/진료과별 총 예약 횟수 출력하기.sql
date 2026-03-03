SELECT mcdp_cd, COUNT(*) AS appointment_count
FROM APPOINTMENT
WHERE apnt_ymd >= '2022-05-01' AND apnt_ymd <  '2022-06-01'
GROUP BY mcdp_cd
ORDER BY appointment_count ASC, mcdp_cd ASC;