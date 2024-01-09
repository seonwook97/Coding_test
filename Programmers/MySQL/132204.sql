SELECT
    a.apnt_no,
    c.pt_name,
    c.pt_no,
    a.mcdp_cd,
    b.dr_name,
    a.apnt_ymd
from
    appointment a
join
    doctor b on a.mddr_id = b.dr_id
join 
    patient c on a.pt_no = c.pt_no
where 1=1
and a.mcdp_cd = 'CS'
and a.apnt_cncl_yn = 'N'
and date_format(a.apnt_ymd, '%Y-%m-%d') = '2022-04-13'
order by
    6