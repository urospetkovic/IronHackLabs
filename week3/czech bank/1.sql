select A2 as 'district_name', A11 as 'salary' 
from district
where A11 > 10000;

select loan_id, account_id, amount, status from loan
where status in ('B')
#and amount > 100000
order by amount DESC;

select type, card_id from card
where type ='junior';

select A10 as urban_population, A2 as district_name 
from district
where A10 < 50
order by A10 DESC;



