# Write your MySQL query statement below
with base as 
(
select id , email , row_number()over(partition by email order by id ) as flag
from person
)
select distinct email from 
base 
where flag >1