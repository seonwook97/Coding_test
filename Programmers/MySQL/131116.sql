SELECT
    category,
    price,
    product_name
from
    food_product
where 1=1
and (category, price) in
(
select
    category,
    max(price) max_price
from
    food_product
where 1=1
and category in ('과자', '국', '김치', '식용유')
group by
    1
)
order by
    2 desc