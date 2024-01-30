# 0x07-python-test_driven_development
- In this project, I learnt and practiced;

- In this project I learnt and practiced;
- What’s an interactive test
- Why tests are important
- How to write Docstrings to create tests
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases

- Task files description:

## 0-add_integer.py: Python function that returns the integer addition of two numbers.

- If either of a or b is not an int or float, a TypeError is raised with the message a must be an integer or b must be an integer.

- If either of a or b is a float, it is casted to an int before addition.

## 2-matrix_divided.py: Python function that divides all elements of a matrix by a common divisor.

- Returns a new matrix representing the division of all elements of matrix by div.

- Quotients are rounded to two decimal places.

- If matrix is not a list of lists of ints or floats, a TypeError is raised with the message matrix must be a matrix (list of lists) of   integers/floats.

- If matrix contains rows of different lengths, a TypeError is raised with the message Each row of the matrix must have the same size.

- If the divisor div is not an int or float, a TypeError is raised with the message div must be a number.

- If div is 0, a ZeroDivisionError is raised with the message division by zero.

## 3-say_my_name.py: Python function that prints a name in the format My name is <first_name> <last_name>.

- If either of first_name or last_name is not a str, a TypeError is raised with the message first_name must be a string or last_name must be a   string.

## 4-print_square.py: Python function that prints a square using the # character.

- The paramter size represents the height/width of the square.

- If size is not an int, a TypeError is raised with the message, size must be an integer.

- If size is less than 0, a ValueError is raised with the message size   must be >= 0.

## 5-text_indentation.py: Python function that prints text with indentation.

- Two new lines are printed after any ., ?, or : character.

- If text is not a str, a TypeError is raised with the message text   must be a string.

- No spaces are printed at the beginning or end of each printed line.

tests/
## 6-max_integer_test.py: Python class/script that runs unittests for the function def max_integer(list=[]): (provided by Holberton School).

## 100-matrix_mul.py: Python function that multiplies two matrices.

- Returns a new matrix representing the multiplication of m_a by m_b.

- If either of m_a or m_b is empty (ie. == [] or == [[]]), a ValueError is raised with the message m_a can't be empty or m_b can't   be empty.

- If either of m_a or m_b is not a list, a TypeError is raised with the message m_a must be a list or m_b must be a list.

- If either of m_a or m_b is not a list of lists, a TypeError is raised with the message m_a must be a list of lists or m_b must be a list of lists.

- If either of m_a or m_b is not a list of lists of ints or floats, a TypeError is raised with the message m_a should contain only integers or   floats or m_b should contain only integers or floats.

- If either of m_a or m_b contains rows of different lengths, a TypeError is raised with the message each row of m_a must should be of the same size or each row of m_b must should be of the same size.

- If m_a and m_b cannot be multiplied (ie. row size of m_a does not match column size of m_b), a ValueError is raised with the message m_a and m_b   can't be multiplied.

## 101-lazy_matrix_mul.py: Python function that multiplies two matrices using the module NumPy.

- Identical in function to 100-matrix_mul.py.

## 102-python.c: C function that prints basic information about Python string objects.

- Test files:
- This tests files developed to test the programs as well as test the actual concept of test driven developments.

- 0-add_integer.txt
- 2-matrix_divided.txt
- 3-say_my_name.txt
- 4-print_square.txt
- 5-text_indentation.txt
- 6-max_integer_test.py
- 100-matrix_mul.txt
- 101-lazy_matrix_mul.txt
