/* Recreating Results from the CTE Query Lecture using Window Functions*/

/* This is the CTE we developed in the CTE lecture in  "10_cte_lecture.sql" */

-- 1st CTE: daily_totals
WITH daily_totals AS (
	SELECT flight_date,
		   origin, 
		   dest, 
		   COUNT(*) AS flights_per_day 
	FROM flights
	WHERE (origin, dest) = ('JFK', 'LAX')
	GROUP BY flight_date, origin, dest
),
-- 2nd CTE: monthly_totals
monthly_totals AS (
	SELECT DATE_TRUNC('month', flight_date) AS yearmonth, 
	   origin, 
	   dest, 
	   MAX(flights_per_day) AS max_daily_total_per_month 	
	FROM daily_totals
	GROUP BY yearmonth, origin, dest
),
-- 3rd CTE: add the maximum to the daily detail
daily_totals_with_max AS (
	SELECT f.flight_date,
		   f.origin,
		   f.dest,
		   COUNT(*) AS flights_per_day,
		   MAX(mt.max_daily_total_per_month) AS max_daily_total_per_month
	FROM flights f 
	JOIN monthly_totals mt
	ON DATE_TRUNC('month', f.flight_date) = mt.yearmonth 
		AND f.origin=mt.origin 
		AND f.dest=mt.dest
	GROUP BY flight_date, f.origin, f.dest
)
SELECT * FROM daily_totals_with_max;


/* We will now shorten the last 2 steps 
 * (groupby aggregation + join to the original detail data) 
 * by using the Window Function
 * 
 * The result should be the same
 */


-- 1st CTE: daily_totals
WITH daily_totals AS (
	SELECT flight_date,
		   DATE_TRUNC('month', flight_date) AS yearmonth,
		   origin, 
		   dest, 
		   COUNT(*) AS flights_per_day 
	FROM flights
	WHERE (origin, dest) = ('JFK', 'LAX')
	GROUP BY flight_date, origin, dest
)
SELECT flight_date,
	   origin,
	   dest,
	   flights_per_day,
	   MAX(flights_per_day) OVER (PARTITION BY yearmonth, origin, dest) AS max_daily_total_per_month
FROM daily_totals
