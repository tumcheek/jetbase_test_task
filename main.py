def find_missing_numbers(sequence, low, high):
    """The time complexity  is the O(n log n)"""
    missing_numbers = []

    if low > high:
        return missing_numbers

    mid = (low + high) // 2
    if sequence[mid] - sequence[mid-1] > 1:
        for num in range(sequence[mid-1] + 1, sequence[mid]):
            missing_numbers.append(num)

    missing_numbers_left = find_missing_numbers(sequence, low, mid - 1)
    missing_numbers_right = find_missing_numbers(sequence, mid + 1, high)

    missing_numbers.extend(missing_numbers_left)
    missing_numbers.extend(missing_numbers_right)

    return missing_numbers
