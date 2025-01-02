# Day 11, 10.10.2024
Protocol writer: Tanzhu Dereli

---
## __Introduction__
In these Module parts we discussed different filtering methods in Pandas and many Methods , Functions and Attributes that can act on pandas objects.
We also manipulated Data Frames with these filtering techniques and tested the different attributes, methods and functions.

## __Schedule__ 
|Time|Notes|
|---|---|
|09:30 - 10:00|Previous Protocol Recap|
|10:00 - 11:00|Pandas Filtering|
|11:15 - 12:00|Pandas Filtering|
|12:00 - 12:30|Exercise|
|12:30 - 13:30|Lunch Break|   
|13:30 - 14:00|Methods, Functions, Attributes as exercise in groups|
|14:30 - 15:00|Methods, Functions, Attributes|
|15:00 - 18:00|Exercise| 


# __Part One: Filtering__ 
* Filtering is a fundamental operation in data analysis, which allows the extraction of subsets of data based on specific conditions or criteria.
Comparison Operators are used for basic DataFrame Filtering. Below is an overview of the primary comparison operators used in DataFrame filtering:


- **Equality**: `x == 100`

- **Greater Than and Less Than**: `x > 2`, `y < x` 

- **Not Equal**: `x != y`

- **Value Inclusion**: `x.isin([...])`

- **Value Range**: `x.between(a, b)`

- **Check for NA**: `x.isna()`



## __Filtering Techniques in Pandas__ 

* Pandas provides a variety of methods for filtering data within DataFrames.
These methods allow for the selection of data subsets based on specific conditions, enhancing the ability to perform detailed data analysis.

## 1. Filtering with Single Logical Operators

- **Example**: `df[df['column_name'] > value]`

## 2. Filtering with Multiple Logical Operators

- **Operators**: `&` (AND), `|` (OR), `~` (NOT)
- **Example**: `df[(df['column1'] > value1) & (df['column2'] < value2)]`

- **Alternative `query`Method**
`df.query('coulmn1 > value1 and column2 < value2')`

## 3. Filtering with the **isin** Method

- **Example**: `df[df['column_name'].isin([value1, value2, value3])]`

## 4. Filtering Using the `str` Accessor

- **Example**: `df[df['column_name'].str.contains('substring')]`

## 5. Filtering with the **between** Method

- **Example**: `df[df['column_name'].between(value1, value2)]`


# __Part Two: Methods, Functions and Attributes__

- **Methods**: These are actions you can perform on pandas objects (like DataFrames and Series). Methods are invoked using dot notation and can perform operations such as filtering, grouping, and transforming data.
  Examples include `.groupby()`, `.merge()`, and `.sort_values()`.

- **Functions**: In the context of pandas, functions are standalone procedures called by their name and can take one or more arguments, including pandas objects. Functions perform specific tasks on the data and return a result.
 Common pandas functions include `pd.read_csv()` for reading data into a DataFrame and `pd.to_datetime()` for converting a column to datetime format.

- **Attributes**: Attributes are properties of pandas objects that you can access to gain information about the data's structure or content without modifying the data itself. They are accessed using dot notation.
  For instance, `DataFrame.shape` returns the dimensions of the DataFrame, and `Series.dtype` gives the data type of the Series.

## 1.Key Pandas Functions

- DataFrame Creation (`pd.DataFrame(...)`):
- The `DataFrame` is a two-dimensional tabular data structure with labeled axes (rows and columns). Creating a `DataFrame` involves structuring your data into this format.

- **Series Creation (`pd.Series(...)`):** A `Series` is a one-dimensional array with labels. It can hold data of any type (integer, string, float, python objects, etc.).

- **Reading CSV Files (`pd.read_csv(file)`):** This function is used to read a table from a CSV file (Comma Separated Values) into a DataFrame. 

- **Finding Unique Values (`pd.unique(values)`):** `pd.unique` returns the unique values from a one-dimensional array-like object, helping identify distinct values within a dataset.

- **Combining Data (`pd.concat([df1, df2])`):** This function is used to concatenate pandas objects along a particular axis. `pd.concat` can be used to combine Series, DataFrame, or Panel objects.



## 2. Methods

In Python, methods are functions that are associated with objects and can access and modify the state of those objects. Unlike standalone functions, methods are invoked on specific instances of classes, allowing for object-oriented programming practices.
Methods are inherently tied to the objects on which they are called. This association means that a method is always attached to an object's class and is accessed through the object itself.


### Key Pandas Methods

| Command               | Description                                             |
|-----------------------|---------------------------------------------------------|
| `df.to_csv(file)`     | Write a table to disk.                                  |
| `df.sum()`            | Returns the sum of the values over the requested axis.  |
| `df.sort_values()`    | Sorts by the values along either axis.                  |
| `df.count()`          | Returns count of non-NA cells for each column or row.   |
| `df.nunique()`        | Returns the number of unique values in a Series or DataFrame. |
| `df['col'].str.len()` | Returns the length of each string in pandas Series.     |
| `df.head()`           | Display the contents of the dataframe.                  |
| `df.sample(4)`        | Display 4 random rows.                                  |
| `df['population'].sum()`|You can sum up all the values in a column              |
| `df['continent'].str.len()` | Or get the length of the strings inside a column  |




## 3. Attributes



Attributes in Python play a crucial role in representing the properties or characteristics of an object. They are fundamentally different from methods, focusing on providing information rather than performing actions.

## Nature of Attributes
Attributes are data values tied to a specific object. They encapsulate the properties or state of an object, offering insights into its characteristics without altering it.
For example in a pandas DataFrame, an attribute like `shape` indicates the DataFrame's dimensions, providing the number of rows and columns.

## Accessing Attributes

Attributes are accessed using dot notation but, importantly, without parentheses. This distinction from method calls is crucial because attributes are not functions and do not accept parameters.
Accessing an attribute looks like `object.attribute`, where `object` is your specific Python object (like a DataFrame) and `attribute` is the property you wish to retrieve.

## Example - DataFrame.`shape` Attribute

The `shape` attribute of a pandas DataFrame returns a tuple representing the DataFrame's size as `(rows, columns)`. It is a direct way to get the DataFrame's dimensions.
You can access this attribute as `df.shape` for a DataFrame named `df`. This provides a simple yet effective insight into how large the DataFrame is, facilitating further data processing or analysis decisions.


### Key Pandas Attributes
| Command           | Description                                                  |
|-------------------|--------------------------------------------------------------|
| df.shape          | returns tuple representing the dimensionality of the DataFrame |
| df.index          | returns the index as an array-like object                    |
| df.columns        | returns the column index as an array-like object             |
| df.dtypes         | returns the data types in the DataFrame                      |
| df.values         | returns the values of the DataFrame as an array-like object  |
| df.ndim           | returns an integer representing the number of axes            |







---

## __end: external links and websites__ 
* [The advanced template in this repo](https://github.com/neuefische/da-daily-protocol/blob/main/advanced_version.md) 
* [Markdown Cheatsheet on Github](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) 
* Another link
