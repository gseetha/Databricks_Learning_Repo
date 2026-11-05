"""Dict excercies"""

"""student = {"name": "Alice", "age": 20, "grade": "B"}
student["City"]="NewYork"
#student["name"]="Surya"
#student["age"]=25
#student["grade"]='C'
print(student)"""

"""Delete key in Dictinory"""

"""car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
car.pop("color")
car["color"]="Yellow"
print(car.items())
print("key check","house" in car)"""

"""merge the list to form a dictionary"""

"""keys = ["name", "age", "city"] 
values = ["Bob", 25, "London"]
final_list=dict(zip(keys,values))
print(final_list["name"])
final_list.clear()
print(final_list)"""

"""dict merged"""
"""dict1 = {"a": 1, "b": 2} 
dict2 = {"b": 3, "c": 4}
merged={}

for i in (dict1,dict2):
  for key,values in i.items():
    print(f"key and value pairs",key,values)"""

"""access nested dictionary"""

"""person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
print(person.get("address").get("street"))
print(person["address"]["street"])
"""

"""Initiate dictionary"""
"""keys = ["math", "science", "english", "history"]
default=0
merged={}

for i in keys:
    merged[i]=default
print(merged)
"""
"""list_test=[10,20,30,40]
list_test_1="School"
print(list_test_1[5])
print(list_test[4])
"""

numbers = (10, 20, 30, 40, 50, 60, 70)









