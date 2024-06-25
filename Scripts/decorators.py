import functools
import random

# Part A
def reverse_string(func):
    """If output is a string, reverse it. Otherwise, return None."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result[::-1]
        return None
    return wrapper

# Part B
def prime_filter(func):
    """Given a list of integers, return only the prime integers."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        numbers = func(*args, **kwargs)
        return [num for num in numbers if is_prime(num)]
    return wrapper

def is_prime(num):
    """Utility function to check for prime number."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Part C
def choose_one(func):
    """Given a list of elements, select a random one."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        elements = func(*args, **kwargs)
        return random.choice(elements)
    return wrapper

# Part D
def power(n: int):
    """Given a number, return a tuple where the first element is the original number and the second is the nth power."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            num = func(*args, **kwargs)
            return (num, num ** n)
        return wrapper
    return decorator

# Part E
def mask_data(target_key: str, replace_with: str = "*"):
    """Replace the value of a dictionary with a 'masked' version."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if target_key in result:
                result[target_key] = replace_with * len(result[target_key])
            return result
        return wrapper
    return decorator

#  test function
@reverse_string
def get_university_name() -> str:
    return "Western Institute of Technology and Higher Education"

@reverse_string
def get_university_founding_year() -> int:
    return 1957

@prime_filter
def numbers(from_num: int, to_num: int) -> list:
    return [num for num in range(from_num, to_num)]

@choose_one
def available_options() -> list:
    return ["A", "B", "C"]

@power(n=5)
def get_random_number():
    return random.randint(1, 100)

@mask_data(target_key="name")
def get_user(name: str, age: int):
    return {
        "name": name,
        "age": age
    }

# Execute Tests
# print(get_university_name())  
# print(get_university_founding_year())  
# print(numbers(2, 20))  
# print(available_options())  
# print(get_random_number())  
# print(get_user(name="Alice", age=30))  
# print(get_user(name="Bob", age=25))  
