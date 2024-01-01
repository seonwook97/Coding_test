with cte as -- 월별, 자동차id별 레코드 건수 -> 최종 출력을 위한 format
(
select
    month(start_date) as MONTH,
    car_id as CAR_ID,
    count(*) as RECORDS
from 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
where 1=1
and year(start_date) = 2022 -- 연도 2022
and month(start_date) between 8 and 10 -- 대여 시작일 기준 8~10월
group by 
    1, 2
),
cte2 as -- 해당 기간 내 자동차 id별 레코드 건수 합 >= 5
(
select
    car_id,
    sum(records) as sum_records
from
    cte
group by 
    1
having sum(records) >= 5
)
select
    *
from
    cte
where 1=1
and car_id in (select distinct car_id from cte2) -- 조건에 해당하는 자동차 id
and records >= 1 -- 특정 월의 총 대여 횟수가 0인 경우는 제외
order by
    month, car_id desc -- 정렬 순서 규칙        