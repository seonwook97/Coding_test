select
    round(count(distinct a.player_id) / (select count(distinct player_id) from activity), 2) fraction
from
    activity a
join   
    (
        select
            player_id,
            min(event_date) min_date
        from
            activity
        group by
            1
    ) b 
on a.player_id = b.player_id
and datediff(a.event_date, b.min_date) = 1