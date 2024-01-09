select
    substr(b.sales_date, 1, 4) year,
    substr(b.sales_date, 6, 2) month,
    a.gender,
    count(*) users
from
    user_info a
join
(
 select
    user_id,
    date_format(sales_date, '%Y-%m') sales_date
 from   
    online_sale 
 group by
    1, 2
) b on a.user_id = b.user_id
where 1=1
and a.gender is not null
group by
    1, 2, 3
order by
    1, 2, 3