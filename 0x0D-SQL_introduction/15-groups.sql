-- lists the number of records with the same
-- score in the table second_table of the
-- database hbtn_0c_0 in your MySQL server.
-- The result should display:
-- 1. the score
-- 2. the number of records for this score with the label number
-- 3. The list should be sorted by the number of records (descending)
SELECT score, COUNT(*) AS number FROM second_table 
GROUP BY score ORDER BY score DESC;
