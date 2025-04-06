select
    b.hacker_id,
    b.name,
    sum(max_sc)
from
(
    select
        hacker_id,
        challenge_id,
        max(score) max_sc
    from
        submissions
    group by
        1, 2 
) a
left join
    hackers b on a.hacker_id = b.hacker_id
group by
    1, 2
having
    sum(max_sc) > 0
order by
    sum(max_sc) desc, b.hacker_id
    
    