def recursive_sum(numbers):
    '''
    This function calculates the sum of a list of numbers recursively.

    :param numbers: List of numbers
    :return: Sum of numbers
    '''
    # Base case: if the list is empty, return 0
    if len(numbers) == 0:
        return 0

    # Recursive case: add the first number to the sum of the rest of the list
    return numbers[0] + recursive_sum(numbers[1:])

if __name__ == '__main__':
    numbers = [5, 3, 9, 1, 7]
    result = recursive_sum(numbers)
    print('The sum of numbers is:', result)