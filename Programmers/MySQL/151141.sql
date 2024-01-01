SELECT 
    a.history_id as HISTORY_ID,
    -- 검산용 
    -- a.start_date,
    -- a.end_date,
    -- datediff(end_date, start_date) + 1 date_diff, -- 이 부분 인지 해야함 29, 30일을 빌린다면 2일을 빌리는거라 +1 
    -- a.duration, 
    -- b.daily_fee, 
    -- c.discount_rate, 
    -- (datediff(a.end_date, a.start_date) + 1) * b.daily_fee FEE_NOT_DISC,
    case 
        when datediff(end_date, start_date) + 1 < 7 then (datediff(a.end_date, a.start_date) + 1) * b.daily_fee
        else cast((datediff(a.end_date, a.start_date) + 1) * b.daily_fee * (1 - c.discount_rate / 100) as unsigned) 
    end as FEE
from 
    (
     select
        *,
        case
            when datediff(end_date, start_date) + 1 < 7 then '7일 미만'
            when datediff(end_date, start_date) + 1 between 7 and 29 then '7일 이상'
            when datediff(end_date, start_date) + 1 between 30 and 89 then '30일 이상'
            when datediff(end_date, start_date) + 1 >= 90 then '90일 이상'
        end as duration
     from
        car_rental_company_rental_history
    ) a
left join
    car_rental_company_car b on a.car_id = b.car_id
left join
    car_rental_company_discount_plan c on b.car_type = c.car_type and a.duration = c.duration_type
where 1=1
and b.car_type = '트럭'
order by
    2 desc, 1 desc     