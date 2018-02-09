def twoSum(nums, target):
    if len(nums) <= 1:
        return False
    buff_dict = {}
    for i in range(len(nums)):
        if nums[i] in buff_dict:
            return [buff_dict[nums[i]], i]
        else:
            buff_dict[target - nums[i]] = i
def towSum1(nums,target):
    if len(nums) <=1:
        return False
    buff_dit = {}
    for i in range(len(nums)):
        if nums[i] in buff_dit:
            return [buff_dit[nums[i]],i]
        else:
            buff_dit[target - nums[i]] = i


def twoSum2(nums,target):
    if len(nums) <=1:
        return False
    a=0
    b=[]
    for i in range(len(nums)):
        if target == 0:
            b.append(nums.index(0))
            nums[i] = "a"
            if len(b) == 2:
                return b
            continue
        else:
            a = target - nums[i]
            if (a in nums[i+1:]):
                return [i,nums[i+1:].index(a)+i+1]
            else:
                continue
                


if __name__=="__main__":
    print(twoSum([3,3],6))
    print(twoSum2([3, 3], 6))
    print(twoSum2([3,2,4],6))
    print(twoSum2([0, 4, 3, 0],0))