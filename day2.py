#!/usr/bin/env python
# coding: utf-8

# # Bootcamp Assignment Day2
# Anjali Kumari(2246810)

# # 1. Given a list of integers, remove all occurrences of a specific value using a list method. 

# In[1]:


def remove_all_occurrences(lst, value):
    # Use a list comprehension to filter out all occurrences of 'value'
    return [i for i in lst if i != value]

# Example usage:
lst = [1, 2, 3, 4, 3, 2, 3, 5]
value_to_remove = 3
updated_list = remove_all_occurrences(lst, value_to_remove)
print("Updated list:", updated_list)


# # 2. Concatenate a list of strings into a single string, with each element separated by a space, using a list method.
# 

# In[2]:


def concatenate_strings(string_list):
    # Use the join() method to concatenate strings with a space separator
    result = ' '.join(string_list)
    return result

# Example usage:
string_list = ["Hello", "world", "this", "is", "Python"]
result = concatenate_strings(string_list)
print("Concatenated string:", result)


# # 3. Reverse a list of integers using a built-in list method.

# In[3]:


def reverse_list(lst):
    # Using the built-in reverse method
    lst.reverse()
    return lst

# Example usage:
lst = [1, 2, 3, 4, 5]
reversed_list = reverse_list(lst)
print("Reversed list:", reversed_list)


# # 4.	Sort a list of numbers in descending order using a built-in list method.

# In[4]:


def sort_descending(lst):
    # Using the sort method with reverse=True for descending order
    lst.sort(reverse=True)
    return lst

# Example usage:
lst = [1, 4, 2, 8, 5, 7]
sorted_list = sort_descending(lst)
print("Sorted list in descending order:", sorted_list)


# # 5.	Given two lists, combine them into a single list and remove any duplicate elements using a list method.
#  

# In[5]:


def combine_and_remove_duplicates(lst1, lst2):
    combined_list = list(set(lst1 + lst2))
    return combined_list

# Example usage:
lst1 = [1, 2, 3, 4, 5]
lst2 = [3, 4, 5, 6, 7]
result = combine_and_remove_duplicates(lst1, lst2)
print("Combined list without duplicates:", result)


# # 6.	Convert a tuple of integers into a list and remove the first and last elements using a tuple method.  

# In[6]:


def convert_and_remove_elements(tpl):
    lst = list(tpl)
    
    updated_list = lst[1:-1]
    
    return updated_list

# Example usage:
tpl = (10, 20, 30, 40, 50)
result = convert_and_remove_elements(tpl)
print("List after removing first and last elements:", result)


# # 7.	Given a list of tuples, extract all the first elements of each tuple into a separate list using tuple unpacking.   

# In[7]:


def extract_first_elements(tuples_list):
    # Using tuple unpacking to extract the first elements of each tuple
    first_elements = [a for a, b in tuples_list]  # Assumes each tuple has at least two elements
    return first_elements

# Example usage:
tuples_list = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
result = extract_first_elements(tuples_list)
print("First elements:", result)


# # 8.	Combine two tuples into a single tuple.

# In[8]:


def combine_tuples(tuple1, tuple2):
    # Use the + operator to concatenate two tuples
    combined_tuple = tuple1 + tuple2
    return combined_tuple

# Example usage:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = combine_tuples(tuple1, tuple2)
print("Combined tuple:", result)


# # 9.	Find the maximum and minimum values in a tuple of numbers using tuple methods.

# In[9]:


def find_max_min(tpl):
    # Using max() and min() to find the maximum and minimum values
    max_value = max(tpl)
    min_value = min(tpl)
    return max_value, min_value

# Example usage:
tpl = (10, 20, 30, 5, 50, 1)
max_val, min_val = find_max_min(tpl)
print("Maximum value:", max_val)
print("Minimum value:", min_val)


# # 10.	Convert a tuple of strings into a single string, with each element separated by a comma, using tuple methods.

# In[11]:


def convert_tuple_to_string(string_tuple):
    # Use the join() method to concatenate strings with a comma separator
    result = ', '.join(string_tuple)
    return result

# Example usage:
string_tuple = ("apple", "banana", "cherry", "date")
result = convert_tuple_to_string(string_tuple)
print("Concatenated string:", result)


# # 11.	Given two sets, return the union of the two sets using a set operation.

# In[12]:


def union_of_sets(set1, set2):
    # Using the union() method to get the union of two sets
    return set1.union(set2)

# Example usage:
set1 = {1, 2, 3}
set2 = {3, 4, 5}
result = union_of_sets(set1, set2)
print("Union of sets:", result)


# # 12.	Find the intersection of two sets using a set method.

# In[13]:


def intersection_of_sets(set1, set2):
    # Using the intersection() method to find the intersection of two sets
    return set1.intersection(set2)

# Example usage:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
result = intersection_of_sets(set1, set2)
print("Intersection of sets:", result)


# # 13.	Remove all elements from one set that are also present in another set using a set method.

# In[14]:


def remove_elements(set1, set2):
    # Using the difference_update() method to remove elements from set1 that are in set2
    set1.difference_update(set2)
    return set1

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6}
result = remove_elements(set1, set2)
print("Updated set1 after removal:", result)


# # 14.	Find the difference between two sets using a set method.

# In[15]:


def difference_of_sets(set1, set2):
    # Using the difference() method to find the difference between two sets
    return set1.difference(set2)

# Example usage:
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 6}
result = difference_of_sets(set1, set2)
print("Difference of sets:", result)


# # 15.Convert a list of integers into a set and then back to a list to remove duplicates, using set operations.

# In[16]:


def list_to_set_to_list(int_list):
    # Convert the list to a set to remove duplicates
    unique_set = set(int_list)
    
    # Convert the set back to a list
    unique_list = list(unique_set)
    
    return unique_list

# Example usage:
int_list = [1, 2, 3, 2, 4, 5, 1, 6, 4]
result = list_to_set_to_list(int_list)
print("List after removing duplicates:", result)


# # 16.Merge two dictionaries into a single dictionary using a dictionary method

# In[17]:


def merge_dicts(dict1, dict2):
    # Use the update() method to merge dict2 into dict1
    dict1.update(dict2)
    return dict1

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary using update():", merged_dict)


# In[18]:


def merge_dicts(dict1, dict2):
    # Use the unpacking operator to create a new merged dictionary
    merged_dict = {**dict1, **dict2}
    return merged_dict

# Example usage:
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged_dict = merge_dicts(dict1, dict2)
print("Merged dictionary using unpacking:", merged_dict)


# # 17.Extract all values from a dictionary into a list using a dictionary method.

# In[19]:


def extract_values_to_list(input_dict):
    # Use the values() method to get all values and convert to a list
    values_list = list(input_dict.values())
    return values_list

# Example usage:
sample_dict = {'a': 1, 'b': 2, 'c': 3}
result = extract_values_to_list(sample_dict)
print("List of values:", result)


# In[ ]:




