select count(*)
from flights;

select count (distinct airline)
from flights;

select count(*)
from airports
where country = 'Germany';

select count(*)
from flights
where dep_delay <= 0;

select min(flight_date) as first_day
from flights

select max(flight_date) as last_day
from flights;

select avg(dep_delay)
from flights
where flight_date = '2024-01-01'

select count(*)
from flights
where dep_time is NULL;

select count(*)
from flights
where cancelled = 1;

select
    airline,
    tail_number,
    dep_time
from flights
where dep_time is not NULL
    and cancelled = 1;

select count(*)
from flights
where flight_date = '2024-01-01'
    and ((dep_time is NULL) or (cancelled = 1));

select count(distinct airline)
from flights
where flight_date = '2024-01-01'
    and ((dep_time is NULL) or (cancelled = 1));

select name,
	alt
from airports
order by alt asc
limit 1;



