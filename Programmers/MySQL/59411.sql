select outs.animal_id, outs.name
from animal_outs as outs, animal_ins as ins
where ins.animal_id = outs.animal_id
order by outs.datetime - ins.datetime desc
limit 2