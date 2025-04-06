select
    a.hacker_id,
    a.name,
    count(b.challenge_id) cnt
from
    hackers a
left join
    challenges b on a.hacker_id = b.hacker_id
where 1=1
group by
    1, 2
having  
    cnt = (select
              max(a.cnt)
           from
           (
                select
                    hacker_id,
                    count(challenge_id) cnt
                from
                    challenges
                group by
                    1
            ) a
           )
     or
     cnt in (select
              b.cnt
           from
           (
                select
                    hacker_id,
                    count(challenge_id) cnt
                from
                    challenges
                group by
                    1
            ) b
            group by
                1
            having count(*) = 1
            )
order by
    3 desc, 1
               
