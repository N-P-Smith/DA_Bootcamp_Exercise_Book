# Day 6, 02.10.2024
Protocol writer: Suthatta J-C

---
## __Introduction__
After our long day, we practised and improved our skills in Python dictionaries and for-loops, while also reviewing the location of the lecture materials repository.

## __Schedule__ 
|Time|Notes|
|---|---|
|09:00 - 09:30|Recap Protocol|
|09:30 - 09:50|Review the work repository|
|09:50 - 10:50|Review Python Function/Method; Create Python Dictionaries| 
|11:00 - 12:30|Updating a dictionary, Merging  dictionaries, Nested Dictionaries|   
|13:30 - 15:00|For-loop| 
|15:00 - 18:00|Practise Python Dictionaries and For-loop exercise| 


---

## __Notes Day 6__ 
## __Recap__ 
**Python Function**
* abs() = return the absolute value of a number
* type() = determine the data type
* print() = Outputs data to the console
* min() = Shows the smallest value
* max() = Shows the largest value 
* len() = Shows length of iterable
* input() = Takes input from the user #Result always "string"
* int() = Converts a value to an integer number 
* float() = Converts a value to a floating-point number

**Python Method Command**
* **Not in-place** (Methods that do not modify the original object)
    * .split() = Splits a string into a list
    * .lower() = Converts string to lowercase
    * .upper() = Converts string to uppercase
    * .title() = Title-cases each word in a string
    * etc.
 * **In-place** (Methods that modify the original object)
    * .remove() = Removes the first occurrence of a value #works with int
    * .replace() = Modify text
    * .pop() = Removes and returns an item at an index #works with int
    * etc.
  
**Bracket type**

list[…]

dict{…} 

tuple(..,..,..)

## __Python Dictionaries__ 
Dictionaries consist of key-value pairs. They are very versatile data structures and good for looking up things, or searching in general.

**Creation of Dictionaries**

To create a dictionary in Python, you can use the following syntax:
**a= {key:value,….}**
    
    # Dictionaries are not indexed. This means that you cannot access elements by their position (like you would with lists). 
   
    # You must use the key associated with each value to access its corresponding value.
Example:

<img width="345" alt="Screenshot 2567-10-02 at 10 40 03" src="https://github.com/user-attachments/assets/58898676-fb06-40bb-9cbf-236ede7a60cb">

**Accessing elements of a dictionary**

* To access elements in a Python dictionary, you can use keys.
**dictionary[key]**
        * To get the interable of each key, we need to do it seperately. 
   
    Example:

    <img width="509" alt="Screenshot 2567-10-03 at 14 31 03" src="https://github.com/user-attachments/assets/00cf213b-a2dc-4818-8a65-209d24d960f8">

* With the get() method you can assign an alternative value if the key was not found: **dictionary.get('key','sorry not found')**.

    Example:

    <img width="736" alt="Screenshot 2567-10-03 at 14 23 40" src="https://github.com/user-attachments/assets/7caae80e-2a4c-41ce-92fa-454bfc28a708">

**Updating a dictionary**

We can easily update the key and value by: **dictionary = [“key”] = iterable**
    
    # The key needs to be unique. Otherwise, the interable will be duplicated to the last. 

Example:

<img width="638" alt="Screenshot 2567-10-03 at 14 36 16" src="https://github.com/user-attachments/assets/80fd4cf4-9176-46f2-9a1f-d34a1a6c3bda">

**Dictionary Methods**

* List all keys: **dictionary.key()**

  Example:
  
  <img width="531" alt="Screenshot 2567-10-03 at 14 49 33" src="https://github.com/user-attachments/assets/2cf2d147-a6d3-4397-abb6-477032a042c3">

        * Create the key's list: **list(dictionary.keys())**

          Example:

          <img width="524" alt="Screenshot 2567-10-03 at 14 49 49" src="https://github.com/user-attachments/assets/b5f1f012-800c-4301-8cad-14b34b4abc15">

* List all values: **dictionary.values()**

  Example:
  
  <img width="529" alt="Screenshot 2567-10-03 at 14 53 30" src="https://github.com/user-attachments/assets/aa862d30-759d-49e3-8b8a-01cddce61472">

        * Create the value's list: **list(dictionary.values())**

          Example:
  
          <img width="528" alt="Screenshot 2567-10-03 at 14 54 02" src="https://github.com/user-attachments/assets/e4b240ea-0113-40cb-be41-c9ffa3b6edbc">

* Number of elements in a dictionary: **len(dictionary)**
  Example:
  
  <img width="317" alt="Screenshot 2567-10-03 at 14 57 34" src="https://github.com/user-attachments/assets/df94803a-6903-436b-9ea9-d5d7acaa0ade">

**Merging two dictionaries**

Key and interable of 2 dictionaries can be combined by syntax: **dict1.update(dict2)**

  Example:

  <img width="479" alt="Screenshot 2567-10-03 at 15 00 47" src="https://github.com/user-attachments/assets/f5804819-1819-423c-9ca5-ced6c8e5c67b">


**Nested Dictionaries**

Dictionaries are often used to store raw unprocessed data. For example, data you received from a web-scraper. The structure of unprocessed data can be complex and typically you need nested dictionaries to reflect the raw data correctly. 
    
    # The dictionary can be inside of the dic, list inside of dic etc.. 
   
Here is one example:

<img width="441" alt="Screenshot 2567-10-03 at 15 07 03" src="https://github.com/user-attachments/assets/517b7e93-9d9a-41bb-8b58-d698d421ae79">

---

## __For-Loop__ 
Shorter code to use the repeat function; in general valuable defined with (i,j,k) but can be anything **except function name

To write a for-loop you need two things: 
- **First** a sequence-like object (e.g. a list, a string, a dictionary or the output of a function producing sequences), also called a **iterable**. An **Iterable** is an object, which one can iterate over. 
- **Second**, a variable that takes different values as the loop iterates over the sequence.

### **Syntax**
1. start with **'for'**
3. give the variable name that *refers to the current value of your iterable object* 
4. write **'in'**
5. *name the iterable* object and finish with **':'**
6. Indented block: All indented commands after the colon are executed within a for loop.
7. End: The first unindented command is executed after the loop finishes.

Example:

<img width="245" alt="Screenshot 2567-10-03 at 15 28 37" src="https://github.com/user-attachments/assets/42de0033-9535-4418-995f-bbb4c16c1956">

* **Import time**
  To loop the data, we can also code the specific timing to show in print

  Example:

  <img width="474" alt="Screenshot 2567-10-03 at 15 25 14" src="https://github.com/user-attachments/assets/cebb4a00-b1d8-4445-99f7-81742805d6ad">

* **Print inside/outside For-loop**

  Example:

  <img width="499" alt="Screenshot 2567-10-03 at 15 30 19" src="https://github.com/user-attachments/assets/2e57e497-2f80-4895-806e-6fb5b7eaf618">

### **Things you can iterate over with for loops**
- strings (character by character)
- lists (element by element)
- dictionaries (over keys, values, or both keys and values)
- files (line by line)
- iterable functions (like `range`)

### **Loops executing**
* **Loops executing a given number of times**
With the range() function, you can set the number of iterations.

   Example:

   <img width="933" alt="Screenshot 2567-10-03 at 16 25 29" src="https://github.com/user-attachments/assets/090d4c79-3e23-4af4-95f1-0a8c440e2686">

* **Loops over a string**
With a string as the sequence, you obtain single characters in each iteration.

   Example:

   <img width="625" alt="Screenshot 2567-10-03 at 16 27 26" src="https://github.com/user-attachments/assets/2cfdaecb-b91c-429b-9dfa-a71308162dae">

* **Loops over a list**
A list iterates simply once through each element:

   Example:

   <img width="726" alt="Screenshot 2567-10-03 at 16 32 11" src="https://github.com/user-attachments/assets/cb986ca0-28eb-485f-872b-97cae089d658">

* **Loops to iterate over that number sequence**
There is a function, enumerate(), that will allow us to iterate through a list or string while at the same time keeping track of their index.

   Example:

   <img width="606" alt="Screenshot 2567-10-03 at 16 36 53" src="https://github.com/user-attachments/assets/904d1116-0327-4bb2-9662-d951f3f08fe4">

* **Loops over a dictionary**
With a dictionary, the for loop iterates over the keys.

   Example:

   <img width="352" alt="Screenshot 2567-10-03 at 16 38 27" src="https://github.com/user-attachments/assets/70f15aa7-1dbe-409f-97ab-a1f6c564e91d">

     * **Loops to get the key** : 

       **Syntax**: dictionary.key()
   
        Example:

          <img width="407" alt="Screenshot 2567-10-03 at 16 54 30" src="https://github.com/user-attachments/assets/2b6ef4a4-14e8-4e42-b224-2948e27f0ebc">

     * **Loops to get the key together with the value** :

        **Syntax**: x = key + ', ' + dictionary[key] 
                      print(x)

        Example:

        <img width="367" alt="Screenshot 2567-10-03 at 16 48 13" src="https://github.com/user-attachments/assets/f05c56d9-c1f5-4d93-a4c1-e8a30a8025ae">

     * **Loops to get the value** : 

       **Syntax**: dictionary.values()

        Example:

         <img width="331" alt="Screenshot 2567-10-03 at 16 52 38" src="https://github.com/user-attachments/assets/7ee9f961-18e2-4ace-844a-8a93ea879f3e">

                **Syntax**: print(dic[key])

        Example:
      
        <img width="452" alt="Screenshot 2567-10-03 at 16 39 54" src="https://github.com/user-attachments/assets/ff5603ac-f99a-4896-8f40-13b023b5aa79">
     
     * **Loops for the detail** : 

        View object that displays a list of a dictionary’s key-value pairs in tuples.

        Example:

        <img width="826" alt="Screenshot 2567-10-03 at 17 03 25" src="https://github.com/user-attachments/assets/27aa4eba-bd3b-47af-91ac-b3d8d20a7166">

* **Looping over two lists simultaneously**

the pythonic solution would be to use zip function:

Example :

<img width="754" alt="Screenshot 2567-10-03 at 17 10 53" src="https://github.com/user-attachments/assets/b990d9bc-65f3-4d9e-ab2a-ce78ee12d2d9">

* **Nested Loops**

To run the loop inside one another; loops within loops

Example :

<img width="476" alt="Screenshot 2567-10-03 at 17 13 51" src="https://github.com/user-attachments/assets/8e6be93b-fb81-498d-801c-adf6dadff249">

---

![giphy](https://github.com/user-attachments/assets/02721aa2-7854-48d3-bfc9-7a1b3478e57b)

