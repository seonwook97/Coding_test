select
    year(b.sales_date) year,
    month(b.sales_date) month,
    a.gender,
    count(*) users
from
    user_info a
join
(
 select
    user_id,
    
    online_sale 

) b on a.user_id = b.user_id
where 1=1
and a.gender is not null
group by
    1, 2, 3
order by
    1, 2, 3