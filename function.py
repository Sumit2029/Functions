# -*- coding: utf-8 -*-
"""Function.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cToN0X-WwgxsmuRPQSLovOy-pLZAzuC1
"""



""" 1. What is the difference between a function and a method in Python?
  ->A function is a block of code that can be called multiple times from different parts of a program, while method is a function that belongs to object.
 2. Explain the concept of function arguments and parameters in Python
  -> Function arguments are the values passed to a function when its called,while parameters are the variables defined in the function definition that receive the arguments values.
 3. What are the different ways to define and call a function in Python?
  -> Functions can be defined using the 'def' keyword and called using the function name followed by paranthese containing any required arguments.
 4.  What is the purpose of the `return` statement in a Python function?
  -> The 'return' statement is used to exit a function and return a value to the caller.
 5. What are iterators in Python and how do they differ from iterables?
  ->Iterables are objects that can be iterated over, such as lists or tuples, while iterators are objects that keep track of the current position in an iterable
6. Explain the concept of generators in Python and how they are defined.  
 ->Generators are functions that use the yield keyword to produce a series of values, rather than computing them all at once and returning them in a list.
7.  What are the advantages of using generators over regular functions?
 ->Generators use less memory and can be more efficient than regular functions for large datasets.
8. What is a lambda function in Python and when is it typically used?
 ->Lambda functions are small anonymous functions that can be defined inline within a larger expression.
9. xplain the purpose and usage of the `map()` function in Python.
 ->The map() function applies a given function to each item of an iterable (such as a list or tuple) and returns a list of the results.
10.  What is the difference between `map()`, `reduce()`, and `filter()` functions in Python?
->map() applies a function to each item of an iterable, reduce() applies a function to the items of an iterable, going from left to right, so as to reduce the iterable to a single output, and filter() constructs an iterator from elements of an iterable for which a function returns True
11. . Using pen & Paper write the internal mechanism for sum operation using  reduce function on this given
list:[47,11,42,13];
 ->https://ibb.co/XsNvC0W


"""

#1 Write a Python function that takes a list of numbers as input and returns the sum of all even numbers in list
def sum_even_numbers(numbers):
  return sum(num for num in numbers if num % 2 == 0)
  numbers = [1,2,3,5,6]
  print(sum_even_numbers(numbers))

#2 Create a Python function that accepts a string and returns the reverse of that string.
def reverse_string(string):
  return string[::-1]
  string = "hello world"
  print(reverse_string(string))

#3Implement a Python function that takes a list of integers and returns a new list containing the squares of each numbers
def square(numbers):
  return[num**2 for num in numbers]
  numbers =[1,2,3,4,5]
  print(square(numbers))



#4 Write a Python function that checks if a given number is prime or not from 1 to 200.
def is_prime(n):
  if n<2:
    return False
    for i in range(2, int(n**0.5)+1):
      if n% i== 0:
        return True
        for i in range (1,201):
          if is_prime(i):
            print(i)

from typing_extensions import Self
#5 Create an iterator class in Python that generates the Fibonacci sequence up to a specified number of terms
class FibonacciIterator:
  def __init__(self,n) :
    self.n = n
    self.a, self.b = 0, 1
    self.count =0
  def __iter__(self) :
    return self
  def __next__(self):
    if self.count >= self.n:
      raise StopIteration
    result = self.a
    self.a, self.b = self.b, self.a + self.b
    self.count += 1
    return result
fib_iter = FibonacciIterator(10)
for num in fib_iter:
  print(num)

#6 Write a generator function in Python that yields the powers of 2 up to a given exponent.
def power_of_2(exponent):
  for i in range(exponent + 1):
    yield 2** i
    powers = powers_of_2(5)
    for power in powers:
      print(power)

#7 Implement a generator function that reads a file line by line and yields each line as a string.
def read_file_lines(filename):
  with open(filename, 'r') as file:
    for line in file:
      yield line.strip()
      lines=read_file_lines('example.txt')
      for line in lines:
        print(line)

#8 Use a lambda function in Python to sort a list of tuples based on the second element of each tuple.
students = [('Rishav',20),('Sumit',19),('Suhana',21)]
students.sort(key=lambda x:x[1])
print(students)

#9 Write a Python program that uses `map()` to convert a list of temperatures from Celsius to Fahrenheit.
temperatures =[0,10,20,30,40]
Fahrenheit =list(map(lambda x:(x* 9/5)+ 32, temperatures))
print(Fahrenheit)

#10 Create a Python program that uses `filter()` to remove all the vowels from a given string.
vowels = 'aeiouAEIOU'
s= "Hello, World"
result = ''.join(filter(lambda x: x not in vowels, s))
print(result)

