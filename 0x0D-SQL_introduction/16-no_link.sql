-- The script that lists all records of the table second_table of the database hbtn_0c_0.
-- Don’t list rows without name value.
-- The results should display the score and the name (in this order).
-- The records should be listed by descending score.
SELECT score, `name`
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY score DESC;
