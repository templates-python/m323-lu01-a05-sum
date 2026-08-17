"""Summe der Elemente einer Liste.

Aufgabenstellung: https://wiki.bzz.ch/modul/m323/learningunits/lu01/aufgaben/listsum
"""

def recursive_sum(numbers):
    """
    This function calculates the sum of a list of numbers recursively.

    :param numbers: List of numbers
    :return: Sum of numbers
    """
    # TODO: Implement the recursive function to calculate the sum of numbers


if __name__ == '__main__':
    demo_numbers = [5, 3, 9, 1, 7]
    result = recursive_sum(demo_numbers)
    print('The sum of numbers is:', result)
