# Write your MySQL query statement below
select
    round(count(case when a.order_date = a.customer_pref_delivery_date then a.delivery_id end) / count(a.delivery_id) * 100, 2)  immediate_percentage
from
(
    select
        *,
        rank() over(partition by customer_id order by order_date) rnk
    from
        delivery
) a
where a.rnk = 1