# numbers = [1,2,3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)

numbers = [1,2,3]
# new_list = [new_item for item in list]
new_list = [n+1 for n in numbers]
print(new_list)

name = "krish"
# new_list = [letter for letter in name]
letters_list = [letter for letter in name]
print(letters_list)

double = [n*2 for n in range(1,5)]
print(double)

#conditional list comprehension
#new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name.upper() for name in names if len(name) >= 5]
print(short_names)

#Example
with open("file1.txt") as file1:
    list1 = file1.readlines()
with open("file2.txt") as file2:
    list2 = file2.readlines()
result = [int(num) for num in list1 if num in list2]
print(result)