class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1


        sorted_freq = sorted(
            freq.items(),
            key=lambda item: item[1],
            reverse=True
        )
        result = []

        for num, count in sorted_freq[:k]:
            result.append(num)

        return result