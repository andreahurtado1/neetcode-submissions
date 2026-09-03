class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # input -> list of nums []
        # output -> len of sequence
        nums_set = set(nums)
        print(nums_set)
        longest_seq = set()

        if nums == []:
            return 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_len = 1
                while current_num + 1 in nums_set:
                    current_num += 1 # 3, 4, 5
                    current_len += 1 # 2, 3, 4
                print(longest_seq)
                longest_seq.add(current_len)

        return list(longest_seq)[-1]
                
                
        