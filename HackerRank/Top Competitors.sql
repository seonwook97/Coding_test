select
    a.hacker_id, 
    a.name
from
(
    select
        nm.name,
        a.hacker_id,
        count(*) cnt
    from
        submissions a
    join
        hackers nm on a.hacker_id = nm.hacker_id
    left join
        challenges b on a.challenge_id = b.challenge_id
    left join
        difficulty c on b.difficulty_level = c.difficulty_level
    where 1=1
    and a.score = c.score
    group by 
        1, 2
    having
        cnt > 1
) a
order by
    cnt desc, hacker_id