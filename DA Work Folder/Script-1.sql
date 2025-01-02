table flights;

select *
from flights
limit 20;

select
	flight_date,
	origin,
	dest,
	cancelled
from flights
limit 20;
	
select name
from airports
order by faa desc
limit 1;

select distinct
	country
from airports;

select
	country,
	city,
	name
from airports
order by city desc, name asc;

select
	name,
	alt
from airports
order by alt
limit 1;

select
	name,
	alt
from airports
order by alt desc
limit 1;

select name,
	alt*(-1)
from airports
order by alt*(-1)
limit 1;