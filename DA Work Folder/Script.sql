table airports;

select faa,
	name,
	city,
	country
from airports;

select *
from airports
limit 15;

select
	name,
	city,
	country
from airports
order by city asc, country desc;

select *
from airports
order by country;

select distinct country
from airports
order by country;

select
	name,
	city,
	country,
	alt
from airports
order by alt;

select
	faa,
	name,
	city,
	country
from airports
order by faa;

