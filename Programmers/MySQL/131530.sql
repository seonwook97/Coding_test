SELECT
    -- * 다른 풀이
    -- floor(): 지정된 숫자보다 작거나 같은 가장 큰 정수 값을 반환
    -- floor(price / 10000) * 10000 as price_group,
    case
        when price < 10000 then 0        
        when price >= 10000 then cast(substr(cast(price as char), 1, 1) as double) * 10000
    end as price_group,
    count(*) as products
from 
    product
group by
    1
order by
    1  