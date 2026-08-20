class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        [1,5,10,12,20,30], target = 32
        """

        a = 0
        b = len(numbers) - 1
        
        for i in range(len(numbers)):
            if numbers[a] + numbers[b] == target:
                return [a+1, b+1]

            if numbers[a] + numbers[b] > target:
                b -= 1
            
            if numbers[a] + numbers[b] < target:
                a += 1
            
            




