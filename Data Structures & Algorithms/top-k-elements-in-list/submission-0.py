class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {} # {'1': 1, '2': 2,'3': 3}
        for num in nums:
            if num not in frequency:
                frequency[num] = 1
            else:
                frequency[num] += 1

        
        sorted_freq = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
        list_freq = list(sorted_freq.keys())
        print(list_freq[:k])
        return list_freq[:k]