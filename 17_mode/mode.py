def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    count_dict = {}
    for num in nums:
        if count_dict.get(num, -1) == -1:
            count_dict[num] = nums.count(num)
    highest_value = 0
    highest_key = ''
    for key in count_dict.keys():
        if count_dict[key] > highest_value:
            highest_value = count_dict[key]
            highest_key = key
    return highest_key
