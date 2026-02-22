SELECT id, email, first_name, last_name
FROM DEVELOPER_INFOS
WHERE skill_1 = 'Python' or skill_2 = 'Python' or skill_3 = 'Python'
ORDER BY id ASC