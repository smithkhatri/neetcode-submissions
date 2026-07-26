class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        ans = []
        bucket = [ [] for _ in range(len(nums)+1)]
        h_map = {}

        for i in nums:
            if i in h_map:
                h_map[i] += 1
            else:
                h_map[i] = 1
        
        for key, value in h_map.items():
            bucket[value].append(key)


        print(bucket)
        c = 0
        for i in reversed(bucket):
            for j in i:
                ans.append(j)
                if len(ans) == k:
                    return ans





