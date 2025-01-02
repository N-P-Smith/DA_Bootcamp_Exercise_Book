# Day 13, 14.10.2014
## Statistics in Python + Aggregation & GroupBy
Protocol writer: Isadora Batagin

<span style="color:grey">
In these module parts, we discussed the basics of descriptive statistics and how to apply them to a DataFrame with pandas. During the second part of the class, we discussed the data aggregation methods and Group By.
</span>

---
##  __Schedule__
<span style="color:grey">

|Time|Content|
|---|---|
|10:00 - 10:20|Introduction to Descriptive Statistics with Python|
|10:20 - 10:45|Sample vs. Population Group Discussion|
|10:45 - 11:30|Descriptive Statistics with Python|
|11:30 - 12:30|Exercises|
|12:30 - 13:30|Lunch Break| 
|13:30 - 14:30|BoxPlot & Aggregation and Group By|
|15:00 - 17:00|Exercises and Ending|

---
# <span style="color:black"> __Part One: Descriptive Statistics with Python__ </span>
<span style="color:grey">

## <span style="color:black"> __General Concepts__ </span>
**Statistics:** Collecting, cleaning, analyzing datasets, and subsequently making quantitative assertions about a broader population or phenomena.

* **Descriptive Statistics:** Describe and summarize the main features of a dataset.
Utilizes metrics such as mean, median, mode, standard deviation, and variance to describe data attributes.
Examples: Average Temperature of Berlin in January.

* **Inferential statistics:** Uses the data collected from a sample to make predictions or inferences about the larger population from which the sample was drawn. 

**Population & Sample:**

* **Population:** The complete set of items or individuals that share one or more characteristics from which data can be gathered and analyzed. 

* **Sample:** It is a smaller collection of units from the population intended to represent the larger group.

**Categorical & Numeric Variables:**

* **Categorical:** They represent types of data that can be divided into groups rather than numerical values.

* **Numeric:** They quantify amounts and allow for mathematical operations, providing a basis for most statistical analyses and data science applications.

## <span style="color:black"> __Measures of Central Tendency__ </span>

* **Mean:** Calculated as the average value of all the numbers in a dataset.
  - Formula: *Mean* = Sum of all values / Number of values
  - Method: `.mean()`
    
* **Mode:** The value that appears most frequently in a dataset.
  - Method: `.mode()`

* **Median:** The middle value in a dataset when it is ordered from smallest to largest.
  - Method: `.median()`
    

## <span style="color:black"> __Key Measures of Dispersion__ </span>

* **Variance:** It provides a measure of how data points differ from the mean.
    
* **Standard Deviation:** It provides a measure of the average distance between the values of the dataset and the mean

* **Range:** It represents the difference between the highest and the lowest values in the data set.

* **Methods:** `.min()`, `.max()`, `.std()`

* **Quantile:** In the case of a dataset, it refers to the division of the data into equal-sized subsets based upon their values. `.quantile()`
`
* **Correlations:** Mutual connection between two or more variables: values from -1 : 1. Describes the strength of linear relationship between two variables. `.corr`

* **BoxPlot:** `.boxplot()`

  ![image](https://github.com/user-attachments/assets/30fdcb6f-8147-435f-9c75-b0af5ded9f5f)

 
</span>

---
# <span style="color:black"> __Part 2: Aggregation and Group By__ </span>
<span style="color:grey">
 
## <span style="color:black"> __Pandas Aggregation and Grouping__ </span>

- `groupby()`: Allows us to group the data based on one or more variables and then apply aggregation functions to each group.

- `agg()`: This function is used in combination with `groupby()` to specify the aggregation functions to apply to each group.

- Using method chaining: multiple operations can be applied in sequence using dot notation. For example, `groupby().agg().reset_index()`.

- **Pandas Grouping + Descriptive Statistics:** mean(), median(), sum(), min(), max(), std(), var()

- `size()` function to count the number of records in each group.

- `count()`  to count non-null values within each group for specific columns.

- **Others:**

    - `.value_counts()`: count of unique values
 
    - `.value_counts(normalize=True)`: for corresponding percentages

---
# <span style="color:black"> __Exercises__ </span>
</span>

## **Descriptive Analytics 👶 🧓**

</span>

**Q3**

![image](https://github.com/user-attachments/assets/961b487b-960c-4efc-a475-f800a3652e32)


**Q7**

![image](https://github.com/user-attachments/assets/e6377550-35f4-428b-8631-3c67a840c36e)


## **Aggregation and Group By 🐧**

**Pandas Aggregation** - Different Options

- **To calculate the mean, median and standard deviation of the penguins bill length**

  - As a list: `penguins['bill_length_mm'].agg(['mean', 'median', 'std'])`
    
   ![image](https://github.com/user-attachments/assets/588b3ee2-408a-485b-b43a-000bb1a49551)

  - As a list of columns: `penguins[['bill_length_mm', 'bill_depth_mm']].agg(['mean', 'median', 'std'])`
 
    ![image](https://github.com/user-attachments/assets/f79de28b-c004-4085-b1fb-391be8284e4f)

  - Using a dictionary:
 
  ![image](https://github.com/user-attachments/assets/8b1e5e11-780e-45ee-b9d9-228a1e3e1a3e)

  - Using a tuple (you can name the result row index):
 
    ![image](https://github.com/user-attachments/assets/5fe4b338-f60a-42d8-833a-ccaee02dfb3e)


## **Aggregation 🌎**

### 4. Which continent has the lowest average fertility rate overall?

![image](https://github.com/user-attachments/assets/26a32ef2-b77b-4793-a531-2a8c98a039a0)



### 5. What was the average life expectancy in Europe in 2015? Hint: first filter for 2015 then apply groupby.

![image](https://github.com/user-attachments/assets/76c47531-f727-47c3-8db0-bfb6c7ced5c3)



### 8. What is the highest population a continent ever had? Hint: group by multiple columns

![image](https://github.com/user-attachments/assets/39a49e0f-3a1a-4e41-af1c-d6f091d42925)


### 9. Which continent had that population and in which year?

![image](https://github.com/user-attachments/assets/c6acded3-4e9d-43df-b6ca-14e63c04bfed)



__
![lisa gif](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzB3bm5vdjk5ZWExemJ1bmM4Y2Vudzg5bWEwdnlweWI4eGVjbDY1eiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3o6MbrACMlFCny8zmw/giphy.gif)

![lisa gi2](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzB3bm5vdjk5ZWExemJ1bmM4Y2Vudzg5bWEwdnlweWI4eGVjbDY1eiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/l2JdSDAAwdtVa4bzW/giphy.gif)



