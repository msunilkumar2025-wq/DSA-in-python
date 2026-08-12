
#Three largest number
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))

if num1>num2 & num1>num3:
    print(num1,"is the largest number")
elif num2>num1 & num2>num3:
    print(num2,"is the largest number")
else:
    print(num3,"is the largest number")
    
# Find the area of circle,traiangle,rectangle,square

num=int(input("enter radius of circle:"))
print(3.14*(num*num),"area of a circle")

num2=int(input(" enter side of a square: "))
print(num2*num2,"area of a square")

num3=int(input(" enter length of a length: "))
num4=int(input(" enter length of a width: "))
area=num3*num4
print(num3*num4,"area of rectangle")

num5=int(input(" enter base of a triangle: "))
num6=int(input(" enter height of a triangle: "))
print(1/2*num5*num6,"area of traingle")

#Find the fernite Celsius to Fahrenheit:
num1=int(input(" enter temperature in Celsius: "))
print((num1*9/5)+32,"temperature in Fahrenheit")
num2=int(input(" enter temperature in Fahrenheit: "))
print((num2-32)*5/9,"temperature in Celsius")


#Three largest number by using ternary operator
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
num3=int(input("Enter third number: "))
largest = num1 if (num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
print(largest, "is the largest number")


#Palindrome number
num=int(input("Enter a number = "))
original = num
reverse=0
while(num>0):
    dig=num%10
    reverse=(reverse*10)+dig
    num=num//10
if original==reverse:
    print("palindrome")
else:
    print("not a palindrome")
    
    
#Factorial of a number
num=int(input("Enter a number: "))
Factorial=1
while num>0:
     Factorial=Factorial*num
     num-=1
    
print("Factorial=",Factorial)

#reseve a number
num=int(input("Enter a number: "))
reverse=0
while num>0:
    dig=num%10
    reverse=(reverse*10)+dig
    num=num//10
print("Reverse number=",reverse)

#Fibonacci
num=int(input("enter a number = "))
a,b=0,1
for i in range(num):
    print(a)
    c=a+b
    a=b
    b=c
    


#TRAPPING RAINWATER(WITHOUT USING FUNCTION)
height = [1,8,6,2,5,4,8,3,7]
n = len(height)
left_max = [0] * n
right_max = [0] * n
water_trapped = 0

left_max[0] = height[0]
for i in range(1, n):
    left_max[i] = max(left_max[i-1], height[i])

right_max[n-1] = height[n-1]
for i in range(n-2, -1, -1):
    right_max[i] = max(right_max[i+1], height[i])

for i in range(n):
    water_trapped += min(left_max[i], right_max[i]) - height[i]

print("Trapped rainwater:", water_trapped)

#Search in rotated sorted array
def search_rotated_array(nums, target): 
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[left] <= nums[mid]:  # Left half is sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1



#Valid Anagram (without using function)
def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for char in s:
        count_s[char] = count_s.get(char, 0) + 1

    for char in t:
        count_t[char] = count_t.get(char, 0) + 1

    return count_s == count_t


#First Unique Character in a String (without using function)
def first_unique_char(s):
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    for i, char in enumerate(s):
        if char_count[char] == 1:
            return i

    return -1

#Shorest subarray with sum at least K (without using function)
def shortest_subarray_with_sum_at_least_k(nums, k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)

    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    min_length = float('inf')
    deque = []

    for i in range(n + 1):
        while deque and prefix_sum[i] - prefix_sum[deque[0]] >= k:
            min_length = min(min_length, i - deque.pop(0))

        while deque and prefix_sum[i] <= prefix_sum[deque[-1]]:
            deque.pop()

        deque.append(i)

    return min_length if min_length != float('inf') else -1



#Longest duplicate substring
def longest_duplicate_substring(s):
    def search(length):
        seen = set()
        base = 256
        mod = 2**63 - 1
        hash_value = 0

        for i in range(length):
            hash_value = (hash_value * base + ord(s[i])) % mod

        seen.add(hash_value)

        baseL = pow(base, length, mod)
        for start in range(1, len(s) - length + 1):
            hash_value = (hash_value * base - ord(s[start - 1]) * baseL + ord(s[start + length - 1])) % mod
            if hash_value in seen:
                return start
            seen.add(hash_value)

        return -1

    left, right = 1, len(s)
    start_index = -1

    while left <= right:
        mid = (left + right) // 2
        idx = search(mid)
        if idx != -1:
            start_index = idx
            left = mid + 1
        else:
            right = mid - 1

    return s[start_index:start_index + left - 1] if start_index != -1 else ""

#Left and Right Sum Difference
def left_right_sum_difference(nums):    
    n = len(nums)
    left_sum = [0] * n
    right_sum = [0] * n

    for i in range(1, n):
        left_sum[i] = left_sum[i - 1] + nums[i - 1]

    for i in range(n - 2, -1, -1):
        right_sum[i] = right_sum[i + 1] + nums[i + 1]

    result = [abs(left_sum[i] - right_sum[i]) for i in range(n)]
    return result