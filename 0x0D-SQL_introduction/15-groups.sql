-- The script used to list the number of records with the same score in the table.

-- second_table of the database hbtn_0c_0.

-- result to display the score.

-- number of records for this score with the label number.

-- list should be sorted by the number of records (descending).

from second_table
GROUP BY score
ORDER BY number DESC;
