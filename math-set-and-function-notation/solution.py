def is_subset(a, b):
    """
    a, b: Python sets

    Returns:
        True if every element of a is also in b (a is a subset of b,
        written a subseteq b), False otherwise.
    """
    # TODO: Implement using Python's own set operations.
    for item in a:
        if item not in b:
            return False
    return True


def argmax(values):
    """
    values: a non-empty list or tuple of numbers

    Returns:
        The INDEX of the largest value in values. If multiple values are
        tied for the maximum, return the first such index.
    """
    # TODO: Implement argmax from Theory: scan once, tracking the best
    # value and its index, updating only on a strictly larger value.
    best_idx = 0
    best_val = values[0]

    for i in range(1, len(values)):
        if values[i] > best_val:
            best_val = values[i]
            best_idx = i
    return best_idx
