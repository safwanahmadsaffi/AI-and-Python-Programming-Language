 # Table of Contents
1. [What is a Programming Language?](#what-is-a-programming-language)
2. [Why Python?](#why-python)
3. [Comments](#comment)
4. [Python Variables](#python-variables)
5. [Data Types](#data-types)
6. [Operators](#operators)
   - [Arithmetic Operators](#arithmetic-operators)
   - [Operator Precedence](#operator-precedence)
   - [Assignment Operators](#assignment-operators)
   - [Comparison Operators](#comparison-operators)
   - [Logical Operators](#logical-operators)
   - [Membership Operators](#membership-operators)
   - [Identity Operators](#identity-operators)
7. [Type Casting in Python](#type-casting-in-python)
8. [Python Strings](#python-strings)
   - [Multiline Strings](#multiline-strings)
   - [String Concatenation](#string-concatenation)
   - [Slicing](#slicing)
   - [String Methods](#string-methods)
9. [Lists](#list)
   - [Add List Items](#add-list-items)
   - [Remove List Items](#remove-list-items)
   - [Copy List](#copy-list)
   - [Nested List](#nested-list)
10. [Tuples](#tuple)
    - [Accessing Tuple Elements](#accessing-tuple-elements)
    - [Update Tuples](#update-tuples)
11. [Sets](#sets)
    - [Add Items in a Set](#add-items-in-a-set)
12. [Dictionaries](#dictionaries)
    - [Accessing Elements in Dictionary](#accessing-elements-in-dictionary)
    - [Dictionary Methods](#dictionary-methods)
13. [Conditions](#conditions)
14. [Loops](#loops)
15. [Functions](#functions)

# **What is a programming Language?**
A programming language is an artificial language that can be used to control the behaviour of a machine, particularly a computer. Programming languages, like human languages, are defined through the use of syntactic and semantic rules, to determine structure and meaning respectively.

- Versatile:
It is used in web development, data science and artificial intelligence and automation etc.
- Pyhton is equipped of libraies like pandas numpy and framework ....

# Why Python?
*   Free and open source
*   Easy to learn
*   Portable
*   A lot of applications including web developing, app developing and data science
*   Can be treated in a procedural way, object oriented way and fuctional way

# **Comment**
Comments can be used to explain Python code.

Comments can be used to make the code more readable.

Comments can be used to prevent execution when testing code.


### 2 types of comments in Python:


*   Single line comment #
*   Multi-line comment '''  '''

## **Python Variables**
Variables are containers for storing data values.

Python has no command for declaring a variable. There is no need to write the data type of a variable before it.

A variable is created the moment you first assign a value to it.
## **Data Types**
Following are some built-in data types in Python:


*   Text Type:  `str`  -->   " "
*   Numeric Types:  `int`, `float`  -->  123, 12.97683
*   Sequence Types: `list`, `tuple`  -->  [1,3,4,5] , (1,8,6,4)
*   Mapping Type: `dict`  -->  {}
*   Set Type: `set` -->  {[ ]}
*   Boolean Type: `bool`  -->  TRUE and FALSE

## **Operators**

Operators are used to perform operations on variables and values.
Python divides the operators in the following groups:
*   Arithmetic operators

*   Assignment operators

*   Comparison operators

*   Logical operators

*   Membership operators

### **Arithmetic Operators**

* Addition +
* Subtraction -
* Multiplicatin *
* Division /
* Modulus %
* Exponential **
* Floor Division //

### **Operator Precedence**


paranthesis

exponentiation

multiplication / division / f.d / modulus

addition, subtraction

### **Assignment Operators**

Assignment operators are used to assign values to variables

### **Comparison Operators**


These are used to compare two variables with each other.

">"  is greater than

"<"  is smaller than

">="  is greater than or equal to

"<="  is smaller than or equal to

"=="  is equal to

"!=" is not equal to

### **Logical Operators**

Python has three Boolean operators, or logical operators: and , or , and not.

Logical operators are used to combine conditional statements

  

`and` 	      Returns "True" if both statements are true
`or`	        Returns "True" if one of the statements is true
`not`	        Reverse the result, returns "False" if the result is true

### **Membership Operators**

Membership operators are used to test if a sequence is presented in an object

`in` Returns "True" if a sequence with the specified value is present in the object

`not in` Returns "True" if a sequence with the specified value is not present in the object

### **Identity Operators**

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

`is` Returns True if both variables are the same object

`is not` Returns True if both variables are not the same object


## **Type Casting in Python**
We can change the data type of a variable or a value.
- implicit typecasting
- explicit typecasting

## **Python Strings**

Strings in python are surrounded by either single quotation marks, or double quotation marks.

You can display a string literal with the `print()` function

### **Multiline Strings**


You can assign a multiline string to a variable by using three quotes or three single quotes:

The line breaks are inserted at the same position as in the code.


### **String Concatenation**
To concatenate, or combine, two strings you can use the "+" operator.

### **Strings are Arrays:**

Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters.

However, Python does not have a character data type, a single character is simply a string with a length of 1.

Square brackets can be used to access elements of the string.

### **Slicing**
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
There are three values separated by a colon(:) that can be used in slicing. And all of them are optional.

Syntax= string[start:end:step]

### **String Methods:**
Python has a set of built-in methods that you can use on strings.

**Upper Case**

The upper() method returns the string in upper case:

**Lower Case**

The lower() method returns the string in lower case:

**Capitalize**

The capitalize() method returns the string with first character capitalized:


**Sorted**

The sorted function is used to sort the string alphabatically.

**Join**

join() is used to join characters of a list in the form of string separated by the specified character.

**Count**

The count method is used to count the occurences of a specific character or substring in a string.

**endswith**

It checks whether a string ends with a specified character.

**startswith**

It checks whether a string starts with a specified character.

**endswith**

It checks whether a string ends with a specified character.

**find**

It checks at what position a specified character is present.


## **List**

Lists are used to store multiple items in a single variable.

List items are ordered, changable, allow duplicate values.

List items can be of any data type.
### **List Length**

Use `len()` function to determine how many items a list has.

### **Add List Items**

We can add items in the list using:


*   `append()` method
*   `insert()` method
*   `extend()` method

### **Remove List Items**

We can remove items from list using:

* `remove()` method

* `pop()` method

* `del` keyword

* `clear()` method

### **Copy List**

You cannot copy a list simply by typing `list2 = list1`, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method `copy()`.

Another way to make a copy is to use the built-in method `list()`.

### **Nested List:**
If there is a sublist within a list, it is known as nested list. We can access the elements of nested list by using its indexes.

## **Tuple**

Tuples are used to store multiple items in a single variable.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.

### **Accessing Tuple Elements**

Items in the tuples can be accessed by entering the index number inside square bracket.

The index can be a positive index, a negative index or a range of the indices.
### **Update Tuples**

Tuples are immutable. You can't add or remove items in it. However, there are some hacks to do that.


### **Multiply Tuples**

If you want to multiply the content of a tuple a given number of times, you can use the `*` operator.
### **Tuple Methods**

Python has two built-in methods for tuple.

* `count()` method

* `index()` method
## **Sets**

Like lists and tuples, sets are used to store multiple values of different data types in a single variable.

Set items are unordered, unindexed, unchangable and don't allow duplicate values.

(Set items are unmutable, we can still add and remove items).

Sets are written with curly brackets.
### **Length of a Set**

To determine how many items a set has, use the `len()` function.
### **Access Set Items**

You cannot access items in a set by referring to an index or a key.

But you can loop through the set items using a `for` loop, or ask if a specified value is present in a set, by using the `in` keyword.

### **Add items in a Set**

Once a set is created, you cannot change its items, but you can add new items.

To add an item to a set, use the `add()` method.

To add items from another set into the current set, use the `update()` method.
### **Some Set Methods**

* `intersection_update()`
* `intersection()`
* `symmetric_difference()`
* `difference()`

## **Dictionaries**

Dictionaries are used to store data values in key:value pairs.

Dictionary items are ordered, changable, and do not allow duplicates.

Dictionaries are written with curly brackets, and have keys and values.


### **Accessing Elements in dictionary:**

There is no concept of indexes in dictionary. It is an ordered object but we cannot access elements by using its number indexes. For accessing dictionary elements, we use keys. These keys map the values present against them in dictionary.
### **Duplicate Values in Dictionary:**
In case of dictionary values, duplicates are allowed. But duplication of keys is not allowed.

*  If we use same key two times in a dictionary, the value against that key gets updated and the former value get discarded. And the dictionary will contain only one key of that name.

*  Key is a unique identifier that is used to map a specific value present against it in the dictionary. It cannot be duplicated. You cannot use  same key to map two different values.



### **Memebership Operators:**
In dictionary, we can use membership operators to know whether a key present in a dictionary or not.
It cannot be used to check values in dictionary.
### **Dictionary Methods:**


* **clear()**
It is used to clear data from a dictionary.
*  **keys()**
It is used to get a list of all the keys present in a dictionary.
*   **values()**
It is used to get a list of all the values present in a dictionary.
*   **item()**
It is used to get all the elements of a dictionary.
*   **get()**
It is used to get specified keys' value from a dictionary.




### **Removing Elements from Dictionary:**
To remove elements from a dictionary, following methods are used:
* **pop()**
It is used to remove specified element from a dictionary.
*  **popitem()**
It is used to remove last element from a dictionary. It takes no argument.
## **Conditions:**

Conditions are used in program when we want to execute a specific portion of that on the basis of the incoming input.

The statement next to a condition will only excecute if it's true otherwise it'll be ignored by the interpretor.

**Keywords:**

if

elif

else
## **Loops:**

If we want to perform few steps of a program repeatedly, we will use loops instead of writing these lines each time.

Loops make the program more efficient.

In python, no braces are used to separate a block of statemments from the whole program. On the other hand, proper indentations are used for this purpose.

Two types of loops are used in python.


*   For loop
*   while loop

## **Functions:**

Functions allow us to create blocks of code that can be easily executed many times without needing to constantly rewrite the entire block of code.



### **Built-in Functions:**

There are a lot of built-in functions in python that make programming more easier and efficient.


    '''
    Prepared by Safwan
    '''
