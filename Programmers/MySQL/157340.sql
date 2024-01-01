select
    car_id,
    max(case
        -- end_date가 2022-10-16일 경우도 '대여중'으로 포함했기 때문에
        -- 2022-10-16 00:00:00, 2022-10-16 23:59:59 유의 
        when '2022-10-16' between start_date and end_date then '대여중'
        else '대여 가능'
    end) as availability
from 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by
    1
order by
    1 desc  