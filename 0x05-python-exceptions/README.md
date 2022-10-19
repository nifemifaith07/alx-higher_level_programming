# [0x05-python-exceptions](https://github.com/nifemifaith07/alx-higher_level_programming/tree/main/0x05-python-exceptions)
**PYTHON**
## RESOURCES
- [Errors and Exceptions](https://alx-intranet.hbtn.io/rltoken/Yj7sDOzmKwICSHr7WEAW3A)
- [Learn to Program 11 Static & Exception Handling](https://alx-intranet.hbtn.io/rltoken/xASzXarhF1sBhzYkJ14LvQ)(*starting at minute 7*)
## LEARNING OBJECTIVES
- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception
## REQUIREMENTS
- Allowed editors: vi, vim, emacs
- All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- code should use the pycodestyle (version 2.8.*)
- All files must be executable
- The length of files will be tested using wc
## TASKS
### 0. Safe list printing
**Write a function that prints x elements of a list.**
- Prototype: def safe_print_list(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All elements must be printed on the same line followed by a new line.
- x represents the number of elements to print
- x can be bigger than the length of my_list
- Returns the real number of elements printed
- You have to use try: / except:
- You are not allowed to import any module
- You are not allowed to use len()
### 1. Safe printing of an integers list
**Write a function that prints an integer with "{:d}".format().**
- Prototype: def safe_print_list_integers(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- x represents the number of elements to access in my_list
- x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed
- You have to use try: / except:
- You have to use "{:d}".format() to print an integer
- You are not allowed to import any module
- You are not allowed to use len()
### 2. Print and count integers
**Write a function that prints the first x elements of a list and only integers.**
- Prototype: def safe_print_list_integers(my_list=[], x=0):
- my_list can contain any type (integer, string, etc.)
- All integers have to be printed on the same line followed by a new line - other type of value in the list must be skipped (in silence).
- x represents the number of elements to access in my_list
- x can be bigger than the length of my_list - if it’s the case, an exception is expected to occur
- Returns the real number of integers printed
- You have to use try: / except:
- You have to use "{:d}".format() to print an integer
- You are not allowed to import any module
- You are not allowed to use len()
### 3. Integers division with debug
**Write a function that divides 2 integers and prints the result.**
- Prototype: def safe_print_division(a, b):
- You can assume that a and b are integers
- The result of the division should print on the finally: section preceded by Inside result:
- Returns the value of the division, otherwise: None
- You have to use try: / except: / finally:
- You have to use "{}".format() to print the result
- You are not allowed to import any module
