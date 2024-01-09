SELECT
    a.product_id,
    a.product_name,
    a.price * b.amount total_sales
from
    food_product a
join
(
    select
        product_id,
        sum(amount) amount
    from
        food_order
    where 1=1
    and date_format(produce_date, '%Y-%m') = '2022-05'
    group by
        1     
) b on a.product_id = b.product_id
order by
    3 desc, 1