with cte as 
(
    select
        date_format(sales_date, '%Y-%m-%d') as sales_date,
        product_id,
        user_id,
        sales_amount
    from online_sale
    where 1=1
    and year(sales_date) = 2022
    and month(sales_date) = 3
    union
    select
        date_format(sales_date, '%Y-%m-%d') as sales_date,
        product_id,
        null as user_id,
        sales_amount
    from offline_sale
    where 1=1
    and year(sales_date) = 2022
    and month(sales_date) = 3
)
select
    *
from
    cte
order by
    1, 2, 3