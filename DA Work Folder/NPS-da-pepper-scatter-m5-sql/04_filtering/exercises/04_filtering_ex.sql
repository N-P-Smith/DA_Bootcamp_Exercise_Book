-- SQL - Filtering data with the WHERE clause

-- remark: we don't always specify if you have to select distinct values or all. decide what makes more sense :)

/* Q1. Return list of all airports in Canada.
 *     Please provide the query below.
 */
select *
from airports
where country = 'Canada';

/* Q2. Return list of all airports that are above 500 and below 1500 altitude.
 *     Please provide the query below.
 */
 select *
 from airports
 where alt between 500 and 1500;

/* Q3. Return list of all flights that had a departure delay smaller or equal to 0.
 *     Please provide the query below.
 */
 select *
 from flights
 where dep_delay <= 0;

/* Q4. Return list of all flights that have a missing value (NULL value) as their departure time.
 *      Please provide the query below.
 */
select *
from flights
where dep_time is NULL;

/* Q5. Return list of all airports from BENELUX countries.
 *      Please provide the query below.
 */
select *
from airports
where country in ('Belgium', 'Netherlands', 'Luxembourg');

/* Q6. Return list of all airports from BENELUX countries that are below 0 altitude.
 *      Please provide the query below.
 */
select *
from airports
where country in ('Belgium', 'Netherlands', 'Luxembourg')
    and alt < 0;

 /*Q7. How can we quickly change the query from Q6. and see what other airports have altitude below 0?
 * 	  Hint: we need to revert something.
 * 		Please provide the query and answer below
 */
select *
from airports
where country not in ('Belgium', 'Netherlands', 'Luxembourg')
    and alt < 0;

/* Q8. Return list of all flights on December 31, 2023 that have a departure time of NULL or were cancelled.
 *      Please provide the query below.
 */
select *
from flights
where flight_date = '2023-12-31'
    and ((dep_time is NULL) or (cancelled = 1)); 

