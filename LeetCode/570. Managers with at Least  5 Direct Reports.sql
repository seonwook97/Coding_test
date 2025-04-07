select
    a.name
from
    employee a
join
(
    select  
        managerid
    from
        employee
    group by
        1
    having
        count(*) >= 5
) b
on a.id = b.managerid
