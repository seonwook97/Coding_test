-- 1
select
    concat(name,'(',substr(occupation, 1, 1),')') as result
from
    occupations
order by
    name
;

-- 2
with occ_cnt as 
(
    select 
        occupation, 
        count(*) cnt 
    from 
        occupations 
    group by 
        1
)
select
    concat('There are a total of ', cnt, ' ' , lower(occupation), 's.') as result
from
    occ_cnt
order by
    cnt, occupation
;