# 전체 데이터 개수
select count(*) from tbl_navernews;

# 데이터 중 상위
select distinct(title) from tbl_navernews order by pubDate desc; # 중복값 제거 distinct

select * from tbl_navernews 
group by title
order by pubDate desc;


