def is_safe(report):
    """Return True if report is safe."""
    if len(report) < 2:
        # single level? assume safe
        return True
    diffs = [report[i+1] - report[i] for i in range(len(report)-1)]
    # check monotonic direction
    # all positive or all negative
    if all(d > 0 for d in diffs):
        direction = 1  # increasing
    elif all(d < 0 for d in diffs):
        direction = -1  # decreasing
    else:
        return False
    # check magnitude between 1 and 3
    for d in diffs:
        abs_diff = abs(d)
        if abs_diff < 1 or abs_diff > 3:
            return False
    return True

def count_safe(reports):
    """Return number of safe reports."""
    return sum(1 for r in reports if is_safe(r))

# Example data
example = [(7,6,4,2,1), (1,2,7,8,9),(9,7,6,2,1),(1,3,2,4,5),(8,6,4,4,1),(1,3,6,7,9)]
print("Safe count:", count_safe(example))
# for r in example:
#     print(r, is_safe(r))
