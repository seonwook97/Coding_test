with cte as
(
SELECT
    user_id,
    product_id,
    count(*) cnt
from
    online_sale
group by
    1, 2
having 
    cnt >= 2
)
select
    user_id,
    product_id
from cte
order by
    user_id, product_id desc    