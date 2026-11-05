"""Code to find maximum of three number:"""
"""def maximum_of_number(a,b,c):
  if a > b and a > c:
    print(f"{a} is the greatest")
  elif b > a and b > c:
    print(f"{b} is the greatest")
  else:print(f"{c} is the greatest")
       

maximum_of_number(10,20,30)"""

"""Sum of all numbers"""
"""def sum_of_all_numbers(*args):
    sum_of_numbers=0
    for i in args:
        sum_of_numbers=i+sum_of_numbers
    print(f"sum of all numbers is {sum_of_numbers}")

sum_of_all_numbers(2,4,8,10)"""

"""Reverse a string"""
"""def ref_string(a):
    reversed_string=""
    for i in a:
     reversed_string=i+reversed_string 
    print(reversed_string)

        

ref_string("Surya")"""

"""Factorial of a number"""

"""def find_factorial(a):
    num1=int(a)
    fact_num=1
    for i in range(1,a+1):
        fact_num=fact_num*i
    print(f"factorial of number is {fact_num}")

find_factorial(5)"""

"""Check if its upper case"""

"""def char_upper(a):
    is_upper=0
    is_lower=0
    for i in a:
        if i.isupper():
          is_upper=is_upper+1
        else:
          is_lower=is_lower+1
    print(f"{is_upper} is count of upper case words")
    print(f"{is_lower} is count of lower case words")
char_upper("Sur@ya")"""



"""test_list=[1,2,3,3,5]
unique_list=list(set(test_list))
print(unique_list)"""

"""def unique_list(*args):
    con_list=list(set(list(args)))
    print(con_list)

unique_list(1,2,3,4,5,5,6,6,6,7,7,7,77)"""


"""Find even numbers from the given list"""
"""def even_numbers(*args):
    for i in args:
        if i%2==0:
            print(f"{i} in list is even number")
        else: print(f"{i} is the odd number")

even_numbers(1,2,3)"""


"""Check if a string is palindrome"""

"""def check_palindrome (a):
    input_string=str(a)
    reversed_string=""
    for i in a:
        reversed_string=i+reversed_string
    if reversed_string==input_string:
        print(f"{input_string} is a Palindrome")
    else :print(f"{input_string} is not a palindorme")

check_palindrome("tenet")""""


