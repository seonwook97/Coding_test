SELECT
    member_id,
    member_name,
    gender,
    date_format(date_of_birth, '%Y-%m-%d') as date_of_birth
from
    member_profile
where 1=1
and month(date_of_birth) = 3
and gender = 'W'
and TLNO is not null
order by
    1 