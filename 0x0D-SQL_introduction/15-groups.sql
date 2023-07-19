-- Grouping BY group equal score values
SELECT score, COUNT(score) as number FROM second_table
GROUP BY score
ORDER BY score DESC;
