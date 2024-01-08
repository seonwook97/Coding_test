SELECT
    a.author_id,
    b.author_name,
    a.category,
    sum(c.sales * a.price) total_sales
from
    book a
join author b on a.author_id = b.author_id
join
(
select
    book_id,
    sum(sales) sales
from
    book_sales
where 1=1
and date_format(sales_date, '%Y-%m') = '2022-01'
group by 
    1
) c on a.book_id = c.book_id
group by
    1, 2, 3
order by
    1, 3 desc