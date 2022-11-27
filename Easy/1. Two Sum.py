class Solution:

    # first attempt - LEETCODE SUBMISSION: Wrong Answer
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        answer = []
        if len(nums) == 2:
            return [0, 1]
        for i in range(len(nums)):
            pointer = nums[i]
            for j in range(len(nums) - 1):
                pointer_next = nums[j+1]
                print(pointer)  
                check = pointer + pointer_next
                print(check)
                if check == target:
                    answer.append(nums.index(pointer))
                    answer.append(nums.index(pointer_next))
                    print(answer)
                    return answer

    # took me a while to understand how to do it without it being very inefficient however i just
    # ended up brute forcing it, it only passed a couple test cases but i was able to get it to work
    # i didnt really know how to deal with duplicate values as index would only return the first
    # so i just brute forced it on the first line which is not a good idea..
    
    # second attempt with google - LEETCODE SUBMISSION: Time Limit Exceeded
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    # this attempt is basically the same as the first attempt but i was able to get it to work
    # in a neater manner, also noticed that i could use the range function to make it more efficient
    # and not have to use the index function to find the index of the numbers
    # this one passed all test cases, however still too slow
    
    # neetcode attempt - LEETCODE SUBMISSION: Accepted
    # https://youtu.be/KLlXCFG5TnA
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

if __name__ == "__main__":
    sol = Solution()
    nums = [3, 3]
    target = 6
    print(f'returns: {sol.twoSum(nums, target)}')
    assert sol.twoSum(nums, target) == [0, 1]
