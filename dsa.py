#Que. 1+11+111+1111+____N
n = int(input("Enter the number of terms (N): "))
sum_series_1 = 0
term_1 = 0
print("\nSeries 1: ", end="")
for i in range(n):
    term_1 = term_1 * 10 + 1
    sum_series_1 += term_1
    print(term_1, end=" + " if i < n - 1 else "")
print(f"\nThe sum of the series (1+11+...) is: {sum_series_1}")

sum_series_5 = 0
term_5 = 0
print("\nSeries 2: ", end="")
for i in range(n):
    term_5 = term_5 * 10 + 5
    sum_series_5 += term_5
    print(term_5, end=" + " if i < n - 1 else "")
print(f"\nThe sum of the series (5+55+...) is: {sum_series_5}")


#sum of all digits in a number
def sum_digits_in_number(number):
    total_sum = 0
    num_str = str(number)
    for digit_char in num_str:
        total_sum += int(digit_char)
    return total_sum
example_number = 2345678
digit_sum = sum_digits_in_number(example_number)
print(f"The sum of digits in {example_number} is: {digit_sum}")


#find the missing value
arr=[1,3,4,5,6]
n=max(arr)
ex_sum=n*(n+1)//2
ac_sum= sum(arr)
missing_value = ex_sum - ac_sum
print("missing value",missing_value)
