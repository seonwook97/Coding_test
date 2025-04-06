select
    c.name
from
    friends a
left join
    students b on a.friend_id = b.id
left join
    students c on a.id = c.id
left join
    packages d on a.id = d.id
left join
    packages e on a.friend_id = e.id
where 1=1
and e.salary > d.salary
order by
    e.salary
