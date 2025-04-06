-- select
--     (case when a.marks < 70 then null else a.name end) as name,
--     (case when b.grade is null then 10 else b.grade end) as grade,
--     a.marks as marks
-- from
--     students a 
-- left join
--     grades b
-- on (a.marks - mod(a.marks, 10)) = b.min_mark
-- order by 
--     grade desc, name
    
-- clean code
SELECT 
    CASE
        WHEN g.Grade >= 8 THEN s.Name
        ELSE 'NULL'
    END AS Name,
    g.Grade,
    s.Marks
FROM Students s
JOIN Grades g
    ON s.Marks BETWEEN g.Min_Mark AND g.Max_Mark
ORDER BY 
    g.Grade DESC,
    CASE
        WHEN g.Grade >= 8 THEN s.Name
        ELSE s.Marks
    END ASC;