def twoSum(nums, target):

    lens = len(nums)
    out = []
    for i in range(lens):
        for j in range(i+1, lens):
            if nums[i] + nums[j] == target:
                out.append(i)
                out.append(j)
                break
            else:
                return []        
    return out
    print(out)
    # for i in range(len(nums)):
    #         if target-nums[i] in nums[i+1:]:
    #             return [i,nums.index(target-nums[i],i+1)] 

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    twoSum(nums, target)
