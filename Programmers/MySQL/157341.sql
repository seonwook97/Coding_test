SELECT
    distinct a.car_id
from
    CAR_RENTAL_COMPANY_CAR a
left join
    CAR_RENTAL_COMPANY_RENTAL_HISTORY b 
on a.car_id = b.car_id
where 1=1
and month(b.start_date) = 10
and a.car_type = '세단'
order by
    1 desc 