#find first and last occurance of an element
my_list = [1, 2, 3, 4, 2, 5, 2, 6]
element_to_find = 2

first_occurrence = -1
last_occurrence = -1

try:
    first_occurrence = my_list.index(element_to_find)
except ValueError:
    pass

for i in range(len(my_list) - 1, -1, -1):
    if my_list[i] == element_to_find:
        last_occurrence = i
        break

print(f"List: {my_list}")
print(f"Element to find: {element_to_find}")

if first_occurrence != -1:
    print(f"First occurrence of {element_to_find} is at index: {first_occurrence}")
    print(f"Last occurrence of {element_to_find} is at index: {last_occurrence}")
else:
    print(f"{element_to_find} not found in the list.")
    
    
 #reverse a num
arr=[10,20,30,40,50]
arr.reverse()
print(arr)

#Find the second largest
second_largest=lis[0]
for j in lis:
  if j> second_largest and j < largest:
    second_largest=j
print("second largest",second_largest)


#Find the largest no.
lis=[2,3,4,5,6,10]
largest=lis[0]
for i in lis:
  if i > largest:
    largest=i
print("largest no.",largest)


#find the missing value
arr=[1,3,4,5,6]
n=max(arr)
ex_sum=n*(n+1)//2
ac_sum= sum(arr)
missing_value = ex_sum - ac_sum
print("missing value",missing_value)