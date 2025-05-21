def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.

    Parameters
    ----------
    left : list
        The first sorted array
    right : list
        The second sorted array

    Returns
    -------
    list
        The merged sorted array
    """
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def merge_sort()