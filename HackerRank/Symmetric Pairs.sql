-- sol1
-- SELECT f1.X, f1.Y
-- FROM Functions f1
-- JOIN Functions f2 ON f1.X = f2.Y AND f1.Y = f2.X
-- WHERE f1.X <= f1.Y
-- GROUP BY f1.X, f1.Y
-- HAVING COUNT(*) > 1 OR f1.X < f1.Y
-- ORDER BY f1.X

-- sol2
select
    x, y
from
    functions
group by
    x, y
having
    count(*) = 2
union
select
    f1.x, f1.y
from
    functions f1
join
    functions f2 
on f1.x = f2.y 
and f2.x = f1.y
where f1.x < f1.y
order by
    x