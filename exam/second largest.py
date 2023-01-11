nums1_list = [54, -1, 45, 987, 5, 2, 65, 7, 12]



def second_largest(list) -> int:
    largest = nums1_list[0]
    second = nums1_list[0]
    for n in nums1_list:
        if n > largest:
            largest = second
            second = n
        if n > second != largest:
            second = n
    return second

result = second_largest(nums1_list)
print(result)


