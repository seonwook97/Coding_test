select
    a.user_id,
    case
        when b.action is null then 0
        else round(count(case when b.action = 'confirmed' then b.action end) / count(*), 2)
    end confirmation_rate
from    
    signups a
left join
    confirmations b on a.user_id = b.user_id
group by
    1