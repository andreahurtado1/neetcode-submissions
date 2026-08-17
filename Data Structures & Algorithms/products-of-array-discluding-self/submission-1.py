class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            #prefix_list = nums[:i]
            output[i] = prefix
            prefix *= nums[i]
            #sufix = nums[i+1:]
            #print(f'index: {i}| prefix: {prefix_list}; sufix: {sufix}')
            #print(f'output: {output}')

        for j in range(len(nums) -1, -1, -1):
            output[j] = output[j] * suffix
            suffix *= nums[j]
            #print(f'j: {j}| suf: {suffix}')
            #print(f'output: {output}')

        return output


        