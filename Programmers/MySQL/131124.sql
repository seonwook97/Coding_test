with cnt_lst as
(
    select
        member_id,
        count(*) cnt
    from
        rest_review
    group by 
        1
    order by 
        2 desc
    limit 1
)
select 
    b.member_name,
    a.review_text,
    date_format(a.review_date, '%Y-%m-%d') review_date
from
    rest_review a
left join
    member_profile b on a.member_id = b.member_id
where 1=1
and a.member_id = (select member_id from cnt_lst)
order by
    3, 2