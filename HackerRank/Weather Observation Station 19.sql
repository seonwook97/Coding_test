select
    round(sqrt(pow(max(lat_n) - min(lat_n), 2) + pow(max(long_w) - min(long_w), 2)), 4)
from    
    station