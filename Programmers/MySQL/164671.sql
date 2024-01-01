SELECT
    concat('/home/grep/src/', a.board_id, '/', b.file_id, b.file_name, b.file_ext) as FILE_PATH -- 파일 경로 출력 조건 -> concat을 통한 문자열 합침
from 
    used_goods_board a
left join
    used_goods_file b on a.board_id = b.board_id
where 1=1
and a.views = (select max(views) from used_goods_board) -- 조건: 조회수 제일 많은 것 
order by 
    b.file_id desc -- 조건: file_id를 기준으로 내림차순