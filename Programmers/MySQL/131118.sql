SELECT
    a.rest_id,
    a.rest_name,
    a.food_type,
    a.favorites,
    a.address,
    b.score
FROM
    rest_info a
join
(
    select
        rest_id,
        round(avg(review_score), 2) score
    from 
        rest_review
    group by
        1
) b on a.rest_id = b.rest_id
where 1=1
and a.address like '서울%' -- 문제에서 서울로 시작인지 포함인지 명확하게 제시하지 않음.
order by
    6 desc, 4 desc