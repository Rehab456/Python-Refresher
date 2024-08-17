#(1)Calculate the Area of a Rectangle:
length = 5
width = 3
area = (length * width)
print(area)

#(2)Check if a Number is Even or Odd:
numbers = [7]       # we can add list of numbers in it like[7,8,4,3]  

for number in numbers:
    if number % 2 == 0:
        print(f'{number} is even')
    else:
        print(f'{number} is odd')

#(3)Reverse a String:
a = 'hello'
reversed_string = ''.join(reversed(a))
print(reversed_string)

#(4)Find the Factorial of a Number:
import math

number = 5
factorial = math.factorial(number)
print(factorial)

#(5)Check if a String is Palindrome or Not:
def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]  

string = "radar"
print(is_palindrome(string))  # Output: True

string = "hello"
print(is_palindrome(string))  # Output: False

#(6)Generate Fibonacci Series up to n terms
def generate_sequence(n):
    return list(range(n))
n = 7
print(generate_sequence(n))

#(7)Find the Largest Among Three Numbers:
def find_largest(a, b, c):
    return max(a, b, c)
num1 = 10
num2 = 25
num3 = 5

largest = find_largest(num1, num2, num3)
print(f"The largest number is {largest}")

#(8)Calculate Simple Interest:
principal_amount = 1000
rate_interest = 5
time_period = 2 
simple_interest = principal_amount * (rate_interest /100) * time_period
print(simple_interest)

#(9)Convert Celsius to Fahrenheit:

temperature_in_celcius = 37   # from farenheit to celcius =(1.8×25)+32
Fahrenheit = (9/5 *temperature_in_celcius)+32
print(Fahrenheit)

#(10)Check Leap Year:
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

    #Programming Challenges
#(1)Find the Median of Three Numbers:
def median_of_three(a,b,c):
    numbers = [a , b , c]
    numbers_sorted = sorted(numbers)
    # The median is the second number in the sorted list
    return numbers_sorted[1]
a = 10
b = 5
c = 20

print(f"Median: {median_of_three(a, b, c)}")  # Output: Median: 5

#(2)Count the Number of Words in a Sentence:

def count_words(text):
    words = text.split()
    return len(words)
text = 'The quick brown fox jumps over the lazy dog'
word_count = count_words(text)
print(word_count)

#(3)Calculate the Sum of Digits in a Number:

def sum_of_digits(number):
    return sum(map(int, str(abs(number))))  # Convert number to string, then sum digits
number = 12345
print(f"Sum of digits: {sum_of_digits(number)}")

#(4)Find the Longest Common Prefix in a List of Strings:

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    prefix = strs[0]  
    
    for string in strs[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

strings = ["flower", "flow", "flight"]
print(f"Longest common prefix: '{longest_common_prefix(strings)}'")

#(5)Check if a Number is a Prime Number:

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    for i in range(5, number):
        if number % i == 0:
            return False
    return True
number = int(input("Enter a number to check if it is prime: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

    








