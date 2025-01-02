/* Q1. Select the first 20 rows of all columns in the 'flights' table.
 *      Please provide the query below.
 */
 select *
from airports
limit 20;

/* Q2. Select the first 20 rows the 'flights' table with columns that have
 * 	   - the date of the flight,
 * 	   - the airport code of the origin airport
 * 	   - the airport code of the destination airport
 * 	   - information whether the flight was cancelled or not
 *     Please provide the query below.
 */
select
	flight_date,
	origin,
	dest,
	cancelled
from flights
limit 20;

/* Q3. What's the name of the airport that is shown in the first row when sorting by airport code descending?
 * 	   Hint: the whole row is too much information, show only the necessary fields.
 *     Please provide the query and answer below.
 */
select name
from airports
order by faa desc
limit 1;

Zanesville Municipal Airport

/* Q4. Return a list of all unique countries with an airport in this table. 
 * 	   What does that tell you about the airports table?
 *     Please provide the query below.
 */
select distinct
	country
from airports;

/* Q5. Select the country, city and name of all airports. 
 * 	    Sort city in ascending and name in descending order.
 * 		What's the name of the airport that is listed last?
 *      Hint: somethimes you need to put things upside down to see what is at the bottom.
 *      Please provide the query below.
 */
select
	country,
	city,
	name
from airports
order by city asc, name desc;

Australia		Ararat Airport

/* Q6. Which airport has the lowest altitude?
 *      Please provide the query and answer below.
 */
select
	name,
	alt
from airports
order by alt
limit 1;

Bar Yehuda Airfield	-1266

/* Q7. Which airport would have the lowest altitude if we transformed all positive altitudes into negative altitudes and vice versa?
 *     Hint: How can you mathematically make a 10 to -10? 
 * 	   Please provide the query and answer below.
 */
select
	name,
	alt
from airports
order by alt desc
limit 1;

Daocheng Yading Airport	14472

/* Teacher solution
*/
select
	name,
	alt*(-1)
from airports
order by alt*(-1)
limit 1;

Daocheng Yading Airport	-14472

 /* Q8. Give each column selected in the query below a more descriptive name using aliasing.
 * 		If you're not sure what the column means, check out this documentation: https://cran.r-project.org/web/packages/nycflights13/nycflights13.pdf
 */
SELECT faa as aiportCode,
	   lat as latitude,
	   lon as longitude,
	   alt as altitude,
	   tz as timeZone,
	   dst as destination
FROM airports;

-- BONUS: probably obsolete

 /* Q9. Create a column that turns dep_delay into a categorical variable with one of 5 categories.
 * Depending on the delay a flight will be either:
 * '>15 min Early', '<=15 min Early', 'On time', '<=15 min Delayed' or '>15 min Delayed'.
 */