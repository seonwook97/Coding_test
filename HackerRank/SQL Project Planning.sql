select
    min(a.start_date),
    max(a.end_date)
from
(
    SELECT 
        start_date,
        end_date,
        start_date - row_number() over(order by start_date) seq
    from
        projects
) a
group by
    seq
order by
    (max(a.end_date) - min(a.start_date)), min(a.start_date)