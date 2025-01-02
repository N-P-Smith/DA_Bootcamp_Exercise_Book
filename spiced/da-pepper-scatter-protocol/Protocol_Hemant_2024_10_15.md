# Day 14, 15.10.2024
Protocol writer: Hemant Gulati
---
## __Introduction__
In this session, we learned about seaborn which is a Python visualization library that has transformed the landscape of statistical graphics. In addition, we also learned about merging or combining dataframes which is a critical aspect of data manipulation and analysis in Pandas. 
## __Schedule__
|Time|Notes|
|---|---|
|09:20 - 10:00|Protocol|
|10:00 - 10:20|Self Introduction|
|10:20 - 12:15|Seaborn|
|12:15 - 13:15|Lunch Break|
|13:15 - 14:00|Seaborn's Exercise|
|14:00 - 15:00|Merging Dataframes|
|15:00 - 16:00|Exercise|
|16:00 - 17:00|Exercise|
---
# Part 1 Seaborn
## What is a Seaborn?
Seaborn is a powerful visualization tool in Python that focuses on statistical plotting. It integrates closely with Pandas DataFrames, making it an indispensable tool for comprehensive data analysis. With Seaborn, creating complex plots becomes an effortless task, thanks to its user-friendly interface and the ability to generate visually appealing charts with minimal code.
* **pip install seaborn**
* **import seaborn as sns**
## Plotting distributions
## 1. Histogram
A histogram is a type of bar chart that represents the distribution of numerical data by dividing the data into intervals (also known as bins or buckets) and counting the number of data points that fall into each interval. The intervals are typically specified as consecutive, non-overlapping ranges of values, and the bins are usually of equal size. The vertical axis of a histogram represents the count or frequency of data points within each bin, while the horizontal axis represents the variable being measured. Histograms are widely used in statistics and data analysis:
* To visually summarize the distribution of a dataset.
* To understand its central tendency, skewness, and the presence of outliers or unusual observations.
* They provide a quick way to get a sense of the shape of the data distribution, such as whether it is normal (bell-shaped), bimodal (two peaks), skewed (leaning to one side), or uniform (evenly spread).
## 2. Box plots
A box plot displays the distribution of data based on five summary statistics: minimum, first quartile (Q1), median, third quartile (Q3), and maximum. It provides insights into the central tendency and spread of the data, as well as any potential outliers.
## 3. Catplot
Catplot is used for drawing plots for categorical variables.The advantages of a catplot:
* It has the access to all of seaborn categorical plots.
* It is built on top of the FacetGrid, which means it is specifically designed to handle multiple subplots (or facets) and visualize data across different categories or groups in the dataset. 
A FacetGrid is a multi-axes grid with subplots visualizing the distribution of variables of a dataset and the relationship between multiple variables.
Multi-plot grid for plotting conditional relationships.
* catplot options are: “strip”, “swarm”, “box”, “violin”, “boxen”, “point”, “bar”, or “count”.
## 4. Bar plot
It plots numeric values for levels of a categorical feature as bars. Each bar represents one categorical value, and the length of each bar corresponds to the bar’s value.
## 5. Scatter plots
A scatterplot is a type of plot that visually represents the relationship between two numerical variables. In a scatterplot, each data point is represented by a dot, where:
* The x-axis shows the value of one variable.
* The y-axis shows the value of another variable.
# Part 2 Merging dataframes
## Objectives of Merging DataFrames
Merging or combining DataFrames is a critical aspect of data manipulation and analysis in pandas. This process allows for the integration of related data from multiple sources into a single, cohesive dataset. Understanding the objectives and applications of different merging techniques is essential for effective data analysis. Below are the key objectives associated with merging DataFrames:
## 1. Concatenation
* **Objective**: To append one DataFrame to another along a particular axis (either rows or columns).
* **Usage**: This is particularly useful when you have data in similar structures that you want to compile into a single dataset. Concatenation is straightforward and does not require overlapping data between the DataFrames.
* **Functionality:** Concatenation is performed along a specified axis, with the option to apply set logic on the other axes. This allows for the vertical or horizontal merging of DataFrames, depending on the data organization and the desired outcome.
### Specifying the Axis
* **Vertical Concatenation (axis=0):** When concatenating vertically, DataFrames are stacked on top of each other. This is the default behavior and is typically used when the DataFrames have the same columns but additional rows of data that you want to append.
* **Horizontal Concatenation (axis=1):** In contrast, horizontal concatenation aligns DataFrames side by side, adding columns. This method is chosen when the DataFrames share the same rows (observations) but contain different sets of features or variables.
### Combining Multiple DataFrames
* Concatenation is not limited to two DataFrames; you can combine several DataFrames at once, provided they align correctly according to the specified axis.
### Key Parameters
* **axis:** Determines the direction of the concatenation. axis=0 for vertical and axis=1 for horizontal merging.
* **ignore_index:** When set to True, this parameter ignores the existing index labels and creates a new range of integer indices. This is particularly useful if the index does not carry meaningful information for the concatenated DataFrame or if you want to avoid duplicate indices.
* **sort:** This parameter controls whether to sort the columns if concatenating along axis=0 (vertically) when the DataFrames have non-aligned columns. Sorting can help in identifying similar columns and aligning the data appropriately.
### Practical Use Cases
* **When axis=0:** This axis choice is most suitable for scenarios where DataFrames share the same columns but represent additional data points, such as new records or observations that should be appended below the existing ones.
* **When axis=1:** Choosing axis=1 is appropriate for cases where the DataFrames hold different variables or features for the same observations. This expands the data's feature space horizontally by adding new columns.
Concatenating DataFrames along a specific axis, with careful consideration of parameters like axis, ignore_index, and sort, allows for flexible data manipulation. Whether integrating additional observations or expanding the dataset with new variables, concatenation is a powerful tool in the pandas library for structuring and analyzing data.
## 2. Inner join
* **Objective:** To combine two DataFrames based on common keys, retaining only the rows that have matching values in both original datasets.
* **Usage:** This method is ideal for situations where you wish to merge data that shares a common identifier and you're only interested in observations present in both DataFrames. It ensures that the resulting DataFrame contains only the intersecting set of entries.
* **How It Works:** The inner join operation aligns rows from two DataFrames based on common values in one or more shared columns. This approach is akin to an SQL inner join, where the resulting set comprises only those rows that have matching values in the join columns of both DataFrames.
### Common Column Requirement
* Key Columns: A prerequisite for an inner join is the presence of at least one column common to both DataFrames. This column, often referred to as the "join key," is crucial for the merge operation. The values within this key column are used to identify matching rows across the DataFrames.
### Characteristics of Inner Join
#### Selective Inclusion
* **Matching Rows Only:** The essence of an inner join is its selectivity—only rows with matching keys in both DataFrames are included in the final result. Any row without a counterpart in the other DataFrame, based on the join column, is omitted. This ensures that the merged data is relevant and fully matched.
#### Result Composition
* **Columns and Rows:** The resulting DataFrame from an inner join encompasses all columns from the original DataFrames. However, it selectively includes only those rows where the keys are present in both sources. This criterion guarantees that the information in the merged DataFrame is comprehensive and pertinent, reflecting a complete overlay of the data based on the specified keys.
The inner join stands out for its ability to ensure data integrity and relevance by focusing on commonalities between DataFrames. This method is indispensable for data analysts and scientists looking to consolidate and examine interconnected datasets thoroughly.
## 3. Right join
* **Objective:** To merge two DataFrames using all keys from the right DataFrame and matching keys from the left DataFrame. If there is no match, the left side will contain null.
* **Usage:** This is useful when you want to ensure that all records from the right DataFrame are retained in the merge, filling in missing matches from the left DataFrame with NaNs. It is particularly helpful in cases where the right DataFrame holds a reference or a complete set of observations.
### Characteristics of Right Join
#### Inclusive of Right DataFrame
* **Complete Inclusion:** The defining aspect of a right join is that all rows from the right DataFrame are retained in the merged result. This ensures no data from the right DataFrame is lost, regardless of whether matching rows exist in the left DataFrame.
#### Handling Missing Matches
* **Filling with Nulls:** When rows in the right DataFrame do not find a corresponding match in the left DataFrame, the resulting DataFrame will still include these rows. However, the columns from the left DataFrame that lack matching entries will be filled with null values (typically NaN in pandas). This approach maintains the integrity of the right DataFrame's data while clearly indicating where matches are not found.
A right join is invaluable for scenarios where preserving the entirety of the right DataFrame is crucial, even when exact matches are not found in the left DataFrame. It provides a comprehensive way to merge datasets, ensuring that all data from the right side is considered during analysis.
## 4. Left Join
* **Objective:** Similar to the right join, but in this case, all keys from the left DataFrame are retained, and matching keys from the right DataFrame are used to merge the data. Where there's no match, the right side will contain null.
* **Usage:** This approach is suitable when the left DataFrame contains a set of records you wish to preserve in the merge, filling in missing data from the right DataFrame where matches are found.
**Note - Using indicator=True to check how the dataframes were merged and if it corresponds to your expectations**
## 5. Outer/Full Join
* **Objective:** To merge two DataFrames using the union of keys from both DataFrames. This method ensures that all records from both DataFrames are included in the resulting dataset, filling in missing matches with NaNs.
* **Usage:** The outer join is ideal when you want a comprehensive merge that retains all entries from both DataFrames, providing a complete picture of the available data, even if it means including rows with missing data.
* **Mechanism:** The outer join operation merges rows from two DataFrames based on common values in one or more shared columns. Its defining feature is the inclusion of all rows from both the left and right DataFrames, making it the most inclusive type of join.
### Characteristics of Outer Join
#### Inclusion of All Rows
* **Comprehensive Merging:** Unlike inner, left, or right joins that may exclude some rows based on the presence or absence of matching data, an outer join ensures the inclusion of all rows from both DataFrames. This approach guarantees that no data is left behind, providing a complete picture of the merged datasets.
#### Handling Missing Data
* **Null Value Filling:** When there are rows in one DataFrame that do not find corresponding matches in the other, these rows are still included in the resulting DataFrame. To address the lack of matching data, columns from the DataFrame without matching rows are filled with null values (NaN in pandas). This is true for both sides of the join, ensuring that the dataset remains comprehensive even when exact matches are not found
The outer join is an invaluable tool in data analysis, especially when working with datasets that require a full overview without losing any data due to non-matching keys. It allows analysts to combine disparate datasets into a single DataFrame, where the absence of matching information is clearly indicated through null values, facilitating further analysis or data cleaning.


