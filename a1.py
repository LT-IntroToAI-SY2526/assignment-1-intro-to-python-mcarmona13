# Assignment 1: AI-Generated Python Problems
# Name: Max Carmona

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
["I'm learning Python basics in a high school programming class. I'm new to programming 
but have been learning variables, data types, conditionals, loops, and functions. 
Can you create 6 practice problems that cover:
- Variables and basic data types
- Conditionals (if/else/else if) 
- Loops (for and while)
- Functions
- Basic list operations

Make them progressively more challenging and include clear instructions with 
example inputs/outputs. I want problems that complement basic exercises like 
absolute value, factorial, and list operations."] 



Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
PROBLEM 1: [Problem Title/Description]
[Copy the complete problem description from your AI assistant]

Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False



PROBLEM 1: [ Temperature Converter/A functions called 'celsius_to_fahrenheit' that takes a temperature in Celsius
and converts it to fahrenheit using the formula: F = (C * 9/5) + 32 ]

The function should also categorize the temperature:
- Below 0 F: "Freezing"
- 0-32 F: "Very Cold"
- 33-60 F: "Cold"
- 61-80 F: "Mild"
- Above 80 F: "Hot"

Returns the converted temperature

Example inputs/outputs:
- celsius_to_fahrenheit(0) should return (32.0, "Very Cold")
- celsius_to_fahrenheit(25) should return (77.0, "Mild")
- celsius_to_fahrenheit(-10) should return (14.0, "Freezing")
"""
def celsius_to_fahrenheit(celsius):
    """
    My APPROACH:
    1. Convert celsius to fahrenheit using the given formula
    2. Use if/else if/else to categorize the temperature
    3. Return both values
    """
    # Converting temperature
    fahrenheit =  (celsius * 9/5) + 32

    # Categorizing temperature
    if fahrenheit < 0:
        category = "Freezing"
    if fahrenheit <= 32:
        category = "Very Cold"
    if fahrenheit <= 59:
        category = "Cold"
    if fahrenheit <= 73:
        category = "Mild"
    else: 
        category = "Hot"

    return (fahrenheit, category)



"""
PROBLEM 2: Password Strength Checker/A function called 'check_password_strength' 
that takes a password string and a strength rating based on these criteria:

- Length: At least 8 characters (1 point)
- Contains uppercase letter (1 point)
- Contains lowercase letter (1 point)
- Contains a digit (1 point)
- Contains special character (!@#$%^&*) (1 point)

Return the total score (0-5) and a strength description:
- 0-1: "Very Weak"
- 2: "Weak" 
- 3: "Fair"
- 4: "Strong"
- 5: "Very Strong"

Example inputs/outputs:
- check_password_strength("password") should return (2, "Weak")
- check_password_strength("Password123!") should return (5, "Very Strong")
""" 
def check_password_strength(password):
    """
    MY APPROACH:
    1. Initialize score to 0
    2. Check each criterion and add points
    3. Use conditionals to determine strength description
    4. Return score and description 
    """

    score = 0

    # Check length
    if len(password) >= 8:
        score += 1
    
    # Check for uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if has_upper:
        score += 1
    
    # Check for lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if has_lower:
        score += 1
    
    # Check for digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if has_digit:
        score += 1
    
    # Check for special character
    special_chars = "!@#$%^&*"
    has_special = False
    for char in password:
        if char in special_chars:
            has_special = True
            break
    if has_special:
        score += 1
    
    # Determine strength description
    if score <= 1:
        strength = "Very Weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Fair"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return (score, strength)



"""
PROBLEM 3: [ List Statitsics Calculator/A function called 'calculate_stats' 
that takes a list of numbers and a dictionary with the following statistics: ]
- "count": number of items in the list
- "sum": sum of all numbers
- "average": mean of the numbers
- "min": smallest number
- "max": largest number
- "even_count": count of even numbers
- "odd_count": count of odd numbers

Example inputs/outputs:
- calculate_stats([1,2,3,4,5]) should return: 
    {"count": 5, "sum": 15, "average": 3.0, "min": 1, "max": 5, "even_count": 2, "odd count": 3}
"""
def calculate_stats(numbers):
    """
    MY APPROACH:
    1. Handle empty list 
    2. Use loops to calculate each statistic 
    3. Store results in a dictionary
    4. Return the dictionary
    """

    if not numbers: # Handles empty list
        return {"count": 0, "sum": 0, "average": 0, "min": None, "max": None, "even_count": 0, "odd count": 0}
    
    # basic stats
    count =len(numbers)
    total_sum = 0
    for num in numbers:
        total_sum += num

    average = total_sum / count

    # find min & max
    min_num = numbers[0]
    max_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num

    # counts even and odd numbers 
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return {
        "count": count,
        "sum": total_sum,
        "min": min_num, 
        "max": max_num,
        "even_count": even_count,
        "odd_count": odd_count,
    }

    
    
"""
PROBLEM 4: Word Pattern Finder
Write a function called 'find_word_patterns' that takes a sentence (string) and 
finds words that match certain patterns:

- Words that start and end with the same letter
- Words that are palindromes (read the same forwards and backwards)
- Words that contain only vowels
- Words longer than 5 characters

Return a dictionary with lists for each pattern type.

Example inputs/outputs:
- find_word_patterns("A man a plan a canal panama") might return:
{"same_letter": ["A", "a", "a"], "palindromes": ["A", "a", "a"], "only_vowels": ["A", "a", "a"], "long_words": ["panama"]}
"""
def find_word_patterns(sentence):
    """
    MY APPROACH: 
    1. Split sentence into words 
    2. For each word, check all pattern conditions 
    3. Add matching words to appropriate lists
    4. Return dictionary with all pattern lists
    """
    words = sentence.split()
    same_letter = []
    palindromes = []
    only_vowels = []
    long_words = []

    vowels = "aeiouAEIOU"

    for word in words:
        # removes punctuation for pattern checking 
        clean_word = ""
        for char in word:
            # FIXED: was isaplha(), should be isalpha()
            if char.isalpha():
                clean_word += char

        if not clean_word: # skips if no letters
            continue

        # FIXED: checks if starts and ends with same letter (was missing this logic)
        if clean_word[0].lower() == clean_word[-1].lower():
            same_letter.append(word)

        # FIXED: check if palindrome (was putting this in same_letter check)
        if clean_word.lower() == clean_word.lower()[::-1]:
            palindromes.append(word)

        # check if only vowels
        all_vowels = True
        for char in clean_word:
            if char not in vowels:
                all_vowels = False
                break
        if all_vowels:
            only_vowels.append(word)  # FIXED: was only_vowels.qppend

        # check if longer than 5 characters
        if len(clean_word) > 5:
            long_words.append(word)  # FIXED: was long_words.qppend(word)

    return {
        "same_letter": same_letter,
        "palindromes": palindromes,
        "only_vowels": only_vowels,
        "long_words": long_words
    }



"""
PROBLEM 5: [Number Sequence Generator/Write a function called 'generate_sequence' 
that takes three parameters: ]
- start: starting number
- length: how many numbers to generate
- pattern: either "fibonacci", "squares", "primes", or "even"

The function should return a list of numbers following the specified pattern.

- "squares": 1, 4, 9, 16, 25, ...
- "primes": 2, 3, 5, 7, 11, 13, ...
- "even": 2, 4, 6, 8, 10, ...

"""        
def generate_sequence(start, length, pattern):
    """
    MY APPROACH:
    1. Use if/elif to handle different patterns
    2. For each pattern, use appropriate logic to generate numbers
    3. Use loops to build the sequence
    4. Return the list of generated numbers
    """

    sequence = []

    if pattern == "squares":
        # perfect squares starting from start
        for i in range(length):
            square = (start + i) ** 2
            sequence.append(square)

    elif pattern == "primes":
        # prime numbers
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):  # FIXED: was .5, should be 0.5
                if n % i == 0:
                    return False
            return True
        
        num = 2 # start checking from 2
        while len(sequence) < length:
            if is_prime(num):
                sequence.append(num)
            num += 1

    elif pattern == "even":
        # even numbers starting from first even >= start
        if start % 2 == 0:
            current = start
        else:
            current = start + 1 

        for i in range(length):
            sequence.append(current)  # FIXED: was sequence.qppend(current)
            current += 2

    return sequence
        

# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""


print("\n")
print("\n")
print("\n")
print("\n")


print("Testing Problem 1: Temperature Converter")
print(f"celsius_to_fahrenheit(0): {celsius_to_fahrenheit(0)}")  # Should be (32.0, "Very Cold")
print(f"celsius_to_fahrenheit(25): {celsius_to_fahrenheit(25)}")  # Should be (77.0, "Mild")
print(f"celsius_to_fahrenheit(-10): {celsius_to_fahrenheit(-10)}")  # Should be (14.0, "Freezing")
    
print("\nTesting Problem 2: Password Strength")
print(f"check_password_strength('password'): {check_password_strength('password')}")  # Should be (2, "Weak")
print(f"check_password_strength('Password123!'): {check_password_strength('Password123!')}")  # Should be (5, "Very Strong")
    
print("\nTesting Problem 3: List Statistics")
test_list = [1, 2, 3, 4, 5]
stats = calculate_stats(test_list)
print(f"calculate_stats({test_list}): {stats}")
    
print("\nTesting Problem 4: Word Patterns")
test_sentence = "A man a plan a canal panama"
patterns = find_word_patterns(test_sentence)
print(f"find_word_patterns('{test_sentence}'): {patterns}")
    
print("\nTesting Problem 5: Number Sequences")
print(f"generate_sequence(1, 4, 'squares'): {generate_sequence(1, 4, 'squares')}")
print(f"generate_sequence(2, 5, 'primes'): {generate_sequence(2, 5, 'primes')}")

print("\n")
print("\n")
print("\n")
print("\n")


