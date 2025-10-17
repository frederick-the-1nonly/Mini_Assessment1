def product(num1, num2):
    return num1 * num2


def square(number):
    return number ** 2


def even(n):
    return True if n % 2 == 0 else False


def sum_of_list(numbers):
    return sum(numbers)


def list_of_even_numbers(numbers):
    even_no = []
    for n in range(1,numbers):
        if even(n):
            even_no.append(n)
    return even_no

def sum_of_odd_numbers(numbers):
    """
    Calculates the sum of all odd numbers in a list.

    Parameters:
        numbers (list of int): A list of integers.

    Returns:
        int: The sum of all odd numbers in the list.
    """
    odd = []
    for n in numbers:
        if not even(n):
            odd.append(n)
    return sum(odd)
