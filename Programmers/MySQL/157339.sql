-- 문제가 좀 애매함
SELECT 
    distinct
    a.car_id as CAR_ID,
    # 검산
    # a.daily_fee,
    # c.duration_type,
    # c.discount_rate,
    # b.start_date,
    # b.end_date,
    a.car_type as CAR_TYPE,
    cast(30 * a.daily_fee * (1 - c.discount_rate / 100) as unsigned) as FEE
from 
    car_rental_company_car a
left join 
(
    select
        car_id,
        min(start_date) as start_date,
        max(end_date) as end_date
    from
        car_rental_company_rental_history
    group by 
        1 
    # having 
    #     min(start_date) > '2022-11-30' or max(end_date) < '2022-11-01'
) 
b on a.car_id = b.car_id
left join
    car_rental_company_discount_plan c on a.car_type = c.car_type and c.duration_type = '30일 이상'
where 1=1
and (b.start_date > '2022-11-30' or b.end_date < '2022-11-01')
and a.car_type in ('세단', 'SUV')
and cast(30 * a.daily_fee * (1 - c.discount_rate / 100) as unsigned) >= 500000 
and cast(30 * a.daily_fee * (1 - c.discount_rate / 100) as unsigned) < 2000000
order by
    3 desc, 2, 1 desc


# 클린코드
# SELECT A.CAR_ID, A.CAR_TYPE,
#        ROUND((A.DAILY_FEE * 30 / 100 * (100 -
#             (SELECT DISCOUNT_RATE 
#              FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
#              WHERE CAR_TYPE = A.CAR_TYPE AND DURATION_TYPE = "30일 이상")))) AS FEE
# FROM CAR_RENTAL_COMPANY_CAR AS A
#      JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS B
#      ON A.CAR_ID = B.CAR_ID
# WHERE A.CAR_TYPE IN ("SUV", "세단") AND
#      (A.CAR_ID NOT IN (SELECT CAR_ID 
#                        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
#                        WHERE start_date <= '2022-11-01' and end_date >= '2022-11-01'))
# GROUP BY A.CAR_ID    
# HAVING FEE >= 500000 AND FEE < 2000000
# ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC