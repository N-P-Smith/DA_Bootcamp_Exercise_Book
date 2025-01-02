/* # JOINS - Exercises */

/* JOINS with Tables: 'flights' and 'airports'  */

/* Q1. What was the longest flight? (not using JOIN yet) 
 * Hint: NULL values are the first in a descending ORDER BY. You might need a filter for that.
 */



/* Q2. From which airport the longest flight? (now with JOIN)
 * Hint: NULL values are the first in a descending ORDER BY. You might need a filter for that.
 */



/* Q3. On a 2024-01-23 find 3 cities: 
 * 
 * Step 1: city the most count of flights (departing) per day
 * Step 2: city with the most unique planes departed
 * Step 3: city with them most unique airlines active
 * 
 * Solving without Subqueries or CTE's (covered tomorrow):
 * first we'll find the values for each statistic (3 queries)
 * in the final query manually paste the values to the grouping condition 
 */

-- Step 1



-- Step 2



-- Step 3



-- Final Query



/* Q4. The table 'flights' is about domestic flights in US. Let's double-check! 
 * 		Find unique country names for all departures in January 2024.
 * 
 * 		Hint: One option to filter dates is to use BETWEEN '2024-01-01' AND '2024-01-31'
 */ 
  


/* Q5. What is the count of all departures per 'country' in January 2024?
 * 
 * 		Hint: some listed flights wer cancelled, consider it in the filter
 */



/* Q6. Which airport and in which city had the most departures in January 2024?
 * 
 * 		Hint: we also need to filter out the cancelled flights.
 */



/* Q7. To which city/cities does the airport with the second most arrivals belong?
 * 
 * 		Hint: remember the the clause to Skip a number of rows before LIMITing it?
 */



/* Q8. Filter the data to January 1, 2023 and count all rows for that day so that your result set has two columns: flight_date, total_flights.  
 * 		Repeat this step, but this time only include data from January 1, 2024.
 * 		Combine the two result sets using UNION.
 */



--> UNION combines the distinct results of two or more SELECT statements


/* Q9. The last query can be optimized, right?
 * 		Rewrite the query above so that you get the same output, but this time you are not allowed to use UNION.
 * 
 * 		Hint: we filter data for those 2 days. 
 */



/* Q10. Which flights had a departure delay of more than 30 minutes?
 *      How big was the delay?
 * 	    What was the plane's tail number?
 * 	    On which day and in which city?   
 * 	    Answer all questions with a single query.
 */



/* Q11. Which airports (add city name)
 * 		- had how many fligts with a departure delay of more than 30 minutes?
 *      	- what was the average delay?
 * 			- how many unique aiplanes were involved?
 */




