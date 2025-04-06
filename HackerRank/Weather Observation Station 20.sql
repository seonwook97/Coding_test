with cte as
(
  SELECT 
    LAT_N,
    ROW_NUMBER() OVER (ORDER BY LAT_N) as row_num,
    COUNT(*) OVER () as total_rows
  FROM 
    STATION
)
SELECT 
  ROUND(AVG(LAT_N), 4) as median
FROM 
    cte
WHERE 1=1
and row_num IN ((total_rows + 1)/2, (total_rows + 2)/2)