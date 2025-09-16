"""Assignment 1

Fill in the following function skeletons - descriptions are provided in 
the docstring (the triple quote thing at the top of each function)

Some assert statements have been provided - write more of them to test your code!

The `raise NotImplementedError(...)`s are placeholders to help you not skip implementing
a function. They should be removed and replaced with your solution.

This portion of the assignment will not be graded, but this gives you some problems to 
check and we'll be doing them in class.

Make sure to complete the a1.py problems which should be AI generated.
"""

from typing import List, TypeVar



def absolute(n: int) -> int:
    """Gives the absolute value of the passed in number. Cannot use the built in
    function `abs`.

    Args:
        n - the number to take the absolute value of

    Returns:
        the absolute value of the passed in number
    """
    if n < 0:
        return -1 * n
    return n 
    


def factorial(n: int) -> int:
    """Takes a number n, and computes the factorial n! You can assume the passed in
    number will be positive

    Args:
        n - the number to compute factorial of

    Returns:
        factorial of the passed in number
    """
    for num in range(1, n+1):
        result = result * num  # result *= num
    return result

T = TypeVar("T")



def every_other(lst: List[T]) -> List[T]:
    """Takes a list and returns a list of every other element in the list, starting with
    the first.

    Args:
        lst - a list of any (constrained by type T to be the same type as the returned
            list)

    Returns:
        a list of every of other item in the original list starting with the first
    """
    # This is the pythonic way
    return lst[::2]

    # This is the java way
    # result = []
    # for index in range(len(lst)):
    #     if index % 2 == 0:
    #         result.append(lst[index])
    # return result



def sum_list(lst: List[int]) -> int:
    """Takes a list of numbers, and returns the sum of the numbers in that list. Cannot
    use the built in function `sum`.

    Args:
        lst - a list of numbers

    Returns:
        the sum of the passed in list
    """
     # This is how the built in function is used
    # return sum(lst)
    total = 0
    for element in lst:
        total += element
    # print(total)
    return total



def mean(lst: List[int]) -> float:
    """Takes a list of numbers, and returns the mean of the numbers.

    Args:
        lst - a list of numbers

    Returns:
        the mean of the passed in list
    """
    return sum_list(lst) / len(lst) if lst else 0



def median(lst: List[int]) -> float:
    """Takes an ordered list of numbers, and returns the median of the numbers.

    If the list has an even number of values, it computes the mean of the two center
    values.

    Args:
        lst - an ordered list of numbers

    Returns:
        the median of the passed in list
    """
    if len(lst) % 2 == 1:
            return lst[len(lst) // 2 ]
    else:
        m1 = len(lst) // 2
        m2 = m1 - 1
        return (lst[m1] + lst[m2]) / 2


def duck_duck_goose(lst: List[str]) -> List[str]:
    """Given an list of names (strings), play 'duck duck goose' with it, knocking out
    every third name (wrapping around) until only two names are left.

    In other words, when you hit the end of the list, wrap around and keep counting from
    where you were.

    For example, if given this list ["roscoe", "kim", "woz", "solin"], you'd first
    knock out woz. Then first 'duck' on solin, wrap around to 'duck' on roscoe and
    'goose' on kim - knocking him out and leaving only roscoe and solin.

    You may assume the list has 3+ names to start

    Args:
        lst - a list of names (strings)

    Returns:
        the resulting list after playing duck duck goose
    """
    position = 0
    current = "duck1"
    while len(lst) > 2:
        if current == "duck1":
            current = "duck2"
            position += 1
        elif current == "duck2":
            current = "goose"
            position += 1
        else: # current is goose
            current = "duck1"
            lst.pop(position)

        # Wrap around
        if position == len(lst):
            position = 0
            
    return lst

# this line causes the nested code to be skipped if the file is imported instead of run
if __name__ == "__main__":
    assert absolute(-1) == 1, "absolute of -1 failed"
    assert absolute(4) == 4, "absolute of 4 failed"
    assert factorial(4) == 24, "factorial of 4 failed"
    assert factorial(5) == 120, "factorial of 5 failed"
    assert factorial(1) == 1, "factorial of 1 failed"
    assert factorial(0) == 1, "factorial of 0 failed"
    assert every_other([1, 2, 3, 4, 5]) == [1,3,5], "every_other of [1,2,3,4,5] failed"
    assert every_other([12, 23, 35, 48, 53, 63]) == [12,35,53], "every_other of [1,2,3,4,5] failed"
    assert sum_list([1, 2, 3]) == 6, "sum_list of [1,2,3] failed"
    assert sum_list([4, 7, 10, 23, 7]) == 51, "sum_list of [4, 7, 10, 23, 7] failed"
    # print(sum_list([4, 7, 10, 23, 7]))
    assert mean([1, 2, 3, 4, 5]) == 3, "mean of [1,2,3,4,5] failed"
    assert mean([1, 2, 3, 4, 5, 6]) == 21/6, "mean of [1, 2, 3, 4, 5, 6] failed"
    assert mean([]) == 0, "mean of [] failed"
    assert median([1, 2, 3, 4, 5]) == 3, "median of [1,2,3,4,5] failed"
    assert median([1, 2, 3, 4, 6, 6]) == 3.5, "median of [1, 2, 3, 4, 5, 6] failed"
    names = ["anakin", "batman", "reiner", "superman", "eren", "toji"]
    assert duck_duck_goose(names) == ["anakin", "eren"], "duck duck goose assert 1 failed"
    names = ["me1", "me2", "me3", "me4", "me5"]
    assert duck_duck_goose(names) == ["me2", "me4"], "duck duck goose assert 2 failed"

    print("All tests passed!")

