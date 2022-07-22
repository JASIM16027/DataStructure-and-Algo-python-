def first_position(nums, target):
    left, right = 0, len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target and nums[mid] > nums[mid - 1]:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def end_position(nums, target):
    left, right = 0, len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target and nums[mid] < nums[mid + 1]:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def find_first_and_last(nums, target):
    first = first_position(nums, target)
    last = end_position(nums, target)
    return [first, last]


nums = [1, 2, 2, 2, 3, 3, 3, 3, 4, 5]
target = 3
print(find_first_and_last(nums, target))
