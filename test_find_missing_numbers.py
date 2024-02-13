import random
import pytest

from main import find_missing_numbers


@pytest.mark.parametrize("sequence_length", [100, 1000, 10000, 100000, 1000000])
def test_find_missing_numbers_large_sequence(sequence_length):
    sequence = list(range(1, sequence_length + 1))
    missing_numbers = random.sample(sequence[1:-1], 2)
    for num in missing_numbers:
        sequence.remove(num)
    expected_missing = sorted(missing_numbers)
    assert find_missing_numbers(sequence, 0, len(sequence) - 1) == expected_missing
