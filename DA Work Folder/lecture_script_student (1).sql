SELECT * FROM  products;
---------------------------
-- let's focus on PRODUCT PER CATEGORY

SELECT category_id 
	   ,product_name
	   ,unit_price
FROM products
ORDER BY category_id;

---------------------------
-- what is the overall average price of the products? -> modify the following query...

SELECT unit_price --<<- Update this line...
FROM products;


---------------------------
-- what is the AVERAGE UNIT PRICE IN EACH CATEGORY? -> modify the following query...

SELECT category_id
	   ,unit_price --<<- Update this line...
FROM products
	               --<<- Update this line...
ORDER BY category_id;

-- Our data colapsed to a table with with unique values in the category_id column
---------------------------
-- What if we still want to see the detailed information: product_name, unit_price? ...

WITH initial_data AS (
					  -- add PRODUCT PER CATEGORY query
),
avg_prices AS (
					  -- add AVERAGE UNIT PRICE IN EACH CATEGORY
)
SELECT * 
FROM initial_data
LEFT JOIN avg_prices 
USING (category_id);

---------------------------
/* WINDOW FUNCTIONS */ 

-- Unlike GROUP BY window functions will not collapse the dataset  
-- and leave the original data intact if that is the users goal. 

/* 3 Types of Window Functions:
		- AGGREGATION window functions
		- RANKING window functions  
		- VALUE window functions
		
General syntax: 

	window_function_name ( expression ) OVER ( partition_clause
											order_clause
											frame_clause
											) 

NOTE: mind those three clauses...  partition, order, frame (row, range)

*/

-- let's look at some examples:
----------------------------------
/* AGGREGATION window functions */
----------------------------------
-- 1. display the information about the products together with 
-- the average price OF ALL the products

SELECT category_id
		,product_name
		,unit_price
		,unit_price --<<- Update this line...
FROM products
ORDER BY category_id;

---------------------------

-- 2. display the information about the products together with 
-- the average CATEGORY price

SELECT category_id
		,product_name
		,unit_price
		,unit_price --<<- Update this line...
FROM products
ORDER BY category_id;

------------------------------
/* RANKING window functions */
------------------------------
-- 3. display product details together with 
-- the rank by price

SELECT product_name 
       ,unit_price 
       ,category_id
       ,unit_price --<<- Update this line...
FROM products;

----------------------------
-- 4. display product details together with 
-- the rank by price
-- but within a category

SELECT product_name 
       ,unit_price 
       ,category_id 
       ,unit_price --<<- Update this line...---
FROM products;

-- other ranking window functions:
-- https://www.postgresqltutorial.com/postgresql-window-function/

---------------------------------------------------------
/* frame_clause (back to aggregation window functions) */
---------------------------------------------------------
-- 5. display product details together with 
-- the max price of 
-- this product, the product before and the product after (within categories!)
SELECT product_name
       ,unit_price 
       ,category_id
       ,unit_price --<<- Update this line...
FROM products;

----------------------------

/* frame_clause (cumulative calculations) */

-- we are using another table "order_details" for that
SELECT * FROM order_details; 

----------------------------

-- 6. display product details together with
-- the cumulative quantity of ordered items

SELECT order_id
	   ,product_id
	   ,quantity
       ,SUM(quantity) OVER(ORDER BY order_id 
	                       ROWS UNBOUNDED PRECEDING) AS cumulative_quantity
FROM order_details;

-- NOTE:  
--"UNBOUNDED PRECEDING" means that the frame starts with the first row of the partition
--"UNBOUNDED FOLLOWING" means that the frame ends with the last row of the partition.

------------------------------
-- 7. display product details together with
-- the cumulative quantity of ordered items per order

SELECT order_id 
	   ,product_id
	   ,quantity
       ,SUM(quantity) OVER(ORDER BY order_id 
       		               RANGE UNBOUNDED PRECEDING) AS cumulative_quantity_per_order
FROM order_details;

------------------------------
-- 8. display product details together with
-- the cumulative quantity of the items within each order

SELECT order_id 
	   ,product_id
	   ,quantity
       ,SUM(quantity) OVER(PARTITION BY order_id 
       		               ORDER BY order_id 
						   ROWS UNBOUNDED PRECEDING) AS cumulative_quantity_within_order
FROM order_details;

----------------------------
/* VALUE window functions */
----------------------------
-- values comparison and difference calculations
-- extract the information from other rows of data

------------------------------
-- 9. display product details together with 
-- the unit price of the previous product

SELECT product_name 
	   ,unit_price
       ,unit_price --<<- Update this line...
FROM products;

------------------------------
-- 10. display product details together with  
-- the unit price of the previous product 
-- and the difference between the prices in percent

SELECT product_name 
       ,unit_price
       ,LAG(unit_price) OVER() AS previous_value
	   , --- ???
FROM products;