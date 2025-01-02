# Print numbers 0 to 4
# for i in range(10):
#     print(i)

# Outputs:
# 0
# 1
# 2
# 3
# 4

#  
# While Loop: Runs as long as a condition is True.

# Repeats as long as a condition is true.

#  📝 Example:

# countdown = int(input("Input a Value"))

# while countdown > 0:
#     print("Counting down:", countdown)
#     countdown -= 1

# print("Blast off! 🚀")



# temperature = int(input("Input the current temperature: "))
# if temperature > 25:
#     print("The Weather is Hot")
# elif temperature >= 25:
#     print("Its Transition")
# else:
#     print("The weather is cold")



# fruits = [ "apple", "banana", "cherry"]

# # Accessing elements
# print(fruits[0])  # Outputs: apple

# # Modifying an element
# fruits[1] = "orange"
# print(fruits)  # Outputs: ['apple', 'orange', 'cherry']

# # Adding an element
# fruits.append("grape")
# print(fruits)  # Outputs: ['apple', 'orange', 'cherry', 'grape']



# coordinates = (10, 20)

# # Accessing elements
# print(coordinates[0])  # Outputs: 10

# # Trying to modify a tuple will raise an error:
# # coordinates[0] = 5  # Error! Tuples can't be modified.



# unique_numbers = {1, 2, 2, 3, 4}

# print(unique_numbers)  # Outputs: {1, 2, 3, 4} (Notice that 2 is only included once)



# # Dictionaries
# student_info = {"name": "Charlie", "age": 21, "grade": "A"}

# # Accessing a value by its key
# print(student_info["name"])  # Outputs: Charlie

# # Modifying a value
# student_info["age"] = 22
# print(student_info)  # Outputs: {'name': 'Charlie', 'age': 22, 'grade': 'A'}


# # Now you know how to organize data like a pro!

# # Functions - Python’s Superpowers! 🦸‍♂️

# # Functions are blocks of reusable code—they save you from repeating the same code over and over. Think of functions like superpowers you can call whenever you need them! 💪

# # 📝 Example:

# # Defining a function
# def greet(name):
#     print("Hello, " + name + "! 👋")

# # Calling the function
# greet("Alice")  # Outputs: Hello, Alice! 👋
# greet("Bob")    # Outputs: Hello, Bob! 👋
# # 💡 Return Values: Functions can also return values!

# def add_numbers(x, y):
#     return x + y

# result = add_numbers(10, 5)
# print(result)  # Outputs: 15



# # Modules - Python’s Toolkit! 🧰

# # Python comes with a toolkit of modules—specialized code libraries that you can use without building everything from scratch. It’s like using a toolbox instead of crafting tools by hand! 🔨

# # To use a module, just import it:



# # 📝 Example 1: Math Module: For mathematical functions.

# import math

# # Using the math module to calculate the square root
# print(math.sqrt(16))  # Outputs: 4.0



# # Example 2: Random Module: For generating random numbers.

# import random

# # Generate a random number between 1 and 6 (like rolling a die)
# dice_roll = random.randint(1, 6)
# print("You rolled a", dice_roll)


# #  Mini-Challenge:
# # Write a Python function that checks if a number is even or odd and prints the result. Here's a start:

def check_even_odd(number):
    if number % 2 == 0:
        print(number, "is an even Number! ⚖️")
    else:
        print(number, "is an odd Number! 🎯")

check_even_odd(int(input("Input  value")))  # Try with different numbers! 
