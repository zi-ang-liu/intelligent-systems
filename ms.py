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


def merge_sort(arr):
    """
    Merge sort algorithm.

    Parameters
    ----------
    arr : list
        The array to be sorted

    Returns
    -------
    list
        The sorted array
    """

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


if __name__ == "__main__":
    # Example usage
    arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr = merge_sort(arr)
    print("Sorted array:", sorted_arr)
