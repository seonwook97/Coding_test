with cte as 
(
select
    a.flavor,
    a.sum_order_1 + b.sum_order_2 total_ord
from
(
    select
        flavor,
        sum(total_order) sum_order_1
    from
        first_half
    group by 
        1
) a
join
(
    select
        flavor,
        sum(total_order) sum_order_2
    from
        july
    group by
        1
) b on a.flavor = b.flavor 
order by
    2 desc
limit 
    3
)
select
    flavor
from
    cte