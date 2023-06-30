def min_swaps(nums):
    # mp记录排序后数值应在的正确位置
    mp = {}
    sort_nums = sorted(nums)
    for i in range(len(sort_nums)):
        mp[sort_nums[i]] = i

    # 循环节个数
    lops = 0
    # 该位置的数是否被访问过
    flags = []
    for i in range(len(nums)):
        flags.append(False)
    for i in range(len(nums)):
        if not flags[i]:
            j = i
            while not flags[j]:
                flags[j] = True
                # j是当前值应在的正确位置
                j = mp[nums[j]]
            lops += 1
    return len(nums) - lops

