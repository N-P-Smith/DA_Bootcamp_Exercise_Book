-- Functions for Aggregation Data in SQL

/* Q1.1 What is the total number of rows in the flights table?
 * 		Please provide the query and answer below.
 */
select count(*)
from flights;

7017434

/* Q1.2 What is the total number of unique airlines in the flights table?
 * 		Please provide the query and answer below.
 */
select count (distinct airline)
from flights;

15

/* Q3. How many airports does Germany have?
 *     Please provide the query and answer below.
 */
select count(*)
from airports
where country = 'Germany';

95

/* Q4. How many flights had a departure delay smaller or equal to 0?
 *     Please provide the query and answer below.
 */
select count(*)
from flights
where dep_delay <= 0;

4320210

/* Q5. What's the first day and what's the last day of flight_dates in the flights table?
 *     Please provide the query and answer below.
 */
select min(flight_date) as first_day
from flights

2023-09-01 00:00:00.000

select max(flight_date) as last_day
from flights;

2024-08-31 00:00:00.000

/* Q6. What was the average departure delay of all flights on January 1, 2023.
 *     Please provide the query and answer below.
 */
select avg(dep_delay)
from flights
where flight_date = '2024-01-01';

5.3159420289855072

/* Q7.1 How many flights have a missing value (NULL value) as their departure time?
 *      Please provide the query and answer below.
 */
select count(*)
from flights
where dep_time is NULL;

88223

/* Q7.2 Out of all flights how many flights were cancelled? 
 *      Is this number equal to the number of flights that have a NULL value as their departure time above?
 *      Please provide the query and answer below.
 */
select count(*)
from flights
where cancelled = 1;

92079

/* Q7.3 The number of canceled_flights (Q7.2) is higher than the no_dep_time (Q7.1), 
 * 		which means there are flight records with departure time (flight started) but the flights were stil cancelled.
 * 		Show those canceled flight with departure time.
 */
select
    airline,
    tail_number,
    dep_time
from flights
where dep_time is not NULL
    and cancelled = 1;

/* Q8. What's the total number of flights on January 1, 2023 that have a departure time of NULL or were cancelled?
 *      Please provide the query and answer below.
 */
select count(*)
from flights
where flight_date = '2024-01-01'
    and ((dep_time is NULL) or (cancelled = 1));

18

/* Q9. What's the number of airlines that had flights on January 1, 2023 that have a departure time of NULL or were cancelled?
 *      Please provide the query and answer below.
 */
select count(distinct airline)
from flights
where flight_date = '2024-01-01'
    and ((dep_time is NULL) or (cancelled = 1));

6

/* Q10. Which airport has the lowest altitude?
 *      Please provide the query and answer below.
 */
select name,
	alt
from airports
order by alt asc
limit 1;

Bar Yehuda Airfield	-1266



