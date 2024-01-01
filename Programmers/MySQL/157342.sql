SELECT
    car_id,
    round(avg(datediff(end_date, start_date) + 1), 1) as average_duration -- 시간 단위를 따질 시 일 수 차이를 1일 더해줘야 하는데 뭔가 좀 이상함 문제가
from 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by
    1
having 
    average_duration >= 7
order by 
    2 desc, 1 desc  