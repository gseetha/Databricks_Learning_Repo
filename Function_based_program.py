"""Function programming practice"""
"""def fact_number(a):
    result =1
    for i in range(1,a+1):
      result=result *(i)
    return (result)


a=int(input("Enter the number"))
print(f"Factorial of the number {a} is {fact_number(a)}")"""

"""Converting number to dictinoary"""
"""def dict_input(a):
   dict_output={}
   for i in range(1,a+1):
      dict_output[i]=i*i
   return dict_output

a=int(input("Enter the number"))
print(f"Creating dictionary using {a} by calling function {dict_input(a)}")"""

"""Accept input as comma seperated and convert to list and tuples"""
"""def data_convert(*args):
    list_input=list(args) 
    list_input=tuple(args)
    return list_input,list_input
    print(f"input has been converted to list {list_input}")
    print(f"input has been converted to list {tuple_input}")
    
data_convert(30,10)"""


"""Create 2 dimensional matrix"""
"""column_value=4
row_value=3
outer_list=[]
for i in range(1,row_value+1):
    inner_list=[]
    for j in range(1,column_value+1):
        inner_list.append(i*j)
    outer_list.append(inner_list)
print(f"{outer_list}")"""

"""COnverting comma seperated to list"""

"""input_value=input("Enter the string").split(',')
print(type(input_value))
input_value.sort()
print(input_value)"""


"""Remove duplicates """

"""input_string=input("Enter the string ").split(" ")
output_string= " ".join(sorted((set(input_string))))
print((output_string))"""


"""Divisible by 5"""
"""def div_by(*args):
    final_list=[]
    for i in args:
        if(i%5)==0:
            final_list.append(i)
    return final_list

input_num=input("Enter comma seperated numbers")
numbers=[int(i)for i in input_num.split(",")]
print (f"The numbers that are divisible by 5 is {div_by(*numbers)}")"""



from pathlib import Path
test_file =r"C:\Users\555782\OneDrive - TMNA\Desktop\py_de_ai_project\landing\cust.csv"
file_path=Path(test_file)
print(file_path)


            
 
    


      
    