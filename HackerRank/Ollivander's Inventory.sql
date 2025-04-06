select
    B.id,
    B.age,
    A.coins_needed,
    B.power
from
(
    select
        Wands.power power,
        Wands_Property.age age,
        min(coins_needed) coins_needed
    from
        Wands
    left join 
        Wands_Property on Wands.code = Wands_Property.code
    where Wands_Property.is_evil = 0
    group by 
        power, age
) A
left join
(
    select 
        Wands.id,
        Wands.power power,
        Wands_Property.age age,
        Wands.coins_needed
    from 
        Wands 
    left join 
        Wands_Property on Wands.code = Wands_Property.code
    where Wands_Property.is_evil = 0
) B
on 1=1
and a.power = b.power
and a.age = b.age
and a.coins_needed = b.coins_needed
order by power desc, age desc